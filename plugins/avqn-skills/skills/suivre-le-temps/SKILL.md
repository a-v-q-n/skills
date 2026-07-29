---
name: suivre-le-temps
description: >-
  À utiliser dès qu'on saisit du temps passé, qu'on corrige une saisie ou qu'on veut savoir
  combien d'heures sont allées où : « j'ai passé 2 h sur… », « combien sur ce client ce mois-ci ? ».
  Orchestre le domaine temps d'AVQN OS — saisies rattachées au niveau le plus fin, activités
  comme référentiel de prestations, taux dérivé par cascade, rapport par client, projet ou
  activité. Commence par la grammaire du serveur (avqn-os:grammaire). NE COUVRE PAS la facturation de ces heures
  (creer-une-facture) ni les tâches elles-mêmes (gerer-les-taches).
---

# Suivre le temps

Commencer par appeler **`avqn-os:grammaire`** (sans argument, puis `{domaine: "temps"}`).

## S'accrocher au niveau le plus fin connu

Une saisie se rattache à une **tâche** si elle est connue, sinon à un **projet**, sinon à rien.
Projet et partie effectifs se **dérivent** en remontant la chaîne — **ne jamais les recopier sur
la saisie**, ils n'y ont pas leur place.

```
avqn-os:timesheet_create { begin, end, description, taskId }     ← le mieux
avqn-os:timesheet_create { begin, end, description, projectId }  ← à défaut
```

Toujours mettre une **description** : une saisie sans description n'est pas indexée et ne se
retrouve pas. C'est la différence entre une heure comptée et une heure racontée.

## Le taux se dérive, il ne se saisit pas

Ordre de résolution — **le premier renseigné gagne** :

1. le taux de l'**activité** (le type de prestation),
2. le taux du **projet**,
3. le taux par défaut de la **partie**.

Pour changer ce qui sera facturé, poser le taux au bon niveau plutôt que de corriger saisie par
saisie.

## Les activités

Le référentiel des types de prestation (Dev, Réunion, Design…), avec un taux optionnel :
`avqn-os:activity_list` / `activity_create` / `activity_update`. C'est un référentiel, pas une
catégorisation obligatoire — ne pas en inventer une par saisie.

## Les gestes

- **`avqn-os:timesheet_list`** — filtres de période et de rattachement.
- **`avqn-os:timesheet_get`** — une saisie avec ses champs **résolus** (projet, partie, taux).
- **`avqn-os:timesheet_update`** — corriger bornes, description, rattachement.
- **`avqn-os:timesheet_delete`** — destructif, `confirm` requis.
- **`avqn-os:timesheet_report { groupBy, from, to }`** — total d'heures agrégé.
  `groupBy` vaut `client`, `project` ou `activity`. L'axe `client` agrège par **partie** (le nom
  de l'axe a gardé le mot d'usage comptable).

`billable` marque ce qui est facturable ; le rapport distingue total et facturable.

## Répondre à « combien de temps sur X ? »

Passer par **`avqn-os:contexte`** sur la partie ou le projet : la section `temps` rend déjà
l'agrégat des six derniers mois et les dernières saisies décrites, avec leur `agir`. C'est plus
direct que de reconstruire depuis `timesheet_list`.

Pour une période précise ou un axe particulier, `timesheet_report` avec `from` / `to`.
