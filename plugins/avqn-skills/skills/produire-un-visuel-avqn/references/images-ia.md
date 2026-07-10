# Images IA — « l'anticipation douce »

> **Source unique : [styleguide.avqn.ch/doctrine/da-image.md](https://styleguide.avqn.ch/doctrine/da-image.md).**
> La doctrine complète de la DA image (grade, recettes de lumière, vermillon sémantique, touche futur,
> gabarit) y vit. Ce fichier en est le rappel opérationnel ; le styleguide fait foi.

Le rendu des visuels générés reprend la DA photo des vidéos : le monde d'un indépendant, décalé de deux degrés vers le futur, photographié comme un film 35 mm des années 70. **Crédible d'abord, futur ensuite, rétro dans le rendu.** Références : *Her*, *Severance*, *Foundation*, pellicule Cinestill 800T (la halation).

Toujours : **jamais de texte dans l'image** — les mots vivent dans la mise en page, jamais dans l'image générée.

## Le grade commun (chaque prompt finit par)

```
shot on 35mm film, fine film grain, subtle halation on highlights, muted desaturated Kodak
color palette, warm blacks (#211C17), cream highlights (#FAF8F3), soft directional light,
shallow depth of field, carefully composed editorial frame, no readable text anywhere,
no frame line, no border
```

Noirs chauds jamais bleus ni purs, hautes lumières crème jamais cliniques, saturation contenue. La halation (halo chaud autour des sources) tire naturellement les lumières vers le vermillon.

## La touche futur (obligatoire, discrète)

UN détail impossible aujourd'hui, analogique et chaud — terminal à écran bombé et texte ambré, e-paper souple, molette physique pilotant un système intelligent, diode de présence qui veille. **Dans un coin, jamais au centre.** Jamais d'hologramme bleu, de robot, de HUD flottant. La techno de cet univers est chaude, tactile, en bois / métal brossé / tissu technique.

## Les recettes de lumière (une palette, pas des règles)

Cinq ambiances possibles, à choisir selon le propos — des **directions artistiques**, pas des contraintes. Une dominante suffit ; un contrepoint (une zone qui répond) enrichit souvent le plan.

| recette | lumière | dominante | contrepoint possible |
|---------|---------|-----------|----------------------|
| `ardoise` | nuit, heure bleue | bleus d'ombre `#46647A` | tungstène ambré |
| `ambre` | matin, soleil rasant | ors chauds `#C89B5A` | une ombre ardoise froide |
| `sauge` | plein jour, végétal | verts doux `#71805F` | bois et terre argile |
| `argile` | intérieur doré, humain | terracotta / peau `#BC8272` | crème et blancs cassés |
| `prune` | crépuscule, focus | violets sourds `#5F5069` | une lueur chaude |

## Les lieux sont contemporains

Le rétro vit dans le **rendu** (grain, halation), jamais dans le **décor** : intérieurs modernes, lignes nettes, mobilier actuel — pas de vieilles fermes ni de poutres rustiques. Le dire dans le prompt (`contemporary interior, modern furniture, no vintage furniture, no rustic beams; the retro lives only in the film rendering`).

## Le vermillon sémantique (la signature)

**UN seul objet vermillon `#E0542B` par image, et il désigne ce dont le visuel parle** : le carnet qu'on ouvre, la diode du système qui tourne, le post-it qui déborde. Jamais décoratif, toujours porteur de sens — la règle qui unifie tous les visuels de la marque.

## Personnes & écrans

Visages encouragés : des gens crédibles saisis dans un moment (jamais posés face caméra, jamais de sourire stock), émotions lisibles, diversité naturelle, **pas de ressemblance avec Manu**. Une pièce vide ou un objet raconte aussi bien — l'absence est éloquente. Écrans autorisés (ils portent souvent la touche futur), mais **tout texte illisible** : ajouter `any on-screen text unreadable and out of focus`.

## Gabarit de prompt

`Cinematic editorial photograph, vertical composition` + **la scène contemporaine** (sujet, action, moment — dire aussi ce qui est absent) + **la direction de couleur** (si elle sert le propos) + **l'objet vermillon et son sens** + **la touche futur** + le grade commun. Peu d'éléments, de l'air, un premier plan travaillé. Fixer l'intention — la phrase que l'image porte toute seule — avant de générer ; la banque de référence ([styleguide.avqn.ch/media/photo](https://styleguide.avqn.ch/media/photo)) donne des prompts réels appariés à leur résultat, par usage (b-rolls vidéo, posts).

## Poser l'image

Génération via `media_generate_image` (MCP médiathèque) → URL galerie. On la pose :
- **en grand** dans une mise en page hero (image + titre serif dessous), ou
- **plein cadre en duotone** sur un fond nocturne (niveaux de gris + voile encre + vignette), le texte crème par-dessus.

La recette qui exploite l'image fournit le gabarit (ex. `creer-un-visuel-social` → gabarit image-éditorial).
