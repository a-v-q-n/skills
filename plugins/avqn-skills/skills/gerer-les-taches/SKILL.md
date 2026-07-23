---
name: gerer-les-taches
description: >-
  À utiliser dès que Manu mentionne quelque chose à faire, veut trier sa journée, replanifier,
  déléguer ou clore une tâche. Orchestre le domaine tâches d'AVQN OS — capture sans friction,
  quatre postures d'engagement (Capture, Aujourd'hui, Plus tard, Peut-être) et des facettes
  (planifiée, échéance, en attente) qui ne sont jamais des statuts, et le rattachement d'une
  tâche à son projet. Charge d'abord le socle piloter-avqn-os. NE COUVRE PAS les tâches de dev
  (elles vont en Issue GitHub), le temps passé dessus (suivre-le-temps) ni la tenue des projets
  eux-mêmes — nom, fiche, statut (gerer-les-projets).
---

# Gérer les tâches

Commencer par charger **`piloter-avqn-os`**.

## Capturer d'abord, trier ensuite

Dès que Manu mentionne quelque chose à faire, **`avqn-os:task_capture { title }`** — un titre
suffit, la tâche tombe dans la Capture. Ne jamais interrompre Manu pour demander un projet, une
date ou une priorité : le tri vient après, c'est tout l'intérêt d'une boîte de capture.

**Une tâche de dev n'entre pas ici.** Si le livrable est du code (commit, PR), c'est une **Issue
GitHub** — GitHub est le système de référence du domaine code, on n'y duplique rien.

## Les quatre postures

Le `bucket` dit l'**engagement**, pas l'avancement :

| Bucket | Produit | Ce que ça engage |
|---|---|---|
| `inbox` | Capture | capturé, pas encore trié |
| `today` | Aujourd'hui | choisi pour aujourd'hui |
| `next` | Plus tard | engagé, sans date — groupé par projet, tête de pile = prochaine action |
| `someday` | Peut-être | parking assumé, zéro engagement |

Terminaux : `done` (fait) et `dropped` — **rayé consciemment, ce n'est pas la même chose que
fait**. Utiliser `dropped` quand Manu renonce, pas `done`.

## Les facettes ne sont pas des statuts

Elles se posent **en plus** du bucket et font remonter la tâche toute seule :

- **`scheduledFor`** — dormante jusqu'à sa date, puis remonte dans Aujourd'hui. C'est l'outil du
  « pas maintenant, le 12 ».
- **`dueDate`** — échéance externe. Dépassée, la tâche remonte dans Aujourd'hui où qu'elle soit.
- **`waitingOn`** — en attente de quelqu'un ; la tâche reste où elle est, grisée. À utiliser dès
  que la balle est dans le camp d'un tiers.

Ne jamais déplacer une tâche dans `today` pour signaler une urgence : poser `dueDate`. Ne jamais
la sortir de la liste parce qu'on attend : poser `waitingOn`.

## Les gestes

- **`avqn-os:task_list`** — sans filtre : toutes les ouvertes, triées par position (ordre manuel
  de Manu, à respecter). Filtres `buckets`, `projectId`, `q`, `dueBefore`, `scheduledUntil`.
- **`avqn-os:task_update`** — bucket, dates, projet, `waitingOn`, notes.
- **`avqn-os:task_complete`** / **`avqn-os:task_reopen`** — clore, rouvrir.
- **`avqn-os:task_create`** — quand le contexte est déjà connu (projet, date). Sinon, capturer.
- **`avqn-os:task_delete`** — destructif, `confirm` requis. Préférer `dropped` : ça garde la
  trace du renoncement.
- **`avqn-os:task_digest_send`** — envoie le digest par mail.

Les sous-étapes sont une **checklist markdown dans `notes`** (`- [ ] …`), pas des sous-tâches :
il n'y a pas d'arbre.

## Ranger une tâche dans son projet

Une tâche se rattache à un projet — le pivot qui regroupe tâches, temps et notes :
`avqn-os:task_update { projectId }`. Ici on ne fait que **rattacher**. Créer, nommer, dater,
clore ou fusionner un projet, c'est **`gerer-les-projets`**.

`repo` (au format `owner/nom`) fait d'un projet un projet de dev : son travail vit alors en
Issues GitHub, pas en tâches maison.

## Trier une journée

1. `avqn-os:task_list { buckets: ["inbox"] }` — vider la Capture : chaque élément part vers une
   posture, un projet, une date, ou `dropped`.
2. `avqn-os:task_list { buckets: ["today"] }` — ce qui est choisi, plus ce que les facettes ont
   fait remonter (planifiées du jour, échues).
3. Proposer, ne pas décider : l'ordre manuel appartient à Manu.
