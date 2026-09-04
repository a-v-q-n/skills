"""Tests de l'outil d'auteur `skills.py` — conformité et génération de la table du README."""

import importlib.util
import os
import shutil
import tempfile
import unittest

_ICI = os.path.dirname(os.path.abspath(__file__))
_SPEC = importlib.util.spec_from_file_location("skills", os.path.join(_ICI, "skills.py"))
skills = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(skills)


MARKETPLACE = """{
  "name": "avqn",
  "plugins": [
    { "name": "avqn-skills", "source": "./plugins/avqn-skills" },
    { "name": "avqn-dev", "source": "./plugins/avqn-dev" }
  ]
}
"""

README = """# Titre tenu à la main

Du texte avant.

{debut}
à remplacer
{fin}

## Agents

Du texte après, tenu à la main.
""".format(debut=skills.MARQUEUR_DEBUT, fin=skills.MARQUEUR_FIN)


def frontmatter(name, couche="recette", moment="Un moment.", famille=None, description="Une description."):
    lignes = ["---", f"name: {name}"]
    if description is not None:
        lignes += ["description: >-", f"  {description}"]
    if couche is not None:
        lignes += [f"couche: {couche}"]
    if moment is not None:
        lignes += ["moment: >-", f"  {moment}"]
    if famille is not None:
        lignes += [f"famille: {famille}"]
    lignes += ["---", "", "# Corps", ""]
    return "\n".join(lignes)


class BaseRepo(unittest.TestCase):
    """Un dépôt jouet : deux plugins, quelques skills, un README à marqueurs."""

    def setUp(self):
        self.repo = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.repo)
        self.ecrire(".claude-plugin/marketplace.json", MARKETPLACE)
        for plugin in ("avqn-skills", "avqn-dev"):
            self.ecrire(
                f"plugins/{plugin}/.claude-plugin/plugin.json",
                '{"name": "%s", "description": "d"}\n' % plugin,
            )
        self.skill("avqn-skills", "ecrire-comme-manu", couche="socle", famille="cycle-client",
                   moment="La voix de Manu.")
        self.skill("avqn-skills", "emettre-une-offre", couche="recette", famille="cycle-client",
                   moment="Accord de vive voix : devis puis PDF.")
        self.skill("avqn-skills", "creer-une-ressource", couche="recette",
                   famille="contenu-autonomes", moment="De la matière à la ressource.")
        self.skill("avqn-skills", "produire-la-vo", couche="recette",
                   famille="video-contentos", moment="La voix off et l'avatar.")
        self.skill("avqn-dev", "dev", couche="recette", moment="Le cycle M jusqu'au FF merge.")
        self.ecrire("README.md", README)

    def readme_pollue(self):
        """Le README courant, précédé d'une prose qui cite les deux marqueurs — deux zones."""
        return (f"# Titre\n\nUne phrase qui cite {skills.MARQUEUR_DEBUT} et "
                f"{skills.MARQUEUR_FIN}.\n\n" + self.lire("README.md"))

    def ecrire(self, chemin, contenu):
        cible = os.path.join(self.repo, chemin)
        os.makedirs(os.path.dirname(cible), exist_ok=True)
        with open(cible, "w", encoding="utf-8") as f:
            f.write(contenu)

    def lire(self, chemin):
        with open(os.path.join(self.repo, chemin), encoding="utf-8") as f:
            return f.read()

    def skill(self, plugin, nom, **kw):
        self.ecrire(f"plugins/{plugin}/skills/{nom}/SKILL.md", frontmatter(nom, **kw))

    def problemes(self):
        return skills.controler(self.repo)


class TestFrontmatter(unittest.TestCase):
    def test_lit_les_scalaires_simples_et_les_blocs_replies(self):
        texte = (
            "---\n"
            "name: relire-un-skill\n"
            "description: >-\n"
            "  Une description sur\n"
            "  deux lignes.\n"
            "couche: recette\n"
            "moment: >-\n"
            "  Un moment : avec deux-points.\n"
            "---\n\n# Corps\n"
        )
        fm = skills.lire_frontmatter(texte)
        self.assertEqual(fm["name"], "relire-un-skill")
        self.assertEqual(fm["description"], "Une description sur deux lignes.")
        self.assertEqual(fm["couche"], "recette")
        self.assertEqual(fm["moment"], "Un moment : avec deux-points.")

    def test_frontmatter_absent(self):
        self.assertIsNone(skills.lire_frontmatter("# Pas de frontmatter\n"))

    def test_scalaire_simple_avec_deux_points_est_refuse(self):
        bloc = "name: dev\ndescription: Onboarde un repo : et voilà.\n"
        self.assertTrue(skills.problemes_yaml(bloc),
                        "un scalaire simple contenant « : » n'est pas du YAML lisible")

    def test_frontmatter_lisible_ne_pose_pas_de_probleme(self):
        bloc = "name: dev\ndescription: >-\n  Une phrase : avec deux-points.\ncouche: recette\n"
        self.assertEqual(skills.problemes_yaml(bloc), [])


