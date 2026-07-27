---
name: tenir-le-carnet
description: >-
  À utiliser dès qu'on consigne ou retrouve ce qui S'EST PASSÉ dans AVQN OS : « prends note
  que… », un compte rendu, le suivi d'un échange, une décision prise un jour donné. Orchestre le
  carnet — le journal daté de l'OS, titre selon la portée, UN rattachement par note (le plus fin :
  tâche > projet > deal > partie) plus les présents, dérivation à la lecture, archive douce,
  recherche plein-texte française. Charge d'abord le socle piloter-avqn-os. NE COUVRE PAS ce qu'un
  objet EST (sa fiche, écrite par le tool de son domaine), ce qu'il faut faire (gerer-les-taches)
  ni la recherche transversale mails/agenda (outil recall du socle).
---

# Tenir le carnet

Commencer par charger **`piloter-avqn-os`**.

Le carnet est le **journal** de l'OS : ce qui s'est passé, daté. Le compte rendu d'une réunion, le
suivi d'une relation, une décision prise ce jour-là.

## Le test, avant d'écrire

> **Est-ce que ça a une date qui compte ?**
> **Oui** → une note de carnet.
> **Non**, ça décrit ce qu'un objet **est** maintenant → **sa fiche** (`partie_update {fiche}`,
> `deal_update {fiche}`, `project_update {fiche}`… ou `fiche_append` pour ajouter sans relire).

« Antoine rappelle en septembre » a une date : c'est une note. « 3D Swiss View fait du relevé 3D
par laser scanner, siège à Martigny » n'en a pas : c'est la fiche de la partie. Poser la seconde au
carnet la condamne à vieillir sans que personne ne la corrige — et l'agent la lira comme vraie.

Quand le monde change, **corriger la fiche** ; si le changement compte en lui-même (un
déménagement, une signature), ajouter **aussi** une note datée.

### Le corollaire : une note ne dit pas ce qu'un objet est

Une note qui décrit un profil, un métier, une manière de travailler est mal rangée : son contenu
appartient à une fiche. La note garde l'événement, la fiche reçoit ce qu'on en a appris.

> « Appel de cadrage. Elle est plus avancée qu'attendu : Summit de l'IA, formation Copilot,
> bidouille en AppleScript. Son vrai besoin est de montrer des exemples dans sa boîte. »

L'appel a une date — la note le garde. Le niveau et le besoin réel n'en ont pas — ils vont dans sa
fiche, et la note y renvoie : *« profil et vrai besoin consignés dans sa fiche »*.

## Le titre : selon la portée

- **Jalon** — quelque chose qu'on voudra retrouver dans six mois (une signature, une livraison, une
  séance, une rupture) : **titre**, court et factuel. C'est ce qui rend un fil lisible d'un coup
  d'œil.
- **Note de fil** — un point de suivi courant, un échange sans conséquence : **pas de titre**.

```
avqn-os:carnet_create {
  body: "Appelé Antoine, il rappelle en septembre.",
  lien: { kind: "deal", targetId: "<id-deal>" },
  interlocuteurs: ["<id-antoine>"]
}
```

```
avqn-os:carnet_create {
  title: "Livraison du dashboard et clôture du mandat",
  body: "…",
  lien: { kind: "project", targetId: "<id-projet>" },
  interlocuteurs: ["<id-interlocuteur>"]
}
```

## Le rattachement — un seul, le plus fin

Une note porte **UN rattachement** (0..1) : l'endroit le plus fin que l'événement concerne. La
hiérarchie décide, il n'y a rien à arbitrer :

> **tâche > projet > deal > partie**

Tout le reste **se dérive à la lecture**. Le dossier d'une partie hérite des notes de ses deals et
de ses projets, avec le motif du rattachement (`via`) : une note liée au projet apparaît chez le
client sans lui être liée. C'est pour ça qu'on ne re-lie **jamais** un ancêtre — poser à la fois le
projet et sa partie duplique une information que la lecture sait reconstruire, et brouille la
question « qu'est-ce que cette note concerne exactement ? ».

Une note sans rattachement est une **note libre** du journal : une idée, un apprentissage
transversal, une réflexion qui ne concerne aucun objet en particulier.

### Les présents, à côté du rattachement

`interlocuteurs` consigne les **personnes présentes** à l'événement (0..N) — même modèle que les
participants d'un deal. On n'y met que ce que le graphe CRM ne sait pas déduire : la personne
rattachée à l'organisation cliente, l'interlocuteur habituel d'un deal se dérivent déjà. Un tiers
venu à la séance, un décideur croisé une fois, un collègue du client présent à l'atelier : eux
méritent d'y figurer.

### Par type d'événement

