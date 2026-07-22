# Grammaire des objets d'AVQN OS — référence

À charger quand un nom d'objet fait douter. Source : `avqn-os/docs/specs/2026-07-21-crm-grammaire-design.md`.

## Le CRM

| Objet | Table | Ce que c'est |
|---|---|---|
| Partie | `avqn_partie` | Une personne physique **ou** une organisation. `kind` les distingue. Cible unique de tout l'aval. |
| Affiliation | `avqn_affiliation` | Personne ↔ organisation, N-N, datée (`role`, `startedOn`, `endedOn`). |
| Deal | `avqn_deal` | Le commercial. Vise **une partie**, FK non nulle. |
| Participant | `avqn_deal_participant` | Les interlocuteurs d'un deal (décideur, prescripteur, utilisateur). Plusieurs par deal. |
| Offre | `avqn_offre` | Ce qu'AVQN vend. `price` nullable = sur devis. `avqn_deal.offre_id` dit ce que l'affaire vend. |

AVQN elle-même est une partie, marquée `soi` : c'est elle qui émet les factures et se tient en
face de chaque deal. Elle est exclue des listes de l'annuaire et de la dérivation des rôles — être
client de soi-même n'a pas de sens.

### Mots qui n'existent plus

L'ancienne grammaire séparait `client` (organisation), `contact` (personne) et `crm_note`. Elle
ne pouvait pas représenter une personne physique cliente, et laissait mourir les notes avec leur
entité. Correspondances utiles pour lire un vieux document ou une vieille note :

| Ancien | Nouveau |
|---|---|
| `client` (l'objet) | une partie de `kind: organisation` |
| `contact` | une partie de `kind: personne` |
| `contact.clientId` | une affiliation |
| `crm_note` | une note du carnet + un lien |
| étape `prospect` | étape `piste` |
| étape `qualified` / `proposal` | `qualifie` / `proposition` |
| étape `won` / `lost` | `gagne` / `perdu` |
| « client actif / archivé » | un rôle **dérivé** + `archived` (archive douce, indépendante du rôle) |

Le mot **prospect** ne désigne plus qu'un rôle dérivé, jamais une étape.

## Les étapes d'un deal

`piste` → `qualifie` → `proposition` → `gagne` / `perdu`

L'entonnoir s'arrête à `gagne` ; `perdu` est de l'attrition, il vit à part. Les valeurs en base
sont des codes stables ; les libellés affichés (Piste, Qualifié, Proposition, Gagné, Perdu) vivent
à part et peuvent changer sans toucher la donnée.

## Les tâches

`bucket` porte l'engagement — `inbox` (Capture), `today` (Aujourd'hui), `next` (Plus tard),
`someday` (Peut-être), plus les terminaux `done` et `dropped` (rayé consciemment ≠ fait).

Les **facettes** ne sont jamais des statuts :

- `scheduledFor` — dormante jusqu'à sa date, puis remonte seule dans Aujourd'hui ;
- `dueDate` — échéance externe ; dépassée, la tâche remonte dans Aujourd'hui où qu'elle soit ;
- `waitingOn` — en attente de quelqu'un, grisée sur place.

## La fiche et le carnet

Deux natures, une seule question pour les séparer : **est-ce que ça a une date qui compte ?**

**La fiche** — colonne `fiche` (markdown) sur `avqn_partie`, `avqn_deal`, `avqn_project`,
`avqn_task`, `avqn_offre`. Ce que l'objet **est** maintenant. Une par sujet : c'est une colonne,
elle ne peut pas exister en double. Elle n'a pas de date — l'`updatedAt` de l'objet suffit.

**Le carnet** — `avqn_note` : `title` **nullable**, `body` markdown, `noteDate` (le jour concerné,
≠ `createdAt`), archive douce (`archivedAt`). Ce qui s'est **passé**. Ni tags ni épinglage : dans
un journal daté et lié, l'ordre du temps et le rattachement suffisent à retrouver.

`avqn_note_lien` — une ligne = un lien, une seule cible parmi `partie`, `deal`, `project`, `task`,
par une vraie clé étrangère. `on delete cascade` porte sur **le lien**.

## Le temps

Le temps s'accroche au niveau le plus fin connu : tâche > projet > rien. Projet et partie
effectifs se **dérivent** en remontant.

Résolution du taux horaire, dans cet ordre — le premier renseigné gagne :

1. taux de l'**activité** (type de prestation),
2. taux du **projet**,
3. taux par défaut de la **partie**.

## La facturation

La facture est l'exception assumée à « dérivé, jamais recopié » : à l'émission, tout est **figé**
(numéro `AAAA-NNN`, snapshot du destinataire, lignes, montants). Les objets vivants bougent
ensuite, la facture jamais. Montants en **centimes**.

Les colonnes de snapshot gardent le préfixe `client_` : sur une pièce comptable, le destinataire
**est** le client, qu'il soit une personne ou une entreprise.

## L'index de recherche

`avqn_rag_chunk` est une **projection dérivée reconstructible**, jamais une source de vérité.
Sortes indexées : `partie`, `deal`, `project`, `task`, `timesheet`, `offre`, `note`, `mail`,
`event`. La fiche d'un objet est indexée **avec lui** : chercher un mot de la fiche remonte
l'objet, avec de quoi ouvrir son dossier — pas un document flottant qui parle de lui.
Le document d'une personne agrège ses organisations d'affiliation — c'est ce qui la rend trouvable
par le nom de sa boîte. `avqn-os:rag_status` dit où en est l'index ; `avqn-os:rag_reindex` le
reconstruit (par sorte ou en entier).
