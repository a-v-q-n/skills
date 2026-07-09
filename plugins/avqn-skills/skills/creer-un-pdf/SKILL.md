---
name: creer-un-pdf
description: >-
  À utiliser dès qu'on assemble plusieurs images en un PDF multi-pages (carrousel LinkedIn, document
  illustré, lookbook, dossier) : produire les pages une par une via le MCP médiathèque (rendu HTML→PNG
  ou image IA), collecter leurs URLs dans l'ordre, puis les joindre en un PDF. Mécanique brand-neutral,
  appelée par les recettes visuelles quand il leur faut un PDF. NE COUVRE PAS la direction artistique
  des pages (voir produire-un-visuel-avqn) ni les gabarits d'un canal (réseaux, cover ressource).
---

# Créer un PDF illustré

Assembler **N images en un PDF multi-pages** — une page par image. C'est une **mécanique**, pas une charte : ce skill ne connaît ni la marque ni le canal. Le look de chaque page vient de qui la produit ; ici on ne fait que **générer les pages une par une puis les joindre**.

Un PDF illustré ne reflowe pas : **chaque page EST une image figée**. Toute la mise en page se fait en amont, au niveau image.

## La mécanique

1. **Produire chaque page comme une image, dans l'ordre.** Selon la nature de la page :
   - page composée (texte, mise en page) → `media_render_html` (HTML autonome → PNG) ;
   - page illustrée par IA → `media_generate_image` ;
   - image déjà en galerie → la retrouver via `media_list_images`, ou l'importer.
   Récupérer l'**URL galerie** de chaque page et les garder **dans l'ordre des pages**.
2. **Vérifier chaque page à l'œil** avant d'assembler — une page ratée fait un PDF raté, et le PDF ne se corrige pas après coup, on régénère la page puis on réassemble.
3. **Joindre** → `media_create_pdf` avec `image_urls=[…]` **dans l'ordre** : une page par image, un PDF.
4. **Nommer le livrable** → `media_update`.

## Contraintes

- **Un seul format pour toutes les pages** — un PDF veut des pages cohérentes : rendre toutes les images aux mêmes `width`/`height`.
- **L'ordre de `image_urls` = l'ordre des pages.** Le vérifier deux fois avant d'assembler.
- **Pas de texte réel dans le PDF** (sélection, liens) : ce sont des images. Si le PDF doit rester lisible/accessible en texte, ce n'est pas la bonne mécanique.

## Pages on-charte AVQN

Ce skill ne porte pas de direction artistique. Pour des pages **on-charte**, produire chaque page via `produire-un-visuel-avqn` (ou une recette : `creer-un-visuel-social` pour un carrousel réseaux), puis revenir ici pour l'assemblage. La séparation est nette : **la recette dessine les pages, `creer-un-pdf` les relie.**

## Outils MCP (médiathèque)

- `media_render_html` — page composée → image.
- `media_generate_image` — page illustrée par IA.
- `media_create_pdf` — joindre les images en un PDF (`image_urls` dans l'ordre).
- `media_update` — nommer le livrable · `media_list_images` — retrouver une image.
