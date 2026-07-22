---
name: tenir-le-crm
description: >-
  À utiliser dès qu'on touche à une relation d'affaires d'AVQN : ajouter ou retrouver quelqu'un
  dans l'annuaire, rattacher une personne à une organisation, ouvrir ou faire avancer un deal,
  noter un échange, savoir qui est client. Orchestre le domaine CRM d'AVQN OS — parties
  (personne|organisation), affiliations datées, deals à étapes et leurs interlocuteurs, catalogue
  d'offres. Charge d'abord le socle piloter-avqn-os. NE COUVRE PAS la facturation
  (creer-une-facture), le carnet lui-même (tenir-le-carnet) ni le temps passé (suivre-le-temps).
---

# Tenir le CRM

Commencer par charger **`piloter-avqn-os`** : la grammaire des parties et des rôles dérivés y est
posée, ce skill ne la répète pas.

## Avant d'écrire, chercher

`avqn-os:contexte { q: "<nom>" }` rend le dossier complet et évite de créer un doublon. Une
ambiguïté renvoie des candidats : relancer avec `kind` + `id`.

## L'annuaire

- **`avqn-os:partie_list`** — filtres `kind` (`personne` | `organisation`), `role`
  (`client` | `prospect` | `reseau`), `includeArchived`.
- **`avqn-os:partie_get`** — le dossier **avec** ses rôles dérivés, ses affiliations (ou ses
  membres si c'est une organisation) et ses deals.
- **`avqn-os:partie_create`** — `kind` obligatoire. Pour une **personne** : `firstName` /
  `lastName` (le nom affiché se dérive). Pour une **organisation** : `displayName`.
- **`avqn-os:partie_update`** — `archived: true` masque une relation éteinte sans rien perdre.
  Le type ne se change pas : une personne devenue société est une autre entité.
- **`avqn-os:partie_delete`** — destructif, `confirm` requis. **Refusé** si la partie porte des
  deals. Préférer l'archivage, toujours.

**Ne jamais créer une organisation pour pouvoir facturer quelqu'un.** Une personne physique se
facture directement.

### La fiche d'une partie

`fiche` (markdown) porte **ce que cette partie est** : son métier, ses implantations, ses gens, ce
qu'on a compris d'elle. Une seule par partie, et elle doit rester juste — on la corrige quand le
monde change, on ne l'empile pas. Ce qui s'est *passé* (un appel, une proposition) va au carnet,
daté (`tenir-le-carnet`).

Pour compléter une fiche longue sans la relire ni risquer d'écraser ce que Manu vient d'y écrire :
**`avqn-os:fiche_append { kind: "partie", targetId, texte }`**.

Le deal porte sa fiche au même titre : ce dont l'affaire parle, les conditions négociées.

### AVQN elle-même

AVQN est une partie de l'annuaire, marquée `soi` — elle n'apparaît pas dans les listes ni dans la
dérivation des rôles. Sa fiche porte le positionnement, les valeurs, ce que Manu refuse. Les
données administratives structurées (dénomination, adresse, IBAN, mention TVA) vivent dans le
**profil émetteur** de facture (`invoice_issuer_get`), qui en est la source unique : la fiche ne
les répète pas.

## Les affiliations

`avqn-os:affiliation_create { personneId, organisationId, role }` rattache. Une personne peut
appartenir à plusieurs organisations.

**Un départ se clôt, il ne s'efface pas** : `avqn-os:affiliation_update { id, endedOn }`.
`affiliation_delete` est réservé aux erreurs de saisie.

Ne rattacher que ce que la donnée établit. Un employeur supposé d'après un nom de domaine n'est
pas un fait — laisser sans affiliation vaut mieux qu'un rattachement inventé.

## Les deals

- **`avqn-os:deal_create { name, partieId }`** — la partie est **obligatoire**.
- **`avqn-os:deal_update`** — étape, montant, probabilité, partie, raison de perte, `offreId`.
- **`avqn-os:deal_win { id, projectName? }`** — **le seul chemin vers `gagne`**. Passe l'étape
  ET crée le projet rattaché. `deal_update` refuse `gagne`.
- **`avqn-os:deal_participant_add { dealId, personneId, role }`** — plusieurs interlocuteurs par
  deal (`decideur`, `prescripteur`, `utilisateur`).

### Quand ouvrir un deal

**Un deal se crée quand il y a un objet à vendre.** Une relation intéressante sans objet identifié
est une **partie de l'annuaire** (rôle *réseau*), accompagnée d'une note et, si utile, d'une tâche
de relance — pas un deal vide qui ferait office de fiche contact.

Poser une raison de perte (`lostReason`) en passant un deal à `perdu` : c'est ce qui rend
l'attrition relisible.

## Le catalogue d'offres

Ce qu'AVQN vend, en objets — c'est ce qui rend « combien de Parcours vendus ce trimestre »
répondable par l'OS.

- **`avqn-os:offre_list`** — le catalogue courant ; `includeInactive` pour relire un deal ancien.
- **`avqn-os:offre_create { name, price?, fiche? }`** — **laisser `price` vide** pour une offre sur
  devis : l'absence de prix est une information, pas un oubli.
- **`avqn-os:offre_update`** — `active: false` retire l'offre du catalogue sans toucher aux deals
  qui la portent. Il n'y a pas de suppression, et c'est voulu.

Rattacher l'offre au deal (`deal_update { offreId }`) **quand elle correspond vraiment**. Un deal
hors catalogue reste sans offre : forcer un choix ferait entrer du faux dans les comptes.

## Noter un échange

Le fil d'une relation vit dans le **carnet**, pas dans le CRM :

```
avqn-os:carnet_create { body: "…", liens: [{ kind: "partie", targetId: "<id>" }] }
```

Sans titre — une note de fil n'en a pas. Détails dans `tenir-le-carnet`.

Un échange a une date : c'est une note. Ce qu'on **apprend** sur la partie (son métier, son
organisation, ses gens) n'en a pas : ça enrichit sa **fiche**.

## Ce qu'on ne fait pas

- Marquer quelqu'un « client » : le rôle se dérive d'un deal gagné ou d'une facture émise.
- Supprimer une partie pour faire propre : archiver.
- Créer un deal pour garder une trace de quelqu'un : créer la partie et une note.
- Écrire au carnet ce qu'une partie **est** : ça va dans sa fiche, qui doit rester juste.
