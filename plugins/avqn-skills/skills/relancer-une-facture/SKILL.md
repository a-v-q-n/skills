---
name: relancer-une-facture
description: >-
  À utiliser dès qu'une facture émise reste impayée à son échéance : vérifier qu'aucun
  paiement n'est réellement arrivé, choisir le palier (rappel amical, second rappel ferme,
  mise en demeure), écrire le brouillon adapté dans la voix de Manu, consigner la relance
  et programmer la suivante. Charge d'abord le socle ecrire-comme-manu. NE COUVRE PAS
  l'envoi initial de la facture (envoyer-une-facture), l'enregistrement d'un paiement
  arrivé (paiement_record, grammaire facturation) ni la relance commerciale d'un prospect
  (relancer-un-prospect).
---

# Relancer une facture

La règle d'or : **on ne relance jamais une facture payée.** La deuxième : le ton monte par
paliers, et chaque palier laisse au client une sortie honorable. Un impayé est presque
toujours un oubli ; le traiter comme tel jusqu'à preuve du contraire préserve la relation,
qui vaut plus que le délai.

**Charger d'abord le skill `ecrire-comme-manu`** pour la voix.

Adresse : celle de la relation (le tu d'un client établi, en général). Le palier change le
fond, jamais la politesse.

## Avant tout : vérifier que l'argent n'est pas arrivé

1. `invoice_get` — la pièce est bien émise, non soldée, échéance dépassée.
2. `paiement_list` sur la pièce — aucun encaissement enregistré.
3. Le relevé bancaire — un virement peut être arrivé sans avoir été rapproché :
   `rapprochement_suggest`, et au besoin les dernières transactions (`banque_tx_list`).
   S'il est là, le geste est `paiement_record`, pas une relance.

Ce contrôle se refait **à chaque palier**. Une relance partie après le paiement coûte plus
cher que dix jours de retard.

## Les paliers

- **Rappel amical** — vers dix jours après l'échéance. Le bénéfice du doute, assumé :
  la facture « a peut-être glissé », on la rejoint pour simplifier, tout va bien. Deux ou
  trois phrases, chaleureuses.
- **Second rappel, ferme et courtois** — vers trente jours, ou deux à trois semaines après
  le premier. Les faits, posés sans reproche : numéro, montant, échéance dépassée, un
  nouveau délai court et précis. On propose la sortie (« si quelque chose bloque, dis-le
  moi ») : un client en difficulté qui parle vaut mieux qu'un silence.
- **Mise en demeure** — après le second rappel resté sans effet. Un délai ferme (dix
  jours), la mention des suites (intérêts moratoires, poursuite). **Ce palier ne s'écrit
  qu'avec l'accord explicite de Manu, demandé avant même le brouillon** : c'est un acte qui
  engage la relation, pas une routine.

Entre deux paliers, un vrai délai. Deux relances rapprochées disent la panique, pas le
sérieux.

## La séquence

1. **Choisir le palier** d'après l'historique : `contexte` sur le projet, les relances déjà
   consignées au carnet, les mails du fil.
2. **Écrire le brouillon** : `mail_draft_reply` dans le fil d'envoi de la facture —
   toujours un brouillon, Manu relit et envoie. Le PDF de la facture est joint à nouveau :
   le client ne doit pas la chercher.
3. **Consigner** : `carnet_create` rattachée au projet (palier, date, délai posé).
4. **Programmer la suite** : `task_create { scheduledFor }` rattachée au projet, à la date
   du prochain contrôle — revérifier le paiement, puis palier suivant s'il le faut.

## Le ton, quel que soit le palier

- Les faits, jamais les interprétations : « la facture est échue depuis le… », pas « vous
  ne m'avez pas payé ».
- Aucune excuse de relancer : réclamer son dû est normal, le ton n'a pas à s'en excuser.
- Court. La facture jointe porte les détails.
- Une seule demande : le paiement (ou un signe de vie sur ce qui bloque).

## Checklist avant de rendre la main

- [ ] Paiement vérifié (pièce, encaissements, banque) : la facture est réellement impayée
- [ ] Le palier découle de l'historique consigné, avec un vrai délai depuis le précédent
- [ ] Mise en demeure : accord explicite de Manu obtenu avant le brouillon
- [ ] C'est un brouillon dans le fil, PDF de la facture joint, une seule demande
- [ ] Checklist anti-tics du socle `ecrire-comme-manu` passée
- [ ] Relance au carnet (projet), tâche datée pour le prochain contrôle
