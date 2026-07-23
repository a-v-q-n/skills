---
name: suivre-les-objectifs
description: >-
  À utiliser dès qu'on touche au pilotage d'AVQN OS : poser ou revoir les objectifs d'un
  trimestre (OKR), définir des cibles chiffrées, créer ou corriger une métrique, enregistrer
  ou rattraper des mesures, ou lire l'avancement (« où en est le trimestre ? »). Orchestre le
  domaine pilotage — objectif qualitatif par trimestre, métrique unique et permanente
  (jauge|compteur), cible datée posée sur une métrique, mesure par (métrique, jour). Charge
  d'abord le socle piloter-avqn-os. NE COUVRE PAS le relevé quotidien automatique des réseaux
  (routine cloud « zernio-daily ») ni les statistiques sociales elles-mêmes (MCP Zernio).
---

# Suivre les objectifs

Commencer par charger le socle `piloter-avqn-os`.

## La grammaire du pilotage

Quatre objets, une hiérarchie stricte :

- **L'objectif** — le cap d'un trimestre, qualitatif, **sans aucun chiffre**. Clé `2026-q3.o1`.
  Peu d'objectifs à la fois : le focus est la règle, un seul est un bon défaut.
- **La métrique** — ce qu'on mesure. **Unique et permanente** : on ne la duplique jamais pour
  poser une nouvelle ambition dessus, et elle ne porte jamais de valeur d'arrivée.
- **La cible** (le KR) — une ambition datée posée **sur** une métrique existante : « amener
  cette métrique de A à B ». Elle hérite la période de son objectif ; son échéance est le
  dernier jour du trimestre, toujours. Clé `2026-q3.o1.kr1`.
- **La mesure** — une valeur sur (métrique, jour), signée d'une `source`. **Upsert** : rejouer
  le même jour corrige le point au lieu d'en créer un second — les routines sont idempotentes
  par construction, et un rattrapage se rejoue sans précaution.

`avqn-os:pilotage_dashboard` rend tout ça d'un coup : avancement des cibles + galerie des
métriques avec leurs courbes. C'est la lecture par défaut ; ne pas reconstruire à la main.

## Jauge ou compteur — le seul vrai choix

Le `type` d'une métrique dit ce qu'**une ligne de mesure** signifie :

- **jauge** = un état à cette date (abonnés, rang, clients actifs). Valeur courante = la
  dernière mesure.
- **compteur** = ce qui s'est produit **ce jour-là** (posts, CHF facturés, audits). Valeur =
  la somme sur la période.

Test : *ce nombre peut-il baisser tout seul ?* Oui → jauge. Non → compteur.

**Le piège classique : écrire un cumul dans un compteur.** On enregistre le delta du jour,
le serveur somme tout seul. Une source qui expose un cumul (total de posts, CA à date) se
convertit en deltas avant d'écrire — sinon la courbe explose.

## Les métriques réseaux se relèvent toutes seules

Une routine cloud (« Relevé quotidien réseaux », source `zernio-daily`) tourne chaque matin
à 8 h et alimente depuis Zernio : `abonnes-linkedin`, `abonnes-tiktok`, `abonnes-youtube`
(jauges) et `posts-publies`, `interactions` (compteurs). Elle rebalaie les 7 derniers jours
à chaque passage pour absorber les resynchros Zernio.

- **Ne pas saisir ces cinq métriques à la main** : le prochain passage écraserait la saisie.
  Un trou se rattrape en relançant la routine, pas au clavier.
- `interactions` = likes + commentaires + partages + saves **gagnés ce jour-là** (attribution
  « received » : l'engagement d'un vieux post compte le jour où il arrive).
- TikTok et YouTube ne remontent ni impressions ni portée à Zernio (vues + likes +
  commentaires seulement) ; LinkedIn remonte tout.

## Gestes courants

| Geste | Outil |
|---|---|
| Lire l'avancement du trimestre | `avqn-os:pilotage_dashboard` |
| Poser ou retoucher un objectif | `avqn-os:objectif_upsert` |
| Créer ou retoucher une métrique | `avqn-os:metrique_upsert` |
| Poser un KR | `avqn-os:cible_upsert` |
| Enregistrer des mesures | `avqn-os:mesure_record` (en lot, source signée) |
| Savoir quelles ambitions s'appuient sur une métrique | `avqn-os:cible_list {metriqueKey}` |

## Invariants

- **Un objectif ne porte aucun chiffre** ; toute ambition chiffrée est une cible.
- **Créer la métrique avant la cible** qui la vise.
- **Retirer une métrique des vues** = `metrique_upsert active=false` — la courbe survit. La
  suppression détruit toute la série, exige `confirm`, et est refusée tant qu'une cible
  s'appuie dessus.
- **Supprimer un objectif** emporte ses cibles, jamais les mesures.
- **En refonte : définir la nouvelle structure d'abord, effacer ensuite** — jamais d'ardoise
  vide entre les deux. Et vérifier avant de jeter : les courbes d'historique ont de la valeur.
- **`fromValue` d'une cible** : le laisser se dériver (jauge : état à l'entrée de période ;
  compteur : zéro), sauf départ connu et daté — un point de départ faux fausse toute la
  progression.
