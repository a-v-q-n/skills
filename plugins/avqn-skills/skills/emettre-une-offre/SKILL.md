---
name: emettre-une-offre
description: >-
  À utiliser dès qu'il faut transformer un accord de vive voix en proposition commerciale
  écrite : rédiger le devis d'un deal, le faire valider par Manu, générer son PDF et
  préparer l'email qui l'accompagne. Porte la méthode : matière tirée du CRM, structure en
  trois blocs (situation, proposition, ce que vous recevez), validation interactive du
  texte AVANT toute génération, échéancier, PDF en pièce jointe, email court en réponse
  dans le fil. Charge d'abord le socle ecrire-comme-manu pour la voix. NE COUVRE PAS la
  prise de contact en amont (accueillir-une-prise-de-contact), la relance d'une offre sans
  réponse (relancer-un-prospect) ni la facturation en aval (envoyer-une-facture).
---

# Émettre une offre

Une proposition AVQN n'est pas un catalogue de prestations, c'est la preuve écrite qu'on a écouté. Le client doit se reconnaître dans le premier paragraphe avant même de lire le prix. Tout le reste en découle : la matière vient de ce qu'il a dit, pas de ce qu'on vend.

**Charger d'abord le skill `ecrire-comme-manu`** : il porte la voix, les règles non négociables et la checklist anti-tics. Ce skill-ci n'ajoute que la méthode de l'offre.

Adresse : **vous**, du devis comme de l'email. Un prospect qui n'a pas encore signé n'est pas un client établi.

## Le prérequis

Une offre écrite ne précède jamais l'accord, elle le formalise. Avant d'ouvrir ce skill, il faut :

- un **deal** existant dans l'OS, avec sa partie ;
- un **échange de vive voix** déjà eu (appel, rendez-vous), consigné au carnet ;
- un **accord de principe sur le prix et le format**.

Si l'un des trois manque, le dire à Manu plutôt que d'écrire. Une proposition envoyée avant l'accord se négocie ; une proposition envoyée après l'accord se signe.

## La séquence

L'ordre compte, et il est **strict** : le texte se valide en conversation avant que quoi que ce soit ne soit généré. Un PDF rendu trop tôt donne l'illusion du travail fini et fait passer les corrections pour des retouches.

### 1. Rassembler la matière

`contexte {q}` sur le deal, et lire la note de carnet de l'appel. Le prix, le format, le lieu, les dates visées, les contraintes du client : tout est là. Si un élément manque, le demander à Manu. **Ne jamais combler un trou par une supposition** : c'est exactement ce que le client repérera.

### 2. Rédiger le texte et le faire valider

Écrire les trois blocs (voir « Anatomie » ci-dessous) et les **présenter en conversation**, en markdown lisible. Puis itérer avec Manu jusqu'à ce qu'il valide explicitement.

Pendant l'itération :
- appliquer ses corrections telles quelles, sans les réinterpréter ;
- signaler ce qu'une coupe fait perdre, une fois, puis se ranger à sa décision ;
- reproposer le texte **entier** après chaque tour, pas seulement le fragment modifié, pour qu'il relise d'un bloc.

Ne pas appeler `devis_create` à ce stade. Ne pas rendre de PDF. Ne pas préparer l'email.

### 3. Générer le devis et son PDF

Une fois le texte validé : `devis_create` (ou `devis_update` si un brouillon existe déjà sur ce deal), puis `devis_render_pdf`.

**Relire systématiquement le PDF produit** avant d'aller plus loin : le télécharger et en extraire le texte. C'est le document qui part chez le client, c'est lui qu'on vérifie, pas le JSON du tool.

### 4. Préparer l'email

`mail_draft_reply` dans le fil existant, PDF en pièce jointe. Toujours un brouillon, **jamais un envoi**. Manu relit et envoie lui-même.

### 5. Après l'envoi

Sur retour de Manu : `devis_update { sentOn }` quand c'est parti, `{ acceptedOn }` à l'accord du client, puis `deal_win { devisId }` pour créer le projet et ses tranches. La facture d'acompte se prépare avec `envoyer-une-facture` ; une offre restée sans réponse se traite avec `relancer-un-prospect`.

## Anatomie de l'offre

Le PDF tient en **deux pages** : le rendu échoue si le contenu déborde. Viser environ **1'400 signes** au total pour les trois blocs. Écrire court dès le départ coûte moins cher que de dégraisser après trois échecs de rendu.

### LA SITUATION

