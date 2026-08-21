# Doctrine — où vit le savoir des agents

Trois supports portent du savoir pour les agents (skills, instructions MCP, `.claude/` d'un
repo), et la frontière entre eux était floue. Ce document la fixe. Décision de juillet 2026,
étendue en août à la méthode de dev (plugin `avqn-dev`).

## Le critère central

> **Un savoir vit avec ce qui le fait changer.**

C'est le seul critère. Tout le reste (les trois supports, les règles de rangement) en découle.

| Ce qui fait changer le savoir | Où il vit | Exemple |
|---|---|---|
| **Une surface de tools MCP** (renommage, nouveau domaine…) | Le **serveur** qui expose ces tools : `instructions` + grammaire embarquée, déployées avec les tools | La grammaire des objets d'AVQN OS |
| **Le goût et le métier de Manu** (voix, charte, recettes) | Le repo **`skills`** (plugin git, activé sur le compte claude.ai) | `ecrire-comme-manu`, les recettes d'écriture |
| **La méthode de dev** (comment on développe, review, livre — partout) | Le plugin **`avqn-dev`** (même repo `skills`), qui **découvre** le contrat de chaque repo | `dev`, `chantier`, `local`, `review-pr` |
| **Ce qui est propre à un repo** (son contrat, son amorçage, une procédure qui déborde) | Le **`CLAUDE.md`** et le **`.claude/`** de ce repo | sections Démarrer / Gate / Livrer ; hook SessionStart ; `/check-skills` dans `skills` |

Cas hybride (ex. `creer-une-facture`) : la **mécanique** (quel tool, quel ordre, quels
invariants serveur) descend dans le serveur ; le **jugement** (quoi facturer, quel ton, quel
geste) reste un skill. On découpe, on ne déménage pas en bloc.

## Les trois supports, et ce qu'ils savent faire

### 1. Le serveur MCP : `instructions` courtes + grammaire à la demande

- Les **`instructions`** du serveur sont chargées dans **toute** session où le connecteur est
  branché — c'est le `CLAUDE.md` du serveur. Elles restent donc **courtes** : le périmètre, les
  réflexes (`recall`, `contexte`), et **l'index** vers la grammaire (« avant d'écrire dans un
  domaine, lis sa grammaire »).
- La **grammaire détaillée** se tire à la demande — l'équivalent MCP du `references/` d'un
  skill : un tool en lecture seule (`grammaire {domaine}`), doublé de resources
  (`avqn://grammaire/<domaine>`) pour les clients qui les lisent. Le tool est le chemin garanti
  (le support client des resources est inégal) ; les resources sont le bonus portable.
- Force : **toujours synchrone avec les tools** (même déploiement), et accessible à **tout
  client MCP** — pas seulement Claude. C'est ce qui rend l'OS autoporté.
- Limite : rien ne se déclenche tout seul. C'est aux `instructions` de créer le réflexe.

### 2. Le repo `skills` : le craft de Manu, en plugin

- Un plugin **git** (marketplace `a-v-q-n/skills`), activé sur le **compte** claude.ai — c'est
  ce qui le rend présent partout : web, mobile, Cowork, sessions cloud.
- La distribution des plugins passe par **git ou npm, rien d'autre** (pas d'URL de serveur) ;
  côté claude.ai, uniquement un dépôt git. Inutile de chercher un autre canal.
- **Pas de champ `version`** dans `plugin.json` ni dans l'entrée marketplace : sans lui, chaque
  commit est une version et la mise à jour se propage seule. Un `version` posé **épingle** le
  plugin — c'est la cause historique des « mises à jour qui ne partent pas ».
- Y vivent : la voix, la charte d'usage, les recettes d'écriture et de production — ce qui n'a
  aucun rapport avec un déploiement de serveur.

### 3. Le `.claude/` d'un repo : son contrat, pas la méthode

Un « agent », dans la flotte, est un tuple : **un repo + son `CLAUDE.md` + son `.claude/` + les
outils à portée**. La **méthode** (triage, cycle, review, démarrage) est la même pour tous et vit
dans le plugin `avqn-dev` — un repo ne la recopie jamais, il la **déclare** (`settings.json`) et
l'**amorce** en session cloud (hook SessionStart). Son `.claude/` ne porte que ce qui lui est
propre : le hook, et un skill quand une procédure du repo déborde du `CLAUDE.md`.

Test rapide pour un skill candidat : **a-t-il besoin d'un arbre de travail** (branches, gate,
fichiers) ? Oui → plugin `avqn-dev` s'il est générique (il marche dans Claude Code, local et cloud),
`.claude/` du repo s'il lui est propre. Non → plugin `avqn-skills`, et il sert aussi sur claude.ai.

## Ce que ça interdit

- Recopier la grammaire d'un serveur dans un skill (elle se périme au premier renommage de
  tool) ; le skill renvoie au serveur, jamais l'inverse.
- Gonfler les `instructions` d'un serveur avec le contenu détaillé (elles se paient à chaque
  session) : l'index dedans, le contenu derrière le tool.
- Publier dans `avqn-skills` (claude.ai) un skill qui exige un arbre de travail : sa place est dans `avqn-dev`.
