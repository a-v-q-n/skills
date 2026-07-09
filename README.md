# AVQN — Skills

Marketplace de plugins Claude qui regroupe les skills AVQN. Un seul plugin,
`avqn-skills`, embarque toutes les recettes maison.

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
        └── avqn-social-visuals/     Un skill = un dossier avec un SKILL.md
```

## Ajouter un skill

1. `/new-skill <nom>` — scaffolde le dossier et un `SKILL.md` pré-rempli.
2. Rédiger le skill (corps + `references/`/`templates/` au besoin) et l'ajouter à la
   table ci-dessous.
3. `/check-skills` — valider, puis commiter et pousser.

Les skills du dossier `skills/` sont découverts automatiquement — rien à déclarer.
Aucune version à gérer : chaque push devient la nouvelle version, tirée côté client
par `/plugin marketplace update avqn`. La méthodologie complète est dans `CLAUDE.md`.

## Skills disponibles

| Skill | Rôle |
| :---- | :--- |
| `avqn-social-visuals` | Assets visuels réseaux sociaux dans la charte AVQN (HTML→PNG, images IA, carrousels PDF). |
