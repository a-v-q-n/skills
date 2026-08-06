# AVQN — Skills

Marketplace de plugins Claude qui regroupe les skills AVQN. Un seul plugin,
`avqn-skills`, embarque le craft du business : la voix de Manu, les canaux d'écriture,
et les recettes qui orchestrent AVQN OS (`os.avqn.ch`).

## Installer dans Claude

### Depuis claude.ai (Extensions → Marketplaces)

1. **Ajouter une marketplace** avec le dépôt `a-v-q-n/skills`.
2. Installer le plugin **avqn-skills** dans la liste.

### Depuis Claude Code (CLI)

```bash
/plugin marketplace add a-v-q-n/skills
/plugin install avqn-skills@avqn
```

Mettre à jour après un push :

```bash
/plugin marketplace update avqn
```

## Structure

```
.claude-plugin/marketplace.json     Catalogue de la marketplace « avqn »
plugins/
└── avqn-skills/
    ├── .claude-plugin/plugin.json   Manifeste du plugin
    └── skills/
        └── <nom-du-skill>/          Un skill = un dossier (socle ou recette)
```

## Ajouter un skill

1. `/new-skill <nom>` — scaffolde le dossier et un `SKILL.md` pré-rempli.
2. Rédiger le skill (corps + `references/`/`templates/` au besoin) et l'ajouter à la
   table ci-dessous.
3. `/check-skills` — valider, puis commiter et pousser.

Les skills du dossier `skills/` sont découverts automatiquement — rien à déclarer.
Pas de champ `version` : chaque commit poussé est une version (SHA git) et la mise à jour
se propage seule côté claude.ai (au besoin, « Mettre à jour » / `/plugin marketplace update
avqn` force le rafraîchissement). La méthodologie complète est dans `CLAUDE.md`.

## Skills disponibles

| Skill | Couche | Rôle |
| :---- | :----- | :--- |
| `ecrire-comme-manu` | socle | La voix de Manu : essence, règles non négociables, lexique, adresse. Chargé par les skills d'écriture. |
| `ecrire-pour-linkedin` | recette | Rédige un post LinkedIn dans la voix de Manu. |
| `ecrire-pour-threads` | recette | Rédige un post Threads (court, spontané, chaînable) dans la voix de Manu. |
| `emettre-une-offre` | recette | Transforme un accord de vive voix en proposition écrite : devis, validation, PDF, email. Orchestre AVQN OS, charge la voix. |
