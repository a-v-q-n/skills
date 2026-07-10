---
name: creer-une-illustration-ui
description: >-
  À utiliser dès qu'on illustre un élément d'interface dans une ressource AVQN (sidebar, modale,
  formulaire, tableau…) : la maquette filaire — fausse UI en traits filet et textes gris sur fond
  papier, l'élément enseigné seul porteur du vermillon, annotation eyebrow. Composée en HTML,
  rendue via media_render_html en 1600×900. Charge le socle produire-un-visuel-avqn.
  NE COUVRE PAS les covers de ressources (creer-une-cover-ressource) ni les visuels de posts
  (creer-un-visuel-social).
---

# Créer une illustration UI

> **Source unique : [styleguide.avqn.ch/doctrine/ressources.md](https://styleguide.avqn.ch/doctrine/ressources.md).**
> La doctrine de la maquette filaire y vit ; ce skill en est le rappel opérationnel.

Composer la **maquette filaire** qui enseigne un élément d'interface — une illustration = un
élément. **Commencer par charger `produire-un-visuel-avqn`** (charte, rendu, vérification à
l'œil).

## La règle

La fausse UI recule : fond papier quadrillé, fenêtre d'app en trait encre, structure en traits
`filet`, textes gris — mais des **labels réels en Geist** (le vocabulaire s'apprend avec de
vrais mots, en français). **L'élément enseigné est le seul porteur du vermillon** : classe
`.focus` (mise en évidence au trait) + une `.annot` (eyebrow vermillon, Geist Mono UPPERCASE)
posée hors de la fenêtre. Jamais deux vermillons, jamais de réalisme de screenshot (ombres
portées, chrome de navigateur).

## Boucle

1. Identifier **l'élément enseigné** et sa phrase (« La modale : décider avant de continuer. »).
2. Partir de `templates/maquette.html` : composer la fausse UI minimale autour de l'élément,
   poser `.focus` + `.annot`.
3. Rendre : `media_render_html` (`width: 1600, height: 900, wait_for: 1500`).
4. **Vérifier à l'œil** : un seul vermillon, labels français lisibles, structure qui recule.
5. Livrer l'URL (module image de la ressource) ou nommer via `media_update`.

## Références

- `templates/maquette.html` — le gabarit canonique (tokens, `.focus`, `.annot`).
- La banque d'exemples : [styleguide.avqn.ch/media/ressources](https://styleguide.avqn.ch/media/ressources).
