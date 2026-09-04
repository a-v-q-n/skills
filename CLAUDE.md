# Repo `skills` — méthodologie

Ce repo est **le dépôt unique de tous les skills AVQN**. Il publie une marketplace Claude,
`avqn`, poussée sur `a-v-q-n/skills` et branchée à claude.ai via Extensions → Marketplaces,
qui porte deux plugins :

- **`avqn-skills`** — tout le métier AVQN, en trois familles : le cycle de vie du client sur
  AVQN OS (`os.avqn.ch`), le contenu Autonomes (ressources et blog, images comprises) et la
  vidéo Contentos. Chaque famille a son socle d'écriture ; les recettes le chargent.
- **`avqn-dev`** — la méthode de dev : triage par calibre, cycle `dev` jusqu'au FF merge,
  `chantier`, `review-pr`, `apercu`, `local`, `new-project`, `gerer-les-secrets`, l'écriture et
  la relecture de skills (`avqn-skill-authoring`, `relire-un-skill`), et les sous-agents
  `revieweur` / `verificateur`. Elle ne sait rien d'un repo à l'avance : elle
  **découvre** son contrat (`CLAUDE.md` — Démarrer en local / Gate / Livrer) et marche en local
  comme en session cloud. L'infra elle-même est un connecteur (`AVQN OPS`) qui fournit des
  outils ; ses recettes vivent ici.

  **Une tension assumée.** `avqn-dev` se veut agnostique du dépôt, et ces deux skills-là sont
  spécifiques à celui-ci. Un troisième plugin pour deux skills serait du YAGNI : ils vivent dans
  `avqn-dev` parce que c'est le seul plugin publié qu'une session hors de ce dépôt charge déjà —
  et parce qu'écrire un skill *est* un geste de dev. Le jour où un troisième arrive, ils sortent.

Un repo de la flotte ne porte que **son contrat**, jamais la méthode.

**La frontière avec le serveur** : AVQN OS embarque sa propre grammaire (tool `grammaire` —
socle transverse + détail par domaine). Le fonctionnement des objets (partie, deal, projet,
facture, note…) vit là-bas et ne se redocumente jamais ici. Les skills de ce repo portent
ce que le serveur ne peut pas porter : le **craft** et le **jugement** — la voix, la méthode
d'une offre, ce qui se valide avec Manu avant d'agir.

Les principes de travail généraux vivent dans `~/.claude/CLAUDE.md`. Ce fichier ne couvre
que la production de skills dans ce repo.

## Architecture : socle et recettes

Deux couches, et une seule règle pour ranger n'importe quel skill.

- **Socle** — le *craft* transverse, réutilisable : la voix (`ecrire-comme-manu`), la plomberie
  du brouillon d'email (`deposer-un-brouillon-email`), la méthode (`travailler-sur-un-repo`). Un skill de socle ne se déclenche presque jamais seul ; les
  recettes le composent.
- **Recettes** — des skills-actions qui vont de bout en bout : `accueillir-une-prise-de-contact`,
  `emettre-une-offre`, `dev`, `local`. Une recette **orchestre** : elle route, appelle les
  outils MCP, et tire le socle.

Le grain d'une recette est **le moment de vie du client** (une prise de contact, un jalon à
facturer), jamais le geste unitaire d'un domaine (« créer un deal », « ajouter une note ») :
ces gestes sont des étapes des recettes, et leur mécanique vit dans la grammaire du serveur.

Physiquement, socle et recettes sont tous des dossiers de `skills/`. C'est le rôle et le
nommage qui les distinguent, pas l'arborescence.

### Les familles

`avqn-skills` couvre trois familles — **cycle client**, **contenu Autonomes**, **vidéo
Contentos** — chacune avec son socle d'écriture : `ecrire-comme-manu`, `ecrire-mes-ressources`
(+ `titrer-une-ressource`), `ecrire-mes-videos`. Une recette charge le socle de **sa** famille
et jamais celui d'une autre : la voix écrite, la voix des ressources et la voix parlée sont
trois crafts distincts.

Les familles ne sont pas des dossiers. `skills/` reste plat — c'est la clé `famille` du
frontmatter qui situe un skill, et la table générée du `README.md` qui les regroupe.

### Le critère : skill à part ou fichier `references/` ?

> Un bloc devient un **skill à part** quand il a un **usage indépendant** — on l'invoque seul,
> ou plusieurs recettes le réutilisent. Sinon, il reste un **fichier `references/`** de son parent.

Corollaire (YAGNI) : on ne crée pas un skill par anticipation. Un nouveau moment du cycle
(faire le point, boucler un projet…) devient un skill le jour où un vrai cas le réclame,
pas avant.

### Composition

- Une recette **charge son socle en début de corps** (« commencer par charger
  `ecrire-comme-manu` »). C'est un appel de skill à skill, non négociable.
- Les fichiers `references/` restent **à un niveau** depuis `SKILL.md` : une référence n'en
  appelle pas une autre.

## Arborescence

