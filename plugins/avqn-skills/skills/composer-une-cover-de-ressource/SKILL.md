---
name: composer-une-cover-de-ressource
description: >-
  À utiliser dès qu'une ressource Autonomes (tuto, fiche, cheatsheet, exercice) a besoin
  de sa cover (vignette), même si Manu dit seulement « la cover de la ressource », « la
  vignette du tuto » ou « l'image de la fiche ». Compose un HTML 1280×720 puis un PNG via la Médiathèque. Porte le
  système visuel complet (rampes de ciel par type de ressource, 9 recettes de composition,
  banque de glyphes au trait, tuiles logos) et le pipeline : 3 variantes, validation de
  Manu, PNG versé à la médiathèque et ajouté à la ressource dans Autonomes. NE COUVRE PAS
  les covers des articles du blog (composer-une-cover-d-article) ni les images du corps
  d'une ressource (illustrer-une-ressource).
---

# Covers de ressources Autonomes

Ce skill fabrique les vignettes des ressources du site Autonomes. Chaque cover est un fichier HTML autonome de 1280×720 exactement (div#cover), composé selon le système ci-dessous, puis exporté en PNG.

## La sortie attendue

- Un fichier HTML autonome par variante : div#cover de 1280×720, overflow hidden, aucune dépendance sauf les URLs de logos.
- 3 variantes par demande, toujours, présentées côte à côte pour que Manu choisisse.
- Après validation : PNG 1280×720 versé à la médiathèque (MCP) puis ajouté à la ressource concernée dans Autonomes.

## Ressource ou article ?

Le blog a ses propres covers, et les deux systèmes visuels n'ont rien en commun (ciels
dégradés et glyphes au trait ici, ciel bleu et Anton là-bas). Si Manu dit seulement « fais
la cover » sans dire de quoi, poser la question en une ligne avant de composer.

## Le système en une phrase

Deux axes indépendants : la RAMPE (le dégradé de ciel en fond) dit le type de la ressource ; la RECETTE (la composition posée dessus) dit ce que montre le contenu. Toutes les combinaisons sont valides, sauf le duel qui coupe le ciel en deux.

## Invariants — jamais négociables

