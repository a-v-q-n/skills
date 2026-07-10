---
name: creer-une-cover-ressource
description: >-
  À utiliser dès qu'on crée la bannière de couverture d'une ressource AVQN (lead magnet, guide, tuto,
  cheatsheet) : une image 16:9 1280×720 portée par une accroche-objectif qui dit ce qu'on va apprendre,
  lisible sans le titre. Porte la doctrine de l'accroche (formes + tests de relecture), le principe
  climat + objet central, et le gabarit cheatsheet. Charge le socle produire-un-visuel-avqn pour la
  charte et le rendu. NE COUVRE PAS les visuels de posts (creer-un-visuel-social), le contenu écrit de
  la ressource (ecrire-une-ressource) ni l'assemblage PDF (creer-un-pdf).
---

# Créer la bannière d'une ressource

Composer la **bannière de couverture** d'une ressource — le visage d'un lead magnet, d'un guide, d'un tuto ou d'une cheatsheet dans l'espace ressources. Une seule chose la porte : une **accroche-objectif** qui dit clairement ce qu'on va apprendre.

> **Source unique : [styleguide.avqn.ch/doctrine/ressources.md](https://styleguide.avqn.ch/doctrine/ressources.md).**
> Le format, la doctrine de l'accroche (formes + tests) et le climat + objet y vivent ; ce skill
> en est le rappel opérationnel — en cas de doute, le styleguide fait foi.

**Commencer par charger `produire-un-visuel-avqn`.** La charte (palette, typo, ambiances, gestes, tokens) et l'acte de base (composer → rendre via `media_render_html` → vérifier à l'œil) viennent du socle. Ce skill ajoute le format, la doctrine de l'accroche et les objets.

## Format

**16:9, 1280 × 720, unique.** Rendre via `media_render_html`, puis attacher comme cover. La card recadre légèrement : garder l'accroche et les éléments-clés dans des **marges de sécurité d'environ 8 %** sur chaque bord.

## L'accroche : un objectif pédagogique, lisible seul

**L'accroche dit clairement ce qu'on va apprendre, sans avoir besoin du titre.** C'est la phrase qu'on mettrait sur le programme d'une formation. Elle nomme toujours son sujet, de préférence en **mode action** : « Savoir utiliser le CLAUDE.md. » · « Comprendre les permissions de Claude Code. » · « Les 4 principes pour bien formuler sa demande à l'IA. » · « Claude Code en 20 minutes. »

Formes recommandées (combinables) :

1. **Le verbe d'apprentissage** — « Savoir… », « Comprendre… », « Bien… » + le sujet.
2. **Le périmètre chiffré** — « Les N … pour … », « N commandes, N gestes ».
3. **La durée réelle** — « X en N minutes. » (correspond à la réalité de la ressource).
4. **Le libellé descriptif** — « Sujet : ce que c'est. »

**La clarté prime sur l'originalité.** L'accroche peut être proche du titre de la ressource ; on évite seulement le doublon mot pour mot, en apportant l'angle d'action ou le chiffre que le titre n'a pas. Une seule phrase, point final.

### Les deux tests de relecture (obligatoires)

- **Test de clarté** — si on ne comprend pas de quoi parle la ressource en lisant seulement l'image, l'accroche est ratée.
- **Test anti-slogan** — si la phrase pourrait vendre autre chose que cette ressource, c'est un slogan, on jette. Interdits : antithèses (« Vous décrivez. Il construit. »), promesses émotionnelles (« ne plus en avoir peur »), maximes (« La compétence, c'est de savoir décrire. »), formules elliptiques qui supposent le titre (« 4 principes, un avant / après. »), formules génériques (« Tout ce que vous devez savoir »).

## L'accroche est le seul texte

Pas de sous-titre, pas de kicker, pas de label de pilier/type, **pas de logo** (coins libres, comme dans le socle). L'unique exception : le **badge CHEATSHEET** du gabarit cheatsheet (voir plus bas). L'unique accent vermillon du visuel (règle du socle) est porté par un **segment de l'accroche en italique vermillon** (le mot-clé ou le chiffre), ou par un détail vermillon de l'objet — jamais les deux avec force.

