---
name: apercu
description: >-
  Boucle qualité visuelle LOCALE avant la PR — boote l'app (recette du repo via local), capture
  le rendu aux breakpoints (MCP Playwright en local, script de captures du repo ou Playwright CLI
  en cloud), juge la qualité contre la spec + la charte du repo (AVQN : styleguide.avqn.ch), et
  améliore le code jusqu'à un résultat de qualité (plafond d'itérations). À appliquer dans dev
  pour toute tâche qui touche le front d'un repo à UI. Teste en LOCAL, jamais en preview/prod.
---

# Aperçu — l'œil sur le front

On **regarde** ce qu'on a produit et on **améliore jusqu'à ce que ce soit beau**, en local,
avant que la PR existe. Règle de Manu : travail UI = test local réel + captures, pas juste la gate.

## Quand l'appliquer

- **OUI** : repo avec UI (cf. son `CLAUDE.md`) **et** tâche qui touche le front.
- **NON, saute** : repo sans front, ou tâche sans impact visuel. Dis-le et passe.

## Pré-requis

- Boot : `/avqn-dev:local` (la recette du repo — commande, URL, login dev).
- Pages/routes à inspecter : celles touchées par la tâche + la spec de l'issue.
- Breakpoints par défaut : **390 / 768 / 1440** (sauf autre contrat du repo).
- **Capturer, selon la surface** :
  - local : outils `mcp__playwright__browser_*` (charge via ToolSearch si absents). **`file://`
    est bloqué** → toujours servir en localhost et naviguer en `http://127.0.0.1:<port>/…` ;
  - le repo a son script de captures (ex. `dev-shots.mjs` d'avqn-os, `npm run shots` de
    bibliotheque) → préfère-le, il connaît l'auth et les routes ;
  - cloud sans MCP Playwright : le script du repo, sinon `npx playwright install chromium` puis
    `npx playwright screenshot --viewport-size=<w>,<h> <url> <fichier>` ; si rien ne marche,
    dis-le et saute l'étape en le signalant dans la PR.
- Référence charte : celle du repo ; pour la marque AVQN, `styleguide.avqn.ch/llms.txt`.

## La boucle

```
1. lance l'app (recette du repo ; vérifie que ça répond vraiment)
2. pour chaque page × chaque breakpoint :
     navigue → redimensionne (w,h) → capture → LIS la capture
3. JUGE contre DEUX références :
     - la SPEC (le rendu visé)
     - la CHARTE (celle du repo ; AVQN : styleguide.avqn.ch/llms.txt + conventions du repo)
   Critères : hiérarchie & lisibilité, alignements & espacements, cohérence charte,
   responsive sans casse, états (vide / erreur / chargement) si pertinents.
4. Pas satisfait → défauts concrets → AMÉLIORE LE CODE → retour en 2.
5. Satisfait → continue vers la gate + la PR.
```

## Garde-fous

- **Plafond ~3-4 passes.** Pas de convergence → arrête, montre les captures + ce qui bloque,
  mets de côté. Pas de PR sur un rendu non abouti, pas de boucle infinie non plus.
- **Local uniquement** : jamais de jugement sur la preview/prod.
- **Améliore le code, pas la capture** ; juge contre des références, pas à l'instinct.
