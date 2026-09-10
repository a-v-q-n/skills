---
name: deposer-un-brouillon-email
description: >-
  À utiliser dès qu'un brouillon d'email doit être déposé au nom de Manu, à n'importe quel
  moment du cycle client : trouver le fil réel dans la bonne boîte (le courrier entrant est
  classé hors INBOX), répondre au message de l'interlocuteur pour que le destinataire soit
  le bon, piloter les copies, et relire le brouillon déposé avant de rendre la main. Le
  courrier vit sur le connecteur `comms`, qui porte plusieurs boîtes. Socle chargé par les
  recettes qui écrivent un email — accueillir-une-prise-de-contact, emettre-une-offre,
  envoyer-une-facture, relancer-un-prospect, relancer-une-facture,
  ecrire-un-email-de-prospection. NE COUVRE PAS la voix (ecrire-comme-manu) ni ce que l'email
  doit dire, qui vit dans la recette du moment.
couche: socle
moment: >-
  La plomberie du brouillon : trouver le fil hors INBOX, répondre au bon message, contrôler
  destinataires et copies.
famille: cycle-client
---

# Déposer un brouillon d'email

Un brouillon impeccable adressé à soi-même est un brouillon raté. La plomberie de l'envoi
est invisible tant qu'elle marche, et silencieuse quand elle casse : `mail_draft_reply`
répond à l'expéditeur du message source, donc répondre à un message de `Sent` met Manu en
destinataire de son propre courrier.

Ce socle porte les gestes qui l'évitent : savoir dans quelle boîte on est, trouver le fil,
répondre au bon message, piloter les copies, vérifier le brouillon déposé.

## 0. Le courrier vit sur `comms`

Les tools `mail_*` sont ceux du connecteur **`comms`** (comms.avqn.ch), pas ceux de l'OS.
L'OS tient la relation, l'argent et le travail ; `comms` tient les boîtes.

`comptes_list` donne l'inventaire réel. Deux boîtes aujourd'hui :

| Clé | Adresse | Ce qu'elle est |
| :--- | :--- | :--- |
| `manu` | `manu@avqn.ch` | La boîte de Manu, celle par défaut. Porte aussi ses agendas. |
| `sys` | `sys@avqn.ch` (alias `job@avqn.ch`) | La boîte des machines : notifications, formulaires. |

Un email au nom de Manu part de `manu`. `mail_draft` **exige** `compte` — le serveur ne
choisit jamais la boîte d'où part un message.

Chaque résultat de `mail_search` porte une **`ref`** de la forme `compte/dossier/validité:uid`.
Elle désigne le message ET sa boîte : c'est elle qu'on repasse à `mail_read` et à
`mail_draft_reply`, jamais un couple dossier/uid reconstruit à la main.

## 1. Le courrier entrant ne vit pas dans INBOX

La boîte `manu` est triée automatiquement. INBOX est presque toujours vide : les messages
arrivés sont classés dans des dossiers métier.

| Où chercher | Ce qu'on y trouve |
| :--- | :--- |
| `1-Business/Prospects` | Les messages des prospects et les notifications du formulaire avqn.ch |
| `1-Business/Clients` | Les messages des clients en mandat |
| `5-Reseau`, `3-Fournisseurs`, `6-Sollicitations` | Le reste, par nature de relation |
| `4-Systemes/*` | Ce que les machines envoient (briefs, ops, contenu) |
| `Archive` | Ce qui a été archivé à la main |
| `Sent` | Les envois de Manu — **jamais** une source de réponse |

`mail_folders` donne la liste réelle et à jour. `mail_search` cherche dans **un** dossier à la
fois (défaut INBOX) mais accepte `compte: "*"` pour balayer toutes les boîtes : chercher par
`de:` sur l'adresse de l'interlocuteur, dossier par dossier, reste le geste le plus sûr.

**Une recherche vide ne prouve rien.** Elle dit qu'on a cherché au mauvais endroit bien plus
souvent qu'elle ne dit que le message n'existe pas.

## 2. Les adresses viennent de l'OS

Le carnet d'adresses vit dans l'OS. `contexte {q: "<nom>"}` rend la fiche de la partie **et
l'adresse de chacun de ses affiliés** : c'est la matière du `de:` qu'on donne à `mail_search`.

