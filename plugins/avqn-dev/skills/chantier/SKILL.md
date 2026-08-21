---
name: chantier
description: >-
  Discipline complète pour un chantier (calibre L) — travail multi-jours ou multi-repos, schéma
  d'une base partagée, nouvelle app, ou ambiguïté produit. Enchaîne brainstorm (design validé
  AVANT tout code) → spec persistée (issue via brainstorm-issue) → plan en étapes courtes
  vérifiables (docs/plans du repo pivot) → exécution étape par étape avec checkpoints → review
  renforcée avant merge. À déclencher dès que le triage donne L ; ne pas l'imposer aux tâches M
  (elles vont direct à dev).
---

# Chantier — la grosse artillerie, seulement quand elle rapporte

Charge d'abord `travailler-sur-un-repo`. Cinq phases. La discipline est stricte sur **l'ordre**
(pas de code avant design validé), légère sur la forme (pas de cérémonie pour la cérémonie).

## 1. Brainstorm — comprendre avant de construire

Avec Manu, en dialogue :
- Explore le contexte d'abord (code, docs, issues) pour poser des questions informées.
- **Une question à la fois**, en commençant par le vrai problème — pas la solution supposée.
- Propose **2-3 approches** avec leurs trade-offs ; recommande-en une, dis pourquoi.
- Présente le design retenu **par sections** et fais valider au fur et à mesure.
- **Aucun code tant que le design n'est pas validé.**

## 2. Spec — persister le design

- Le chantier vit dans un repo → `/avqn-dev:brainstorm-issue` : la spec d'intention va dans l'issue
  GitHub, et Manu pose le label `ready` pour valider.
- Chantier transverse (plusieurs repos, ou la méthode elle-même) → issue dans le **repo pivot**
  (le premier à livrer ; `a-v-q-n/skills` quand c'est la méthode).
- Format : **Quoi** (comportement/résultat attendu) · **Pourquoi** · **Critères d'acceptation**
  (cases à cocher) · **Hors-périmètre**. Pas de plan d'implémentation dans la spec.

## 3. Plan — découper en étapes vérifiables

`docs/plans/AAAA-MM-JJ-<slug>.md` dans le repo pivot. Chaque étape :
- est courte, **committable seule**, et laisse chaque repo touché dans un état sain ;
- a sa **preuve de done** (test, commande, capture — décidée à l'écriture du plan) ;
- équivaut à un calibre M : elle se déroulera avec la discipline `/avqn-dev:dev`.

Multi-repos → ordre de merge explicite (les dépendances d'abord, ex. `packages/db` avant l'app,
un provider avant son consommateur).

## 4. Exécution — étape par étape, avec checkpoints

- Une étape à la fois : cycle `/avqn-dev:dev` (TDD, gate, review, PR, CI, FF merge) ou commits
  jalonnés sur la branche du chantier si les étapes ne sont pas livrables séparément.
- **Checkpoint** à chaque fin d'étape : coche le plan, point d'avancement bref à Manu.
- **Si ça dérape** (étape qui gonfle, hypothèse du design invalidée) : **stop**, retour au plan —
  replanifie ou re-brainstorme la section touchée. Ne t'entête pas.

## 5. Clôture

- **Review renforcée** : `/avqn-dev:review-pr` en mode chantier (trois lentilles parallèles).
- **Vérification** : agent `verificateur` sur chaque critère d'acceptation de la spec.
- Bilan : critères cochés dans l'issue, docs du repo mises à jour, restes éventuels notés
  (nouvelles issues, pas de « on verra »).

## Garde-fous

- Le plan est un document vivant : on le met à jour, on ne le contourne pas en silence.
- Une étape qui dépasse ~une session → la redécouper.
- Spec et plan décrivent **l'état cible** (règle doc de Manu : instantané, pas historique) ;
  l'historique vit dans git.
