# Images IA — la figure technique (schémas)

> **Source unique : [styleguide.avqn.ch/doctrine/da-schema.md](https://styleguide.avqn.ch/doctrine/da-schema.md).**
> La doctrine complète du style schéma y vit ; ce fichier en est le rappel opérationnel — en cas de
> doute, le styleguide fait foi.

Le style d'image qui **explique** : une idée, un flux, une relation, un système. Le dessin
technique à l'ancienne — trait d'encre fin, hachures légères, annotations, lettres de renvoi — au
service des sujets d'aujourd'hui (agents, workflows, boucles). La photo montre un monde ; le
schéma montre une structure.

## La métaphore mécanique

Les concepts numériques deviennent des **mécanismes simples** : l'agent est un boîtier
d'engrenages, les skills des plaques gravées, les tools des outils pendus à un rail, la boucle une
courroie circulaire. Jamais de personnages, jamais de robots, jamais d'écrans — des pièces.

## Les règles

- **UN seul élément vermillon `#E0542B`** par figure, et il désigne ce dont la figure parle.
- **Labels courts autorisés** dans l'image : français, minuscules, lignes d'attache fines,
  seulement là où le sens l'exige — l'exception propre à ce style (côté photo, « jamais de
  texte » reste absolu).
- **Ni cadre ni cartouche** : figure nue sur papier crème, marges généreuses, rendu scan à plat.

## Le grade commun (chaque prompt finit par)

```
Precise fine ink lineart on warm cream paper (#FAF8F3), warm dark ink (#211C17). Simple mechanical
objects drawn with thin lines and light hatching — the charm of an old technical drawing, without
any characters, figures or robots. Small lowercase French technical annotations with thin leader
lines, only labels that carry meaning. Generous margins and negative space. No border, no frame,
no cartouche, no ornaments, flat scan look, not a photograph of a document, no 3D render, no
gradients.
```

## Gabarit de prompt

`Technical documentation figure explaining` + **ce qu'on montre** (les unités mécaniques, leur
disposition, les labels exacts en français entre guillemets) + **l'élément vermillon et son sens**
(« the only vermilion element ») + le grade commun. Format **carré** par défaut
(`aspect_ratio: 1:1`). Génération via `media_generate_image` (MCP médiathèque), puis **vérifier à
l'œil** : labels français corrects, pas de charabia, pas de cadre, un seul vermillon. La banque de
référence ([styleguide.avqn.ch/media/schema](https://styleguide.avqn.ch/media/schema)) donne les
prompts réels appariés à leur résultat.
