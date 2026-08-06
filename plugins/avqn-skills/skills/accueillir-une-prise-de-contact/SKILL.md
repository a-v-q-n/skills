---
name: accueillir-une-prise-de-contact
description: >-
  À utiliser dès qu'une prise de contact arrive (email, formulaire, recommandation,
  message après une formation) : enquêter sur la personne, la consigner proprement dans
  le CRM avec son organisation, ouvrir un deal s'il y a un objet à vendre, consigner
  l'échange au carnet et préparer le brouillon de réponse dans la voix de Manu. Charge
  d'abord le socle ecrire-comme-manu pour la voix. NE COUVRE PAS la relance d'un prospect
  resté silencieux (relancer-un-prospect), la proposition écrite (emettre-une-offre) ni
  la mécanique des objets CRM, qui vit dans la grammaire du serveur.
---

# Accueillir une prise de contact

La première réponse fixe le niveau de la relation. Elle doit être rapide, personnelle et
sobre : montrer qu'on a lu, proposer la suite la plus simple, ne rien vendre encore. Tout ce
qui s'apprend au passage se range au bon endroit dans l'OS, pour que la suite (relance,
offre, facture) parte d'un dossier juste.

**Charger d'abord le skill `ecrire-comme-manu`** pour la voix, et appeler
`grammaire {domaine: "crm"}` avant la première écriture CRM de la session.

Adresse : **vous** — un premier contact n'est pas un client établi, même chaleureux.

## La séquence

### 1. Chercher avant de créer

`contexte { q: "<nom>" }` d'abord : la personne existe peut-être déjà (participant d'une
formation, réseau, ancien prospect). Puis `recall` sur son nom ou son organisation, et
`mail_search` pour retrouver le fil complet. **Ne jamais créer un doublon** : une ambiguïté
de `contexte` renvoie des candidats, les départager avant tout.

### 2. Enquêter

Ce que la personne dit d'elle-même dans son message, son site, son profil public. L'objectif
est double : personnaliser la réponse, et remplir le CRM juste.

**Ne consigner que ce que la source établit.** Un employeur supposé d'après un nom de
domaine, un rôle deviné, un téléphone plausible : ce sont des inventions. Un champ vide vaut
mieux qu'un champ plausible.

### 3. Consigner dans le CRM

- La **personne** : `partie_create { kind: "personne", firstName, lastName }`, coordonnées
  dans leurs champs structurés, jamais dans la fiche.
- Son **organisation**, seulement si elle est établie et si elle compte dans la relation :
  `partie_create { kind: "organisation" }` puis `affiliation_create` avec le `role` rempli.
  Ne jamais créer une organisation pour une personne qui se facture en son nom.
- La **fiche** de la personne reste courte : qui c'est, d'où vient le contact, comment
  travailler avec elle. Ce qui s'est dit ce jour-là va au carnet, pas dans la fiche.

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

`mail_draft_reply` dans le fil — **toujours un brouillon, jamais un envoi** ; Manu relit et
envoie. La réponse :

- ouvre sur **ce que la personne a dit**, pas sur AVQN ;
- propose **une seule prochaine étape**, la plus simple : un appel court, avec des créneaux
  tirés du calendrier réel (`cal_event_list` sur tous les calendriers) et l'amplitude
  (« mes journées vont de 8h à 19h ») ;
- ne vend rien, ne chiffre rien : le prix vient après l'échange de vive voix
  (`emettre-une-offre` prend le relais à ce moment-là) ;
- reste courte, un ou deux emojis sobres au maximum.

### 7. Programmer la suite

Une tâche rattachée au deal (ou à la partie) : `waitingOn` tant qu'on attend sa réponse.
Si elle ne répond pas, c'est `relancer-un-prospect` qui prend le relais.

## Checklist avant de rendre la main

- [ ] `contexte` a été consulté avant toute création — zéro doublon
- [ ] Rien d'inventé dans le CRM : chaque champ rempli a sa source
- [ ] Le deal n'existe que s'il y a un objet à vendre, nommé par contrepartie et objet
- [ ] L'échange du jour est au carnet, rattaché au plus fin, avec ses présents
- [ ] La réponse est un brouillon, en vous, une seule étape proposée, créneaux réels
- [ ] Checklist anti-tics du socle `ecrire-comme-manu` passée
- [ ] Une tâche porte la suite (attente ou relance datée)
