---
name: gerer-les-secrets
description: >-
  À utiliser dès qu'une tâche touche un secret ou une variable d'environnement : lire une clé pour
  un .env.local, créer un secret neuf, le câbler dans l'env d'une app déployée (Coolify), lister ou
  modifier les env runtime d'une app, faire tourner une clé. Porte où vivent les secrets AVQN
  (coffre Bitwarden Secrets Manager, env Coolify), les gestes selon la surface (local : CLI bws
  avec le token du poste ; cloud : broker ops, jamais de valeur) et les invariants (aucune valeur
  dans le contexte, un commit ou un log). NE COUVRE PAS les secrets de CI GitHub (secret d'org
  COOLIFY_TOKEN, hérité) ni l'infra elle-même (connecteur AVQN OPS).
---

# Gérer les secrets — lire, créer, câbler, sans jamais montrer

Charge d'abord `travailler-sur-un-repo` (surface locale ou cloud).

## Où vivent les secrets

- **Le coffre** : Bitwarden Secrets Manager (`https://vault.bitwarden.eu`), source de vérité de
  toute clé AVQN (`COOLIFY_TOKEN`, `RESEND_API_KEY`, `AVQN_OS_DATABASE_URL`, clés Cloudflare /
  Hetzner / Infomaniak / GitHub, `ANTHROPIC_API_KEY`…). Un secret s'y pose une fois.
- **L'env runtime d'une app** : Coolify (`ops:coolify_application_envs`, `…_env_create`,
  `…_env_update`). C'est ce que l'app lit en prod.
- **Le `.env.local` d'un repo** : gitignoré, dérivé du coffre, jamais édité à la main quand un
  script le génère (`env:sync` là où il existe).
- **La CI** : `COOLIFY_TOKEN` est un secret d'organisation GitHub — rien à poser par repo.

## Les gestes

| Geste | Local (Mac) | Cloud (session claude.ai, téléphone) |
|---|---|---|
| Lister les noms | `ops:secret_list` ou `bws secret list` | `ops:secret_list` |
| Lire une valeur pour un `.env.local` | recette ci-dessous — la valeur va **directement** dans le fichier, jamais à l'écran | **impossible par design** (pas de coffre en cloud) : base éphémère + valeurs de dev ; une vraie clé exige de téléporter en local |
| Créer un secret aléatoire | `ops:secret_generate` (`name`, `policy` ex. `hex:32`) | idem |
| Créer un secret à valeur donnée | `bws secret create <KEY> <valeur> <projectId>` — la valeur vient d'un fichier ou de Manu hors chat, jamais du contexte | Manu le pose dans l'UI Bitwarden |
| Câbler vers une app | `ops:secret_wire` (`from`, `app`, `as`) puis redéploie (`ops:coolify_deploy`) | idem |
| Lire / modifier l'env runtime | `ops:coolify_application_envs` · `ops:coolify_application_env_update` | idem |
| Rotation | nouveau secret dans le coffre → `secret_wire` → redeploy → ancien supprimé | idem |

Recette locale, une clé vers `.env.local` sans l'afficher :

```bash
set -a; source ~/.config/avqn/vault.env; set +a
bws secret list | jq -r '.[] | select(.key=="RESEND_API_KEY") | "RESEND_API_KEY=\(.value)"' >> .env.local
```

## Invariants

- **Aucune valeur ne transite** par le contexte, un commit, un log, une réponse. `bws` écrit dans
  un fichier gitignoré, jamais dans un `echo`. Le broker `ops` ne rend jamais une valeur.
- **Le token du poste** (`~/.config/avqn/vault.env`, chmod 600) se source explicitement dans la
  commande qui en a besoin — jamais injecté dans l'env des sessions, **jamais** dans un
  environnement cloud (pas de secret store : ses variables sont lisibles par quiconque l'utilise).
- Un `.env` généré ne s'édite pas à la main ; un `.env.local` ne se commite jamais.
- Variable Coolify qui contient `$` → `is_literal`, sinon interpolée (le hash argon2 qui meurt en
  silence sous un healthcheck vert).
