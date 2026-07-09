---
name: avqn-social-visuals
description: >-
  Produit les assets visuels des réseaux sociaux AVQN (LinkedIn, Threads, Instagram) dans la
  charte de la marque : éditorial chaud, papier écru ou encre à lueur vermillon, serif qui porte
  le message. Images composées en HTML puis rendues en PNG, images IA « anticipation douce »
  (cinématique 35 mm), et carrousels PDF multi-pages. À utiliser dès qu'on crée un visuel de post,
  une slide, une couverture de carrousel, une stat/citation illustrée ou tout asset image destiné
  aux réseaux sociaux d'AVQN. NE COUVRE PAS la vidéo ni les visuels de ressources — autres périmètres.
---

# AVQN — Assets visuels réseaux sociaux

Composer des visuels de posts **on-charte** — l'univers des vidéos AVQN porté à l'image fixe : palette chaude (papier `#FAF8F3`, encre `#211C17`, un seul vermillon `#E0542B`), la serif **Instrument Serif** qui porte le message (accent italique vermillon), **Anton** pour le hook display, **Geist / Geist Mono** pour les appuis et labels. Deux ambiances : **papier quadrillé** (clair) et **nocturne** (encre + lueur vermillon qui respire + quadrillage + vignette). Atmosphère éditoriale, aérée, peu d'éléments par visuel.

Deux voies : **HTML composé → PNG** (le cas courant) et **image IA** (hero « anticipation douce »). Sortie unitaire (une image) ou **carrousel PDF**.

Périmètre : réseaux sociaux uniquement (LinkedIn en tête, décliné Threads / Instagram par les formats). Hors périmètre : vidéo, et visuels de ressources.

## Rendu : MCP médiathèque

**Tout le système rend via le MCP médiathèque — le skill ne rend rien lui-même.** Le HTML rempli est envoyé à l'outil de rendu partagé (Chromium mutualisé) ; le média produit atterrit dans la galerie et renvoie une URL, réutilisée pour le PDF ou la publication.

- **Rendre un visuel** → `media_render_html` : `html` (le gabarit rempli, complet et autonome), `width`, `height`, `wait_for` (ms — laisser fonts + fonds finir : **composés ~1500**, **hero avec image distante ~2600**), `name`, `tags`. Sortie PNG par défaut. → renvoie l'URL galerie.
- **Assembler un carrousel** → `media_create_pdf` : `image_urls` (URLs galerie des slides, **dans l'ordre**) → un PDF, une slide par page.
- **Générer une image IA** → `media_generate_image` (prompt de `references/images-ia.md`), puis poser l'URL dans le `<img>` du gabarit `social-image-editorial`.
- **Nommer le livrable** → `media_update`. **Retrouver un média / les icônes n8n** → `media_list_images`.

## Boucle de production

1. **Cadrer le message** — une idée par visuel, le hook (résultat brut ou objection nommée). Charger la voix si le texte doit sonner AVQN (skill `voix-manu`).
2. **Choisir un gabarit** dans `templates/CATALOG.md`, d'après la **forme du contenu** (statement, manifeste, chiffre, liste, citation, terminal, carrousel-cover, image-éditorial).
3. **Remplir le texte** — prendre le `.html`, remplacer les placeholders, **retours à la ligne à la main**. Un seul fragment en `.acc` (italique vermillon). Pour un format ≠ natif, régler `--W`/`--H` dans `:root` sur les dimensions cibles.
4. **Rendre** via `media_render_html` (`width`/`height` = les dimensions du format, `wait_for` adapté).
5. **Vérifier à l'œil** l'image produite (charger l'URL). Corriger débordements, veuves, alignements, contraste, la lueur nocturne. Re-rendre. **Cette étape n'est pas optionnelle.**
6. **Livrer** l'image, ou assembler un **carrousel PDF** via `media_create_pdf`.

## Formats & multi-réseaux

4:5 (1080×1350) = défaut, meilleure portée LinkedIn + IG portrait + Threads. 1:1 (1080×1080) = feed universel. 9:16 (1080×1920) = stories. 16:9 (1200×627) = aperçu de lien. Le format se règle en passant `width`/`height` à `media_render_html` **et** en alignant `--W`/`--H` du gabarit sur ces mêmes dimensions. Le catalogue indique, par gabarit, le format natif et ceux qui suivent proprement. Détail dans `references/charte-visuelle.md §9`.

## Carrousel → PDF

LinkedIn rend un PDF multi-pages comme un carrousel navigable. Slide 1 = `social-carrousel-cover`, slides suivantes piochées au catalogue en **alternant clair / nocturne**. Rendre chaque slide en 4:5 via `media_render_html` (récupérer les URLs), puis `media_create_pdf(image_urls=[...])` dans l'ordre.

## Image IA (« anticipation douce »)

La seule direction d'image générée (`references/images-ia.md`) : photo cinématique 35 mm, mondes-couleurs (dominante + contrepoint), **un objet vermillon sémantique**, grain film et halation. **Toujours sans texte dans l'image** — les mots vont dans la mise en page. Générer via `media_generate_image` (MCP médiathèque), puis poser l'URL dans le `<img>` du gabarit `social-image-editorial`, ou plein cadre en duotone sur un fond nocturne.

## Références

- `references/charte-visuelle.md` — le socle (palette, gamme typo, les 2 ambiances, gestes-signature, formats, tokens CSS, do/don't). **À respecter partout.**
- `references/images-ia.md` — la direction d'image générée « anticipation douce ».
- `templates/CATALOG.md` — l'index des gabarits + comment en ajouter.
- `assets/n8n-logo.svg` — logo n8n officiel (asset de marque).
- `examples/` — un rendu de chaque gabarit + une planche-contact (`_planche-contact.png`) : la cible visuelle de référence.

## Règles d'or (rappel)

Un seul vermillon porteur par visuel · la serif porte, le mono recule · alignements porteurs de sens · retours à la ligne à la main · beaucoup d'air, jamais vide de sens · la lueur ne vit que sur nocturne · filets pour séparer et fermer · ni cadre à ombre dure, ni arrondi, ni trame · coins libres · images IA sans faux texte · **toujours vérifier le rendu à l'œil avant de livrer.**
