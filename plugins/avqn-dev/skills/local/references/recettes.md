# Recettes connues de la flotte AVQN

Cache de démarrage : la source de vérité est la section `## Démarrer en local` du `CLAUDE.md` de chaque repo. Une entrée quitte ce fichier dès que son repo la porte.

## Recettes

| Projet | Lancer | URL | Services | Login dev |
|---|---|---|---|---|
| avqn-os | `npm install && npm run dev:cockpit` | localhost:3002 | Postgres local auto (:5434) | `/dev-login` |
| ops | pas de dev local documenté — gate/tests suffisent | — | — | — |
| bibliotheque | `npm run dev:setup` puis `npm run dev:fresh` | localhost:3000 | Postgres **local** ×2 | OTP, code dans `tmp/dev.log` |
| mediatheque | `npm run dev` · UI sans auth : `test/harness/serve.ts` | localhost:3000 | Postgres central | harnais |
| product-site-avqn | `pnpm run dev` (jamais npm) | localhost:4321 | aucun | — |
| product-barometre-ia | `docker compose up -d db` puis `DATABASE_URL=postgres://barometre_ia:barometre_ia@localhost:5432/barometre_ia npm run dev` | localhost:3000 | Postgres compose | `/admin` (mdp coffre) |
| styleguide | `npm run dev` (exports + serveur) | localhost (astro) | aucun, zéro secret | — |
| model-arena | `npm run dev` (site) · runs via opencode | localhost (astro) | clés providers pour les runs | — |
| skills | pas de « run » — session DANS le repo, skills d'auteur (`/new-skill`, `/check-skills`) | — | — | — |
| demo-crm | tunnel SSH puis `npm run dev` | localhost:3007 | Postgres central, base `demo_crm` | `hello@avqn.ch` / `123456` |
| blog | `npm run dev:setup` puis `npm run dev:fresh` | localhost:3008 | Postgres **local** ×2 (`blog`, `avqn_mcp`) | OTP, code dans `tmp/dev.log` |

## Notes par projet (ce qui piège)

