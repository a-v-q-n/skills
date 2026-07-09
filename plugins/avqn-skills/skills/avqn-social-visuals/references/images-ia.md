# Images IA — « l'anticipation douce »

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

## Les mondes = des recettes de lumière (paires, jamais monochromes)

UNE recette par image : une **dominante + un contrepoint**. C'est le contrepoint qui rend la couleur intelligente ; un plan monochrome est un plan raté.

| monde | lumière | dominante | contrepoint |
|-------|---------|-----------|-------------|
| `ardoise` | nuit, heure bleue | bleus d'ombre `#46647A` | tungstène ambré |
| `ambre` | matin, soleil rasant | ors chauds `#C89B5A` | une ombre ardoise froide |
| `sauge` | plein jour, végétal | verts doux `#71805F` | bois et terre argile |
| `argile` | intérieur doré, humain | terracotta / peau `#BC8272` | crème et blancs cassés |
| `prune` | crépuscule, focus | violets sourds `#5F5069` | une lueur chaude |

Nommer explicitement la paire dans le prompt (ex. `warm amber golden light dominates, counterpointed by one cool slate-blue shadow area`). Jamais deux mondes dominants dans le même plan.

## Le vermillon sémantique (la signature)

**UN seul objet vermillon `#E0542B` par image, et il désigne ce dont le visuel parle** : le carnet qu'on ouvre, la diode du système qui tourne, le post-it qui déborde. Jamais décoratif, toujours porteur de sens — la règle qui unifie tous les visuels de la marque.

## Personnes & écrans

Visages encouragés : des gens crédibles saisis dans un moment (jamais posés face caméra, jamais de sourire stock), émotions lisibles, diversité naturelle, **pas de ressemblance avec Manu**. Une pièce vide ou un objet raconte aussi bien — l'absence est éloquente. Écrans autorisés (ils portent souvent la touche futur), mais **tout texte illisible** : ajouter `any on-screen text unreadable and out of focus`.

## Gabarit de prompt

`Cinematic editorial photograph, vertical composition` + **la scène** (sujet, action, moment — dire aussi ce qui est absent) + **la paire du monde** + **l'objet vermillon et son sens** + **la touche futur** + le grade commun. Peu d'éléments, de l'air, un premier plan travaillé.

## Poser l'image

Génération via `media_generate_image` (MCP médiathèque) → URL galerie. On la pose :
- dans le `<img>` du gabarit `social-image-editorial` (image en grand + titre serif dessous), ou
- **plein cadre en duotone** sur un fond nocturne (niveaux de gris + voile encre + vignette), le texte crème par-dessus.