Chercher sur la seule adresse générique d'une organisation (`info@…`) manque tout l'échange
réel, qui passe par les personnes. Prendre les adresses des affiliés, pas seulement celle de
la fiche.

## 3. Répondre au message de l'interlocuteur

`mail_draft_reply { ref, corps }` construit la réponse à partir du message source : le
destinataire est **l'expéditeur de ce message**, et le brouillon se dépose dans la boîte que
la `ref` désigne. Le message source doit donc venir de la personne à qui l'on écrit.

Avant d'appeler le tool, vérifier le `from` du message retenu (`mail_read`). S'il porte
`manu@avqn.ch`, c'est un envoi : ce n'est pas la source, il faut remonter au message auquel
il répondait.

Attention aussi aux notifications du formulaire de contact (`hello@avqn.ch`, `sys@avqn.ch`,
`job@avqn.ch`) : elles annoncent un lead sans être de lui. Y répondre écrit à la machine.

## 4. Les copies se reprennent seules

**`mail_draft_reply` reprend les `Cc` du message source**, moins les adresses de la boîte qui
répond (pas d'auto-copie) et moins les doublons avec le `to`. C'est le défaut, sans paramètre
à passer : un fil à quatre reste un fil à quatre. Rien à recopier à la main.

Les autres destinataires du `To:` source, en revanche, ne sont pas reconduits — à ajouter par
`cc_ajout` quand on veut un vrai « répondre à tous ».

Trois leviers quand ce défaut ne convient pas :

| Paramètre | Effet |
| :--- | :--- |
| `cc` | Remplace la liste des copies. `cc: ""` dépose le brouillon sans copie. |
| `cc_ajout` | Ajoute ces adresses à celles reprises du fil |
| `cc_retrait` | Retire ces adresses de celles reprises du fil |

`cc` et le couple `cc_ajout`/`cc_retrait` s'excluent : les passer ensemble lève une erreur.

`bcc` existe sur les trois tools d'écriture et n'est jamais repris d'un fil. `mail_draft_forward`
prend `cc` et `bcc` mais ne reprend rien : un transfert choisit ses destinataires.

Les trois tools **rendent `to`, `cc` et `bcc` tels qu'ils sont posés sur le brouillon** : leur
retour suffit à savoir à qui il s'adresse.

## 5. Quand l'interlocuteur n'a jamais écrit

Un prospect qui n'a jamais répondu ne laisse aucun message source. Le geste est alors
`mail_draft { compte: "manu", to, sujet, corps }` avec l'adresse en clair, en reprenant le
sujet du fil précédé de `Re:` pour que la conversation reste lisible chez lui.

C'est le seul cas où un message neuf remplace une réponse. Partout ailleurs, la réponse dans
le fil l'emporte : elle porte l'historique.

## 6. Relire le brouillon déposé

Le retour du tool porte les destinataires réellement posés : les lire suffit à contrôler à qui
le brouillon part. Ce qu'il ne dit pas, c'est le corps et les pièces — donc après le dépôt,
`mail_search { compte: "manu", dossier: "Drafts" }` puis `mail_read` sur sa `ref`, et
contrôler :

- le champ `to` — c'est bien la personne visée, pas Manu, pas une adresse de notification ;
- la pièce jointe attendue est là, sous le bon nom ;
- le corps est celui qu'on croit avoir écrit.

Ce contrôle fait partie du geste : sans lui, le skill n'a pas fini. Il ne sert plus, en
revanche, à rattraper une perte de destinataires — le serveur ne la produit plus.

## Checklist avant de rendre la main

- [ ] Les adresses viennent du dossier `contexte`, affiliés compris — pas de la seule fiche
- [ ] Le fil a été cherché dans les dossiers métier, pas seulement dans INBOX
- [ ] Le message source vient de l'interlocuteur, jamais de `Sent` ni d'une notification
- [ ] Aucun message entrant dans le fil → `mail_draft` avec `compte` et destinataire explicites
- [ ] Les copies rendues sont celles voulues — ajustées par `cc_ajout`/`cc_retrait` si besoin
- [ ] Le brouillon déposé a été relu : `to` juste, pièce jointe présente, corps conforme
- [ ] C'est un brouillon, jamais un envoi : Manu relit et envoie lui-même
