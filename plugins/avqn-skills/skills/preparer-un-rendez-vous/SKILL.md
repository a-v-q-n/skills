---
name: preparer-un-rendez-vous
description: >-
  À utiliser avant un call, un rendez-vous ou une séance : rassembler tout ce que l'OS
  sait du dossier et rendre un brief court à Manu — qui, où on en est, ce qui s'est dit
  la dernière fois, les points ouverts et les drapeaux, l'objectif du rendez-vous et les
  questions à poser. Lecture seule : ce skill n'écrit rien dans l'OS. NE COUVRE PAS le
  débrief d'après le rendez-vous (debriefer-un-rendez-vous) ni la création de
  l'événement à l'agenda.
---

# Préparer un rendez-vous

Arriver briefé, c'est arriver en ayant relu — pas en improvisant sur des souvenirs. L'OS
sait tout ce qui s'est passé avec cette personne ; ce skill le condense en un brief qui se
lit en deux minutes avant de décrocher. Il ne modifie rien : ce qui manque au dossier
devient une question à poser pendant le rendez-vous, et c'est le débrief qui consignera.

## La séquence

### 1. Identifier le rendez-vous

Ce que Manu dit, ou l'agenda : `cal_event_list` sur la plage concernée (les calendriers se
découvrent par `cal_calendars`, jamais présumés). En tirer : avec qui, quand, quel objet.

### 2. Charger le dossier

`contexte { q: "<nom>" }` sur la partie, le deal ou le projet concerné — le 360° : fiche,
rôles, deals, projets, tâches, notes, factures, mails et événements récents. C'est la
colonne vertébrale du brief.

### 3. Creuser ce qui compte pour CE rendez-vous

- **Le fil du carnet** : les dernières notes rattachées — ce qui s'est dit la dernière
  fois, ce qui avait été convenu.
- **Les mails récents** du fil (`mail_search`) : ce qui s'est échangé depuis.
- **Le commercial** : un devis en cours et ses dates (`sentOn`, `validUntil` — expire-t-il
  bientôt ?), l'étape et la probabilité du deal.
- **L'argent** : une facture émise et impayée, un jalon d'échéancier qui approche.
- **Les engagements** : tâches ouvertes du dossier, en particulier ce qui est `waitingOn`
  — lui ou Manu.

### 4. Rendre le brief

Court, en conversation, toujours la même ossature :

1. **Qui** — deux phrases : la personne, son contexte, la relation.
2. **Où on en est** — l'état du deal ou du projet, en une phrase factuelle.
3. **La dernière fois** — ce qui s'est dit et ce qui avait été convenu, daté.
4. **Points ouverts et drapeaux** — ce qui attend une réponse, ce qui frotte : offre qui
   expire, facture échue, promesse non tenue (des deux côtés). Les nommer sans les
   enrober.
5. **L'objectif du rendez-vous** — la seule chose à obtenir pour que le dossier avance.
6. **Questions à poser** — y compris ce qui manque au dossier (une adresse de
   facturation, une date, un décideur) : le rendez-vous est le moment de l'obtenir.

## Les règles

- **Lecture seule.** Aucune écriture dans l'OS : pas de note « préparation », pas de mise
  à jour de fiche. Le débrief d'après-call range tout.
- **Les faits, datés.** Le brief cite ce que les sources établissent ; un trou dans le
  dossier se dit comme un trou (« la dernière séance n'a pas de contenu consigné »),
  jamais comblé de mémoire.
- **Court.** Un brief qui dépasse l'écran a raté sa cible : condenser, le dossier complet
  reste à un `contexte` de distance.
