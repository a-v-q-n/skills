---
name: gerer-les-projets
description: >-
  À utiliser dès qu'on crée, renomme, date, décrit, met en pause, clôt ou range un projet
  d'AVQN OS — ou qu'on remet de l'ordre dans la liste des projets. Orchestre le domaine projet :
  le projet comme engagement réel (jamais sur-découpé), la convention de nommage, le format de
  fiche unifié (Objectif / Cadre / Points clés), les dates de période et le cycle de vie du
  statut (active, paused, done, dropped — pas de suppression dure). Commence par la grammaire
  du serveur (avqn-os:grammaire). NE COUVRE PAS les tâches d'un projet (gerer-les-taches), le temps passé
  (suivre-le-temps), la facturation (creer-une-facture) ni la naissance d'un projet gagné
  (deal_win, voir tenir-le-crm).
---

# Gérer les projets

Commencer par appeler **`avqn-os:grammaire`** (sans argument, puis `{domaine: "taches"}` — le
projet y vit avec les tâches).

Un projet (`avqn_project`) est le **pivot** : il agrège tâches, temps et notes autour d'une
partie / d'un deal. Ce skill porte ce qu'un projet **est** et comment le tenir propre ; les
gestes sur ce qu'il contient vivent dans les recettes des domaines (`gerer-les-taches`,
`suivre-le-temps`, `creer-une-facture`).

## Un projet = un engagement réel

On crée un projet quand il y a **plusieurs étapes** et un résultat à suivre — pas pour ranger.
Pas de sur-découpage : un mandat qui contient formation + dashboard + suivi reste **un** projet
dont la fiche liste les volets, pas quatre projets frères.

Un projet **gagné** naît tout seul : `deal_win` le crée et le rattache. Ne pas le doubler à la
main (voir `tenir-le-crm`).

## Nommage

Forme `<Livrable/Type> — <Client>` : `Coaching n8n — Kévin`,
`Formation « X » — <Client>`, `Bootcamp n8n — Emploi Lausanne (pilote)`. Un projet interne prend
un nom court et parlant (`Site AVQN.ch`, `Baromètre IA des indépendants romands`). Le nom se
formule comme un résultat, pas comme une catégorie fourre-tout.

## La fiche — toujours la même structure

Courte, elle dit l'**état** du projet, jamais un journal (les événements datés vont au carnet) :

```
**Objectif** — une phrase : ce que le projet vise.

**Cadre** — client ou interne · facturable ou non · période.

**Points clés**
- 2 à 4 puces : livrable, angle, jalon.
```

Bloc optionnel **Repères** quand le projet porte des données de référence à garder sous la main
(études à citer, seuils, chiffres d'ancrage). Au-delà, si un bloc a une vie propre — qu'on
voudra compter, dater ou retrouver seul — c'est un objet (note, tâche), pas une section de fiche.

## Les dates portent la période

`startDate` / `endDate` (les champs, pas la fiche) portent la période réelle — c'est ce qui
alimente la timeline du cockpit. Période en cours → laisser `endDate` sur la fin prévue.

## Le cycle de vie du statut

| Statut | Ce qu'il dit |
|---|---|
| `active` | en cours |
| `paused` | suspendu, repris plus tard |
| `done` | livré, période close |
| `dropped` | abandonné consciemment |

Règle de barre : période révolue et livrée → `done` ; en cours → `active`.

**Pas de suppression dure pour un projet.** `dropped` est l'état terminal : le projet sort des
vues actives sans rien détruire (ses tâches, temps et notes restent). Pour fusionner un doublon,
porter le contenu sur le projet gardé, puis passer l'autre en `dropped` avec une fiche qui
pointe le survivant.

## Les gestes

- **`avqn-os:project_list`** — actifs + en pause ; `includeClosed: true` pour voir done/dropped.
- **`avqn-os:project_get { id }`** — le projet et toutes ses tâches.
- **`avqn-os:project_create`** — `name`, `clientId`, `dealId`, `billable`, `startDate`/`endDate`,
  `repo`, `fiche`. Ne créer que s'il y a vraiment plusieurs étapes.
- **`avqn-os:project_update`** — nom, statut, dates, fiche, rattachements. `clientId: null` pour
  le rendre interne/perso.
- **`avqn-os:contexte { projet }`** — le dossier 360° d'un projet avant d'agir.

`repo` (`owner/nom`) fait d'un projet un **projet de dev** : son travail vit en Issues GitHub,
pas en tâches maison. Le client se **dérive** du deal rattaché — ne pas le recopier si le deal
le porte déjà.
