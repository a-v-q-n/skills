# Repo `skills` — méthodologie

Ce repo est une **marketplace de plugins Claude**. Il publie un plugin, `avqn-skills`,
qui embarque tous les skills AVQN. Il est poussé sur `a-v-q-n/skills` et se connecte à
claude.ai via Extensions → Marketplaces.

Les principes de travail généraux vivent dans `~/.claude/CLAUDE.md`. Ce fichier ne
couvre que la production de skills dans ce repo.

## Arborescence

```
.claude-plugin/marketplace.json      Catalogue de la marketplace « avqn »
plugins/
└── avqn-skills/
    ├── .claude-plugin/plugin.json    Manifeste du plugin
    └── skills/
        └── <nom-du-skill>/           Un skill = un dossier
            ├── SKILL.md              Requis — la recette
            ├── references/           Détails chargés à la demande
            ├── templates/            Gabarits à remplir
            ├── examples/             Sorties de référence
            └── assets/               Fichiers statiques
.claude/                             Outillage d'auteur (repo-local, non publié)
├── skills/avqn-skill-authoring/     Skill qui guide l'écriture de skills
└── commands/                        /new-skill, /check-skills
```

## Anatomie d'un skill

- **`SKILL.md`** (requis) : la recette, concise. Frontmatter `name` + `description`,
  puis le corps. Reste court — les détails vont dans `references/`.
- **`references/`** : ce qu'on charge seulement quand on en a besoin (specs longues,
  catalogues, procédures).
- **`templates/`** : artefacts à remplir (HTML, prompts, gabarits).
- **`examples/`** : sorties de référence, pour montrer le résultat attendu.
- **`assets/`** : fichiers statiques (logos, polices).

Un skill n'embarque que les dossiers utiles ; seul `SKILL.md` est obligatoire.

## Conventions

- **Nommage** : dossier en kebab-case ; le `name` du frontmatter est **identique au
  nom du dossier**.
- **`description`** (frontmatter) : en français, à la 3e personne, commence par les
  déclencheurs (« À utiliser dès que… ») et pose la limite (« NE COUVRE PAS… »).
  C'est le seul texte qui décide du déclenchement — la soigner.
- **Divulgation progressive** : `SKILL.md` porte l'essentiel et pointe vers
  `references/` pour le reste. On ne charge pas tout d'un coup.
- **Langue et ton** : français, état-cible (décrire ce qui est, sans « désormais »
  ni « au lieu de »).

## Workflow de publication

1. `/new-skill <nom>` — scaffolde le dossier et un `SKILL.md` pré-rempli.
2. Rédiger le skill (corps + `references/`/`templates/` au besoin).
3. Ajouter le skill à la table de `README.md`.
4. `/check-skills` — valider la marketplace et les skills.
5. Commit (message descriptif, emoji 🤖) + push.
6. Côté client : `/plugin marketplace update avqn`.

Aucune version à épingler : les plugins n'ont pas de champ `version`, donc chaque
commit fait foi et la mise à jour se tire directement du dernier push.

## Métier générique

Pour l'artisanat d'un bon skill (rédiger la `description`, structurer, vérifier),
s'appuyer sur `superpowers:writing-skills` et sur le skill repo-local
`avqn-skill-authoring`. Ce repo ne redocumente pas ce que ces skills couvrent déjà.
