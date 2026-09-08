---
name: brainstorm-issue
description: Brainstorme INTERACTIVEMENT une idée ou une issue brute avec Manu, puis dépose la SPEC D'INTENTION résultante dans le corps de l'issue GitHub du repo concerné. S'arrête là — l'aval humain est le lancement (`ops:dev_lancer`), un second geste. Ne code rien, ne planifie pas l'implémentation. Phase spec de chantier quand le chantier vit dans un repo ; utilisable seul pour préparer une tâche M à l'avance.
couche: recette
moment: >-
  De l'idée floue à la spec d'intention dans l'issue GitHub.
---

# Brainstorm Issue — de l'idée floue à la spec dans l'issue

Transforme une intention floue en **spec d'intention** claire, persistée dans l'issue GitHub.
Interactif par nature : on ne pré-brainstorme jamais une issue en autonome.

## Procédure

1. **Cible** : une issue existante (numéro fourni), ou une idée → crée d'abord l'issue
   (`gh issue create` — titre court, corps = l'idée brute).
2. **Brainstorm** : la discipline de la phase 1 de `/avqn-dev:chantier` — contexte d'abord, une question
   à la fois, 2-3 approches avec trade-offs, design validé section par section. **Ne code pas,
   ne propose pas de plan technique** avant l'accord sur le design.
3. **Dépose la spec dans l'issue** (`gh issue edit --body`) au format spec d'intention :
   - **Quoi** : le comportement/résultat attendu (pour du front : le rendu visé).
   - **Pourquoi** : le besoin, la valeur.
   - **Critères d'acceptation** : cases à cocher — comment on saura que c'est fait.
   - **Hors-périmètre** : ce qu'on ne fait pas.
   - **Pas de plan d'implémentation** (fichiers, étapes) — c'est le travail de `/avqn-dev:dev`.
4. **Arrête-toi.** Rends le lien de l'issue. L'aval humain est le lancement lui-même, un second
   geste, explicite : Manu tire `ops:dev_lancer` sur cette issue depuis n'importe quelle
   conversation claude.ai, quand il la juge bonne à lancer. Aucun label ne marque ce feu vert.

## Garde-fous

- Spec d'intention, pas plan : l'issue reste lisible et stable.
- Une idée trop grosse pour une issue → aide à la **découper** en plusieurs issues, chacune
  brainstormée à son tour (ou requalifie en chantier → `/avqn-dev:chantier`).
