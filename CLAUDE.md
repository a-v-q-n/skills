# Repo `skills` — méthodologie

Ce repo est **le dépôt unique de tous les skills AVQN**. Il publie une marketplace Claude
avec un seul plugin, `avqn-skills`, poussé sur `a-v-q-n/skills` et branché à claude.ai via
Extensions → Marketplaces.

Tous les skills vivent ici. Les MCP (contentos, avqn-os, médiathèque…) ne fournissent que
des **outils** ; les **recettes** qui les pilotent sont des skills de ce repo.

**Périmètre** : production de média et gestion du business. L'infra et le dev (Coolify,
Hetzner, DNS, backups) restent dans Claude Code et n'entrent pas ici.

Les principes de travail généraux vivent dans `~/.claude/CLAUDE.md`. Ce fichier ne couvre
que la production de skills dans ce repo.

## Architecture : socle et recettes

Deux couches, et une seule règle pour ranger n'importe quel skill.

- **Socle** — le *craft* transverse, réutilisable : la voix (`ecrire-comme-manu`), le design
  (la charte visuelle). Un skill de socle ne se déclenche presque jamais seul ; les recettes
  le composent.
- **Recettes** — des skills-actions qui vont de bout en bout : `creer-un-post`,
  `ecrire-pour-linkedin`, `creer-un-visuel`, `creer-une-ressource`. Une recette **orchestre** :
  elle route, appelle les outils MCP, et tire le socle.

Physiquement, socle et recettes sont tous des dossiers de `skills/`. C'est le rôle et le
nommage qui les distinguent, pas l'arborescence.

### Le critère : skill à part ou fichier `references/` ?

> Un bloc devient un **skill à part** quand il a un **usage indépendant** — on l'invoque seul,
> ou plusieurs recettes le réutilisent. Sinon, il reste un **fichier `references/`** de son parent.

Corollaire (YAGNI) : on ne crée pas un skill par anticipation. Un nouveau canal ou format
(Instagram, YouTube…) devient un skill fin le jour où on en écrit un vrai, pas avant.

### Composition

- Une recette **charge son socle en début de corps** (« commencer par charger
  `ecrire-comme-manu` »). C'est un appel de skill à skill, non négociable.
- Les fichiers `references/` restent **à un niveau** depuis `SKILL.md` : une référence n'en
  appelle pas une autre.

## Arborescence

```
.claude-plugin/marketplace.json      Catalogue de la marketplace « avqn »
plugins/
└── avqn-skills/
    ├── .claude-plugin/plugin.json    Manifeste du plugin
    └── skills/
        └── <nom-du-skill>/           Un skill = un dossier (socle ou recette)
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

- **`SKILL.md`** (requis) : la recette, concise (sous 500 lignes). Frontmatter `name` +
  `description`, puis le corps. Reste court — les détails vont dans `references/`.
- **`references/`** : ce qu'on charge seulement quand on en a besoin (specs longues,
  catalogues, procédures).
- **`templates/`** : artefacts à remplir (HTML, prompts, gabarits).
- **`examples/`** : sorties de référence, pour montrer le résultat attendu.
- **`assets/`** : fichiers statiques (logos, polices).

Un skill n'embarque que les dossiers utiles ; seul `SKILL.md` est obligatoire.

## Conventions

- **Nommage** : dossier en kebab-case ; le `name` du frontmatter est **identique au nom du
  dossier**. Verbe d'action en tête, sans accent dans l'identifiant (`ecrire-…`, `creer-…`) :
  le `name` n'accepte que minuscules, chiffres et tirets.
- **`description`** (frontmatter) : en français, à la 3e personne, commence par les déclencheurs
  (« À utiliser dès que… ») et pose la limite (« NE COUVRE PAS… »). C'est le seul texte qui
  décide du déclenchement — la soigner.
- **Divulgation progressive** : `SKILL.md` porte l'essentiel et pointe vers `references/` pour
  le reste. On ne charge pas tout d'un coup.
- **Outils MCP** : toujours en nom qualifié `Serveur:outil` pour éviter les « tool not found ».
- **Langue et ton** : français, état-cible (décrire ce qui est, sans « désormais » ni « au
  lieu de »).

## Workflow de publication

1. `/new-skill <nom>` — scaffolde le dossier et un `SKILL.md` pré-rempli.
2. Rédiger le skill (corps + `references/`/`templates/` au besoin).
3. Ajouter le skill à la table de `README.md`.
4. **Bumper la version** : même valeur dans `plugins/avqn-skills/.claude-plugin/plugin.json`
   et dans l'entrée `avqn-skills` de `.claude-plugin/marketplace.json`. C'est ce numéro qui
   déclenche le bouton « Mettre à jour » côté claude.ai — sans bump, la mise à jour ne se
   propage pas.
5. `/check-skills` — valider (JSON, frontmatter, versions cohérentes).
6. Commit (message descriptif, emoji 🤖) + push.
7. Côté client : cliquer « Mettre à jour » sur le plugin (ou `/plugin marketplace update avqn`
   en CLI).

Une fois la tranche validée (`/check-skills` vert), l'agent commite et pousse de lui-même,
sans redemander.

## Métier générique

Pour l'artisanat d'un bon skill (rédiger la `description`, structurer, vérifier), s'appuyer
sur `superpowers:writing-skills` et sur le skill repo-local `avqn-skill-authoring`. Ce repo
ne redocumente pas ce que ces skills couvrent déjà.
