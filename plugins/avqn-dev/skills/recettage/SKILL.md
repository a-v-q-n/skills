---
name: recettage
description: >-
  Vide la file des PR ouvertes d'un repo en UNE livraison — inventaire des PR avec leur état,
  aval de Manu sur le lot, puis chaque PR rebasée à son étage, gate locale et gate CI, et un seul
  push main qui déclenche la livraison du repo. Termine par la vérification de la cible et le
  ménage des branches et worktrees. À utiliser quand plusieurs PR attendent (« recette les PR »,
  « merge tout et déploie ») ; une PR seule se termine par le cycle `dev`.
---

# Recettage — la file des PR en une seule livraison

Charge d'abord `travailler-sur-un-repo` : le contrat du repo (`## Gate`, `## Livrer`, ses
invariants) et la surface. Ce skill **livre** — il finit par un push `main`, qui déclenche seul ce
que le repo déploie. Tu ne déploies jamais à la main.

Le lot est reconstruit **en local, étage par étage**, puis poussé une fois. Une CI, une livraison,
une vérification. N PR ne font pas N déploiements.

## Où il tourne

Depuis le **clone principal**, sur `main` — jamais depuis un worktree : le lot avance `main`, et
`main` n'y est pas disponible. Un dépôt propre : `git status --porcelain` vide, sinon stop.

## Déroulé

1. **Inventaire.** `gh pr list --state open --json number,title,headRefName,isDraft,mergeable,
   updatedAt`. Écarte les brouillons. Pour chacune : le titre, la branche, l'âge, et si elle a
   déjà une review. Ordre du lot : de la plus ancienne à la plus récente, sauf dépendance
   déclarée dans une PR.
2. **L'aval.** Présente le lot à Manu — une ligne par PR, ce qu'elle change, ce qui l'écarte le
   cas échéant — et attends son oui. C'est le SEUL point d'arrêt : ensuite tu vas jusqu'à la
   cible vérifiée sans redemander.
3. **Base du lot.** `git fetch origin` puis `git switch main` et `git pull --ff-only origin main`.
4. **Chaque PR, à son étage.** Dans l'ordre, sur la branche de la PR :
   - `git rebase main` — conflit non trivial → la PR **sort du lot**, commentée sur la PR, et tu
     passes à la suivante (elle se rebasera sur un `main` plus avancé, c'est son problème).
   - La commande `## Gate` du repo. Rouge → hors du lot, avec la sortie d'erreur en commentaire.
   - `git push --force-with-lease` : la branche distante doit porter le commit rebasé, sinon
     GitHub ne reconnaîtra pas la PR comme mergée.
   - La gate CI sur la branche telle que le repo la déclenche (souvent
     `gh workflow run ci.yml --ref <branche>`, parfois automatique sur PR — lis le contrat).
     Attends le vert. Rouge → hors du lot.
   - `git switch main` puis `git merge --ff-only <branche>` : le lot monte d'un étage, **sans
     rien pousser**.
5. **Une seule livraison.** `git push origin main`. Toutes les PR du lot passent à `merged`
   d'elles-mêmes, leur commit étant sur `main`.
6. **Surveille jusqu'au vert.** Le run post-merge, job de livraison compris (`gh run watch`).
   Rouge → tu ne laisses pas le repo dans cet état : diagnostic, correctif, ou revert annoncé.
7. **Vérifie la cible** comme le `## Livrer` l'indique : `/healthz` 200 **et** le sha poussé quand
   le repo en sert un, plus une route qui prouve le changement quand il est visible.
8. **Ménage.** Branches distantes du lot supprimées, branches locales aussi, et les worktrees
   dont la branche est maintenant dans `main` (le repo peut porter son geste — ex.
   `npm run wt:clean`).

## Ce qui protège le lot

- **La gate CI juge l'état FINAL**, après rebase : une PR verte avant rebase ne prouve rien sur le
  lot. C'est pourquoi la gate CI vient après le rebase, jamais avant.
- **Un push `main` ne livre pas forcément** : dans la plupart des repos de la flotte, le job de
  livraison exige la gate verte. Vérifie-le dans le workflow plutôt que de le supposer — s'il
  livre sans condition, la gate CI par branche cesse d'être un confort et devient obligatoire.
- **Une PR écartée n'est jamais silencieuse** : commentaire sur la PR disant pourquoi elle est
  sortie, et mention dans le rapport final.

## Garde-fous

- **Jamais de `--force` sur `main`**, jamais de `gh pr merge` : le FF merge local est le seul
  chemin, il garde l'historique linéaire.
- **Rien ne se merge sans gate verte** — ni locale, ni CI. Une PR qui ne passe pas sort du lot ;
  elle ne « passe » pas parce que les autres sont vertes.
- **Le lot n'est pas une review.** Recetter ne remplace pas `review-pr` : une PR qui n'a jamais
  été reviewée le signale à l'inventaire, et Manu tranche à l'aval.
- **Un repo à double palier** (preview puis promotion) livre en preview au push `main` : le
  recettage s'arrête là, la promotion vers la prod reste un geste séparé déclaré par le contrat.

## Rapport final

Ce qui est en ligne (sha et cible vérifiés), les PR du lot dans l'ordre où elles sont entrées,
celles qui en sont sorties avec la raison, et ce qui reste ouvert.
