#!/usr/bin/env python3
"""Statistiques objectives d'une ressource Autonomes.

Usage :
    python3 stats.py ressource.json            # le JSON renvoyé par ressources_get
    python3 stats.py fichier-de-travail.md     # un fichier de travail annoté [text] [steps] [image: …]

Sort un rapport texte : mots par page, modules par type, ratio image/mots,
tics interdits (tiret cadratin, « , et »), vouvoiement, liens internes, titres de pages.
Ne juge pas : il compte. Le jugement est dans SKILL.md.
"""
import json, re, sys
from collections import Counter

TIRETS = ["—", "–"]
VOUS = re.compile(r"\b(vous|votre|vos)\b", re.I)
TU = re.compile(r"\b(tu|toi|ton|ta|tes)\b", re.I)
LIEN = re.compile(r"/r/([a-z0-9-]+)")
VIRGULE_ET = re.compile(r",\s+et\b")
MOTS = lambda s: len(re.findall(r"\S+", s))


def texte_du_module(m):
    t, c = m.get("type"), m.get("content", {})
    if t == "steps":
        return " ".join(s.get("title", "") + " " + s.get("markdown", "") for s in c.get("steps", []))
    if t == "comparison":
        return " ".join(col.get("title", "") + " " + col.get("markdown", "") for col in c.get("columns", []))
    if t == "image":
        return ""  # alt et caption ne comptent pas dans les mots lus
    return " ".join(str(v) for v in c.values() if isinstance(v, str))


def analyser_json(d):
    pages = d.get("pages", [])
    print(f"RESSOURCE  {d.get('title')!r}  slug={d.get('slug')}  type={[t for t in d.get('tags', []) if t.startswith('type:')]}")
    print(f"description : {MOTS(d.get('description') or '')} mots ; cover : {'oui' if d.get('coverImageUrl') else 'non'} ; tags : {d.get('tags')}")
    total, images, types, tout = 0, 0, Counter(), []
    print("\nPAGES")
    for p in sorted(pages, key=lambda p: (p.get("parentId") is not None, p.get("position", 0))):
        mots, imgs, tps = 0, 0, []
        for m in p.get("modules", []):
            tps.append(m["type"]); types[m["type"]] += 1
            if m["type"] == "image":
                imgs += 1
                if not m["content"].get("alt"): print(f"  ! image sans alt dans {p.get('slug')}")
                if not m["content"].get("caption"): print(f"  ! image sans caption dans {p.get('slug')}")
            txt = texte_du_module(m); mots += MOTS(txt)
            if m["type"] not in ("prompt", "code"):  # un prompt tutoie Claude, un code n'a pas d'adresse
                tout.append(txt)
        total += mots; images += imgs
        niveau = "racine" if not p.get("parentId") else "  sous-page"
        callouts = tps.count("callout"); acc = tps.count("accordion")
        drapeaux = []
        if callouts > 1: drapeaux.append(f"{callouts} callouts")
        if acc: drapeaux.append(f"{acc} accordion")
        if any(t in (p.get("title") or "") for t in TIRETS) or re.match(r"^(Étape|Etape)\s*\d", p.get("title") or ""): drapeaux.append("titre de page à revoir")
        print(f"  {niveau:10} {p.get('slug'):40} {mots:5} mots  {imgs:2} img  [{', '.join(tps)}]" + (f"   <- {'; '.join(drapeaux)}" if drapeaux else ""))
    texte = "\n".join(tout) + "\n" + (d.get("description") or "") + "\n" + (d.get("title") or "")
    print(f"\nTOTAL  {total} mots, {len(pages)} pages, {images} images" + (f" (1 image pour {total // max(images, 1)} mots)" if images else " (aucune image)"))
    print("MODULES ", dict(types))
    rapport_texte(texte, [p.get("title") for p in pages])


def analyser_md(s):
    modules = re.findall(r"^\s*`?\[(\w+)", s, re.M)
    types = Counter(m.lower() for m in modules)
    print(f"FICHIER DE TRAVAIL  {MOTS(s)} mots bruts (annotations comprises), modules annotés : {dict(types)}")
    rapport_texte(s, [])


def rapport_texte(texte, titres):
    print("\nTICS ET ADRESSE")
    n_tirets = sum(texte.count(t) for t in TIRETS)
    print(f"  tirets cadratins/demi-cadratins : {n_tirets}")
    print(f"  « , et » : {len(VIRGULE_ET.findall(texte))}")
    v, t = len(VOUS.findall(texte)), len(TU.findall(texte))
    adresse = "tu" if t and not v else "vous" if v and not t else "MÉLANGE" if v and t else "aucune"
    print(f"  vouvoiement : {v} occurrences ; tutoiement : {t} ; adresse dominante : {adresse}")
    for motif in ["Ce n'est pas", "change tout", "une fois pour toutes", "complet", "professionnel", "Plongeons", "Direction ", "on y revien", "comme on l'a vu", "ne les sautez pas", "ne saute pas"]:
        n = len(re.findall(re.escape(motif), texte, re.I))
        if n: print(f"  motif suspect « {motif} » : {n}")
    liens = LIEN.findall(texte)
    print(f"\nLIENS INTERNES  {len(liens)} ({', '.join(sorted(set(liens))) or 'aucun'})")
    if titres:
        print("\nTITRES DE PAGES")
        for t in titres: print(f"  - {t}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    chemin = sys.argv[1]
    contenu = open(chemin, encoding="utf-8").read()
    if chemin.endswith(".json") or contenu.lstrip().startswith("{"):
        analyser_json(json.loads(contenu))
    else:
        analyser_md(contenu)
