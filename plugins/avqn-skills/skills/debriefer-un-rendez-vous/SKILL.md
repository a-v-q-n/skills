---
name: debriefer-un-rendez-vous
description: >-
  À utiliser après un call, un rendez-vous ou une séance, quand Manu débriefe (souvent en
  vocal) : trier la matière et la ranger dans tout l'OS — la note de carnet, les fiches à
  mettre à jour, le deal à ouvrir ou faire avancer, les tâches, le prochain rendez-vous à
  l'agenda, la séance à saisir en temps — puis restituer à Manu ce qui a été rangé où.
  Jamais une simple transcription de la voice note en note. NE COUVRE PAS la préparation
  en amont (preparer-un-rendez-vous) ni la proposition écrite qui suit un accord
  (emettre-une-offre).
---

# Débriefer un rendez-vous

Le débrief de Manu est de la matière en vrac : dans la même voice note, il y a ce qui s'est
dit, ce qu'il a appris, ce qu'il a promis, ce qui est convenu pour la suite. Chaque morceau
répond à une question différente, donc chaque morceau a sa place à lui dans l'OS. Le
transcrire tel quel dans une note, c'est enterrer les trois quarts de l'information là où
personne ne la retrouvera.

Appeler `grammaire {domaine: "carnet"}` avant la première écriture de la session — la
matrice de rangement vit là-bas, ce skill l'applique au geste du débrief.

## La séquence

### 1. Situer

De quel rendez-vous s'agit-il ? `contexte` sur le dossier (partie, deal ou projet), et au
besoin l'agenda pour la date exacte. Le rattachement de la note en dépend : un appel de
cadrage ou une négociation vise le **deal**, une séance ou un livrable vise le **projet**,
un échange de réseau vise la **partie**.

### 2. Trier la matière

Passer le débrief au crible, morceau par morceau :

| Ce que dit le débrief | Où ça va |
|---|---|
| Ce qui s'est dit, décidé, vécu ce jour-là | **Une note de carnet** — rattachée au plus fin, `noteDate` = le jour du rendez-vous, présents en `interlocuteurs`, titre seulement si c'est un jalon |
| Ce qu'on a appris de durable (structure, profil, contraintes, façon de travailler) | **La fiche** de l'objet concerné (`fiche_append`) — et la note y renvoie au lieu de le répéter |
| Ce qu'il y a à faire (promesse de Manu, suite convenue) | **Une tâche** — `task_capture` en vrac, ou `task_create { scheduledFor }` si la date est convenue. Une tâche de dev (livrable = du code) va en **Issue GitHub**, jamais ici |
| Un prochain rendez-vous convenu | **L'agenda** — `cal_event_create`, heure suisse, sur le bon calendrier (`cal_calendars`) |
| Un objet à vendre qui apparaît ou qui avance | **Le deal** — `deal_create` s'il naît, `deal_update` pour l'étape et la probabilité (toujours cohérentes), le pourquoi daté dans sa fiche |
| Un accord de vive voix sur le prix et le format | Le deal avance, et **la suite est `emettre-une-offre`** — le proposer à Manu |
| Une séance facturable tenue | **Une saisie de temps** (`timesheet_create`, rattachée au plus fin) — c'est elle qui prouve le travail, pas l'invitation d'agenda |

### 3. Écrire

La note d'abord — c'est l'ancre du souvenir — puis le reste. **Une note, pas dix** : le
rendez-vous entier tient dans une note au grain du jalon ; la logistique (« on s'est
rappelés », « décalé d'une heure ») ne s'écrit pas. Et une note ne dit jamais quoi faire :
ce qui est à faire est parti en tâche.

### 4. Restituer

Rendre à Manu le plan de rangement, court : la note (où rattachée), les fiches touchées,
les tâches créées, l'événement posé, le deal bougé. C'est sa relecture — et c'est là qu'il
corrige un tri avant qu'il ne fige.

## Les règles

- **Ne consigner que ce que Manu a dit.** Un débrief n'est pas un procès-verbal : les trous
  restent des trous (*« contenu non consigné »*), jamais comblés par une reconstitution
  plausible.
- **Le fait et la lecture se distinguent.** « Il n'a pas ouvert le devis » est un fait ;
  « il hésite » est une interprétation de Manu — les écrire tous les deux, en les
  distinguant.
- **L'ambigu se demande.** Un prénom sans nom, une date floue, un « on s'est dit qu'on se
  reverrait » sans engagement : demander à Manu plutôt que de deviner un rattachement, une
  échéance ou un montant.
- **Le débrief peut déborder du dossier.** Une personne nouvelle mentionnée avec un vrai
  rôle entre au CRM (jamais sur supposition) ; une idée transversale devient une note
  libre. Le crible s'applique à tout ce que la voice note contient, pas au seul
  rendez-vous.

## Checklist avant de rendre la main

- [ ] La note porte l'événement, rattachée au plus fin, datée du jour du rendez-vous
- [ ] Rien de durable n'est resté dans la note : les fiches concernées sont à jour
- [ ] Chaque chose à faire est une tâche (ou une Issue GitHub si c'est du dev)
- [ ] Le rendez-vous convenu est à l'agenda, la séance tenue est saisie en temps
- [ ] Le deal reflète la réalité du jour (étape, probabilité, fiche datée)
- [ ] Le plan de rangement a été restitué à Manu, l'ambigu lui a été demandé
