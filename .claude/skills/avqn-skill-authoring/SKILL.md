---
name: avqn-skill-authoring
description: >-
  À utiliser dès qu'on crée, édite ou publie un skill dans ce repo (la marketplace
  « avqn » / plugin avqn-skills). Porte l'architecture AVQN — socle vs recettes, le
  critère skill-ou-référence, la composition — et les conventions maison : anatomie
  (SKILL.md + references/templates/examples/assets), frontmatter en français avec
  déclencheurs, divulgation progressive, workflow de publication (/new-skill →
  /check-skills → push → /plugin marketplace update). S'appuie sur
  superpowers:writing-skills pour le métier générique. NE COUVRE PAS l'écriture du
  contenu métier d'un skill donné.
---

# Écrire un skill AVQN

Produire un skill **on-repo** : le bien classer, lui donner la bonne anatomie et le bon
frontmatter, puis le publier proprement. L'architecture d'ensemble (socle/recettes, périmètre)
vit dans `CLAUDE.md` ; ce skill l'applique au geste de création.

## 1. Classer d'abord : socle ou recette ?

Avant d'écrire une ligne, situer le skill.

- **Recette** — une action de bout en bout (`creer-un-post`, `ecrire-pour-linkedin`). Elle
  orchestre : elle route, appelle les outils MCP, et compose le socle.
- **Socle** — un *craft* transverse réutilisé par plusieurs recettes (`ecrire-comme-manu`).

Puis trancher skill-à-part contre simple fichier avec **le critère** :

> Usage indépendant (invoqué seul, ou réutilisé par plusieurs recettes) → **skill**.
> Sinon → **fichier `references/`** du parent.

Ne pas créer par anticipation : un format ou un canal devient un skill le jour où on en écrit
un vrai, pas avant.

## 2. Le métier générique

Pour l'artisanat — une `description` qui déclenche, doser la divulgation progressive, vérifier
avant de livrer — s'appuyer sur **`superpowers:writing-skills`**. Ce skill-ci ne le redocumente
pas ; il ajoute la couche AVQN.

## 3. Emplacement et anatomie

Un skill vit dans `plugins/avqn-skills/skills/<nom>/`. Le `<nom>` est en kebab-case et devient
le `name` du frontmatter (identiques). Scaffolder avec `/new-skill <nom>`.

- **`SKILL.md`** (requis) — la recette, concise (sous 500 lignes). Frontmatter puis corps.
- **`references/`** — détails chargés à la demande, **à un niveau** depuis `SKILL.md`.
- **`templates/`** — artefacts à remplir. **`examples/`** — sorties de référence.
  **`assets/`** — fichiers statiques.

N'ajouter que les dossiers utiles ; seul `SKILL.md` est obligatoire.

## 4. Frontmatter

- `name` : identique au dossier, kebab-case, verbe d'action en tête, sans accent
  (`ecrire-…`, `creer-…`) — minuscules, chiffres, tirets seulement.
- `description` : en français, 3e personne. Déclencheurs (« À utiliser dès que… ») + limite
  (« NE COUVRE PAS… »). C'est le seul texte qui décide du déclenchement — la soigner.

## 5. Corps et composition

Concis, état-cible : décrire ce qui est, sans « désormais » ni « au lieu de ». `SKILL.md` porte
l'essentiel et renvoie vers `references/` pour le reste.

Une **recette compose son socle** : écrire en tête du corps, noir sur blanc, « commencer par
charger `ecrire-comme-manu` » (ou le socle concerné). Les outils MCP se citent en nom qualifié
`Serveur:outil`.

## 6. Publier

1. Ajouter le skill à la table de `README.md`.
2. Bumper la `version` (même valeur dans `plugin.json` et dans l'entrée `avqn-skills` de
   `marketplace.json`) — ce numéro déclenche « Mettre à jour » côté claude.ai.
3. `/check-skills` — valider.
4. Commit 🤖 + push.
5. Côté client : « Mettre à jour » sur le plugin (ou `/plugin marketplace update avqn`).