| L'événement | Le rattachement |
|---|---|
| Lead entrant, premier contact, appel de cadrage | le **deal** (ou la **partie** si aucun deal n'est ouvert) |
| Offre envoyée, relance, négociation, acceptation, perte | le **deal** |
| Séance, atelier, livrable | le **projet** |
| Facture émise, encaissement, clôture de mandat | le **projet** |
| Échange sans objet à vendre (réseau) | la **partie** |
| Avancement d'un engagement précis | la **tâche** |
| Apprentissage transversal (un format qui naît, un tarif qui se fixe) | rien — note libre, ou le deal d'où il vient |

Le deal documente **la conquête**, pas la livraison : il s'arrête à l'étape qui clôt l'affaire.
Tout ce qui suit — séances, livrables, factures, encaissements — vise le **projet**. Sans cette
borne, les deals gagnés accumulent de la matière de production et le pipeline devient illisible.

### Mécanique

**La cascade frappe le lien, jamais la note** : supprimer un deal détache la note, qui survit au
carnet. Retirer une note d'un fil, c'est retirer **le rattachement** — pas la note
(`carnet_update { lien: null }`). `interlocuteurs` se remplace en bloc : renvoyer la liste
complète, jamais le seul nom qu'on ajoute.

## Le grain : un jalon, une note

Une note par événement qui compte. Ni plus fin, ni plus gros.

- **Trop fin** — « il a répondu », « rendez-vous décalé », « correction : c'est lundi pas mardi ».
  Ça n'est pas un événement, c'est de la logistique. Ça se fond dans la note du jalon voisin, ou ça
  ne s'écrit pas.
- **Trop gros** — trois semaines de mandat dans une seule note. Le fil ne se lit plus, et rien n'est
  retrouvable.

**Une note ne corrige pas une note.** Une erreur de chiffre, de date ou de lecture se répare dans
la note elle-même (`carnet_update`). Empiler une note de correction laisse les deux versions
vivantes, et la fausse remonte aussi bien que la vraie dans `recall`.

**Une note ne dit pas ce qu'il faut faire.** Un « next step » consigné au carnet n'est ni rappelé,
ni échéancé, ni clôturable. Ce qui est à faire est une tâche (`gerer-les-taches`) ; la note garde
seulement ce qui s'est passé.

## Reconstituer un fil a posteriori

Quand un dossier ancien n'a pas été suivi au fil de l'eau, le fil se reconstitue depuis les sources
de l'OS plutôt que de mémoire : `recall` pour balayer, `mail_search` / `mail_read` pour le contenu
réel des échanges, `cal_event_list` pour les dates et les durées, `timesheet_list` pour ce qui a été
fait et combien de temps ça a pris.

Deux précautions :

- **Ne consigner que ce que la source établit.** Une séance dont le contenu n'est nulle part se note
  avec sa date et sa durée, et un marqueur explicite — *« contenu non consigné, à compléter »*.
  Inventer un déroulé plausible est pire que de laisser un trou.
- **Croiser avant de conclure.** Un mail d'invitation ne prouve pas qu'une séance a eu lieu ; une
  saisie de temps, oui. Un dossier qui semble s'être bien terminé peut avoir une fin manquée que
  seuls les derniers mails racontent.

## Les gestes

- **`avqn-os:carnet_list`** — les plus récentes d'abord. Filtres `cible` (`{ kind, targetId }` —
  c'est ce qui rend le fil d'une partie ou d'un deal), `includeArchived`.
- **`avqn-os:carnet_get`** — la note complète avec son rattachement et ses présents, noms inclus.
  `carnet_list` rend un résumé : passer par `carnet_get` pour lire un corps en entier.
- **`avqn-os:carnet_update`** — titre, corps, date, `archived`, `lien` (`null` détache),
  `interlocuteurs`.
- **`avqn-os:carnet_delete`** — destructif, `confirm` requis. **Y penser à deux fois** : archiver
  suffit presque toujours.

`noteDate` est **le jour concerné** par la note, pas celui de la saisie. Consigner une réunion de
mardi le jeudi : poser `noteDate` au mardi. Pour un événement étalé (une formation sur deux mois),
poser la date de **début** et donner la période dans le corps.

## Chercher

Pour chercher **dans le contenu**, utiliser **`avqn-os:recall`** (recherche transversale, qui voit
aussi les fiches, les mails et l'agenda) plutôt que de parcourir `carnet_list`. `carnet_list` sert
à dérouler un fil, pas à fouiller.

## Ce qu'on ne fait pas

- Écrire au carnet ce qu'un objet **est** : ça va dans sa fiche.
- Créer une note pour dire quoi faire : c'est une tâche (`gerer-les-taches`).
- Écrire une note qui en corrige une autre : corriger la première.
- Re-lier un ancêtre du rattachement (le projet *et* sa partie) : la lecture le dérive déjà.
- Garder le rattachement au `deal` sur une livraison postérieure au gain : c'est le projet.
- Mettre dans `interlocuteurs` une personne que le graphe CRM déduit seul.
- Supprimer une note pour la sortir d'un fil : la détacher (`lien: null`).
