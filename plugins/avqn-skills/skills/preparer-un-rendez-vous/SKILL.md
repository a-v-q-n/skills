---
name: preparer-un-rendez-vous
description: >-
  À utiliser avant tout rendez-vous, quel que soit le canal (call, visio, présentiel) et
  le registre (appel découverte, cadrage, négociation, séance de coaching ou de
  formation) : rassembler ce que l'OS sait du dossier, y ajouter la correspondance tirée de
  `comms`, et rendre un brief court à Manu — qui, où on en est, ce qui s'est dit
  la dernière fois, les points ouverts et les drapeaux, l'objectif du rendez-vous et les
  questions à poser. Lecture seule : ce skill n'écrit rien. NE COUVRE PAS le
  débrief d'après le rendez-vous (debriefer-un-rendez-vous) ni la création de
  l'événement à l'agenda.
couche: recette
moment: >-
  Un call approche : le dossier relu et condensé en brief. Lecture seule.
famille: cycle-client
---

# Préparer un rendez-vous

Arriver briefé, c'est arriver en ayant relu — pas en improvisant sur des souvenirs. Le brief
se lit en deux minutes avant de décrocher. Il ne modifie rien : ce qui manque au dossier
devient une question à poser pendant le rendez-vous, et c'est le débrief qui consignera.

## Deux serveurs, une jointure

Le dossier se compose de deux moitiés, et **l'adresse est ce qui les relie** :

- **L'OS** (`avqn-os`) sait la relation, le travail et l'argent : la partie, ses affiliés
  **avec leurs adresses**, les deals, projets, tâches, temps, notes et factures.
- **`comms`** tient le courrier et les agendas, sur plusieurs boîtes.

L'un ne sait rien de l'autre. Un brief bâti sur le seul OS ignore ce qui s'est échangé par
mail ; un brief bâti sur le seul courrier ignore l'argent et les engagements.

## La séquence

### 1. Identifier le rendez-vous

Ce que Manu dit, ou l'agenda : `cal_event_list` (sur `comms`) sur la plage concernée. Les
calendriers se découvrent par `cal_calendars`, jamais présumés ; `calendrier: "*"` balaie
ceux de toutes les boîtes. En tirer : avec qui, quand, quel objet.

### 2. Charger le dossier

`contexte { q: "<nom>" }` sur la partie, le deal ou le projet concerné — fiche, rôles,
affiliations, deals, projets, tâches, temps, notes, factures. C'est la colonne vertébrale du
brief.

**En retenir les adresses** : celle de la fiche et celle de chaque affilié. Elles servent à
l'étape 4.

### 3. Identifier le registre

Le rendez-vous est de la **conquête** ou de la **livraison**, et tout le brief s'en
infléchit :

- **Conquête** (appel découverte, cadrage, négociation) — le dossier est le **deal**. Ce
  qui compte : ce que la personne a demandé, l'état du devis et ses dates, l'étape et la
  probabilité, ce qui bloque la décision. L'objectif du rendez-vous est commercial :
  qualifier, obtenir l'accord, débloquer.
- **Livraison** (séance de coaching, formation, atelier, point d'avancement) — le dossier
  est le **projet**. Ce qui compte : la note de la dernière séance, où on s'était arrêté,
  ce que la personne devait pratiquer entre-temps, où on en est dans le programme
  (séances faites sur séances vendues, via le temps saisi). L'objectif est pédagogique :
  ce que cette séance doit faire avancer.

Le canal (call, visio, présentiel) ne change rien au brief — seul le registre compte.

### 4. Creuser ce qui compte pour CE rendez-vous

- **Le fil du carnet** : les dernières notes rattachées — ce qui s'est dit la dernière
  fois, ce qui avait été convenu.
- **La correspondance** : `mail_search` sur `comms`, par `de:` sur **chaque adresse retenue à
  l'étape 2**. Chercher sur la seule adresse générique d'une organisation manque tout
  l'échange réel, qui passe par les personnes. Le courrier entrant est classé hors INBOX et se
  cherche dossier par dossier — la carte des dossiers et les pièges vivent dans
  `deposer-un-brouillon-email`.
- **Le commercial** : un devis en cours et ses dates (`sentOn`, `validUntil` — expire-t-il
  bientôt ?), l'étape et la probabilité du deal.
- **L'argent** : une facture émise et impayée, un jalon d'échéancier qui approche.
- **Les engagements** : tâches ouvertes du dossier, en particulier ce qui est `waitingOn` —
  lui ou Manu.

### 5. Rendre le brief

Court, en conversation, toujours la même ossature :

1. **Qui** — deux phrases : la personne, son contexte, la relation.
2. **Où on en est** — l'état du deal ou du projet, en une phrase factuelle.
3. **La dernière fois** — ce qui s'est dit et ce qui avait été convenu, daté.
4. **Points ouverts et drapeaux** — ce qui attend une réponse, ce qui frotte : offre qui
   expire, facture échue, promesse non tenue (des deux côtés). Les nommer sans les
   enrober.
5. **L'objectif du rendez-vous** — la seule chose à obtenir pour que le dossier avance,
   dans le registre du rendez-vous (l'accord en conquête, l'avancée en livraison).
6. **Questions à poser** — y compris ce qui manque au dossier (une adresse de
   facturation, une date, un décideur) : le rendez-vous est le moment de l'obtenir.

## Les règles

- **Lecture seule.** Aucune écriture : pas de note « préparation », pas de mise à jour de
  fiche. Le débrief d'après-call range tout.
- **Les faits, datés.** Le brief cite ce que les sources établissent ; un trou dans le
  dossier se dit comme un trou (« la dernière séance n'a pas de contenu consigné »),
  jamais comblé de mémoire.
- **`recall` ne connaît pas le courrier.** Il cherche dans ce que l'OS SAIT. Une recherche
  muette n'y dit RIEN d'un échange par email : c'est `mail_search` qui répond de celui-là.
- **Court.** Un brief qui dépasse l'écran a raté sa cible : condenser, le dossier complet
  reste à un `contexte` de distance.

## Boucle d'amélioration

Quand Manu corrige un brief (un point manquant, un détail en trop, un drapeau raté),
chercher la règle qui aurait évité la correction et l'ajouter ici.