```
.claude-plugin/marketplace.json      Catalogue de la marketplace « avqn »
plugins/
├── avqn-skills/                      Le business (cycle de vie du client, voix)
│   ├── .claude-plugin/plugin.json    Manifeste du plugin
│   └── skills/
│       └── <nom-du-skill>/           Un skill = un dossier (socle ou recette)
│           ├── SKILL.md              Requis — la recette
│           ├── references/           Détails chargés à la demande
│           ├── templates/            Gabarits à remplir
│           ├── examples/             Sorties de référence
│           └── assets/               Fichiers statiques
└── avqn-dev/                         La méthode de dev
    ├── .claude-plugin/plugin.json
    ├── agents/<nom>.md               Sous-agents (revieweur, verificateur)
    └── skills/<nom-du-skill>/        Même anatomie ; socle = travailler-sur-un-repo
scripts/                             Outillage de dépôt
├── skills.py                        Conformité (`check`) et génération de la table (`readme`)
└── test_skills.py                   Ses tests
.claude/                             Configuration d'agent (repo-local, non publié)
├── commands/                        /new-skill, /check-skills
└── hooks/                           Accueil de session
```

L'outillage vit dans `scripts/`, **hors de `.claude/`** : Claude Code classe ce dossier-là comme
sensible (il porte hooks, commandes et réglages, donc le comportement de l'agent lui-même) et
demande confirmation à chaque écriture, même en mode `acceptEdits`. Une session autonome s'y
arrêterait net.

L'écriture d'un skill, elle, n'est plus repo-locale : `avqn-skill-authoring` et
`relire-un-skill` vivent dans `plugins/avqn-dev/skills/`, donc disponibles depuis n'importe
quelle session.

## Anatomie d'un skill

- **`SKILL.md`** (requis) : la recette, concise (sous 500 lignes). Frontmatter (`name`,
  `description`, `couche`, `moment`, et `famille` dans `avqn-skills`), puis le corps. Reste
  court — les détails vont dans `references/`.
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
- **`couche`** (frontmatter, requise) : `socle` ou `recette`. Le classement de l'architecture,
  rendu lisible par la machine — c'est la colonne « Couche » de la table du `README.md`.
- **`moment`** (frontmatter, requise) : une phrase, le moment où le skill sert. C'est la colonne
  « Moment » de la table. Le frontmatter n'est donc plus seulement `name` + `description` : il
  **est** la source de la table, et la table ne s'édite jamais à la main.
- **`famille`** (frontmatter, requise dans `avqn-skills`) : `cycle-client`, `contenu-autonomes`
  ou `video-contentos` — la section de la table. Les skills d'`avqn-dev` n'en portent pas ; une
  famille inconnue range le skill sous « Non classé » plutôt que de le perdre.
- **Blocs repliés** : `description` et `moment` s'écrivent en `>-`. Une phrase contenant « : »
  casse un scalaire YAML simple.
- **Divulgation progressive** : `SKILL.md` porte l'essentiel et pointe vers `references/` pour
  le reste. On ne charge pas tout d'un coup.
- **Outils MCP** : cités par leur nom d'usage (`invoice_render_pdf`, `mail_draft_reply`),
  accompagnés d'une formulation française de l'usage — les descriptions serveur sont
  rédigées en français, ce sont elles qui matchent quand les tools sont différés. Ne jamais
  redocumenter la mécanique d'un domaine : elle vit dans `grammaire {domaine}` côté serveur.
- **Langue et ton** : français, état-cible (décrire ce qui est, sans « désormais » ni « au
  lieu de »).

## Contrat

- **Démarrer en local** : rien à lancer — ce dépôt ne porte pas d'application. On travaille les
  fichiers depuis une session ouverte DANS le repo ; les commandes d'auteur (`/new-skill`,
  `/check-skills`) et le plugin `avqn-dev` (déclaré dans `.claude/settings.json`) s'amorcent
  seuls. Le plugin chargé vient de la marketplace **publiée** : une modification locale d'un
  skill ne prend effet dans la session qu'une fois poussée.
- **Gate** : `/check-skills` — vert avant tout push. Elle couvre le JSON de la marketplace, le
  frontmatter des skills et des agents (`couche` et `moment` compris), l'absence de champ
  `version`, la **fraîcheur de la zone générée du `README.md`**, et les tests de l'outil
  d'auteur.
- **Livrer** : le push sur `main` EST la publication (cf. *Workflow de publication*). Ni CI,
  ni image, ni déploiement.

## Workflow de publication

1. `/new-skill <nom>` — scaffolde le dossier et un `SKILL.md` pré-rempli.
2. Rédiger le skill (corps + `references/`/`templates/` au besoin), frontmatter complet.
3. La table de `README.md` **se régénère** : `python3 scripts/skills.py readme`. Elle vit
   entre `<!-- skills:début -->` et `<!-- skills:fin -->` ; rien hors des marqueurs ne bouge, et
   on n'y touche pas à la main — pour changer une ligne, on change le frontmatter du skill.
4. `/check-skills` — valider sur tous les plugins du catalogue.
5. Commit (message descriptif, emoji 🤖) + push.
6. La mise à jour se propage seule : **sans champ `version`**, chaque commit poussé est une
   version (le SHA git fait foi). Un champ `version` posé dans `plugin.json` ou dans l'entrée
   marketplace **épinglerait** le plugin — les clients garderaient leur copie tant que la
   chaîne ne change pas. Au besoin, forcer côté client : « Mettre à jour » sur le plugin, ou
   `/plugin marketplace update avqn` en CLI.

Une fois la tranche validée (`/check-skills` vert), l'agent commite et pousse de lui-même,
sans redemander.

## Métier générique

Pour l'artisanat d'un bon skill (rédiger la `description`, structurer, vérifier), s'appuyer sur
`avqn-dev:avqn-skill-authoring` ; pour le crible avant publication, sur `avqn-dev:relire-un-skill`,
qui est en lecture seule. Ce fichier ne redocumente pas ce qu'ils couvrent déjà.
