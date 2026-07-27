---
name: tenir-le-crm
description: >-
  À utiliser dès qu'on touche à une relation d'affaires d'AVQN : ajouter ou retrouver quelqu'un
  dans l'annuaire, rattacher une personne à une organisation, ouvrir ou faire avancer un deal,
  noter un échange, savoir qui est client, réparer un rattachement erroné. Orchestre le domaine
  CRM d'AVQN OS — parties (personne|organisation), affiliations datées, deals à étapes et leurs
  interlocuteurs, catalogue d'offres. Charge d'abord le socle piloter-avqn-os. NE COUVRE PAS la
  facturation (creer-une-facture), le carnet lui-même (tenir-le-carnet) ni le temps passé
  (suivre-le-temps).
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
facture directement. Le nom d'un produit, d'un site ou d'une marque portée par un indépendant
n'est pas une organisation : c'est une information de sa fiche.

### Les champs structurés d'abord

Téléphone, email, site, adresse ont leur champ. Les y mettre — pas dans le corps de la fiche. Une
coordonnée noyée dans du markdown n'est ni cherchable, ni reprise par la facturation.

Ne jamais compléter un champ structuré par déduction. Une coordonnée absente vaut mieux qu'une
coordonnée plausible : l'agent qui la relira la traitera comme vraie.

### La fiche d'une partie

`fiche` (markdown) porte **ce que cette partie est** : son métier, ses implantations, ses gens, ce
qu'on a compris d'elle. Une seule par partie, et elle doit rester juste — on la corrige quand le
monde change, on ne l'empile pas. Ce qui s'est *passé* (un appel, une proposition) va au carnet,
daté (`tenir-le-carnet`).

Ce qui mérite d'y figurer et ne vit nulle part ailleurs :

- **Sa structure réelle** — les entités derrière un même nom commercial, qui facture qui.
- **Qui fait quoi**, en une ligne par personne : décideur, pilote, relais technique, utilisateur.
  Le détail de chacun vit dans sa propre fiche ; l'organisation n'en garde que la carte.
- **Comment travailler avec elle** — le circuit de décision, le registre, les contraintes
  apprises à ses dépens, les sujets à manier avec tact.
- **Ce que la relation vaut** — référence, témoignage, porte d'entrée.

Ce qui n'y figure pas, parce que ça vit ailleurs : le déroulé d'un mandat (fiche du **projet**), sa
chronologie (**carnet**), l'état d'une créance (**facture**), les conditions négociées (**deal**).

> **Le test du doublon** : une phrase qui pourrait être copiée telle quelle dans deux objets est au
> mauvais endroit dans au moins un des deux.

Pour compléter une fiche longue sans la relire ni risquer d'écraser ce que Manu vient d'y écrire :
**`avqn-os:fiche_append { kind: "partie", targetId, texte }`**.

### AVQN elle-même

AVQN est une partie de l'annuaire, marquée `soi` — elle n'apparaît pas dans les listes ni dans la
dérivation des rôles. Sa fiche porte le positionnement, les valeurs, ce que Manu refuse. Les
données administratives structurées (dénomination, adresse, IBAN, mention TVA) vivent dans le
**profil émetteur** de facture (`invoice_issuer_get`), qui en est la source unique : la fiche ne
les répète pas.

## Les affiliations

`avqn-os:affiliation_create { personneId, organisationId, role }` rattache. Une personne peut
appartenir à plusieurs organisations. Le `role` se remplit : une affiliation sans fonction ne dit
presque rien.

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

**Nommer un deal par sa contrepartie et son objet** : `Kévin Sefsaf — Coaching individuel n8n (5 h)`.
Un intitulé qui ne dit ni qui ni quoi devient illisible dès qu'il y a dix lignes au pipeline.

### Quand ouvrir un deal

**Un deal se crée quand il y a un objet à vendre.** Une relation intéressante sans objet identifié
est une **partie de l'annuaire** (rôle *réseau*), accompagnée d'une note et, si utile, d'une tâche
de relance — pas un deal vide qui ferait office de fiche contact.

Un deal à montant nul est le symptôme de cette faute : rien à vendre, donc rien à suivre.

