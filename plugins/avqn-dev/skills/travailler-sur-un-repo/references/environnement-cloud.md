# Session cloud — ce qui voyage, ce qui se configure

Une session cloud (claude.ai/code, app mobile, `claude --cloud`, routine) part d'un **clone frais
du repo** dans une VM Ubuntu jetable. Tout ce qui est committé arrive ; rien de `~/.claude/` du Mac
n'arrive.

## Ce qui voyage avec le repo

| Dans le repo | Effet en cloud |
|---|---|
| `CLAUDE.md` | lu — c'est le contrat |
| `.claude/settings.json` → `extraKnownMarketplaces` + `enabledPlugins` | déclaration documentée, mais l'auto-install **ne se déclenche pas dans la VM** (vérifié) |
| `.claude/settings.json` → hooks `SessionStart` | tournent — **c'est le hook du repo qui amorce le plugin** en cloud : `claude plugin marketplace add a-v-q-n/skills && claude plugin install avqn-dev@avqn` (marketplace publique, clonée anonymement ; les skills sont visibles dans la même session). Le même hook fait `npm install` et lance `dockerd` si le repo a un compose |
| `.claude/skills/`, `.claude/agents/` | chargés |
| `.mcp.json` | chargé (réseau selon l'allowlist) |

Ne voyagent **pas** : `~/.claude/CLAUDE.md`, skills/agents user, plugins activés en user, MCP
ajoutés en scope user/local, tout token.

## Ce qui se configure à la main (UI claude.ai)

- **Connecteurs** (AVQN OPS, AVQN OS, Médiathèque…) : **par session ou par routine**, au moment de
  la créer — jamais activés depuis `claude --cloud`. Leur trafic passe par Anthropic, pas par
  l'allowlist.
- **Environnement cloud « AVQN »** (sélecteur d'environnement) :
  - réseau **Custom** = liste par défaut (npm, Docker Hub, GitHub…) + `*.avqn.ch` (pour sonder
    `/healthz` et les apps) ;
  - **aucune variable secrète** (pas de secret store : tout est lisible par qui utilise l'env) ;
  - setup script :

    ```bash
    #!/bin/bash
    set -e
    # gh n'est pas préinstallé ; le proxy GitHub l'authentifie (GH_TOKEN=proxy-injected)
    (apt-get update -qq && apt-get install -y -qq gh) &
    # Postgres éphémère prêt à l'emploi pour les repos à base (image en cache d'environnement)
    docker pull -q postgres:16 &
    wait
    ```

    Le cache d'environnement garde ce que le script installe. **Le démon Docker ne tourne pas par
    défaut** dans la VM (binaire présent, pas de systemd) : `(dockerd >/tmp/dockerd.log 2>&1 &)` puis
    `docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=dev postgres:16` — le hook du repo s'en charge
    quand il voit un compose. Chromium pour les captures : `npx playwright install --with-deps
    chromium` dans la session qui en a besoin (long ; préférer le script de captures du repo).

## Signaux et réflexes dans la VM

- `CLAUDE_CODE_REMOTE=true`, `CLAUDE_CODE_REMOTE_SESSION_ID=cse_…` (le `session_…` de l'URL).
- GitHub : `gh` si le setup script l'a installé (auth proxy), sinon le MCP `github` intégré, scopé
  au repo attaché. Pousser une branche, ouvrir la PR, merger : oui. Cloner un autre repo privé : non.
- Pas de coffre, pas de ssh vers la prod, pas de tunnel : Postgres éphémère (docker, démon lancé par le hook) + migrations + fixtures.
- Une session pousse par défaut sur **sa propre branche** `claude/<slug>` ; pour viser une branche
  précise : `git push origin HEAD:<branche>`.
- Lire l'état d'une session depuis le Mac : `claude --teleport <session_id> -p "résume…"` (copie
  locale de la conversation) ; lui parler : `claude -p "…" --cloud <session_id>`.