- **avqn-os** : une seule app Next — `next dev` sert le cockpit, les endpoints MCP, `/signin` et
  `/healthz` sur le même port. `dev:cockpit` fait tout (compose Postgres :5434, `.env.local`,
  seed prod si base vide, next dev) ; les **migrations tournent au boot du serveur**
  (instrumentation), une base locale périmée se remigre donc seule au démarrage. Re-seed des
  DONNÉES : `scripts/dev-db.sh refresh` (ssh `prod`). Captures : `node scripts/dev-shots.mjs`
  (racine) → `tmp/shots/`.
  **Depuis un worktree** : `next dev` (Turbopack) refuse un `node_modules` en lien symbolique
  (« Symlink [project]/node_modules is invalid, it points out of the filesystem root ») — il
  panique au démarrage alors que `npm run build` et `npm test`, eux, l'acceptent. Cloner les
  déps au lieu de les lier : `cp -Rc <clone>/node_modules ./node_modules` (clone APFS, ~7 s,
  quasi zéro disque). Le conteneur `avqn-os-db` porte un nom fixe : un seul à la fois pour
  toute la machine — le démarrer (`docker start avqn-os-db`) plutôt qu'en créer un second.
  Port occupé par une autre session : `next dev -p <port>` + `APP_URL=http://localhost:<port>`
  dans `.env.local` (sinon 403 Invalid origin) + `BASE=http://localhost:<port>` pour
  `dev-shots.mjs`.
  Si `/dev-login` rend 500 ECONNREFUSED alors que le conteneur est healthy : `.env.local`
  (gitignoré, non régénéré s'il existe) peut pointer un port hérité d'une session worktree —
  réaligner `DATABASE_URL` sur `.env.example` (:5434) ; next dev recharge l'env tout seul.
  Si l'auth répond **403 Invalid origin** : `trustedOrigins` se limite à `APP_URL` — quand le
  serveur tourne sur un autre port que celui de l'`APP_URL` de `.env.local` (port hérité, ou
  `-p` improvisé), exporter `APP_URL=http://localhost:<port réel>` pour le serveur ET les
  scripts (ex. `scripts/passkey-e2e.mjs`).
  **Base de prod DIRECTE** (lire/écrire les vraies données, pas une copie) : le 5432/5433 du
  Postgres central est filtré par firewall depuis l'extérieur → tunnel
  `ssh -f -N -L 15432:localhost:5433 -o ExitOnForwardFailure=yes prod`, puis dans `.env.local`
  (base `.env.example`) pointer `DATABASE_URL` sur `localhost:15432/avqn_mcp` avec les creds du
  conteneur prod (`docker exec <conteneur avqn-os prod> printenv DATABASE_URL` via ssh — le
  conteneur prod se reconnaît à `APP_URL=https://os.avqn.ch`, l'autre est la preview). Garde-fous
  AVANT de booter : parité migrations (`git diff <sha prod>..HEAD -- drizzle/` vide — elles
  s'appliqueraient à la PROD au boot) et `RAG_SYNC_ENABLED=0` (défaut serveur = 1). `/dev-login`
  crée une vraie session dans la base prod ; les connexions mail/calendrier restent
  indéchiffrables (secret auth local) ; R2 absent → rendu PDF ok, dépôt KO. Couper le tunnel :
  `pkill -f 'ssh -f -N -L 15432'`.
- **bibliotheque** : `dev:setup` est le point d'entrée — il annonce les bases, migre le métier et
  reproduit le schéma auth en LOCAL (sans lui, le login opérateur échoue sur `relation
  "verification" does not exist`). Les deux bases sont sur `localhost` ; la base métier locale
  porte une **copie** des données de prod, donc ce qu'on y lit ne prouve rien sur la prod —
  vérifier un fait en prod passe par le MCP ou psql sur le Postgres central. Rafraîchir la copie :
  `ssh prod "docker exec -u postgres bokkwc08kk40c00o8cs0wogg pg_dump -d bibliotheque --no-owner
  --no-privileges"`, retirer les lignes `\restrict`/`\unrestrict` (pg_dump plus récent que le psql
  local), dropper les schémas `public` ET `drizzle`, restaurer. Captures :
  `npm run shots -- [--auth] <route...>` → `tmp/shots/` (`--auth` ouvre une vraie session
  opérateur, aucune page protégée n'oblige à toucher son garde-fou). Captures côté LECTEUR
  (contenu derrière le mur, que `--auth` ne couvre pas) : POST `/api/resource/subscribe` avec un
  email de test, lire le magic-link `reader/verify?token=…` dans `tmp/dev.log`, l'ouvrir dans le
  contexte Playwright, puis capturer. Préférer `dev:fresh` à `dev` après avoir touché
  `globals.css` ou supprimé une route (Turbopack sert un CSS obsolète, et les types périmés de
  `.next` cassent `tsc`).
- **mediatheque** : runtime tsx sans build ; providers absents (Gemini, Chromium, R2) =
  dégradation gracieuse — on peut développer sans clés.
- **product-barometre-ia** : seul projet à compose DB dédié ; migrations auto au boot ;
  `npm test`/`build` tournent sans DB.
- **demo-crm** : le port 5432 du serveur Prod n'est pas joignable depuis le Mac (transit Hetzner) —
  ouvrir d'abord `ssh -f -N -L 5470:127.0.0.1:5432 root@46.62.162.135`, et faire pointer le
  `DATABASE_URL` de `.env.local` sur `127.0.0.1:5470`. Migrations **et** amorce des données tournent
  au boot du serveur (instrumentation), les deux idempotentes : la base se remplit seule au premier
  démarrage. Écran cible = carré 1080 × 1080, capturer à ce viewport en priorité.
- **ops** : tourner le serveur en local exige la base auth partagée + des tokens infra ; en
  pratique la gate (`npm run check && npm run build && npm test`) suffit au dev. Chaque capacité
  dégrade proprement si sa clé manque.

- **blog** : deux bases **locales** comme la bibliothèque (`blog` pour le métier, `avqn_mcp` pour
  l'auth vendorée). `dev:setup` les migre et pousse le schéma auth. Le port est **3008** en dur
  dans `npm run dev` — 3000 et 3002 sont déjà pris par d'autres projets de la flotte, et un port
  qui glisse casse `APP_URL`, donc les cookies de session et le login. Les pages publiques sont
  **statiques** : après une écriture en base hors MCP (psql, script), relancer `dev:fresh` sinon
  on relit une version en cache.

