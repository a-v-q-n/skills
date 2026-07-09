# AVQN — Charte visuelle

**Le socle de tous les visuels AVQN.** Éditorial, chaud, aéré : fond papier écru ou encre profonde, un seul accent vermillon, la serif qui porte le message. International Typographic Style tempéré d'une chaleur analogique — beaucoup d'air, peu d'éléments par visuel, des alignements qui portent du sens.

Marché : indépendants de Suisse romande. Sujets : n8n, Claude, IA, automatisation.

Le langage est transverse : chaque recette (`creer-un-visuel-social`, `creer-une-cover-ressource`…) l'applique en ajoutant ses formats et ses gabarits. Pour une image IA : ce socle + `images-ia.md`.

---

## 1. Non négociables

1. **Contraste chaud** : encre `#211C17` sur papier `#FAF8F3`, ou l'inverse en nocturne. Jamais de blanc pur ni de noir pur.
2. **Un seul accent par visuel** : vermillon `#E0542B`, réservé au mot actif, au filet, à l'objet qui porte le sens. Jamais en aplat décoratif, jamais sur du texte long.
3. **La serif porte** : Instrument Serif en grand dit le message ; le reste (labels, appuis) recule en Geist / Geist Mono gris.
4. **Alignements porteurs de sens** : la position dit quelque chose (épine gauche, escalier d'accumulation, opposition). On aligne sur une ligne, une grille.
5. **Retours à la ligne à la main** : unités de sens gardées ensemble, jamais un mot seul en dernière ligne.
6. **32 px = plancher** : tout texte à l'écran fait au moins 32 px (base 1080). La discrétion vient du gris et du placement, jamais d'une taille minuscule.
7. **Coins libres** : pas de logo ni signature en coin. La DA suffit.
8. **Beaucoup d'air** : peu d'éléments, du vide maîtrisé. On respire, on ne remplit pas.

---

## 2. Modes clair / nocturne

| Mode | Fond | Texte | Usage |
|------|------|-------|-------|
| **Clair** (défaut) | papier quadrillé `#FAF8F3` | encre `#211C17` | la majorité des visuels |
| **Nocturne** | encre `#211C17` + lueur vermillon | crème `#FAF8F3` | emphase, technique, citation, variété en carrousel |

---

## 3. Palette

| Token | Hex | Rôle |
|-------|-----|------|
| `--paper` | `#FAF8F3` | fond clair, texte sur nocturne |
| `--ink` | `#211C17` | encre : texte/titres sur clair, fond nocturne |
| `--red` | `#E0542B` | vermillon, accent unique |
| `--grey` | `#7A726A` | secondaire sur clair (appuis, légendes) |
| `--greyd` | `#CBC4BA` | secondaire sur nocturne |
| `--filet` | `#E7E1D8` | filet de séparation (clair) |

---

## 4. Typographies

Quatre voix, une seule gamme. Toutes chargées depuis Google Fonts (`@import`).

- **Instrument Serif** (400 + italique) — hero, titre, corps. Ce qui **porte** le message. L'emphase = un fragment en **italique vermillon**.
- **Anton** (400, UPPERCASE) — l'accroche display condensée, la plus percutante ; le chiffre-choc. Réservé aux hooks.
- **Geist** (400/500/600) — l'appui : sous-titre, légende, phrase de contexte. Gris par défaut.
- **Geist Mono** (500/600, UPPERCASE, interlettrage large) — eyebrows et mentions : labels de catégorie, index de liste, crédits, noms de fichiers.

Échelle de référence (base 1080) : hero serif 140–190 · titre serif 90–130 · corps serif 56–80 · chiffre Anton 300–440 · eyebrow mono 32–40 · appui Geist 40–52. Chaque format réadapte. `text-wrap: balance` partout — jamais un mot seul en dernière ligne.

---

## 5. Les deux ambiances (fonds)

Chaque visuel pose l'une des deux.

- **Papier quadrillé** (clair) : fond `#FAF8F3`, quadrillage fin encre ~4 % à 46 px. Le papier millimétré écru de la marque.
- **Nocturne** (encre) : fond `#211C17`, **une lueur vermillon radiale** (ellipse décentrée à ~35 %/42 %, cœur `rgba(224,84,43,.18)` fondu à zéro), un quadrillage crème ~5 % à 120 px, et une **vignette douce** (radiale sombre aux bords). La lueur ne vit que sur nocturne — c'est la texture de l'encre.

Blocs CSS canoniques en §10.

---

## 6. Les gestes-signature

- **Eyebrow** : label Geist Mono UPPERCASE vermillon, précédé d'un **carré vermillon plein**, interlettrage large. Catégorie réelle (« Sous le capot », « Recette n8n »), jamais décorative.
- **Filet vermillon** : trait plein vermillon (~6 px, ~120 px de long) sous l'eyebrow ou comme séparateur porteur.
- **Titre à accent italique** : Instrument Serif encre (ou crème en nocturne), le fragment qui porte en **italique vermillon**.
- **Filet de séparation** : trait 1 px `#E7E1D8` (clair) ou crème 14 % (nocturne) entre les items d'une liste, sous une conclusion.
- **Duotone encre** : une photo posée en fond passe en niveaux de gris + voile encre `rgba(33,28,23,.5)` + vignette — le texte crème vit dessus.

---

## 7. Images IA

Direction unique : **« l'anticipation douce »** (`images-ia.md`). Photo cinématique 35 mm, mondes-couleurs, **un objet vermillon sémantique**, **jamais de texte dans l'image** — les mots vivent dans la mise en page. Une image générée se pose plein cadre en duotone (fond nocturne) ou en grand dans une mise en page hero. La génération passe par le MCP médiathèque (`media_generate_image`).

---

## 8. Icônes n8n (asset de marque partagé)

La collection média **n8n-node** (médiathèque) contient les icônes officielles (n8n, Gmail, Slack, Webhook, Anthropic, OpenAI, Postgres, Notion…). À utiliser telles quelles, posées sur une carte claire, dès qu'un node est le sujet. Logo officiel : `assets/n8n-logo.svg`. Les autres : `media_list_images(collection='n8n-node')`, sinon un glyphe monoline maison (trait 3.5–4 px, un carré vermillon = le node clé).

---

## 9. Formats — piloté par width/height

Un visuel n'a pas de format figé : il est piloté par `width`/`height` passés à `media_render_html`, alignés sur `--W`/`--H` du gabarit dans `:root`. **Chaque recette déclare les formats de son canal** (réseaux : 4:5 1080×1350, 1:1, 9:16, 16:9 lien · cover ressource : 16:9 1280×720).

Un gabarit en flux suit un changement de ratio proprement ; un gabarit à positionnement tenu demande d'ajuster quelques offsets, puis de re-rendre et **vérifier à l'œil**.

---

## 10. Tokens CSS canoniques

Source unique. Tout gabarit part de ce bloc.

```css
:root{
  --W:1080px; --H:1350px;                 /* format : voir §9 */
  --paper:#FAF8F3; --ink:#211C17; --red:#E0542B;
  --grey:#7A726A; --greyd:#CBC4BA; --filet:#E7E1D8;
  --serif:"Instrument Serif",serif; --display:"Anton",sans-serif;
  --sans:"Geist",sans-serif; --mono:"Geist Mono",monospace;
}
/* Charger : Instrument Serif(400+ital) · Anton · Geist(400,500,600) · Geist Mono(500,600) */

/* Ambiance CLAIRE : papier quadrillé */
.paper{
  background:
    repeating-linear-gradient(0deg, rgba(33,28,23,.04) 0 1px, transparent 1px 46px),
    repeating-linear-gradient(90deg, rgba(33,28,23,.04) 0 1px, transparent 1px 46px),
    var(--paper);
  color:var(--ink);
}

/* Ambiance NOCTURNE : lueur vermillon + quadrillage crème + vignette */
.night{
  background:
    radial-gradient(ellipse 82% 44% at 34% 42%, rgba(224,84,43,.18) 0%, rgba(224,84,43,.06) 46%, rgba(224,84,43,0) 78%),
    repeating-linear-gradient(0deg, rgba(250,248,243,.055) 0 1px, transparent 1px 120px),
    repeating-linear-gradient(90deg, rgba(250,248,243,.055) 0 1px, transparent 1px 120px),
    var(--ink);
  color:var(--paper);
}
.night::after{ /* vignette */
  content:""; position:absolute; inset:0; pointer-events:none;
  background:radial-gradient(ellipse 78% 74% at 50% 44%, transparent 52%, rgba(0,0,0,.36) 100%);
}

/* Gestes-signature */
.eyebrow{font-family:var(--mono);font-weight:600;font-size:34px;letter-spacing:.22em;
  text-transform:uppercase;color:var(--red);display:flex;align-items:center;gap:20px;line-height:1}
.eyebrow::before{content:"";width:18px;height:18px;background:var(--red);flex:none}
.filet{height:6px;width:120px;background:var(--red)}          /* filet vermillon */
.rule{height:1px;background:var(--filet)}                     /* séparateur clair */
.night .rule{background:rgba(250,248,243,.14)}               /* séparateur nocturne */
.acc{font-style:italic;color:var(--red)}                     /* accent serif */
```

---

## 11. Do / Don't

**Do** — un message par visuel · la serif porte, le mono recule · un seul vermillon porteur de sens · alignements signifiants · des filets pour séparer et fermer · beaucoup d'air · vérifier le rendu à l'œil avant de livrer.

**Don't** — blanc ou noir purs · plus d'un accent vermillon · vermillon décoratif · trame / halftone · cadres à ombre dure, arrondis, ombres floues lourdes · petits labels décoratifs · coupe de phrase au mauvais endroit · logo en coin · texte lisible dans une image IA.
