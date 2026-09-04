#!/usr/bin/env python3
"""Outil d'auteur du dépôt `skills` : conformité de la marketplace et génération de la table.

Deux gestes, un seul modèle de données lu depuis le dépôt :

    python3 scripts/skills.py check     conformité + fraîcheur de la zone générée
    python3 scripts/skills.py readme    régénère la zone du README entre les marqueurs

La table du `README.md` se génère depuis le frontmatter des skills (`couche`, `moment`,
`famille`). Rien hors des marqueurs n'est touché.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys

try:  # PyYAML lit le frontmatter comme le fera le chargeur de skills ; sinon, repli maison.
    import yaml
except ImportError:  # pragma: no cover — dépend de l'environnement
    yaml = None

MARQUEUR_DEBUT = "<!-- skills:début -->"
MARQUEUR_FIN = "<!-- skills:fin -->"

COUCHES = ("socle", "recette")
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

FAMILLE_PAR_DEFAUT = "Non classé"

# Mise en page de la zone générée : l'ordre des plugins, celui des familles, et la prose
# d'introduction de chaque section. Un plugin absent d'ici est rendu à la suite avec un
# titre dérivé de son nom ; une famille inconnue tombe dans « Non classé ».
SECTIONS = [
    {
        "plugin": "avqn-skills",
        "titre": "Skills disponibles — `avqn-skills`",
        "intro": (
            "Quatre familles. Dans chacune, un **socle** porte le craft transverse et les "
            "**recettes** vont\nde bout en bout en le chargeant."
        ),
        "familles": [
            ("cycle-client", "Cycle de vie du client — AVQN OS"),
            ("contenu-autonomes", "Contenu Autonomes — ressources et blog"),
            ("video-contentos", "Vidéo Contentos"),
            ("outillage", "Outillage des skills"),
        ],
    },
    {
        "plugin": "avqn-dev",
        "titre": "Skills disponibles — `avqn-dev`",
        "intro": "Invocation préfixée : `/avqn-dev:dev`, `/avqn-dev:local`…",
        "familles": [],
    },
]

# Les familles attendues d'un plugin, dérivées de la mise en page : un skill d'`avqn-skills`
# doit en porter une, un skill d'`avqn-dev` n'en porte pas.
FAMILLES_ATTENDUES = {
    s["plugin"]: [cle for cle, _ in s["familles"]] for s in SECTIONS if s["familles"]
}

ENTETE = "| Skill | Couche | Moment |\n| :---- | :----- | :--- |"


class ErreurDeGeneration(Exception):
    """La zone générée n'a pas pu être écrite (marqueurs absents, dupliqués ou inversés)."""


# --- Lecture du dépôt --------------------------------------------------------------------


def bloc_frontmatter(texte):
    """Rend le texte brut entre les deux `---` d'en-tête, ou None s'il n'y en a pas."""
    m = re.match(r"^---\s*\n(.*?)\n---", texte, re.S)
    return m.group(1) if m else None


def _scalaire(valeur):
    if valeur is None:
        return ""
    if isinstance(valeur, (list, dict)):
        return valeur
    return str(valeur)


def _parser_replie(bloc):
    """Repli sans PyYAML : scalaires simples et blocs repliés (`>-`), seules formes du dépôt."""
    champs = {}
    cle = None
    morceaux = []

    def clore():
        if cle is not None:
            champs[cle] = " ".join(morceaux).strip()

    for ligne in bloc.split("\n"):
        entete = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", ligne)
        if entete and not ligne.startswith((" ", "\t")):
            clore()
            cle, valeur = entete.group(1), entete.group(2).strip()
            morceaux = [] if valeur in (">-", ">", "|", "|-", "") else [valeur.strip("\"'")]
        elif cle is not None:
            morceaux.append(ligne.strip())
    clore()
    return champs


def lire_frontmatter(texte):
    """Rend le frontmatter d'un `SKILL.md` sous forme de dict, ou None s'il n'y en a pas.

    PyYAML fait foi quand il est là — c'est lui qui décide ce qu'un chargeur de skills verra.
    Un frontmatter qu'il refuse retombe sur le parseur maison pour que le contrôle puisse
    quand même nommer le skill fautif ; `problemes_yaml` rapporte l'erreur en propre.
    """
    bloc = bloc_frontmatter(texte)
    if bloc is None:
        return None
    if yaml is not None:
        try:
            charge = yaml.safe_load(bloc)
        except Exception:  # noqa: BLE001 — l'erreur est rapportée par problemes_yaml
            charge = None
        if isinstance(charge, dict):
            return {str(k): _scalaire(v) for k, v in charge.items()}
    return _parser_replie(bloc)


