---
name: produire-un-visuel-avqn
description: >-
  À utiliser pour produire un visuel AVQN on-charte (image composée en HTML puis rendue en PNG),
  et comme socle chargé par les recettes visuelles (creer-un-visuel-social, creer-une-cover-ressource…).
  Porte la charte — palette chaude papier/encre, un seul vermillon, Instrument Serif qui porte,
  modes clair/nocturne, gestes-signature, tokens CSS — et l'acte de base : composer un HTML on-charte,
  rendre via le MCP médiathèque, vérifier à l'œil. Sert aussi seul pour un visuel sans canal dédié.
  NE COUVRE PAS les formats et gabarits d'un canal précis (réseaux, cover ressource — voir leur recette)
  ni l'assemblage multi-pages en PDF (creer-un-pdf).
---

# Produire un visuel AVQN

Composer un visuel **on-charte** et le rendre en image. Ce skill est le **socle** visuel d'AVQN : il porte le langage de la marque (la charte) et l'acte de base commun à tous les visuels — composer un HTML, le rendre en PNG, vérifier le résultat à l'œil. Les recettes visuelles (`creer-un-visuel-social`, `creer-une-cover-ressource`…) le chargent et n'ajoutent que leurs formats, leurs gabarits et leur doctrine. Il sert aussi directement pour un visuel qui n'a pas de canal dédié.

## La charte (le langage)

L'univers : éditorial, chaud, aéré. Papier écru `#FAF8F3` ou encre profonde `#211C17`, **un seul vermillon `#E0542B`** porteur de sens, **Instrument Serif** qui porte le message (accent en italique vermillon), **Anton** pour le hook display, **Geist / Geist Mono** pour les appuis et labels. Deux ambiances : **papier quadrillé** (clair, défaut) et **nocturne** (encre + lueur vermillon + vignette). Beaucoup d'air, peu d'éléments, des alignements qui portent du sens.

Le détail complet — palette, gamme typo, les deux ambiances, gestes-signature, tokens CSS canoniques, do/don't — vit dans **`references/charte-visuelle.md`**. **À respecter partout.**

## Rendu : MCP médiathèque

**Le rendu passe par le MCP médiathèque — le skill ne rend rien lui-même.** Le HTML composé (complet et autonome : fonts en `@import`, tout le CSS inline) est envoyé au rendu partagé ; le média produit atterrit dans la galerie et renvoie une URL.

- **Rendre** → `media_render_html` : `html` (le gabarit rempli), `width`, `height`, `wait_for` (ms — laisser fonts + fonds finir : **composés ~1500**, **hero avec image distante ~2600**), `name`, `tags`. Sortie PNG, renvoie l'URL galerie.
- **Nommer le livrable** → `media_update`. **Retrouver un média / les icônes n8n** → `media_list_images`.
- **Générer une image IA** → `media_generate_image` (photo : `references/images-ia.md` · schéma : `references/images-schema.md`).

## L'acte de base : composer → rendre → vérifier

1. **Cadrer le message** — une idée par visuel, un hook. Si le texte doit sonner AVQN, charger la voix (`ecrire-comme-manu`).
2. **Composer le HTML on-charte** — partir des tokens `:root` (charte §10), poser **une** ambiance (papier ou nocturne), les gestes-signature. **Retours à la ligne à la main**, un seul fragment en `.acc` (italique vermillon).
3. **Rendre** via `media_render_html` (`width`/`height` = les dimensions cibles, alignées sur `--W`/`--H`, `wait_for` adapté).
4. **Vérifier à l'œil** — charger l'image produite. Corriger débordements, veuves, alignements, contraste, la lueur nocturne. Re-rendre. **Cette étape n'est pas optionnelle.**
5. **Livrer** — ou nommer via `media_update`.

## Images IA — deux styles

Deux directions d'image générée, une par usage — générer via `media_generate_image`, puis poser l'URL dans la mise en page :

- **Photo** — « l'anticipation douce » (`references/images-ia.md`) : montrer un monde. Cinématique 35 mm, lieux contemporains, un objet vermillon sémantique, **jamais de texte dans l'image**. Se pose en grand dans une mise en page hero, ou plein cadre en duotone sur un fond nocturne.
- **Schéma** — la figure technique (`references/images-schema.md`) : expliquer une idée, un flux, un système. Mécanismes à l'encre sur papier crème, un vermillon porteur, **labels courts autorisés**, ni cadre ni cartouche.

## Composer et déléguer

- **Une recette charge ce socle en tête de corps** (« commencer par charger `produire-un-visuel-avqn` »), puis ajoute ses formats et gabarits.
- **PDF multi-pages** (carrousel, document illustré) → `creer-un-pdf` (mécanique d'assemblage).
- **Réseaux sociaux** (formats + catalogue de gabarits) → `creer-un-visuel-social`.
- **Bannière de ressource** (16:9, accroche-objectif) → `creer-une-cover-ressource`.

## Références

- `references/charte-visuelle.md` — le langage : palette, typo, ambiances, gestes, tokens CSS, do/don't.
- `references/images-ia.md` — la direction d'image « anticipation douce » (photo).
- `references/images-schema.md` — la direction d'image « figure technique » (schémas explicatifs).
- `assets/n8n-logo.svg` — logo n8n officiel (asset de marque ; les autres icônes via `media_list_images(collection='n8n-node')`).

## Règles d'or (rappel)

Un seul vermillon porteur par visuel · la serif porte, le mono recule · alignements porteurs de sens · retours à la ligne à la main · beaucoup d'air, jamais vide de sens · la lueur ne vit que sur nocturne · ni cadre à ombre dure, ni arrondi, ni trame · coins libres · images photo sans texte, schémas aux labels courts · **toujours vérifier le rendu à l'œil avant de livrer.**
