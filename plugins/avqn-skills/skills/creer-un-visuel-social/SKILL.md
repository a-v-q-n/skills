---
name: creer-un-visuel-social
description: >-
  Produit les assets visuels des réseaux sociaux AVQN (LinkedIn, Threads, Instagram) : formats du
  feed / stories / aperçu de lien, catalogue de gabarits (statement, manifeste, chiffre, liste,
  citation, terminal, carrousel-cover, image-éditorial) et carrousel PDF. Charge le socle
  produire-un-visuel-avqn pour la charte et le rendu. À utiliser dès qu'on crée un visuel de post,
  une slide, une couverture de carrousel, une stat/citation illustrée ou tout asset image destiné aux
  réseaux sociaux d'AVQN. NE COUVRE PAS la vidéo, les bannières de ressources (creer-une-cover-ressource)
  ni l'assemblage PDF lui-même (creer-un-pdf).
---

# Créer un visuel pour les réseaux sociaux

Composer les visuels de posts AVQN — statements, chiffres, listes, citations, posts techniques, carrousels — déclinés sur LinkedIn (en tête), Instagram et Threads.

**Commencer par charger `produire-un-visuel-avqn`.** La charte (palette chaude, Instrument Serif, modes clair/nocturne, gestes-signature, tokens CSS) et l'acte de base (composer un HTML on-charte → rendre via `media_render_html` → vérifier à l'œil) viennent du socle. Ce skill ajoute le spécifique réseaux : les **formats**, le **catalogue de gabarits** et le **carrousel**.

## Boucle de production

1. **Cadrer le message** — une idée par visuel, le hook (résultat brut ou objection nommée). Charger la voix si le texte doit sonner AVQN (`ecrire-comme-manu`).
2. **Choisir un gabarit** dans `templates/CATALOG.md`, d'après la **forme du contenu** (statement, manifeste, chiffre, liste, citation, terminal, carrousel-cover, image-éditorial).
3. **Remplir le texte** — prendre le `.html`, remplacer les placeholders, **retours à la ligne à la main**, un seul fragment en `.acc`. Pour un format ≠ natif, régler `--W`/`--H` dans `:root` sur les dimensions cibles.
4. **Rendre** via `media_render_html` (`width`/`height` = les dimensions du format, `wait_for` adapté).
5. **Vérifier à l'œil** l'image produite, corriger débordements/veuves/alignements/contraste, re-rendre.
6. **Livrer** l'image, ou assembler un **carrousel PDF** (voir plus bas).

## Formats & multi-réseaux

> **Source unique : [styleguide.avqn.ch/doctrine/formats-sociaux.md](https://styleguide.avqn.ch/doctrine/formats-sociaux.md).**
> Les formats, règles d'affichage et familles de composition du support social y vivent ; ce
> tableau en est le rappel opérationnel — en cas de doute, le styleguide fait foi.

Le format se règle en passant `width`/`height` à `media_render_html` **et** en alignant `--W`/`--H` du gabarit sur ces mêmes dimensions.

| Format | Dimensions | Usage |
|--------|------------|-------|
| **4:5 vertical** | 1080 × 1350 | **défaut**, portée max (LinkedIn, IG portrait, Threads) |
| **1:1 carré** | 1080 × 1080 | feed universel |
| **9:16 vertical** | 1080 × 1920 | stories / couverture verticale |
| **16:9 horizontal** | 1200 × 627 | aperçu de lien |

Le catalogue indique, par gabarit, le format natif et ceux qui suivent proprement (les gabarits en flux reflowent seuls ; ceux à positionnement tenu demandent d'ajuster quelques offsets, puis de re-rendre et vérifier à l'œil).

## Carrousel → creer-un-pdf

LinkedIn rend un PDF multi-pages comme un carrousel navigable. **Slide 1 = `social-carrousel-cover`** ; slides suivantes piochées au catalogue en **alternant clair / nocturne** (c'est ce qui donne le rythme). Rendre chaque slide en 4:5 via `media_render_html` (récupérer les URLs), puis **déléguer l'assemblage à `creer-un-pdf`** (`media_create_pdf` dans l'ordre). Ce skill dessine les slides ; la mécanique du PDF vit dans `creer-un-pdf`.

## Références & gabarits

- `templates/CATALOG.md` — l'index des gabarits + comment en ajouter.
- `templates/*.html` — les gabarits, autonomes (tokens de la charte inline).
- `examples/` — un rendu de chaque gabarit + une planche-contact (`_planche-contact.png`) : la cible visuelle de référence.
- La **charte**, la **direction d'image IA** et l'**asset n8n** vivent dans le socle `produire-un-visuel-avqn`.

## Règles d'or (rappel)

Un seul vermillon porteur par visuel · la serif porte, le mono recule · retours à la ligne à la main · alterner clair / nocturne en carrousel · beaucoup d'air · **toujours vérifier le rendu à l'œil avant de livrer** — le détail dans le socle `produire-un-visuel-avqn`.
