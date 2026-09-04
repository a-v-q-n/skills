---
name: consigner-un-contact
description: >-
  À utiliser dès qu'une personne ou une organisation doit entrer au CRM ou y être mise à
  jour, que la demande arrive seule (« ajoute cette personne au CRM », « note ses
  coordonnées ») ou au fil d'une recette : chercher avant de créer, n'écrire que ce que la
  source établit, créer la personne avec ses coordonnées structurées, son organisation
  quand elle compte, l'affiliation avec son rôle, et une fiche courte. Socle chargé par
  accueillir-une-prise-de-contact et debriefer-un-rendez-vous. NE COUVRE PAS le deal (il
  se juge dans la recette du moment), la note au carnet ni le brouillon de réponse.
couche: socle
moment: >-
  L'entrée au CRM : chercher avant de créer, coordonnées structurées, organisation, affiliation,
  fiche courte.
famille: cycle-client
---

# Consigner un contact

Un CRM juste vaut par ce qu'il ne contient pas : pas de doublon, pas de champ deviné, pas
d'organisation fantôme. Ce skill porte le geste d'entrée d'une personne (et de son
organisation quand elle compte) dans l'annuaire, et rien d'autre : le deal, la note, la
réponse vivent dans la recette qui l'a appelé.

## 1. Chercher avant de créer

`contexte { q: "<nom>" }` d'abord : la personne existe peut-être déjà (participant d'une
formation, réseau, ancien prospect). Puis `recall` sur son nom ou son organisation.
**Ne jamais créer un doublon** : une ambiguïté de `contexte` renvoie des candidats, les
départager avant tout. Si la personne existe, le geste est une mise à jour, pas une
création.

## 2. N'écrire que ce que la source établit

Un employeur supposé d'après un nom de domaine, un rôle deviné, un téléphone plausible :
ce sont des inventions. **Un champ vide vaut mieux qu'un champ plausible.** Une fiche
fausse est pire qu'une fiche absente : elle sera lue comme vraie.

## 3. La personne

`partie_create { kind: "personne", firstName, lastName }`. Les coordonnées (email,
téléphone, site, adresse) vont dans leurs champs structurés, jamais dans la fiche.

## 4. L'organisation, seulement si elle compte

`partie_create { kind: "organisation" }` puis `affiliation_create` avec le `role` rempli,
seulement si l'organisation est établie ET compte dans la relation.

- **Ne jamais créer une organisation pour une personne qui se facture en son nom** : une
  personne physique est facturable telle quelle, et le nom commercial d'un indépendant est
  une information de sa fiche, pas une entité.
- **Un départ se clôt** (`affiliation_update { endedOn }`), il ne s'efface pas.

## 5. La fiche, courte

La fiche de la personne dit ce qu'elle **est** : qui c'est, d'où vient le contact, comment
travailler avec elle. Ce qui s'est dit un jour donné a une date : il va au carnet, pas
dans la fiche. Pour ajouter sans réécrire, `fiche_append`.

## Les rôles se dérivent

`client`, `prospect`, `réseau` se dérivent de l'activité (un deal, une facture) et ne se
saisissent jamais. Ne jamais chercher à « marquer quelqu'un comme client » : son activité
le dit.

## Checklist avant de rendre la main

- [ ] `contexte` a été consulté avant toute création — zéro doublon
- [ ] Chaque champ rempli a sa source ; rien de déduit, rien de plausible
- [ ] Les coordonnées sont dans leurs champs structurés, pas dans la fiche
- [ ] L'organisation n'existe que si elle est établie et significative, affiliation avec rôle
- [ ] La fiche est courte et dit ce que la personne est ; l'événementiel est au carnet

## Boucle d'amélioration

Quand Manu corrige une entrée CRM (un rattachement, un champ, une fiche trop bavarde),
chercher la règle qui aurait évité la correction et l'ajouter ici avec l'exemple.
