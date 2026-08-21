---
name: dev
description: >-
  Porte une tâche de dev (calibre M) jusqu'au FF merge main — branche depuis origin/main, TDD,
  aperçu visuel si UI, gate du repo, auto-review adversariale, PR, CI verte, FF merge ; le push
  main déclenche seul la livraison que le CLAUDE.md du repo déclare (preview, prod, Vercel,
  Cloudflare…). Jamais de geste de déploiement direct. Marche en local comme en session cloud,
  dans n'importe quel repo qui porte un contrat. À utiliser pour tout nouveau comportement borné
  à un repo ; une retouche (S) s'en passe, un chantier (L) passe d'abord par chantier.
---

# Dev — le cycle jusqu'au FF merge

Charge d'abord `travailler-sur-un-repo` : calibre annoncé, contrat du repo lu, surface (local ou
cloud) connue. S → pas ce skill, va direct. L → `/avqn-dev:chantier` d'abord, puis chaque étape du
plan revient ici.

Tu portes du travail **jusqu'au FF merge `main`** : codé en TDD, beau et vérifié, mergé quand la
CI est verte. Le push `main` déclenche seul la livraison du repo — ce qu'elle déploie (preview en
double-palier, prod en mono-palier, Vercel, Cloudflare…) est écrit dans le `## Livrer` de son
`CLAUDE.md`. Tu ne déploies rien toi-même.

## Le cycle

1. **Contrat + branche** : `CLAUDE.md` du repo (gate, livraison, invariants). En local, un
   worktree dédié si une autre session travaille déjà sur ce clone. Branche :
   `git fetch origin && git checkout -b <type>/<slug> origin/main`.
2. **TDD** : test rouge d'abord, puis le code minimal qui le rend vert. Changement minimal.
   Un bug → diagnostic méthodique avant toute correction (reproduire, localiser la cause,
   corriger la cause — pas de rustine).
3. **Aperçu visuel** : si le repo a une UI **et** que la tâche touche le front → `/avqn-dev:apercu`
   (boot via `/avqn-dev:local`, captures, boucle qualité). Sinon saute, en le disant.
4. **Gate complète** : la commande `## Gate` du repo. Corrige jusqu'au vert — n'ouvre pas une PR
   que la CI rejettera.
5. **Auto-review** : `/avqn-dev:review-pr` en mode léger (agent `revieweur` sur le diff). Applique
   les corrections réelles, re-gate.
6. **Commit + rebase + PR** : commit descriptif 🤖 (bump de version si le repo en a un) ;
   `git rebase origin/main` (conflit non trivial → abort, mise de côté, signale) ; push ;
   PR via `gh pr create` (`Closes #n` si issue ; corps = quoi / pourquoi / comment vérifier).
7. **CI verte sur la branche** : suis le run (`gh run watch` ou `gh pr checks --watch`).
   Rouge → ne merge pas : corrige ou mets de côté avec un commentaire.
8. **FF merge** : `git checkout main && git pull --ff-only origin main && git merge --ff-only
   <branche> && git push origin main`. Push rejeté → rebase + re-gate + retry. Puis surveille la
   livraison post-merge jusqu'au vert et vérifie la cible comme le `## Livrer` l'indique
   (`/healthz` 200 **et** le sha poussé quand le repo en a un).
9. **Clôture** : agent `verificateur` sur les affirmations clés avant de dire « fait » ;
   branche supprimée, issue/PR à jour, bilan honnête (vérifié vs non vérifié).

## Amorces

- **Interactif** (défaut) : la spec naît de la conversation avec Manu — ou d'une issue existante.
  Ambiguïté → question, pas de devinette.
- **Routine** (session autonome ou planifiée) : la spec **est** une issue ouverte `label=ready`
  (jamais de brainstorm en autonome). Une issue par repo par run ; pose `in-progress` en claim ;
  issue ambiguë ou trop grosse → commente, retire le claim, passe. En mono-palier le FF merge
  déploie la prod sans supervision : c'est assumé pour tout repo dont le `CLAUDE.md` le déclare.

## Garde-fous

- **Jusqu'au FF sur `main`, jamais plus** : pas de promote, pas d'appel Coolify / Vercel /
  Cloudflare, pas de dispatch de workflow de déploiement.
- **Jamais merge sur CI rouge** ; **rebase avant le FF** ; gate + aperçu **avant** la PR.
- **Sans contrat lisible** : mode prudent — arrêt avant le push, et tu montres.
- GitHub via `gh` (en cloud, le proxy l'authentifie) ; un 403 sur les Actions → connecteur
  `ops:github_*`.
- Jamais de secret dans un commit, un log ou le contexte.
