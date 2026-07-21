---
name: tenir-le-carnet
description: >-
  À utiliser dès qu'on consigne ou retrouve un fait durable dans AVQN OS : « prends note que… »,
  un compte rendu, un brief, une décision, le suivi d'un échange avec quelqu'un. Orchestre le
  carnet — magasin unique de notes de l'OS, titre optionnel, N liens typés par note (partie,
  deal, projet, tâche), archive douce, recherche plein-texte française. Charge d'abord le socle
  piloter-avqn-os. NE COUVRE PAS ce qu'il faut faire (gerer-les-taches) ni la recherche
  transversale mails/agenda (outil recall du socle).
---

# Tenir le carnet

Commencer par charger **`piloter-avqn-os`**.

Le carnet est **le** magasin de notes de l'OS : le compte rendu d'une réunion, le brief d'un
projet, une décision, et le fil de suivi d'une relation vivent tous ici. Il n'y a pas d'autre
endroit où noter.

## Deux façons d'écrire

**La note de fil** — un post rapide dans le suivi d'une partie ou d'un deal. **Pas de titre** :

```
avqn-os:carnet_create {
  body: "Appelé Antoine, il rappelle en septembre.",
  liens: [{ kind: "partie", targetId: "<id>" }]
}
```

**Le fait durable** — titre, tags, éventuellement épinglé :

```
avqn-os:carnet_create {
  title: "Kickoff — cadrage technique",
  body: "…",
  tags: ["reunion", "cadrage"],
  liens: [{ kind: "project", targetId: "<id>" }, { kind: "partie", targetId: "<id>" }]
}
```

Les deux sont des notes de plein droit : même recherche, mêmes tags, même archive.

## Les liens

Une note porte **N liens**, chacun visant exactement une cible : `partie`, `deal`, `project`,
`task`. Une note de réunion peut viser à la fois la personne, le deal et le projet — **la lier
partout où elle est vraie** plutôt que de choisir ou de la dupliquer.

**La cascade frappe le lien, jamais la note** : supprimer un deal retire le rattachement et laisse
la note au carnet. Retirer une note d'un fil, c'est retirer **le lien** — pas la note.

`carnet_update { liens }` **remplace l'ensemble** des liens. Pour en ajouter un, relire d'abord la
note (`carnet_get`) et renvoyer la liste complète, sous peine d'effacer les autres.

## Les gestes

- **`avqn-os:carnet_list`** — épinglées d'abord, puis les plus récentes. Filtres `tag`, `cible`
  (`{ kind, targetId }` — c'est ce qui rend le fil d'une partie ou d'un deal), `includeArchived`.
- **`avqn-os:carnet_get`** — la note complète avec ses liens et le nom de chaque cible.
- **`avqn-os:carnet_update`** — titre, corps, date, tags, épinglage, `archived`, liens.
- **`avqn-os:carnet_delete`** — destructif, `confirm` requis. **Y penser à deux fois** : le carnet
  est le magasin des faits durables ; archiver suffit presque toujours.

`noteDate` est **le jour concerné** par la note, pas celui de la saisie. Consigner une réunion de
mardi le jeudi : poser `noteDate` au mardi.

## Chercher

Pour chercher **dans le contenu**, utiliser **`avqn-os:recall`** (recherche transversale, qui voit
aussi les mails et l'agenda) plutôt que de parcourir `carnet_list`. `carnet_list` sert à lister un
fil ou un tag, pas à fouiller.

## Ce qu'on ne fait pas

- Créer une note pour dire quoi faire : c'est une tâche (`gerer-les-taches`).
- Dupliquer une note pour la rattacher à deux entités : lui poser deux liens.
- Supprimer une note pour la sortir d'un fil : retirer le lien.