Deux paragraphes courts. Ce que le client a dit, rendu dans ses termes : les faits datés, l'échéance qui commande, ce dont il dispose déjà, la contrainte qui complique.

- Aucune promesse, aucun argument de vente. Ce bloc ne vend rien, il prouve l'écoute.
- Aucune supposition. Si un point n'est pas confirmé, l'écrire tel quel (« a priori », « sous réserve de »).
- **Ne pas conclure par une phrase de transition** vers l'offre. Le passage se fait tout seul, une bascule rhétorique alourdit.

### LA PROPOSITION

**Un paragraphe d'ouverture au niveau du résultat**, avant tout détail : ce que la personne achète, ce qu'elle emporte, à quoi ça lui sert au-delà de l'échéance immédiate. Trois phrases suffisent. C'est le paragraphe qui justifie le prix, et c'est celui qu'on oublie d'écrire en allant droit au concret.

Puis, dans l'ordre :

1. **Le cadre** en une phrase : nombre et durée des séances, format, lieu, rythme.
2. **Les séances**, une par bloc, titrées (`**Séance 1.**`) et suivies de leur contenu en une ou deux phrases nominales.
3. **Les modalités** en une ligne : ce qui se passe entre les séances.

Vendre le résultat, jamais les heures. Le nombre de séances décrit un cadre de travail, il ne sert pas de justification tarifaire.

### CE QUE VOUS RECEVEZ

Trois à cinq puces. Chacune est un **actif que la personne emporte**, pas une activité qu'on mène. « Vos outils sur mesure, construits sur vos propres cas » plutôt que « Construction d'outils ».

La dernière puce dit ce qui survit à la prestation : l'autonomie, l'évolutivité, ce qui sert après.

## Le montant et l'échéancier

- Le montant est **celui qui a été accordé de vive voix**. Le devis formalise, il ne renégocie pas. Aucune remise ne s'invente au moment de la rédaction.
- Défaut pour un accompagnement court : **50 % d'acompte à la signature, 50 % de solde après la dernière séance**. Les lignes somment exactement au montant, sinon le tool refuse.
- Les échéances sont indicatives : acompte à la date de la première séance visée, solde peu après la dernière.
- `validUntil` : la veille du démarrage visé, ou trente jours si aucune date n'est posée. Une validité courte est cohérente quand le client a une échéance proche, elle ne sert pas à mettre la pression.

## L'email d'accompagnement

**Cent cinquante mots maximum**, hors liste de créneaux. L'offre est dans le PDF ; l'email ne fait que l'apporter et demander la seule chose qui reste à décider.

Règles :

- **En réponse dans le fil existant** (`mail_draft_reply`), jamais un message neuf. Le fil porte l'historique.
- **PDF en pièce jointe**, jamais un lien. Nommer le fichier `AAAA-MM-JJ-prenom-nom-slug-offre.pdf`.
- **Zéro doublon avec l'offre.** Ne pas répéter le prix, ni les séances, ni l'échéancier.
- **Une seule action attendue.** Ne pas glisser de demande annexe (un document à fournir, une information à vérifier) dans le mail qui porte l'offre. Ça dilue la décision. Ces demandes attendent le mail suivant.
- **Les créneaux viennent du calendrier réel** : `cal_event_list` sur tous les calendriers, y compris le personnel. Proposer des demi-journées, préciser l'amplitude horaire (« mes journées vont de 8h à 19h ») plutôt que de promettre de réserver.
- Deux emojis sobres au maximum, en fin de phrase.

Structure :

1. Une ligne de remerciement pour l'échange.
2. La pièce jointe, et la prochaine étape concrète (« si elle vous convient je vous envoie la facture avec le QR code »).
3. Les créneaux, en deux groupes : la première séance, puis les suivantes.
4. Une clôture chaleureuse, ancrée dans ce que la personne vit (vacances, échéance, saison).

## Checklist avant de rendre le PDF

- [ ] Le texte a été validé explicitement par Manu en conversation
- [ ] La situation ne contient que des faits venant du client
- [ ] La proposition ouvre sur le résultat avant le détail des séances
- [ ] Chaque livrable est un actif emporté, pas une activité
- [ ] Le montant correspond à l'accord verbal, l'échéancier somme juste
- [ ] Checklist anti-tics du socle `ecrire-comme-manu` passée (zéro tiret cadratin, zéro « , et »)
- [ ] Le PDF rendu a été relu, il tient en deux pages

## Références

`references/exemples.md` contient un exemple complet et générique (offre plus email) à imiter pour le ton et le découpage.
