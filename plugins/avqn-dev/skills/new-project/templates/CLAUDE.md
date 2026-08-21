# {{REPO}} — {{DESC}}

{{REPO}} suit le cycle de dev continu AVQN. La méthode vit dans le plugin `avqn-dev` (déclaré dans
`.claude/settings.json` : `/avqn-dev:dev`, `/avqn-dev:apercu`, `/avqn-dev:brainstorm-issue`…) ; la mécanique
de déploiement dans `a-v-q-n/ci` — ce repo ne porte que **son contrat** (ci-dessous), son build et
son code.

## Contrat

- **UI ?** : {{UI_LINE}}
- **Versioning** : pas de bump (version figée `0.1.0` tant que le repo n'a pas de consommateurs).
- **Palier** : `{{PALIER}}` — {{PALIER_DESC}}
- **Mode Coolify** : `{{MODE}}` — {{MODE_DESC}}
- **Coordonnées Coolify** :
{{COORDS_BLOCK}}

## Démarrer en local

- Services requis : {{SERVICES_LINE}}
- `npm install && npm start` → http://localhost:3000 (`/healthz` → `{ ok, sha }`).

## Gate

`{{GATE_CMD}}` — exactement ce que la CI rejoue avant de livrer l'image.

## Livrer

Push `main` → `.github/workflows/ci.yml` construit et teste l'image immuable `sha-<commit>`, la
pousse sur GHCR (`ghcr.io/a-v-q-n/{{REPO}}`), puis Coolify la pull par sha (Coolify ne build
jamais). Le secret `COOLIFY_TOKEN` est hérité du secret d'organisation — rien à poser par repo. La
route `/healthz` répond `{ ok, sha }` : le health-check du deploy exige un 200 **et** le sha
attendu. L'agent va jusqu'au FF merge `main`, jamais au-delà.

## App

Squelette « hello » minimal (serveur HTTP Node sans dépendance, `server.mjs`). La vraie stack est
amenée par le dev normal (`/avqn-dev:dev`) : remplacer l'app, ajuster la gate et le `test` job du
`ci.yml`, et si un build apparaît passer le `Dockerfile` en multi-étage (garder `ARG GIT_SHA` +
`HEALTHCHECK` + PORT dynamique + la route `/healthz`).