class TestControle(BaseRepo):
    def test_depot_conforme(self):
        skills.generer_readme(self.repo)
        self.assertEqual(self.problemes(), [])

    def test_couche_absente(self):
        self.skill("avqn-skills", "ecrire-comme-manu", couche=None, famille="cycle-client")
        skills.generer_readme(self.repo)
        self.assertTrue(any("couche" in p and "ecrire-comme-manu" in p for p in self.problemes()))

    def test_couche_invalide(self):
        self.skill("avqn-skills", "ecrire-comme-manu", couche="socle-bis", famille="cycle-client")
        skills.generer_readme(self.repo)
        self.assertTrue(any("socle-bis" in p for p in self.problemes()))

    def test_moment_absent(self):
        self.skill("avqn-dev", "dev", moment=None)
        skills.generer_readme(self.repo)
        self.assertTrue(any("moment" in p and "dev" in p for p in self.problemes()))

    def test_champ_version_refuse(self):
        self.ecrire("plugins/avqn-dev/.claude-plugin/plugin.json",
                    '{"name": "avqn-dev", "version": "1.2.3"}\n')
        skills.generer_readme(self.repo)
        self.assertTrue(any("version" in p for p in self.problemes()))

    def test_name_different_du_dossier(self):
        self.ecrire("plugins/avqn-dev/skills/dev/SKILL.md", frontmatter("developpement"))
        skills.generer_readme(self.repo)
        self.assertTrue(any("developpement" in p for p in self.problemes()))

    def test_name_hors_kebab_case(self):
        self.skill("avqn-dev", "Dev_Rapide", couche="recette", moment="m")
        skills.generer_readme(self.repo)
        self.assertTrue(any("Dev_Rapide" in p for p in self.problemes()))

    def test_marqueurs_absents(self):
        self.ecrire("README.md", "# Sans marqueurs\n")
        self.assertTrue(any("marqueur" in p.lower() for p in self.problemes()))

    def test_marqueurs_en_double(self):
        """Deux zones : régénérer écraserait la prose entre la première paire de marqueurs."""
        skills.generer_readme(self.repo)
        self.ecrire("README.md", self.readme_pollue())
        self.assertTrue(any("2 fois" in p for p in self.problemes()), self.problemes())

    def test_generation_refusee_si_marqueurs_en_double(self):
        skills.generer_readme(self.repo)
        pollue = self.readme_pollue()
        self.ecrire("README.md", pollue)
        with self.assertRaises(skills.ErreurDeGeneration):
            skills.generer_readme(self.repo)
        self.assertEqual(self.lire("README.md"), pollue, "rien n'a été écrasé")

    def test_marqueurs_inverses(self):
        self.ecrire("README.md", f"# T\n\n{skills.MARQUEUR_FIN}\n\n{skills.MARQUEUR_DEBUT}\n")
        self.assertTrue(any("inversés" in p for p in self.problemes()))

    def test_check_vert_implique_readme_stable(self):
        """Une gate verte garantit qu'une régénération ne touchera pas le fichier."""
        skills.generer_readme(self.repo)
        self.assertEqual(self.problemes(), [])
        self.assertFalse(skills.generer_readme(self.repo))

    def test_famille_absente_dans_avqn_skills(self):
        self.skill("avqn-skills", "sans-famille", couche="recette", moment="m")
        skills.generer_readme(self.repo)
        self.assertTrue(any("famille" in p and "sans-famille" in p for p in self.problemes()))

    def test_famille_inconnue_dans_avqn_skills(self):
        self.skill("avqn-skills", "famille-tordue", couche="recette", famille="cycle-clients",
                   moment="m")
        skills.generer_readme(self.repo)
        self.assertTrue(any("cycle-clients" in p for p in self.problemes()))

    def test_famille_posee_sur_un_skill_avqn_dev(self):
        self.skill("avqn-dev", "dev", couche="recette", moment="m", famille="cycle-client")
        skills.generer_readme(self.repo)
        self.assertTrue(any("n'en portent pas" in p for p in self.problemes()))

    def test_skill_md_manquant(self):
        os.makedirs(os.path.join(self.repo, "plugins/avqn-dev/skills/fantome"), exist_ok=True)
        skills.generer_readme(self.repo)
        self.assertTrue(any("SKILL.md manquant" in p for p in self.problemes()))

    def test_description_absente(self):
        self.skill("avqn-dev", "dev", couche="recette", moment="m", description=None)
        skills.generer_readme(self.repo)
        self.assertTrue(any("description" in p for p in self.problemes()))

    def test_frontmatter_illisible_par_yaml(self):
        """Une phrase avec « : » en scalaire simple : le vrai chargeur de skills la refuse."""
        self.ecrire("plugins/avqn-dev/skills/dev/SKILL.md",
                    "---\nname: dev\ndescription: Une phrase : avec deux-points.\n"
                    "couche: recette\nmoment: >-\n  m\n---\n\n# Corps\n")
        skills.generer_readme(self.repo)
        self.assertTrue(any("dev" in p for p in self.problemes()), self.problemes())

    def test_zone_perimee(self):
        skills.generer_readme(self.repo)
        self.skill("avqn-dev", "dev", couche="recette", moment="Un moment tout neuf.")
        problemes = self.problemes()
        self.assertTrue(any("README" in p for p in problemes), problemes)

    def test_zone_rafraichie_apres_regeneration(self):
        skills.generer_readme(self.repo)
        self.skill("avqn-dev", "dev", couche="recette", moment="Un moment tout neuf.")
        skills.generer_readme(self.repo)
        self.assertEqual(self.problemes(), [])
        self.assertIn("Un moment tout neuf.", self.lire("README.md"))