## Le climat + l'objet central

Deux leviers donnent à la fois cohérence et variété : une **ambiance** du socle en fond, et un **objet central** qui varie.

**L'ambiance** (les deux du socle) suit la nature du sujet :
- **Nocturne** (encre + lueur) — sujets techniques : code, terminal, commandes, recette n8n.
- **Clair** (papier quadrillé) — concepts, fondations, pédagogie posée.

**L'objet central évoque la nature du contenu, pas seulement le sujet.** Deux ressources voisines ne portent pas le même objet si leur nature diffère.

| Nature du contenu | Objet central |
|---|---|
| Cours / tuto (défaut) | Fenêtre code/terminal, l'info-clé en accent vermillon |
| Le sujet est un fichier (CLAUDE.md, .env…) | Fiche document à onglet mono, lignes suggérées |
| Le sujet est une interaction (permissions, prompt…) | La boîte de dialogue elle-même, liseré vermillon, options |
| Automatisation n8n | Ligne de workflow + node encadré (icône collection `n8n-node`) |
| Comprendre / conceptuel | Accroche en escalier, mot-clé final en accent vermillon |
| Fondations | Type fantôme géant (initiale, sigle, glyphe : `>_`, `{ }`) partiellement hors cadre + filet vermillon |

Tout reste **on-charte du socle** : Instrument Serif porte l'accroche (Anton pour un chiffre/durée-choc), **un seul vermillon** porteur, filets pour séparer, **ni cadre à ombre dure ni arrondi**, coins libres. La liste d'objets s'étend quand un nouveau besoin de variété arrive — on documente alors **le contexte d'usage, pas l'exemple particulier**.

## Le gabarit Cheatsheet

Le type cheatsheet est le seul à porter son propre gabarit, parce que sa promesse — la densité de référence — mérite d'être visible, au point d'afficher un **badge de type** (l'unique exception à l'interdiction des labels).

- **Badge CHEATSHEET** en haut-gauche : pastille Geist Mono UPPERCASE, interlettrage large, sur aplat vermillon (la taille d'une pastille de card).
- **Plaque centrale** : l'accroche seule, en encre du fond (crème sur nocturne, encre sur clair), cadrée par un filet vermillon — pas de segment vermillon dans l'accroche ici (le vermillon est déjà pris par le badge). Comme le badge porte le type, l'accroche peut être plus courte (« Les commandes Claude Code. »).
- **Tapisserie pleine page atténuée** (opacité ~.4) qui évoque le contenu (touches de commandes, nodes, glyphes) mais reste en fond, neutre, sans vermillon. Laisser vide la zone sous le badge pour éviter la collision.

## Boucle & gabarits

1. Écrire l'accroche, passer les **deux tests**.
2. Choisir l'ambiance (nocturne/clair) et l'objet selon la nature du contenu.
3. Composer le HTML (partir du seed `templates/`), **retours à la ligne à la main**, un seul accent.
4. Rendre en 1280×720 via `media_render_html` (`wait_for` ~1600), **vérifier à l'œil**, corriger, re-rendre.
5. Attacher la cover à la ressource.

- `templates/cover-defaut.html` — le gabarit de départ clonable (16:9, ambiance + accroche + objet). Les autres natures se déclinent à partir de lui, documentées ci-dessus.
- `templates/CATALOG.md` — l'index des gabarits + comment en ajouter.

## Do / Don't (propres aux covers)

**Do** — une accroche-objectif qui nomme son sujet et se lit sans le titre · mode action quand c'est pertinent · les deux tests (clarté + anti-slogan) · un objet qui reflète la **nature** du contenu · marges de sécurité 8 % · icônes officielles n8n quand le sujet est un node.

**Don't** — accroche elliptique qui suppose le titre · doublon mot pour mot du titre · slogan, antithèse, maxime, promesse émotionnelle, formule générique · deux ressources voisines avec le même objet quand leur nature diffère · écrire le pilier, le type ou le niveau dans l'image (hors badge cheatsheet) · logo ou signature. *(Les interdits de DA — deuxième accent, ombre dure, arrondi, trame — vivent dans le socle.)*
