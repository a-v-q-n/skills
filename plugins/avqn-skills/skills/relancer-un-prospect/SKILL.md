---
name: relancer-un-prospect
description: >-
  À utiliser dès qu'un prospect reste silencieux après un échange, une offre envoyée ou un
  accord de principe : décider si et quand relancer, écrire le brouillon de relance dans le
  fil, consigner la relance et programmer la suivante. Porte le jugement du timing et du
  ton, et la sortie propre quand l'affaire s'éteint. Charge d'abord le socle
  ecrire-comme-manu pour la voix. NE COUVRE PAS la première réponse à une prise de contact
  (accueillir-une-prise-de-contact), la proposition elle-même (emettre-une-offre), la
  relance d'une facture impayée (relancer-une-facture) ni la prospection à froid, qui a
  ses propres relances (ecrire-un-email-de-prospection).
couche: recette
moment: >-
  Le prospect reste silencieux : timing, ton, relance dans le fil, sortie propre.
famille: cycle-client
---

# Relancer un prospect

Une bonne relance apporte quelque chose ; une mauvaise réclame une réponse. Le silence d'un
prospect n'est presque jamais un refus : c'est une priorité qui a glissé. La relance remet
l'affaire en haut de sa pile sans mettre de pression, et chaque relance laisse une trace
pour que la suivante — ou la sortie — se décide sur des faits.

**Charger d'abord les socles** : `ecrire-comme-manu` pour la voix, et
`deposer-un-brouillon-email` pour la plomberie du brouillon (où vit le fil, à quel message
répondre, comment contrôler le destinataire).

Ce skill relance un deal qui vit dans l'OS. Un prospect froid contacté en prospection,
sans deal ouvert, se relance avec `ecrire-un-email-de-prospection`.

Adresse : celle de la relation existante (vous pour un prospect, tu si le lien est déjà
proche) — relire le fil pour la retrouver, jamais la deviner.

## Avant d'écrire : relire le dossier

`contexte` sur le deal : les notes de carnet, le devis et ses dates (`sentOn`,
`validUntil`), les derniers mails du fil. La relance se construit sur ce qui s'est
réellement passé. Si aucune trace n'explique le silence, c'est la relance qui le dira.

## Le timing

- **Offre envoyée** : relancer à mi-chemin de la validité, jamais le lendemain. La
  `validUntil` donne un motif honnête de relance (« l'offre court jusqu'au… ») sans servir
  de menace.
- **Échange sans suite** : une à deux semaines, selon l'urgence que le prospect avait
  lui-même posée.
- **Une seule relance par silence.** Relancer deux fois sans réponse intermédiaire, c'est
  insister ; la deuxième vague attend un vrai délai.

## Le ton

- La relance **apporte** : une information utile, un créneau concret, une réponse à une
  question restée ouverte. Jamais un « je me permets de revenir vers vous » qui ne contient
  que la demande.
- Courte : trois à cinq phrases. Le fil porte déjà tout le contexte.
- Zéro reproche, zéro pression, zéro fausse urgence. Le prospect a le droit d'avoir autre
  chose à faire.
- Une seule question, celle qui débloque.

## La séquence

1. **Écrire le brouillon** dans le fil existant, en suivant `deposer-un-brouillon-email` :
   le message source vient du prospect, jamais de `Sent`. Un prospect qui n'a jamais
   répondu n'a pas de fil : c'est alors `mail_draft` avec son adresse en clair. Toujours un
   brouillon, Manu relit et envoie.
2. **Consigner** : `carnet_create` rattachée au deal (« relance envoyée, motif, ce qu'on
   attend »).
3. **Ajuster le deal** : la probabilité descend quand les relances s'accumulent sans
   réponse — l'étape et la probabilité ne se contredisent jamais, et le pourquoi se note
   dans la fiche du deal, daté.
4. **Programmer la suite** : `task_create { scheduledFor }` rattachée au deal, à la date de
   la prochaine décision (relancer encore, ou clore).

## Sortir proprement

Après deux ou trois relances sans réponse, on arrête de relancer et on ferme la boucle :

- un dernier message court qui **rend la main** (« je ne vous relance plus là-dessus, ma
  porte reste ouverte ») — sans amertume, la relation survit à l'affaire ;
- `deal_update { etape: "perdu", lostReason }` avec la raison réelle, même modeste
  (« sans suite après la proposition du JJ.MM ») ;
- la partie reste dans l'annuaire : un prospect perdu redevient du réseau, pas un fantôme.

## Checklist avant de rendre la main

- [ ] Le dossier a été relu (`contexte`) : la relance colle aux faits du fil
- [ ] Le timing respecte la règle (une relance par silence, vrai délai entre deux)
- [ ] La relance apporte quelque chose, une seule question, trois à cinq phrases
- [ ] C'est un brouillon dans le fil, adresse cohérente avec la relation
- [ ] Brouillon relu après dépôt : le champ `to` porte le prospect, pas Manu
- [ ] Checklist anti-tics du socle `ecrire-comme-manu` passée
- [ ] Note au carnet sur le deal, probabilité cohérente, tâche datée pour la suite

## Boucle d'amélioration

Quand Manu corrige une relance (ton, timing, sortie), chercher la règle qui aurait évité
la correction et l'ajouter ici ; une question de voix va dans `ecrire-comme-manu`.
