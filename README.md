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

1. Créer `plugins/avqn-skills/skills/<nom-du-skill>/SKILL.md`
   (frontmatter `name` + `description`, puis les ressources/templates au besoin).
2. Bumper `version` dans `plugin.json` et dans l'entrée `avqn-skills` de
   `marketplace.json`.
3. Commiter et pousser. Les skills du dossier `skills/` sont découverts
   automatiquement — rien à déclarer.

## Skills disponibles

| Skill | Rôle |
| :---- | :--- |
| `avqn-social-visuals` | Assets visuels réseaux sociaux dans la charte AVQN (HTML→PNG, images IA, carrousels PDF). |
