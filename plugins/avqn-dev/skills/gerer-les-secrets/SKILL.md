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
couche: recette
moment: >-
  Lire, créer, câbler un secret (coffre BWS en local, broker `ops` partout) sans jamais montrer
  une valeur.
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
| Rotation, fournisseur à API (interne, R2, Resend, Cloudflare compte) | `ops:secret_rotate` (`nom`, `confirm`) : frappe, coffre, câblage, redéploiement, healthz, révocation, dans cet ordre | idem |
| Rotation, fournisseur sans API (console) | le pont par fichier, ci-dessous — Manu ne colle rien, il se connecte | Manu, dans l'UI |

Recette locale, une clé vers `.env.local` sans l'afficher :

```bash
set -a; source ~/.config/avqn/vault.env; set +a
bws secret list | jq -r '.[] | select(.key=="RESEND_API_KEY") | "RESEND_API_KEY=\(.value)"' >> .env.local
```

## Le pont par fichier : tourner une clé qu'une console affiche une fois

Quand le fournisseur n'a pas d'API de frappe (Hetzner, Infomaniak, OpenAI, Gemini, ElevenLabs,
HeyGen, Coolify, GitHub, Bitwarden…), la clé neuve n'existe que dans une page web, une fois. Le
geste tient la valeur hors de la conversation ; elle ne touche le disque que quelques secondes,
dans un fichier effacé aussitôt lu :

1. **Frapper** : dans la console, pilotée par Chrome (`claude-in-chrome`), créer la clé neuve avec
   un nom qui dit son consommateur et sa date (`ops-2026-09`). Manu ne fait que se connecter.
   L'onglet doit être **visible** au moment de soumettre : un onglet caché ne fait pas tourner
   `requestAnimationFrame`, et une soumission React y reste bloquée (bouton grisé, aucune
   requête). L'amener devant depuis le Mac (`osascript` : `activate`, puis `set active tab index`
   de la fenêtre qui porte l'URL) et vérifier `document.hidden === false` par `javascript_tool`
   avant le clic — l'extension n'y arrive pas seule, ses onglets naissent en arrière-plan.
   Vérifier les cases (droits, expiration) **avant** de créer : un `zoom` sur le formulaire ; une
   case qui n'a pas pris se voit là, pas après (un jeton Coolify est parti en lecture seule).
2. **Ne plus rien lire de la page** : ni capture d'écran, ni `get_page_text`, ni `find` — `find`
   rend le texte des éléments qu'il décrit, et une ligne de la liste peut porter la valeur (un
   jeton Coolify et un jeton GitHub sont sortis comme ça, tous deux refrappés). Seul
   `javascript_tool` touche la page, et il ne renvoie que des longueurs et des booléens.
3. **Sortir la valeur par un téléchargement** : `javascript_tool` cherche l'élément dont le texte
   a la forme du jeton (`ghp_…`, `<id>|…`, `sk-…`), en fait un `Blob` et clique un `<a download>`
   nommé `jeton-<fournisseur>.txt`. Ça marche onglet caché ou visible, sans presse-papiers, et
   les CSP des sites ne s'y opposent pas (`fetch` vers un serveur local, si : GitHub le bloque ;
   le presse-papiers exige un onglet visible et une fenêtre au premier plan).
4. **Ranger** : en local, lire `~/Downloads/jeton-<fournisseur>.txt`, l'effacer (`rm -P`),
   **tester** la valeur contre l'API du fournisseur (un 200, jamais un affichage), puis
   `bws secret edit --value "$V" <id>` avec l'id de `bws secret list`. Un test qui échoue ne
   range rien.
5. **Quitter la page** avant tout autre geste (`navigate` vers la liste) : la valeur y est
   encore affichée tant qu'on ne recharge pas.
6. **Câbler et prouver** : `ops:secret_wire` sur chaque consommateur (la table est celle de
   `ops:secret_inventaire`), `ops:coolify_deploy`, puis `/healthz` 200 avec le **même sha** — et un
   appel réel qui utilise la clé (`ops:hetzner_servers` pour Hetzner, `ops:dns_domains` pour
   Infomaniak, `lister_voix` de contentos pour ElevenLabs…). Un consommateur hôte
   (`GHCR_PULL_TOKEN`) se repose par `bws … | ssh <hôte> 'docker login … --password-stdin'`.
   Si ops lui-même tourne, câbler et redéployer depuis le poste (`curl` avec le jeton du coffre),
   pas par ops.
7. **Révoquer** les anciennes dans la console, seulement après la preuve, **une par une et
   ciblée sur sa ligne** (`a.closest('.access-token')`, jamais « le premier bouton Supprimer
   trouvé ») : une suppression qui vise large a retiré le jeton vivant, refrappé aussitôt.
   Re-tester la valeur du coffre après chaque suppression.

Ce que le pont ne couvre pas : une clé qui chiffre des données au repos (`COMMS_MASTER_KEY`,
`AGE_VAULT_PRIVATE_KEY`) ne tourne pas sans plan de relecture ; un jeton recopié à la main ailleurs
(`SOUMISSION_JETON` sur le site, les jetons MCP de contentos dans les URL des connecteurs) se
tourne avec ses copies, pas avant.

## Invariants

- **Aucune valeur ne transite** par le contexte, un commit, un log, une réponse. `bws` écrit dans
  un fichier gitignoré, jamais dans un `echo`. Le broker `ops` ne rend jamais une valeur.
- **Le token du poste** (`~/.config/avqn/vault.env`, chmod 600) se source explicitement dans la
  commande qui en a besoin — jamais injecté dans l'env des sessions, **jamais** dans un
  environnement cloud (pas de secret store : ses variables sont lisibles par quiconque l'utilise).
- Un `.env` généré ne s'édite pas à la main ; un `.env.local` ne se commite jamais.
- Variable Coolify qui contient `$` → `is_literal`, sinon interpolée (le hash argon2 qui meurt en
  silence sous un healthcheck vert).
