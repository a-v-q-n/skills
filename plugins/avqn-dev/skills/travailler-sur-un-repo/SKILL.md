---
name: travailler-sur-un-repo
description: >-
  À charger au début de TOUTE tâche de dev, dans n'importe quel repo, en local comme en session
  cloud : annonce le calibre (S retouche / M tâche / L chantier) et le process qui va avec,
  découvre le contrat du repo (son CLAUDE.md : démarrer, gate, livrer) au lieu de le présumer,
  détecte si la session tourne en cloud, et bascule en mode prudent quand le contrat manque.
  Socle chargé par dev, chantier, review-pr, apercu, local, new-project, gerer-les-secrets.
  NE COUVRE PAS le cycle lui-même (dev), le démarrage (local) ni les secrets (gerer-les-secrets).
---

# Travailler sur un repo — le socle de la méthode

Une seule méthode, partout : sur le Mac dans n'importe quel dossier, dans une session cloud,
depuis le téléphone. Elle ne sait rien d'un projet à l'avance : elle **découvre** son contrat.

## 1. Où suis-je ?

Dans l'ordre, sans rien présumer :

| Question | Comment | À défaut |
|---|---|---|
| Dans un repo git ? | `git rev-parse --show-toplevel` | Pas de cycle : dis-le, demande le repo cible |
| Le repo a un contrat ? | `CLAUDE.md` à la racine — lu **avant** tout | **Mode prudent** (ci-dessous) |
| Comment il démarre, se teste, se livre ? | sections `## Démarrer en local`, `## Gate`, `## Livrer` du `CLAUDE.md` — ou leurs équivalents lisibles (Dev local / En local / Commandes ; Contrat ; Déploiement / CI-CD) ; un skill propre au repo dans `.claude/skills/` quand la procédure déborde | Dérive de `package.json` / `README`, teste, et **propose la section au repo** |
| Session cloud ? | `CLAUDE_CODE_REMOTE=true` (ou `CLAUDE_CODE_REMOTE_SESSION_ID` posé) | Session locale |

**Mode prudent** (contrat absent ou illisible) : tu fais, tu montres, tu demandes. Pas de push,
pas de merge, jamais de déploiement. Le défaut est lâche — ce n'est pas une liste blanche de repos
qui protège, c'est le défaut.

## 2. Le triage par calibre

Annonce le calibre ; le poids de la discipline suit la taille de l'enjeu, jamais l'inverse.

| Calibre | C'est quoi | Process |
|---|---|---|
| **S — retouche** | ≤ 2 fichiers, comportement existant, ni schéma, ni API, ni dépendance nouvelle | Direct : modif + gate du repo + commit. Zéro cérémonie. |
| **M — tâche** | Nouveau comportement, borné à un repo | `/avqn-dev:dev` — branche, TDD, aperçu si UI, gate, review, PR, CI verte, FF merge |
| **L — chantier** | Multi-jours ou multi-repos, schéma d'une base partagée, nouvelle app, ambiguïté produit | `/avqn-dev:chantier` — brainstorm → spec → plan → étapes → review renforcée |

Doute entre deux calibres → le plus léger, annoncé ; Manu corrige. Un calibre monte en cours de
route (la retouche qui révèle un chantier → stop, requalifie, ne t'entête pas).

## 3. Local ou cloud : l'isolation

**Deux agents ne touchent jamais la même ressource mutable au même instant.**

- **Local** : une session = un worktree = une branche = sa base locale sur son port. Jamais de
  `reset --hard` dans un clone partagé. Le coffre est disponible (`/avqn-dev:gerer-les-secrets`).
- **Cloud** : la VM est l'isolation — pas de worktree ni de port dédié. Aucun secret dans la VM,
  pas de coffre, pas de tunnel vers une base distante : Postgres éphémère (docker) + migrations +
  fixtures. Livrer = pousser la branche, PR, merger ; la CI du repo déploie. Ce qui voyage avec le
  repo, ce qui se configure dans l'UI (connecteurs par session, environnement, setup script) :
  `references/environnement-cloud.md`.

## 4. Ce qui vaut partout

- **Déployer = merger.** Une session ne déploie jamais elle-même (pas de promote, pas d'appel
  Coolify / Vercel / Cloudflare) : le `## Livrer` du repo dit ce que le push `main` déclenche.
- **Infra et secrets de prod** : connecteur claude.ai « AVQN OPS » (`ops:*` — Coolify, DNS, R2,
  Hetzner, GitHub, broker de secrets), présent sur toutes les surfaces ; aucune valeur ne transite.
- **Le savoir durable descend dans le repo** (`CLAUDE.md`, `docs/`), jamais dans la mémoire
  locale de l'agent : c'est ce qui voyage en cloud et survit aux sessions.
- Jamais de secret dans un commit, un log, le contexte.
