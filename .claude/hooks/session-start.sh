#!/usr/bin/env bash
# Hook SessionStart — accueil de session sur le dépôt des skills. Trois rôles :
#   (1) neutraliser la signature de commit cassée du harness cloud (sinon `git commit` échoue) ;
#   (2) amorcer le plugin avqn-dev en session cloud (l'auto-install de settings.json ne s'y déclenche pas) ;
#   (3) annoncer la branche + rappeler la gate et le mode de publication.
set -uo pipefail

emit() {
  jq -nc --arg c "$1" '{hookSpecificOutput:{hookEventName:"SessionStart",additionalContext:$c}}' 2>/dev/null \
    || printf '%s\n' "$1"
}

git rev-parse --git-dir >/dev/null 2>&1 || { emit "🧰 skills (hors dépôt git)."; exit 0; }
branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo '')"

# Signature de commit : le harness cloud pose une signature SSH globale (commit.gpgsign=true) dont le
# signer est souvent absent/cassé → `git commit` échoue et bloque l'agent. On neutralise au niveau du
# dépôt (le local prime sur le global).
git config --local commit.gpgsign false 2>/dev/null || true

# Méthode en session cloud : le plugin avqn-dev vit DANS ce dépôt, mais une session le charge comme
# n'importe quel repo — depuis la marketplace publiée. Une modif locale du plugin ne prend donc effet
# qu'une fois poussée. Idempotent.
if [ "${CLAUDE_CODE_REMOTE:-}" = "true" ]; then
  if claude plugin list 2>/dev/null | grep -q 'avqn-dev@avqn'; then
    claude plugin marketplace update avqn >&2 2>&1 || true
  else
    claude plugin marketplace add a-v-q-n/skills >&2 2>&1 || true
    claude plugin install avqn-dev@avqn >&2 2>&1 || true
  fi
fi

base="Dis ce que tu veux faire. Gate : \`/check-skills\` (JSON de la marketplace, frontmatter des skills et des agents, absence de champ \`version\`). Rien à déployer : le push sur \`main\` EST la publication — sans champ \`version\`, chaque commit se propage seul aux clients (claude.ai, CLI). Écrire un skill : \`/new-skill <nom>\`, puis la table du README."

if [ "$branch" = "main" ] || [ "$branch" = "master" ]; then
  emit "🧰 skills — le dépôt des skills AVQN (marketplace \`avqn\` : plugins avqn-skills et avqn-dev). Tu es sur \`$branch\`. $base"
else
  emit "🧰 skills — session isolée sur la branche \`$branch\`. $base"
fi
exit 0
