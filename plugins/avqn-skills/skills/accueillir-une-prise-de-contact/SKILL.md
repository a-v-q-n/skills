---
name: accueillir-une-prise-de-contact
description: >-
  À utiliser dès qu'une prise de contact arrive (email, formulaire, recommandation,
  message après une formation) : enquêter sur la personne, la faire entrer au CRM, ouvrir
  un deal s'il y a un objet à vendre, consigner l'échange au carnet et préparer le
  brouillon de réponse dans la voix de Manu. Charge les socles ecrire-comme-manu (la
  voix), deposer-un-brouillon-email (la plomberie) et consigner-un-contact (l'entrée au
  CRM). NE COUVRE PAS la relance d'un prospect resté silencieux (relancer-un-prospect),
  la proposition écrite (emettre-une-offre) ni la consignation CRM elle-même
  (consigner-un-contact).
---

# Accueillir une prise de contact

La première réponse fixe le niveau de la relation. Elle doit être rapide, personnelle et
sobre : montrer qu'on a lu, proposer la suite la plus simple, ne rien vendre encore. Tout ce
qui s'apprend au passage se range au bon endroit dans l'OS, pour que la suite (relance,
offre, facture) parte d'un dossier juste.

**Charger d'abord les socles** : `ecrire-comme-manu` pour la voix,
`deposer-un-brouillon-email` pour la plomberie du brouillon, et `consigner-un-contact`
pour l'entrée au CRM.

Adresse : **vous** — un premier contact n'est pas un client établi, même chaleureux.

## La séquence

### 1. Situer

`contexte { q: "<nom>" }` et `recall` : la personne existe peut-être déjà. Puis
`mail_search` pour retrouver le fil complet — dans les dossiers métier,
`1-Business/Prospects` en tête, jamais seulement INBOX (voir
`deposer-un-brouillon-email`).

### 2. Enquêter

Ce que la personne dit d'elle-même dans son message, son site, son profil public.
L'objectif est double : personnaliser la réponse, et nourrir le CRM — en ne retenant que
ce que la source établit.

### 3. Consigner au CRM

Dérouler `consigner-un-contact` : la personne, son organisation si elle compte,
l'affiliation avec son rôle, une fiche courte. Zéro doublon, rien d'inventé — les règles
vivent là-bas.

### 4. Le deal — seulement s'il y a un objet à vendre

Une demande concrète (accompagnement, formation, mandat) → `deal_create { name, partieId }`,
nommé par la contrepartie et l'objet (`Marie Dupont — Coaching IA individuel`), étape
`piste` ou `qualifie` selon la précision de la demande, `offreId` si le catalogue correspond.

Une prise de contact sympathique **sans objet** n'est pas un deal : la partie reste en
réseau, avec sa note et, au besoin, une tâche de relance. Un deal à montant nul qui dort est
le symptôme de cette faute.

### 5. La note au carnet

`carnet_create` : ce que la personne a demandé, dans ses termes, avec la date. Rattachement
**au plus fin** : le deal s'il existe, sinon la partie ; les présents en `interlocuteurs`.

### 6. Le brouillon de réponse

Le brouillon se dépose selon `deposer-un-brouillon-email` : la notification du formulaire
(`hello@avqn.ch`) annonce le lead sans venir de lui, la réponse se construit sur le message
de la personne, ou par `mail_draft` s'il n'y en a pas. **Toujours un brouillon, jamais un
envoi** ; Manu relit et envoie. La réponse :

- ouvre sur **ce que la personne a dit**, pas sur AVQN ;
- propose **une seule prochaine étape**, la plus simple : un appel court, avec des créneaux
  tirés du calendrier réel (`cal_event_list` sur tous les calendriers) et l'amplitude
  (« mes journées vont de 8h à 19h ») ;
- ne vend rien, ne chiffre rien : le prix vient après l'échange de vive voix
  (`emettre-une-offre` prend le relais à ce moment-là) ;
- reste courte, un ou deux emojis sobres au maximum.

### 7. Programmer la suite

Une tâche rattachée au deal (ou à la partie) : `waitingOn` tant qu'on attend sa réponse.
Si elle ne répond pas, c'est `relancer-un-prospect` qui prend le relais. Le rendez-vous
obtenu se pose à l'agenda, se prépare avec `preparer-un-rendez-vous` et se consigne avec
`debriefer-un-rendez-vous`.

## Checklist avant de rendre la main

- [ ] La checklist de `consigner-un-contact` est passée : zéro doublon, rien d'inventé
- [ ] Le deal n'existe que s'il y a un objet à vendre, nommé par contrepartie et objet
- [ ] L'échange du jour est au carnet, rattaché au plus fin, avec ses présents
- [ ] La réponse est un brouillon, en vous, une seule étape proposée, créneaux réels
- [ ] Brouillon relu après dépôt : le champ `to` porte la personne, pas une adresse de notification
- [ ] Checklist anti-tics du socle `ecrire-comme-manu` passée
- [ ] Une tâche porte la suite (attente ou relance datée)

## Boucle d'amélioration

Quand Manu corrige une réponse ou un rangement, chercher la règle qui aurait évité la
correction et l'ajouter au bon endroit : ici pour l'accueil, `consigner-un-contact` pour
le CRM, `ecrire-comme-manu` pour la voix.
