---
name: tenir-le-carnet
description: >-
  À utiliser dès qu'on consigne ou retrouve ce qui S'EST PASSÉ dans AVQN OS : « prends note
  que… », un compte rendu, le suivi d'un échange, une décision prise un jour donné. Orchestre le
  carnet — le journal daté de l'OS, titre optionnel, N liens typés par note (partie, deal, projet,
  tâche), archive douce, recherche plein-texte française. Charge d'abord le socle piloter-avqn-os.
  NE COUVRE PAS ce qu'un objet EST (sa fiche, écrite par le tool de son domaine), ce qu'il faut
  faire (gerer-les-taches) ni la recherche transversale mails/agenda (outil recall du socle).
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

## Deux façons d'écrire

**La note de fil** — un post rapide dans le suivi d'une partie ou d'un deal. **Pas de titre** :

```
avqn-os:carnet_create {
  body: "Appelé Antoine, il rappelle en septembre.",
  liens: [{ kind: "partie", targetId: "<id>" }]
}
```

**Le compte rendu** — titré, parce qu'il se retrouvera dans une liste :

```
avqn-os:carnet_create {
  title: "Kickoff — cadrage technique",
  body: "…",
  liens: [{ kind: "project", targetId: "<id>" }, { kind: "partie", targetId: "<id>" }]
}
```

## Les liens

Une note porte **N liens**, chacun visant exactement une cible : `partie`, `deal`, `project`,
`task`. Une note de réunion peut viser à la fois la personne, le deal et le projet — **la lier
partout où elle est vraie** plutôt que de choisir ou de la dupliquer.

**La cascade frappe le lien, jamais la note** : supprimer un deal retire le rattachement et laisse
la note au carnet. Retirer une note d'un fil, c'est retirer **le lien** — pas la note.

`carnet_update { liens }` **remplace l'ensemble** des liens. Pour en ajouter un, relire d'abord la
note (`carnet_get`) et renvoyer la liste complète, sous peine d'effacer les autres.

## Les gestes

- **`avqn-os:carnet_list`** — les plus récentes d'abord. Filtres `cible` (`{ kind, targetId }` —
  c'est ce qui rend le fil d'une partie ou d'un deal), `includeArchived`.
- **`avqn-os:carnet_get`** — la note complète avec ses liens et le nom de chaque cible.
- **`avqn-os:carnet_update`** — titre, corps, date, `archived`, liens.
- **`avqn-os:carnet_delete`** — destructif, `confirm` requis. **Y penser à deux fois** : archiver
  suffit presque toujours.

`noteDate` est **le jour concerné** par la note, pas celui de la saisie. Consigner une réunion de
mardi le jeudi : poser `noteDate` au mardi.

## Chercher

Pour chercher **dans le contenu**, utiliser **`avqn-os:recall`** (recherche transversale, qui voit
aussi les fiches, les mails et l'agenda) plutôt que de parcourir `carnet_list`. `carnet_list` sert
à dérouler un fil, pas à fouiller.

## Ce qu'on ne fait pas

- Écrire au carnet ce qu'un objet **est** : ça va dans sa fiche.
- Créer une note pour dire quoi faire : c'est une tâche (`gerer-les-taches`).
- Dupliquer une note pour la rattacher à deux entités : lui poser deux liens.
- Supprimer une note pour la sortir d'un fil : retirer le lien.