### L'étape et la probabilité disent la même chose

Une probabilité qui contredit l'étape rend le pipeline faux :

- `gagne` → **100**. `perdu` → **0**. Sans exception.
- `proposition` à 100 % est un mensonge : si c'était certain, ce serait gagné. Une offre acceptée
  oralement mais suspendue à une validation qu'on ne maîtrise pas plafonne autour de 70.
- Une affaire en attente d'une relance que le client doit initier descend, elle ne stagne pas.

Quand la probabilité bouge, **dire pourquoi dans la fiche du deal**, avec la date. Sinon personne
ne sait si le chiffre est réfléchi ou hérité.

### La fiche d'un deal

Elle porte **ce dont l'affaire parle** : le périmètre vendu, le prix et comment il a été construit,
les conditions négociées, l'échéancier, ce qui bloque. Et, une fois l'affaire close, **ce qu'elle a
appris** — un format qui naît, une règle tarifaire qui se fixe, un travers de vente à corriger.

Poser une raison de perte (`lostReason`) en passant un deal à `perdu` : c'est ce qui rend
l'attrition relisible. **Toujours en poser une**, y compris « sans suite après la proposition du
JJ.MM, raison réelle non documentée » — l'absence d'information est elle-même une information.

## Réparer un rattachement erroné

Un deal, un projet, du temps ou une facture rattachés à la mauvaise partie — typiquement une
fausse organisation créée pour facturer un particulier. Deux situations, à ne pas confondre :

**Le rattachement est faux, l'objet est bon.** Corriger le rattachement, en descendant la chaîne :
`deal_update { partieId }`, `project_update { clientId }`, `invoice_update { clientId }`. Le temps
suit son projet et n'a rien à corriger — la partie et le taux se dérivent en remontant.

**L'objet lui-même n'aurait pas dû exister** — un deal sans objet à vendre, une organisation
fantôme, un projet créé en double. Le délier de tout ce qui pend, puis le supprimer ou l'archiver.
`partie_delete` reste refusée tant qu'un deal la vise : c'est le garde-fou, pas un obstacle à
contourner.

**Un mandat gagné dont le projet n'existe pas** se répare par **`deal_win`**, pas en créant un
projet à la main : c'est le seul geste qui pose le lien deal → projet, et donc la cohérence de tout
l'aval.

Avant toute suppression, lire ce qui pend (`contexte`) : un objet supprimé emporte ses
rattachements, et un rattachement perdu ne se retrouve pas.

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

**Un format inventé en clientèle entre au catalogue** — c'est ainsi qu'il devient vendable deux
fois. La note qui raconte sa naissance vise le deal d'où il vient (`tenir-le-carnet`).

## Noter un échange

Le fil d'une relation vit dans le **carnet**, pas dans le CRM :

```
avqn-os:carnet_create { body: "…", lien: { kind: "partie", targetId: "<id>" } }
```

**Un seul rattachement, le plus fin** : un échange autour d'une affaire en cours vise le **deal**,
une séance ou une facture visent le **projet**, un échange de réseau vise la **partie**. Le client
d'un projet et la partie d'un deal se **dérivent à la lecture** — ne jamais les re-lier. Les
personnes présentes que le graphe ne déduit pas vont dans `interlocuteurs`. Règle complète dans
`tenir-le-carnet`.

Un échange a une date : c'est une note. Ce qu'on **apprend** sur la partie (son métier, son
organisation, ses gens) n'en a pas : ça enrichit sa **fiche**.

## Ce qu'on ne fait pas

- Marquer quelqu'un « client » : le rôle se dérive d'un deal gagné ou d'une facture émise.
- Créer une organisation pour facturer une personne physique.
- Supprimer une partie pour faire propre : archiver.
- Créer un deal pour garder une trace de quelqu'un : créer la partie et une note.
- Laisser une probabilité qui contredit l'étape, ou un deal perdu sans raison.
- Écrire au carnet ce qu'une partie **est** : ça va dans sa fiche, qui doit rester juste.
- Recopier dans une fiche ce qu'un autre objet porte déjà.
