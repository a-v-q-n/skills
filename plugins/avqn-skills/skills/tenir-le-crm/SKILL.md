---
name: tenir-le-crm
description: >-
  À utiliser dès qu'on touche à une relation d'affaires d'AVQN : ajouter ou retrouver quelqu'un
  dans l'annuaire, rattacher une personne à une organisation, ouvrir ou faire avancer un deal,
  noter un échange, savoir qui est client. Orchestre le domaine CRM d'AVQN OS — parties
  (personne|organisation), affiliations datées, deals à étapes et leurs interlocuteurs. Charge
  d'abord le socle piloter-avqn-os. NE COUVRE PAS la facturation (creer-une-facture), le carnet
  lui-même (tenir-le-carnet) ni le temps passé (suivre-le-temps).
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
- **`avqn-os:partie_get`** — la fiche **avec** ses rôles dérivés, ses affiliations (ou ses membres
  si c'est une organisation) et ses deals.
- **`avqn-os:partie_create`** — `kind` obligatoire. Pour une **personne** : `firstName` /
  `lastName` (le nom affiché se dérive). Pour une **organisation** : `displayName`.
- **`avqn-os:partie_update`** — `archived: true` masque une relation éteinte sans rien perdre.
  Le type ne se change pas : une personne devenue société est une autre entité.
- **`avqn-os:partie_delete`** — destructif, `confirm` requis. **Refusé** si la partie porte des
  deals. Préférer l'archivage, toujours.

**Ne jamais créer une organisation pour pouvoir facturer quelqu'un.** Une personne physique se
facture directement.

## Les affiliations

`avqn-os:affiliation_create { personneId, organisationId, role }` rattache. Une personne peut
appartenir à plusieurs organisations.

**Un départ se clôt, il ne s'efface pas** : `avqn-os:affiliation_update { id, endedOn }`.
`affiliation_delete` est réservé aux erreurs de saisie.

Ne rattacher que ce que la donnée établit. Un employeur supposé d'après un nom de domaine n'est
pas un fait — laisser sans affiliation vaut mieux qu'un rattachement inventé.

## Les deals

- **`avqn-os:deal_create { name, partieId }`** — la partie est **obligatoire**.
- **`avqn-os:deal_update`** — étape, montant, probabilité, partie, raison de perte.
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

## Noter un échange

Le fil d'une relation vit dans le **carnet**, pas dans le CRM :

```
avqn-os:carnet_create { body: "…", liens: [{ kind: "partie", targetId: "<id>" }] }
```

Sans titre — une note de fil n'en a pas. Détails dans `tenir-le-carnet`.

## Ce qu'on ne fait pas

- Marquer quelqu'un « client » : le rôle se dérive d'un deal gagné ou d'une facture émise.
- Supprimer une partie pour faire propre : archiver.
- Créer un deal pour garder une trace de quelqu'un : créer la partie et une note.
