---
name: deposer-un-brouillon-email
description: >-
  À utiliser dès qu'un brouillon d'email doit être déposé au nom de Manu, à n'importe quel
  moment du cycle client : retrouver le fil réel dans la boîte (le courrier entrant est
  classé hors INBOX), répondre au message de l'interlocuteur pour que le destinataire soit
  le bon, et relire le brouillon déposé avant de rendre la main. Socle chargé par les
  recettes qui écrivent un email — accueillir-une-prise-de-contact, emettre-une-offre,
  envoyer-une-facture, relancer-un-prospect, relancer-une-facture. NE COUVRE PAS la voix
  (ecrire-comme-manu) ni ce que l'email doit dire, qui vit dans la recette du moment.
---

# Déposer un brouillon d'email

Un brouillon impeccable adressé à soi-même est un brouillon raté. La plomberie de l'envoi
est invisible tant qu'elle marche, et silencieuse quand elle casse : `mail_draft_reply`
répond à l'expéditeur du message source, donc répondre à un message de `Sent` met Manu en
destinataire de son propre courrier.

Ce socle porte les trois gestes qui l'évitent : trouver le fil, répondre au bon message,
vérifier le brouillon déposé.

## 1. Le courrier entrant ne vit pas dans INBOX

La boîte est triée automatiquement. INBOX est presque toujours vide : les messages
arrivés sont classés dans des dossiers métier.

| Où chercher | Ce qu'on y trouve |
| :--- | :--- |
| `1-Business/Prospects` | Les messages des prospects et les notifications du formulaire avqn.ch |
| `1-Business/Clients` | Les messages des clients en mandat |
| `5-Reseau`, `3-Fournisseurs`, `6-Sollicitations` | Le reste, par nature de relation |
| `Archive` | Ce qui a été archivé à la main |
| `Sent` | Les envois de Manu — **jamais** une source de réponse |

`mail_folders` donne la liste réelle et à jour ; `mail_search` ne cherche que dans **un**
dossier à la fois (défaut INBOX), il faut donc l'appeler dossier par dossier.

**Une recherche vide ne prouve rien.** Elle dit qu'on a cherché au mauvais endroit bien plus
souvent qu'elle ne dit que le message n'existe pas.

Même prudence avec la section `mails` de `contexte` : elle vient de l'index RAG et ne remonte
pas tout, notamment pas les dossiers métier. Elle sert à se repérer, pas à conclure qu'un fil
n'existe pas.

## 2. Répondre au message de l'interlocuteur

`mail_draft_reply { folder, uid }` construit la réponse à partir du message source : le
destinataire est **l'expéditeur de ce message**. Le message source doit donc venir de la
personne à qui l'on écrit.

Avant d'appeler le tool, vérifier le `from` du message retenu (`mail_read`). S'il porte
`manu@avqn.ch`, c'est un envoi : ce n'est pas la source, il faut remonter au message auquel
il répondait.

Attention aussi aux notifications du formulaire de contact (`hello@avqn.ch`, `sys@avqn.ch`) :
elles annoncent un lead sans être de lui. Y répondre écrit à la machine.

## 3. Quand l'interlocuteur n'a jamais écrit

Un prospect qui n'a jamais répondu ne laisse aucun message source. Le geste est alors
`mail_draft { to, subject, body }` avec l'adresse en clair, en reprenant le sujet du fil
précédé de `Re:` pour que la conversation reste lisible chez lui.

C'est le seul cas où un message neuf remplace une réponse. Partout ailleurs, la réponse dans
le fil l'emporte : elle porte l'historique.

## 4. Relire le brouillon déposé

Le tool rend `{ ok: true }` même quand le destinataire est mauvais. Après le dépôt,
`mail_search { folder: "Drafts" }` puis `mail_read` sur le brouillon, et contrôler :

- le champ `to` — c'est bien la personne visée, pas Manu, pas une adresse de notification ;
- la pièce jointe attendue est là, sous le bon nom ;
- le corps est celui qu'on croit avoir écrit.

Ce contrôle fait partie du geste : sans lui, le skill n'a pas fini.

## Checklist avant de rendre la main

- [ ] Le fil a été cherché dans les dossiers métier, pas seulement dans INBOX
- [ ] Le message source vient de l'interlocuteur, jamais de `Sent` ni d'une notification
- [ ] Aucun message entrant dans le fil → `mail_draft` avec le destinataire explicite
- [ ] Le brouillon déposé a été relu : `to` juste, pièce jointe présente, corps conforme
- [ ] C'est un brouillon, jamais un envoi : Manu relit et envoie lui-même