class TestGeneration(BaseRepo):
    def test_ne_touche_rien_hors_des_marqueurs(self):
        skills.generer_readme(self.repo)
        texte = self.lire("README.md")
        avant, reste = texte.split(skills.MARQUEUR_DEBUT, 1)
        _, apres = reste.split(skills.MARQUEUR_FIN, 1)
        self.assertEqual(avant, "# Titre tenu à la main\n\nDu texte avant.\n\n")
        self.assertEqual(apres, "\n\n## Agents\n\nDu texte après, tenu à la main.\n")

    def test_une_table_par_famille_dans_l_ordre(self):
        zone = skills.zone_generee(self.repo)
        self.assertIn("### Cycle de vie du client — AVQN OS", zone)
        self.assertIn("### Contenu Autonomes — ressources et blog", zone)
        self.assertLess(zone.index("Cycle de vie du client"), zone.index("Contenu Autonomes"))
        self.assertLess(zone.index("Contenu Autonomes"), zone.index("Vidéo Contentos"))
        self.assertLess(zone.index("`avqn-skills`"), zone.index("`avqn-dev`"))

    def test_socle_avant_recette_puis_alphabetique(self):
        self.skill("avqn-skills", "accueillir-un-contact", couche="recette",
                   famille="cycle-client", moment="Une prise de contact.")
        zone = skills.zone_generee(self.repo)
        self.assertLess(zone.index("`ecrire-comme-manu`"), zone.index("`accueillir-un-contact`"))
        self.assertLess(zone.index("`accueillir-un-contact`"), zone.index("`emettre-une-offre`"))

    def test_le_moment_du_frontmatter_arrive_en_colonne(self):
        zone = skills.zone_generee(self.repo)
        self.assertIn("| `emettre-une-offre` | recette | Accord de vive voix : devis puis PDF. |",
                      zone)

    def test_famille_vide_ne_laisse_pas_de_table_orpheline(self):
        os.remove(os.path.join(self.repo,
                               "plugins/avqn-skills/skills/produire-la-vo/SKILL.md"))
        os.rmdir(os.path.join(self.repo, "plugins/avqn-skills/skills/produire-la-vo"))
        zone = skills.zone_generee(self.repo)
        self.assertNotIn("Vidéo Contentos", zone)

    def test_famille_inconnue_ne_perd_pas_le_skill(self):
        self.skill("avqn-skills", "skill-orphelin", couche="recette", famille="hors-sol",
                   moment="Un moment orphelin.")
        zone = skills.zone_generee(self.repo)
        self.assertIn("`skill-orphelin`", zone)
        self.assertIn("Non classé", zone)

    def test_barre_verticale_echappee(self):
        self.skill("avqn-dev", "dev", couche="recette", moment="Un a | b tordu.")
        zone = skills.zone_generee(self.repo)
        self.assertIn("Un a \\| b tordu.", zone)

    def test_generation_idempotente(self):
        skills.generer_readme(self.repo)
        premier = self.lire("README.md")
        skills.generer_readme(self.repo)
        self.assertEqual(premier, self.lire("README.md"))

    def test_generation_sans_marqueurs_echoue_sans_ecrire(self):
        self.ecrire("README.md", "# Sans marqueurs\n")
        with self.assertRaises(skills.ErreurDeGeneration):
            skills.generer_readme(self.repo)
        self.assertEqual(self.lire("README.md"), "# Sans marqueurs\n")


if __name__ == "__main__":
    unittest.main()
