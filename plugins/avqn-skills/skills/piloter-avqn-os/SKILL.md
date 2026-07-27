---
name: piloter-avqn-os
description: >-
  À charger avant toute action dans AVQN OS (le MCP `avqn-os` : CRM, tâches, carnet, temps,
  facturation, agenda, mail, pilotage). Porte la grammaire des objets — la partie personne|
  organisation comme unité du CRM, les rôles dérivés jamais saisis, le projet comme pivot, la
  fiche comme état d'un objet et le carnet comme journal — la matrice de rangement (où va quelle
  information), le réflexe `recall`/`contexte` avant toute recherche, et les invariants à ne
  jamais violer. Socle chargé par tenir-le-crm, gerer-les-projets, gerer-les-taches,
  tenir-le-carnet, suivre-le-temps, suivre-les-objectifs et creer-une-facture. NE COUVRE PAS les
  gestes d'un domaine précis (voir la recette correspondante) ni l'infra (OS séparé `ops`).
---

# Piloter AVQN OS

AVQN OS est le cerveau business de Manu, exposé par le MCP `avqn-os`. Ce socle donne la carte
et les règles ; les recettes donnent les gestes.

## Deux mondes, une règle

- **Systèmes de référence** — agenda CalDAV, mail IMAP, GitHub pour le code. La vérité vit chez
  le provider ; l'OS pilote à distance et **ne duplique rien**.
- **Cerveau propre** — Postgres interne : CRM, tâches, carnet, temps, facturation, pilotage.
  C'est là que l'OS fait autorité.

L'infra (Coolify, Hetzner, DNS, R2, backups) vit dans un **autre** MCP, `ops`. Ne jamais la
chercher ici.

## Le réflexe : chercher avant d'écrire

Deux outils transverses, à utiliser **avant** de fouiller domaine par domaine :

- **`avqn-os:recall`** — « où ai-je vu ça ? ». Recherche transversale sur tout l'OS **plus** les
  mails et l'agenda indexés. Filtres : `kinds`, `partieId`, `projectId`, `since`/`until`.
- **`avqn-os:contexte`** — « donne-moi le dossier de… ». Consolide le 360° d'une **partie**, d'un
  **deal** ou d'un **projet** : fiche, rôles, affiliations, deals, projets, tâches, temps, notes,
  mails, événements. Résout par nom ; une ambiguïté renvoie des candidats, pas une erreur.

Chaque item rendu porte son `agir` — l'outil exact pour le lire ou le modifier. S'en servir
plutôt que deviner.

`contexte` accepte `sections` pour ne charger qu'une partie du dossier : `affiliations`,
`participants`, `deals`, `projets`, `taches`, `temps`, `notes`, `mails`, `evenements`.

## La grammaire des objets

### La partie — l'unité du CRM

Une **partie** (`avqn_partie`) est une **personne physique** ou une **organisation**. C'est la
cible unique de tout l'aval : deal, projet, facture, note. **Une personne est facturable au même
titre qu'une entreprise** — ne jamais créer une fausse société pour facturer quelqu'un.

Une **affiliation** relie une personne à une organisation, en N-N et datée. Un départ se **clôt**
(`endedOn`), il ne s'écrase pas.

### Les rôles se dérivent, ils ne se saisissent pas

| Rôle | Ce qui le prouve |
|---|---|
| **client** | un deal `gagne`, ou une facture émise (avec numéro) |
| **prospect** | un deal ouvert (`piste`, `qualifie`, `proposition`) |
| **réseau** | présent dans l'annuaire, sans rien de ce qui précède |

`client` et `prospect` **se cumulent**. Aucun statut relationnel n'est stocké : ne jamais chercher
à « marquer quelqu'un comme client », c'est son activité qui le dit.

### Le projet — le pivot

`avqn_project` agrège une partie / un deal et le travail facturable (tâches, temps, notes).
Containment optionnel avec **héritage vers le haut** : on s'attache au niveau le plus fin connu,
et partie / projet / taux se **dérivent** en remontant — jamais recopiés.

