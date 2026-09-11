---
name: dev
description: >-
  Porte une tâche de dev (calibre M) jusqu'au FF merge main — branche depuis origin/main, TDD,
  aperçu visuel si UI, gate du repo, auto-review adversariale, PR, CI verte, FF merge ; le push
  main déclenche seul la livraison que le CLAUDE.md du repo déclare (preview, prod, Vercel,
  Cloudflare…). Jamais de geste de déploiement direct. Marche en local comme en session cloud,
  dans n'importe quel repo qui porte un contrat. À utiliser pour tout nouveau comportement borné
  à un repo ; une retouche (S) s'en passe, un chantier (L) passe d'abord par chantier.
couche: recette
moment: >-
  Le cycle M jusqu'au FF merge `main` : TDD, aperçu, gate, review, PR, CI verte.
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
   les corrections réelles, re-gate. Le diff du correctif repasse devant le revieweur dès que
   la passe précédente a rendu un bloquant, et les passes s'arrêtent quand l'une ne rend plus
   de bloquant : un correctif est écrit vite et sous l'autorité d'un finding, il introduit des
   régressions aussi sûrement qu'un changement, et personne d'autre ne relira avant la prod.
   Pendant qu'un agent, la CI ou un déploiement travaille, pose un `Monitor` et rends la main :
   la notification te réveille. Ne sonde pas `ReadNotifications` en boucle, chaque sonde est un
   tour perdu et rien n'arrive plus vite.
6. **Commit + rebase + PR** : commit descriptif 🤖 (bump de version si le repo en a un) ;
   `git rebase origin/main` (conflit non trivial → abort, mise de côté, signale) ; push ;
   PR via `gh pr create` (`Closes #n` si issue ; corps = quoi / pourquoi / comment vérifier).
   En session cloud (surface connue depuis `travailler-sur-un-repo`), GitHub ne sert du GraphQL
   que les opérations de review de PR épinglées — `gh pr create` y rend un 403 — et la PR
   s'ouvre par la REST, corps lu depuis un fichier (`-F body=@fichier`) pour que les backticks
   et les `$` du « comment vérifier » arrivent intacts :

   ```bash
   gh api repos/<org>/<dépôt>/pulls --method POST \
     -f title="…" -f head="<branche>" -f base=main -F body=@pr-body.md --jq .html_url
   ```

7. **CI verte sur la branche** : l'ouverture de la PR déclenche la gate (`pull_request` dans le
   `ci.yml` de tout repo de la flotte) — rien à dispatcher. Si rien ne vient, lis le bloc `on:`
   du workflow avant d'attendre : un repo hors flotte peut n'écouter que `push main`, et sa
   gate se tire alors à la main (`gh workflow run ci.yml --ref <branche>`). Suis le run
   (`gh run watch`, `gh run list` — API Actions, que le 403 GraphQL n'atteint pas ; un 403 sur
   les Actions → `ops:github_runs`, la liste filtrable par `branch` / `head_sha`, et
   `ops:github_run_get` avec `include: ["jobs"]`, le job et le step qui ont lâché). En cloud,
   l'état des checks se lit par la REST sur le sha effectivement
   poussé, et sur les **deux** surfaces que `gh pr checks` agrège — check runs (Actions) et
   statuts de commit (déploiements, CI externes) :

   ```bash
   sha=$(git rev-parse HEAD)   # après le rebase de l'étape 6
   gh api repos/<org>/<dépôt>/commits/$sha/check-runs \
     --jq '.total_count, (.check_runs[] | "\(.name) \(.status) \(.conclusion // "")")'
   gh api repos/<org>/<dépôt>/commits/$sha/status --jq '.state, (.statuses|length)'
   ```

   Les comptes se lisent, pas seulement `.state` : sur un commit sans aucun statut il vaut
   `pending`, comme sur un statut en cours. L'appel est un instantané — redemande jusqu'à ce que
   chaque check ait conclu, et ne conclus jamais sur un seul relevé. Seul `success` vaut vert :
   toute autre conclusion (`failure`, `cancelled`, `timed_out`, `action_required`, `stale`) ne se
   merge pas — corrige, ou mets de côté avec un commentaire. Deux relevés vides espacés d'une
   minute ne valent « pas de CI à attendre » que si le `## Livrer` du repo **affirme** n'en avoir
   aucune ; son silence vaut attente. Et l'attente est bornée : au bout d'une dizaine de relevés
   sans rien voir venir, mets de côté et signale — une session ne boucle pas sur un mur.
8. **FF merge** : `git checkout main && git pull --ff-only origin main && git merge --ff-only
   <branche> && git push origin main`. Push rejeté → rebase + re-gate + retry. Puis surveille la
   livraison post-merge jusqu'au vert et vérifie la cible comme le `## Livrer` l'indique
   (`/healthz` 200 **et** le sha poussé quand le repo en a un).
9. **Clôture** : agent `verificateur` sur les affirmations clés avant de dire « fait » ;
   branche supprimée, issue/PR à jour, bilan honnête (vérifié vs non vérifié).

## Amorces

- **Interactif** (défaut) : la spec naît de la conversation avec Manu — ou d'une issue existante.
  Ambiguïté → question, pas de devinette.
- **Routine** (session autonome) : Manu a tiré `ops:dev_lancer` sur une issue nommée depuis une
  conversation claude.ai. La spec **est** cette issue, une seule par run (jamais de brainstorm en
  autonome). Le claim `in-progress` est déjà posé par le lanceur : tu le trouves en place, et tu
  le retires en fin de run — livré ou abandonné. Issue ambiguë ou trop grosse → commente, retire
  le claim, arrête-toi. En mono-palier le FF merge déploie la prod sans supervision : c'est
  assumé pour tout repo dont le `CLAUDE.md` le déclare.

## Garde-fous

- **Jusqu'au FF sur `main`, jamais plus** : pas de promote, pas d'appel Coolify / Vercel /
  Cloudflare, pas de dispatch de workflow de déploiement.
- **Jamais merge sur CI rouge** ; **rebase avant le FF** ; gate + aperçu **avant** la PR.
- **Sans contrat lisible** : mode prudent — arrêt avant le push, et tu montres.
- GitHub via `gh` (en cloud, le proxy l'authentifie). Deux 403 distincts, deux sorties : un 403
  GraphQL (`gh pr create`, `gh pr checks`, `gh repo view`, `gh issue list`) n'est pas un défaut
  de droits — la même opération passe par `gh api repos/…` (REST) ; un 403 sur les Actions →
  `ops:github_runs` et `ops:github_run_get` ; pour les issues, les fichiers, les branches et
  les PR, `ops:github_*` passe aussi. Déclencher un workflow n'est pas un geste du cycle.
- Jamais de secret dans un commit, un log ou le contexte.
