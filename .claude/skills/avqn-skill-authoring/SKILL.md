---
name: avqn-skill-authoring
description: >-
  À utiliser dès qu'on crée, édite ou publie un skill dans ce repo (la marketplace
  « avqn » / plugin avqn-skills). Porte les conventions AVQN — emplacement, anatomie
  (SKILL.md + references/templates/examples/assets), frontmatter en français avec
  déclencheurs, divulgation progressive — et le workflow de publication
  (/new-skill → /check-skills → push → /plugin marketplace update). S'appuie sur
  superpowers:writing-skills pour le métier générique. NE COUVRE PAS l'écriture du
  contenu métier d'un skill donné.
---

# Écrire un skill AVQN

Produire un skill **on-repo** : la bonne place, la bonne anatomie, le bon frontmatter,
et le publier proprement.

## D'abord le métier générique

Pour l'artisanat d'un bon skill — rédiger une `description` qui déclenche, doser la
divulgation progressive, vérifier avant de livrer — s'appuyer sur
**`superpowers:writing-skills`**. Ce skill-ci ne le redocumente pas ; il ajoute la
couche AVQN.

## Emplacement

Un skill vit dans `plugins/avqn-skills/skills/<nom>/`. Le `<nom>` est en kebab-case et
devient le `name` du frontmatter (identiques). Scaffolder avec `/new-skill <nom>`.

## Anatomie

- **`SKILL.md`** (requis) — la recette, concise. Frontmatter puis corps.
- **`references/`** — détails chargés à la demande (specs longues, catalogues, procédures).
- **`templates/`** — artefacts à remplir.
- **`examples/`** — sorties de référence.
- **`assets/`** — fichiers statiques.

N'ajouter que les dossiers utiles ; seul `SKILL.md` est obligatoire.

## Frontmatter

- `name` : identique au nom du dossier, kebab-case.
- `description` : en français, 3e personne. Commence par les déclencheurs
  (« À utiliser dès que… ») et pose la limite (« NE COUVRE PAS… »). C'est le seul
  texte qui décide du déclenchement — la soigner.

## Corps

Concis. `SKILL.md` porte l'essentiel et renvoie vers `references/` pour le reste.
Ton français, état-cible : décrire ce qui est, sans « désormais » ni « au lieu de ».

## Publier

1. Ajouter le skill à la table de `README.md`.
2. Bumper la `version` (même valeur dans `plugin.json` et dans l'entrée `avqn-skills`
   de `marketplace.json`) — c'est ce numéro qui déclenche « Mettre à jour » côté claude.ai.
3. `/check-skills` — valider.
4. Commit 🤖 + push.
5. Côté client : « Mettre à jour » sur le plugin (ou `/plugin marketplace update avqn`).