- Canvas 1280×720, dégradé de fond à 165°, grain overlay par-dessus tout (opacité .35 sur rampe claire, .40 sur rampe sombre — voir le bloc grain dans n'importe quel exemple).
- Tuile logo : 148×148 px, rayon 26, fond crème #FBF8F1, ombre 0 6px 26px rgba(10,16,32,.35), logo 78 px centré aux couleurs d'origine. Un logo par tuile, jamais de texte dans une tuile, 4 tuiles maximum par cover. Tuile réduite (coin de fenêtre, feuille) : 134 ou 109 px, logo 76 ou 64 px.
- Le soleil est toujours #F5B326. Quatre motifs autorisés : plein dans un coin, demi sur l'horizon, arc au trait, halo. Un seul soleil par cover.
- Contraste : motifs au trait crème (#FBF8F1 / rgba(251,248,241,.85)) sur rampe sombre ; trait navy #16233F sur rampe claire. Accents jaunes #F5B326 sur sombre, ocre #E8763A sur clair.
- Étoiles : points de 10 px crème (opacité .4–.55), 2 maximum, uniquement sur rampe sombre, dans le tiers haut.
- Texte lisible : mono uniquement (ui-monospace, Menlo), et seulement dans les recettes terminal, prompt, cheatsheet. Jamais de phrase entière hors prompt. Jamais d'emoji, jamais de photo, jamais d'autre dégradé que la rampe, jamais de motif non documenté ici.

## La palette

| Couleur | Hex | Rôle |
|---|---|---|
| Navy | #16233F | le trait, l'autorité (fond profond : #14213D) |
| Jaune | #F5B326 | le soleil, la vie, les accents sur sombre |
| Ocre | #E8763A | l'accent sur clair, les chevrons |
| Aube | #6E8FE8 | l'IA en arrière-plan |
| Rose | #C95B7E | le ciel qui bascule |
| Prune | #5D3E6B | transition des ciels sombres |
| Crème | #FBF8F1 | la matière : tuiles, fenêtres, traits sur sombre |

## Les rampes — le type donne le ciel, sans exception

Le type est le tag `type:` de la ressource dans Autonomes. Il y en a quatre, fermés.

| Type | Ce que le lecteur fait | Rampe | CSS exact |
|---|---|---|---|
| Tuto | il suit un guide | Nuit d'aube | linear-gradient(165deg,#16233F 0%,#5D3E6B 60%,#C95B7E 100%) |
| Fiche | il comprend un contexte | Plein jour | linear-gradient(165deg,#F5B326 0%,#F8C64B 45%,#FBEBC4 100%) |
| Cheatsheet | il retrouve un élément | Aube bleue | linear-gradient(165deg,#16233F 0%,#3D5A9E 55%,#6E8FE8 100%) |
| Exercice | il s'entraîne | Couchant ocre | linear-gradient(165deg,#E8763A 0%,#C95B7E 55%,#5D3E6B 100%) |

Cinquième rampe, en réserve, sans type attaché : Crépuscule, linear-gradient(165deg,#C95B7E 0%,#8A4468 45%,#16233F 100%). Ne pas l'utiliser pour une ressource sans décision de Manu.

Rampes sombres : nuit d'aube, aube bleue, couchant ocre (et crépuscule). Rampe claire : plein jour.

Les anciens noms (pastille, parcours, modèle, retour d'expérience) ne sont plus des types : une pastille est une fiche, un parcours est un tuto, un modèle à copier est une fiche, un retour d'expérience est un article de blog, pas une ressource.

## Les recettes — le contenu donne la composition

| Recette | Quand | Master à copier |
|---|---|---|
| La chaîne | des services à installer dans l'ordre (tuto de setup) | examples/chaine.html |
| Le terminal | des commandes à taper, un geste précis | examples/terminal.html |
| Le pipeline | des services connectés entre eux (workflow, stack) | examples/pipeline.html |
| Le solo | un seul outil au centre (découverte, test, bilan) | examples/solo.html |
| La pile | un document à copier (template, checklist) | examples/pile.html |
| La cheatsheet | des raccourcis ou commandes à retenir (la composition naturelle du type cheatsheet, mais pas la seule) | examples/cheatsheet.html |
| Le prompt | un prompt à copier, une technique de formulation | examples/prompt.html |
| La scène au trait | une notion, un fonctionnement — le cœur du catalogue | examples/scene-agent.html, examples/scene-routines.html |
| Le duel | deux outils ou approches face à face | examples/duel.html |

IMPORTANT : partir du fichier exemple et remplacer le contenu (logos, lignes de commande, glyphes). Ne pas réinventer la géométrie — les cotes exactes de chaque recette sont dans references/recettes.md.

## L'arbre de décision

1. Quel type ? → la rampe (table ci-dessus, non négociable).
2. Que montre le contenu ? → la recette (table ci-dessus).
3. Départages quand deux recettes se disputent le sujet :
   - Commandes ET setup à la fois : ce qu'on voit à l'écran gagne — la commande tapée → terminal ; le chemin parcouru → chaîne.
   - Un outil ET un concept : l'outil est le héros → solo ; l'idée est le héros → scène au trait.
   - Hésitation persistante entre deux recettes → c'est un bon plan de variantes : faire les deux.

## Les scènes au trait (concepts)

Pour les notions sans outil central (gérer le contexte, les connecteurs, un agent, un RAG…) : des objets du quotidien reconnaissables, dessinés au trait — JAMAIS de géométrie abstraite, jamais de logo dans une scène.

- Glyphe héros : 200 à 290 px. Satellites : 110 à 135 px, 2 maximum. Reliés par pointillés crème (5 px, tirets 16/32) ou connecteurs jaunes.
- Un seul accent de couleur par glyphe (aiguilles, broches, coche, remplissage) : jaune sur sombre, ocre sur clair.
- Épaisseur visuelle du trait ≈ 8 px au master. Les glyphes sont des SVG en viewBox 24 : stroke-width = 8 × 24 ÷ largeur affichée (ex. héros de 205 px → 0.95 ; satellite de 128 px → 1.5).
- La banque de 22 glyphes prêts (code SVG complet) : references/glyphes.md. Elle s'étend librement : tout objet dessinable en formes simples, mêmes conventions.
- Raconter une petite histoire lisible : la loupe fouille le manuel → bulle réponse (RAG) ; soleil → horloge → lune (routines) ; messages → jauge qui se remplit (contexte) ; chef à point jaune → escouade en pointillés (sous-agents).

## Tuiles et logos — l'ordre des sources

1. cdn.simpleicons.org/SLUG en URL directe (couvre la plupart des outils : claude, github, vercel, n8n, notion, airtable, make, obsidian, gmail, googlecalendar…).
2. Le dossier Logos de la médiathèque (MCP).
3. Chercher le logo sur internet, le verser dans le dossier Logos de la médiathèque, puis l'utiliser depuis là.
4. Dernier recours, le monogramme : la même tuile crème avec la lettre initiale de l'outil — Schibsted Grotesk 800, navy #16233F, ≈ 70 px (import : fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@800).

## Safe-zone et échelle

- Composition ancrée au centre, positions en % ; seuls les motifs de bord s'ancrent en px (soleils de coin, horizons, la diagonale de la chaîne).
- Rien d'essentiel à moins de 5 % des bords (64 px). Les seuls débordements voulus : soleil plein de coin, halo.
- Le document de travail « Atelier Covers » est coté à l'échelle 400×225 : toute cote atelier × 3,2 = master.

## Le pipeline — à dérouler à chaque demande

1. **Brief.** Il faut : le titre de la ressource, son type (tuto, fiche, cheatsheet, exercice), et ce que montre le contenu (services impliqués, commandes, concept…). S'il manque un de ces trois éléments, poser UNE question, pas plus.
2. **Composer.** Arbre de décision → rampe + recette. Copier le master de la recette, remplacer le contenu. Logos selon l'ordre des sources.
3. **Trois variantes, toujours.** Jamais trois fois la même chose : si la recette est évidente, varier la composition (autre motif de soleil, autre disposition, autre scène) ; si deux recettes se disputaient le sujet, en faire une chacune. Nommer variante-a.html, variante-b.html, variante-c.html et les présenter côte à côte.
4. **Validation.** Manu choisit ou demande des retouches — retoucher la variante choisie, ne pas repartir de zéro.
5. **Livrer.** Exporter le div#cover en PNG 1280×720 via le MCP médiathèque (génération/hébergement des images), puis ajouter l'image à la ressource concernée dans Autonomes. Conserver le HTML source pour les retouches futures.

## Checklist avant de présenter

- [ ] 1280×720 exact, overflow hidden, grain présent à la bonne opacité
- [ ] la rampe correspond au type
- [ ] tailles système : tuiles 148, héros 200–290, satellites 110–135, traits ≈ 8 px, étoiles 10 px (max 2, sombre uniquement)
- [ ] contraste : crème + jaune sur sombre / navy + ocre sur clair
- [ ] un seul soleil ; aucun texte hors mono ; aucun logo dans une scène
- [ ] rien de rogné involontairement aux bords
- [ ] trois variantes réellement différentes

## Boucle d'amélioration

Quand Manu corrige une cover, la correction va dans ce fichier si c'est une règle du
système, dans references/recettes.md si c'est une cote, dans examples/ si la cover
réussie mérite de devenir un master de plus.
