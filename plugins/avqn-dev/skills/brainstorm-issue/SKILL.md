---
name: brainstorm-issue
description: Brainstorme INTERACTIVEMENT une idée ou une issue brute avec Manu, puis dépose la SPEC D'INTENTION résultante dans le corps de l'issue GitHub du repo concerné. S'arrête là — Manu pose le label `ready` (l'aval humain, async). Ne code rien, ne planifie pas l'implémentation. Phase spec de chantier quand le chantier vit dans un repo ; utilisable seul pour préparer une tâche M à l'avance.
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
4. **Arrête-toi.** Dis à Manu : « pose le label `ready` quand tu valides ». Tu ne poses jamais
   `ready` toi-même — c'est le geste humain qui alimente la routine.

## Garde-fous

- Spec d'intention, pas plan : l'issue reste lisible et stable.
- Une idée trop grosse pour une issue → aide à la **découper** en plusieurs issues, chacune
  brainstormée à son tour (ou requalifie en chantier → `/avqn-dev:chantier`).
