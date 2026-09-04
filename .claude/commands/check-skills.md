---
description: Valide la marketplace, les skills et la fraîcheur de la table du README
---

La gate du dépôt. Exécute ce bash depuis la racine, puis résume : si tout est OK, le
confirmer ; sinon, lister les problèmes et proposer la correction de chacun.

```bash
python3 scripts/skills.py check && python3 -m unittest discover -s scripts -p 'test_*.py'
```

Le premier contrôle porte sur le dépôt : JSON de la marketplace et des `plugin.json`,
frontmatter de chaque skill (`name` égal au dossier et en kebab-case, `description`, `couche`,
`moment`, et `famille` — requise sur tout skill d'`avqn-skills`, refusée sur `avqn-dev`),
frontmatter des agents, absence de champ `version` où que ce soit, et **fraîcheur de la zone
générée du `README.md`**. Le second contrôle porte sur l'outil lui-même.

Une zone périmée se règle en régénérant, jamais en éditant la table à la main :

```bash
python3 scripts/skills.py readme
```