Nom, format de fiche, dates et cycle de vie du statut (dont l'absence de suppression dure) :
**`gerer-les-projets`**.

## La matrice de rangement

Avant d'écrire quoi que ce soit, une seule question : **de quoi cette information est-elle la
réponse ?**

| Objet | Répond à | Exemple |
|---|---|---|
| **Fiche de partie** | Qui c'est, comment travailler avec | « Ne pas court-circuiter Sébastien » |
| **Fiche de deal** | Ce qui se vend, à quelles conditions | « 1'100 CHF, payé après chaque phase » |
| **Fiche de projet** | Ce qu'on a fait, ce qu'on en retient | Les phases livrées, les enseignements |
| **Note de carnet** | Quand, et ce qui s'est dit ce jour-là | « Session 3 à Payerne » |
| **Tâche** | Ce qui reste à faire | « Relancer Antoine » |
| **Facture** | L'argent et son état | 10'000 CHF, émise, impayée |

Deux tests, dans cet ordre :

> **1. Est-ce que ça a une date qui compte ?**
> **Oui** → c'est un **événement** → une note du carnet, datée et liée.
> **Non**, ça décrit ce qu'un objet **est** maintenant → c'est son **état** → sa **fiche**.

> **2. Est-ce que cette phrase pourrait être copiée telle quelle dans un autre objet ?**
> **Oui** → elle est au mauvais endroit dans au moins un des deux. Trancher, et faire renvoyer
> l'un vers l'autre plutôt que de dupliquer.

Une fiche qui grossit est presque toujours une fiche qui a absorbé ce qui appartient à un autre
objet : le déroulé d'un mandat, sa chronologie, l'état d'une créance.

**La fiche** est un champ de l'objet (`partie`, `deal`, `project`, `task`, `offre`), en markdown.
Une par sujet, et elle doit rester **juste** : on la corrige, on ne l'empile pas. Elle s'écrit par
le tool de son domaine (`partie_update {fiche}`) ou, pour ajouter sans relire un long document,
par **`avqn-os:fiche_append`**.

La fiche décrit ce que le sujet **est** ; elle n'accueille pas tout ce qui le **concerne**. Un bloc
qui a une vie propre — qu'on voudra compter, dater, relier ou retrouver seul — est un objet, pas
une section. Quand un document n'a pas de sujet, il ne manque pas un tiroir : **il manque un
objet**.

**Le carnet** est le journal : une seule table de notes pour tout l'OS, toutes datées. Le titre
suit la portée (jalon titré, note de fil sans titre). Une note porte **UN rattachement** — l'endroit
le plus fin que l'événement concerne (**tâche > projet > deal > partie**) — et **des présents**
(les personnes impliquées que le graphe ne déduit pas). Tout le reste **se dérive à la lecture** :
le dossier d'une partie hérite des notes de ses deals et de ses projets, on ne re-lie donc jamais un
ancêtre. **La cascade frappe le lien, jamais la note** — supprimer un deal détache sa documentation
sans la détruire. Règle complète : `tenir-le-carnet`.

### Les tâches — un engagement, pas un statut

Quatre postures (`Capture`, `Aujourd'hui`, `Plus tard`, `Peut-être`) et des **facettes**
(`scheduledFor`, `dueDate`, `waitingOn`) qui ne sont jamais des statuts. Détail dans
`gerer-les-taches`.

## Écrire juste

**Une fiche fausse est pire qu'une fiche absente** : l'agent la lit comme vraie et agit dessus.

- **Ne consigner que ce que la source établit.** Un numéro de téléphone plausible, un rôle déduit
  d'un nom de domaine, un déroulé de séance reconstitué de mémoire : ce sont des inventions. Un
  champ vide, ou un marqueur explicite (*« à confirmer »*, *« contenu non consigné »*), vaut mieux.
- **Croiser avant de conclure.** Un mail d'invitation ne prouve pas qu'une réunion a eu lieu ; une
  saisie de temps, oui. Un dossier qui semble réussi peut avoir une fin manquée que seuls les
  derniers mails racontent.
- **Distinguer le fait de la lecture.** « Il ne s'est pas présenté » est un fait ; « il se
  désintéresse » est une interprétation. Écrire les deux, en les distinguant.
- **Les données structurées vont dans leurs champs**, pas dans le corps d'une fiche. Une
  coordonnée noyée dans du markdown n'est ni cherchable, ni reprise par la facturation.

## Lire ce qu'on écrit

L'objet renvoyé par un tool d'écriture porte ce que le serveur a réellement enregistré, y compris
ce qu'il a **dérivé** : l'id du projet créé par `deal_win`, le taux résolu d'une saisie de temps,
le numéro attribué à l'émission d'une facture. Le lire plutôt que le supposer — c'est de là que
vient l'id qu'on passera à l'étape suivante.

Quand une opération ne peut pas aboutir — un statut qui interdit le geste, une suppression refusée
— **s'arrêter et le dire à Manu**, plutôt que de contourner par un chemin qui laisserait des
références cassées. Le refus est presque toujours un garde-fou, pas un obstacle.

## Invariants

- **Une tâche de dev** (livrable = du code) va en **Issue GitHub**, jamais en tâche maison.
- **`deal_win` est le seul chemin vers `gagne`** : il crée le projet rattaché. `deal_update`
  refuse cette étape.
- **Les outils destructifs exigent `confirm`** répétant l'identifiant exact. Toujours demander
  l'aval de Manu avant — et préférer l'archivage à la suppression quand il existe.
- **Ne jamais afficher un secret ni un OTP**, même lu au passage.
- **Le journal s'écrit tout seul** : ne pas chercher à le tenir à la main.
- **Ne pas recopier ce qui se dérive** (le client d'un temps, le taux d'un projet) : lire la
  valeur résolue, ne pas la figer ailleurs.
- **Une fiche fausse est pire qu'une fiche absente.** Ce qui change se corrige dans la fiche ; si
  le changement compte, il devient aussi une note datée.

## Les domaines et leur recette

| Domaine | Outils | Recette |
|---|---|---|
| CRM | `partie_*`, `affiliation_*`, `deal_*`, `offre_*` | `tenir-le-crm` |
| Projets | `project_*` | `gerer-les-projets` |
| Tâches | `task_*` | `gerer-les-taches` |
| Carnet | `carnet_*` | `tenir-le-carnet` |
| Fiches | `fiche_append` (transverse) | ce socle |
| Temps | `timesheet_*`, `activity_*` | `suivre-le-temps` |
| Facturation | `invoice_*` | `creer-une-facture` |
| Agenda | `cal_*` | — outils directs (CalDAV) |
| Mail | `mail_*` | — outils directs (IMAP) |
| Pilotage | `objectif_*`, `metrique_*`, `cible_*`, `mesure_record`, `pilotage_dashboard` | `suivre-les-objectifs` |

Le vocabulaire complet, avec les correspondances depuis l'ancienne grammaire, est dans
`references/grammaire.md` — à charger si un doute subsiste sur un nom d'objet.

## Le cockpit

`cockpit.avqn.ch` rend la même donnée en interface (Cockpit, Tâches, Projets, Temps, CRM,
Carnet, Pilotage, Facturation). Y renvoyer Manu quand il s'agit de **regarder** plutôt que d'agir.