def problemes_yaml(bloc):
    """Rend le problème de lecture YAML du frontmatter, ou une liste vide."""
    if yaml is not None:
        try:
            yaml.safe_load(bloc)
        except Exception as e:  # noqa: BLE001 — le message importe plus que le type
            detail = " ".join(str(e).split())[:160]
            return [f"frontmatter illisible par un parseur YAML — {detail}"]
        return []
    # Sans PyYAML, on attrape la faute qui casse en pratique : un scalaire simple qui
    # contient « : » (une phrase française) au lieu d'un bloc replié `>-`.
    for ligne in bloc.split("\n"):
        entete = re.match(r"^([A-Za-z0-9_-]+):\s+(\S.*)$", ligne)
        if entete and ": " in entete.group(2) and entete.group(2)[0] not in "\"'":
            return [f"'{entete.group(1)}' est un scalaire simple contenant « : » — "
                    "l'écrire en bloc replié (>-)"]
    return []


def lire_plugins(repo):
    """Rend (catalogue, [plugins], problèmes) — chaque plugin porte entrée, manifeste, skills.

    Les problèmes de lecture (fichier manquant, JSON invalide) sont collectés plutôt que
    levés : `controler` les rapporte tous d'un coup.
    """
    problemes = []
    catalogue = _charger_json(os.path.join(repo, ".claude-plugin/marketplace.json"), problemes)
    plugins = []
    for entree in (catalogue or {}).get("plugins", []):
        nom = entree.get("name") or "?"
        siens = []
        source = entree.get("source")
        if not isinstance(source, str):
            siens.append(f"marketplace.json : source de {nom} non gérée ({type(source).__name__})"
                         " — attendu un chemin relatif")
            racine = repo
        else:
            racine = os.path.join(repo, re.sub(r"^\./", "", source))
        manifeste = _charger_json(os.path.join(racine, ".claude-plugin/plugin.json"), siens) \
            if isinstance(source, str) else None
        plugins.append(
            {
                "nom": nom,
                "entree": entree,
                "manifeste": manifeste,
                "racine": racine,
                "skills": _lire_skills(racine, siens) if isinstance(source, str) else [],
                "agents": sorted(glob.glob(os.path.join(racine, "agents", "*.md")))
                if isinstance(source, str) else [],
                "problemes": siens,
            }
        )
    return catalogue, plugins, problemes


