---
name: local
description: >-
  Démarre n'importe quel repo en local (Mac) ou dans une session cloud — trouve la recette dans
  le contrat du repo (section « Démarrer en local » de son CLAUDE.md), applique le socle
  transverse AVQN (Postgres central, auth partagée, secrets par le coffre, seeds), prouve que ça
  répond, et PERSISTE dans le repo toute recette dérivée ou corrigée. À utiliser dès qu'il faut
  lancer, tester ou capturer un projet (avant apercu, pour reproduire un bug, pour vérifier un
  changement). NE COUVRE PAS les secrets eux-mêmes (gerer-les-secrets) ni la boucle visuelle
  (apercu).
---

# Local — démarrer un repo, et prouver qu'il tourne

Charge d'abord `travailler-sur-un-repo` (racine, contrat, surface).

## 1. La recette vit dans le repo

Lis la section **`## Démarrer en local`** du `CLAUDE.md` du repo (ou son équivalent : Dev local,
En local, Commandes) : commande, port, services, env, login dev. Un repo à procédure longue la porte dans un skill propre (`.claude/skills/`).
Ne redécouvre pas ce qui est écrit.

À défaut, dérive-la de `package.json` + `README` (et de la mémoire de session s'il y en a),
teste-la, et rends-la au repo (règle d'or en bas).

## 2. Socle transverse AVQN (vaut pour toute la flotte)

- **Postgres central** (coordonnées dans le `CLAUDE.md` du repo) : la plupart des apps utilisent
  une **base logique dédiée** dessus, sauf mention contraire dans la recette. Depuis le Mac son
  port est filtré → tunnel ssh ; le tunnel multiplie les N+1 (46 ms l'aller-retour contre 0,3 en
  prod) : un écran lent en local ne l'est pas forcément en prod.
- **Auth partagée** : base `avqn_mcp` (propriété avqn-os), `BETTER_AUTH_SECRET` identique à
  avqn-os, schéma auth **vendoré, jamais migré** depuis un autre repo. SSO de flotte : cookie
  `.avqn.ch`, sessions 90 j — une session née sur `os.avqn.ch` vaut sur les autres apps.
- **Secrets** : par le coffre, jamais une valeur dans le contexte (`/avqn-dev:gerer-les-secrets`).
- **Seeds depuis la prod** : alias ssh `prod` (ex. `dev-db.sh` d'avqn-os).
- **Preuve de boot** : après lancement, `curl` l'URL ou `/healthz` avant de dire « c'est lancé ».

## 3. En session cloud

Pas de coffre, pas de ssh, pas de tunnel : **Postgres éphémère** (`docker run postgres:16` ou le
`compose.yaml` du repo — le démon Docker ne tourne pas par défaut : `(dockerd >/tmp/dockerd.log 2>&1 &)`
si le hook ne l'a pas fait), migrations au boot, fixtures du repo. Pas de données de prod — pour un
aperçu sur vraies données, téléporter en local. Le hook SessionStart du repo a déjà fait
`npm install`.

## Règle d'or : la recette retourne au repo

Recette absente, incomplète ou qui échoue → (1) dérive-la, (2) **teste-la réellement** (boot +
preuve), (3) **écris-la dans le `CLAUDE.md` du repo** (section `## Démarrer en local`, commit S
ou petite PR). La recette non testée ne s'écrit pas.