def _charger_json(chemin, problemes):
    if not os.path.isfile(chemin):
        problemes.append(f"Manquant : {chemin}")
        return None
    try:
        with open(chemin, encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:  # noqa: BLE001 — le message importe plus que le type
        problemes.append(f"JSON invalide : {chemin} — {e}")
        return None


def _lire_skills(racine, problemes):
    skills = []
    for dossier in sorted(glob.glob(os.path.join(racine, "skills", "*/"))):
        nom = os.path.basename(dossier.rstrip("/"))
        chemin = os.path.join(dossier, "SKILL.md")
        if not os.path.isfile(chemin):
            problemes.append(f"{nom} : SKILL.md manquant")
            continue
        with open(chemin, encoding="utf-8") as f:
            texte = f.read()
        skills.append({"dossier": nom, "chemin": chemin, "bloc": bloc_frontmatter(texte),
                       "fm": lire_frontmatter(texte)})
    return skills


# --- Génération de la table --------------------------------------------------------------


def _cellule(valeur):
    return str(valeur or "").replace("|", "\\|")


def _ligne(skill):
    fm = skill["fm"] or {}
    return f"| `{skill['dossier']}` | {_cellule(fm.get('couche'))} | {_cellule(fm.get('moment'))} |"


def _table(lot):
    """Une table markdown : socles d'abord, puis les recettes, alphabétiques dans chaque couche."""
    ordonnes = sorted(lot, key=lambda s: (0 if (s["fm"] or {}).get("couche") == "socle" else 1,
                                          s["dossier"]))
    return "\n".join([ENTETE] + [_ligne(s) for s in ordonnes])


def _section(config, skills):
    blocs = [f"## {config['titre']}"]
    if config.get("intro"):
        blocs.append(config["intro"])
    familles = config.get("familles") or []
    if not familles:
        blocs.append(_table(skills))
        return blocs
    restants = list(skills)
    for cle, titre in familles:
        lot = [s for s in restants if (s["fm"] or {}).get("famille") == cle]
        if not lot:  # une famille vidée ne laisse pas une table à en-tête seul
            continue
        restants = [s for s in restants if s not in lot]
        blocs += [f"### {titre}", _table(lot)]
    if restants:
        blocs += [f"### {FAMILLE_PAR_DEFAUT}", _table(restants)]
    return blocs


def zone_generee(repo):
    """Le contenu qui doit se trouver entre les deux marqueurs du README."""
    _, plugins, _ = lire_plugins(repo)
    par_nom = {p["nom"]: p for p in plugins}
    blocs = []
    vus = set()
    for config in SECTIONS:
        plugin = par_nom.get(config["plugin"])
        if plugin is None:
            continue
        vus.add(config["plugin"])
        blocs += _section(config, plugin["skills"])
    for plugin in plugins:
        if plugin["nom"] in vus:
            continue
        blocs += _section({"titre": f"Skills disponibles — `{plugin['nom']}`", "familles": []},
                          plugin["skills"])
    return "\n\n".join(blocs)


def _decouper_readme(repo):
    chemin = os.path.join(repo, "README.md")
    if not os.path.isfile(chemin):
        raise ErreurDeGeneration("README.md manquant")
    with open(chemin, encoding="utf-8") as f:
        texte = f.read()
    for marqueur in (MARQUEUR_DEBUT, MARQUEUR_FIN):
        vus = texte.count(marqueur)
        if vus == 0:
            raise ErreurDeGeneration(f"README.md : marqueur {marqueur} absent")
        if vus > 1:
            raise ErreurDeGeneration(
                f"README.md : marqueur {marqueur} présent {vus} fois — la zone générée doit être "
                "unique, sinon régénérer écraserait du texte rédigé à la main")
    debut, fin = texte.find(MARQUEUR_DEBUT), texte.find(MARQUEUR_FIN)
    if fin < debut:
        raise ErreurDeGeneration(
            f"README.md : marqueurs inversés ({MARQUEUR_FIN} avant {MARQUEUR_DEBUT})")
    return chemin, texte, debut, fin


def readme_rendu(repo):
    """Rend (chemin, texte actuel, texte attendu) du README, zone générée à jour."""
    chemin, texte, debut, fin = _decouper_readme(repo)
    attendu = texte[:debut] + MARQUEUR_DEBUT + "\n\n" + zone_generee(repo) + "\n\n" + texte[fin:]
    return chemin, texte, attendu


def generer_readme(repo):
    """Réécrit la zone entre les marqueurs. Rend True si le fichier a changé."""
    chemin, texte, attendu = readme_rendu(repo)
    if attendu == texte:
        return False
    with open(chemin, "w", encoding="utf-8") as f:
        f.write(attendu)
    return True


# --- Contrôle ----------------------------------------------------------------------------


def controler(repo):
    """Rend la liste des problèmes du dépôt — vide quand tout est conforme."""
    catalogue, plugins, problemes = lire_plugins(repo)
    problemes = list(problemes)
    if catalogue is not None and not plugins:
        problemes.append("marketplace.json : aucun plugin déclaré")

    for plugin in plugins:
        nom = plugin["nom"]
        problemes += [p if p.startswith("marketplace.json") else f"{nom} : {p}"
                      for p in plugin["problemes"]]
        if plugin["entree"].get("version"):
            problemes.append(
                f"marketplace.json : 'version' ({plugin['entree']['version']}) épingle {nom} — la retirer")
        manifeste = plugin["manifeste"]
        if manifeste is not None:
            if manifeste.get("version"):
                problemes.append(
                    f"{nom}/plugin.json : 'version' ({manifeste['version']}) épingle le plugin — la retirer")
            if manifeste.get("name") != nom:
                problemes.append(
                    f"{nom}/plugin.json : name = '{manifeste.get('name')}' ≠ entrée marketplace")
        if not plugin["skills"] and not plugin["problemes"]:
            problemes.append(f"{nom} : aucun skill dans {plugin['racine']}/skills/")
        for skill in plugin["skills"]:
            problemes += _controler_skill(nom, skill)
        for agent in plugin["agents"]:
            problemes += _controler_agent(nom, agent)

    problemes += _controler_readme(repo)
    return problemes


def _controler_skill(plugin, skill):
    dossier = skill["dossier"]
    prefixe = f"{plugin}/{dossier}"
    if skill["bloc"] is None:
        return [f"{prefixe} : frontmatter absent (--- … ---)"]
    problemes = [f"{prefixe} : {p}" for p in problemes_yaml(skill["bloc"])]
    fm = skill["fm"] or {}
    nom = fm.get("name")
    if not nom:
        problemes.append(f"{prefixe} : 'name' absent du frontmatter")
    elif nom != dossier:
        problemes.append(f"{prefixe} : 'name' = '{nom}' ≠ dossier '{dossier}'")
    if not KEBAB.match(dossier):
        problemes.append(
            f"{prefixe} : nom hors kebab-case (minuscules, chiffres, tirets, sans accent)")
    if not fm.get("description"):
        problemes.append(f"{prefixe} : 'description' absente du frontmatter")
    if fm.get("version"):
        problemes.append(f"{prefixe} : 'version' dans le frontmatter — la retirer")
    couche = fm.get("couche")
    if not couche:
        problemes.append(f"{prefixe} : 'couche' absente du frontmatter (socle | recette)")
    elif couche not in COUCHES:
        problemes.append(f"{prefixe} : 'couche' = '{couche}' — attendu socle | recette")
    if not fm.get("moment"):
        problemes.append(f"{prefixe} : 'moment' absent du frontmatter (une phrase)")
    problemes += _controler_famille(prefixe, plugin, fm)
    return problemes


def _controler_famille(prefixe, plugin, fm):
    attendues = FAMILLES_ATTENDUES.get(plugin)
    famille = fm.get("famille")
    if attendues is None:
        if famille:
            return [f"{prefixe} : 'famille' = '{famille}' — les skills de {plugin} n'en portent pas"]
        return []
    if not famille:
        return [f"{prefixe} : 'famille' absente du frontmatter ({' | '.join(attendues)})"]
    if famille not in attendues:
        return [f"{prefixe} : 'famille' = '{famille}' — attendu {' | '.join(attendues)}"]
    return []


def _controler_agent(plugin, chemin):
    nom = os.path.splitext(os.path.basename(chemin))[0]
    with open(chemin, encoding="utf-8") as f:
        texte = f.read()
    bloc = bloc_frontmatter(texte)
    if bloc is None:
        return [f"{plugin}/agents/{nom} : frontmatter absent (--- … ---)"]
    problemes = [f"{plugin}/agents/{nom} : {p}" for p in problemes_yaml(bloc)]
    fm = lire_frontmatter(texte) or {}
    if fm.get("name") != nom or not fm.get("description"):
        problemes.append(
            f"{plugin}/agents/{nom} : frontmatter name (== fichier) + description requis")
    return problemes


def _controler_readme(repo):
    try:
        _, texte, attendu = readme_rendu(repo)
    except ErreurDeGeneration as e:
        return [str(e)]
    if texte != attendu:
        return ["README.md : la zone générée ne correspond plus au frontmatter — "
                "relancer `python3 scripts/skills.py readme`"]
    return []


# --- Entrée ------------------------------------------------------------------------------


def main(argv=None):
    parseur = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parseur.add_argument("commande", choices=("check", "readme"))
    parseur.add_argument("--repo", default=".", help="racine du dépôt (défaut : le dossier courant)")
    args = parseur.parse_args(argv)
    repo = os.path.abspath(args.repo)

    if args.commande == "readme":
        try:
            change = generer_readme(repo)
        except ErreurDeGeneration as e:
            print(f"ÉCHEC : {e}")
            return 1
        print("README.md : zone générée mise à jour." if change
              else "README.md : zone générée déjà à jour.")
        return 0

    problemes = controler(repo)
    if problemes:
        print("PROBLÈMES :")
        for p in problemes:
            print(" -", p)
        return 1
    _, plugins, _ = lire_plugins(repo)
    total = sum(len(p["skills"]) for p in plugins)
    lecteur = "PyYAML" if yaml is not None else "parseur de repli (PyYAML absent)"
    print(f"OK — marketplace et skills valides ({len(plugins)} plugin(s), {total} skill(s), "
          f"zone du README à jour, frontmatter lu par {lecteur}, versionnage par SHA git).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
