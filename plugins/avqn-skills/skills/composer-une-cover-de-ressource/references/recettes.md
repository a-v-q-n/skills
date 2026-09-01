# Les 9 recettes : cotes master (1280×720)

Toujours partir du fichier examples/ correspondant. Les cotes ci-dessous servent aux retouches.

## 1 · La chaîne (examples/chaine.html)
- Soleil plein : cercle 352 px, coin bas gauche (left -83, bottom -102), opacité .92.
- Diagonale : pointillé crème 5 px (tirets 19/38), rotation -16°, origin left center, de (227, 493), longueur 659.
- 2 à 4 tuiles 148 px montant le long de la diagonale : (154, 419) → (474, 330) → (794, 240). Espacement horizontal 320, élévation 89-90 par pas.
- La première tuile part du bas gauche, la dernière vise le coin haut droit.

## 2 · Le terminal (examples/terminal.html)
- Fenêtre crème 690 px de large, rayon 26, ombre 0 19px 58px, centrée à (50%, 54%).
- Barre navy : padding 26/32, trois points de 22 px rgba(245,239,226,.4).
- Corps : mono 40 px weight 600 navy, 3 lignes max, chevron › ocre, padding 32/45, gap 16.
- Tuile 134 px chevauchant le coin haut droit : left calc(50% + 230px), top 170.

## 3 · Le pipeline (examples/pipeline.html)
- Ligne d'horizon : 5 px rgba(245,179,38,.55) à bottom 96.
- Demi-soleil 90×45 posé sur l'horizon, du côté resté libre (right ou left 83).
- 2 à 4 tuiles 148 px centrées à (50%, 46%), connecteurs jaunes 77×5, gap 35.

## 4 · Le solo (examples/solo.html)
- Horizon 5 px à bottom 109 ; arc 416×208 (border 5 px, border-bottom none) posé sur l'horizon, centré.
- Tuile unique 148 px à (50%, 47%) — elle chevauche l'arc d'environ 30-50 px (le soleil levant).
- Rampe sombre : halo radial 544 px rgba(245,179,38,.4) derrière la tuile, arc jaune. Rampe claire : pas de halo, arc et horizon en navy rgba(22,35,63,.4-.5).

## 5 · La pile (examples/pile.html)
- Bloc 480×346 centré à (50%, 52%). Trois feuilles rayon 26 : #EFE8D8 rotate(-7°) translate(-32,13) ; #F5EFDF rotate(-3°) translate(-13,6) ; #FBF8F1 devant.
- Feuille avant : padding 51, lignes factices h26 rayon 13 (rgba(22,35,63,.16/.12/.12), largeurs ~294/346/205). Jamais de vrai texte.
- Tuile 109 px agrafée au coin haut droit (right -42, top -42), logo 64.

## 6 · La cheatsheet (examples/cheatsheet.html)
- Touches façon clavier : padding 26/38, rayon 19, fond crème, mono 37 px weight 600 navy, ombre plate 0 8px 0 rgba(10,16,32,.45), white-space nowrap.
- 4 à 6 touches sur deux rangées (gap 32/35), la seconde décalée de 83 px. Tokens courts uniquement.

## 7 · Le prompt (examples/prompt.html)
- Barre de saisie crème 806 px, rayon 32, padding 42/51, centrée à (50%, 52%).
- Chevron › ocre 42 px, texte mono 40 px weight 600 navy (3 à 5 mots du prompt), curseur bloc ocre 26×48.
- Tuile 134 px du modèle visé chevauchant le coin : left calc(50% + 307px), top 237.

## 8 · La scène au trait (examples/scene-agent.html, examples/scene-routines.html)
- Héros 200–290 px, satellites 110–135 px (2 max), pointillés crème 5 px (tirets 16/32).
- Voir SKILL.md section scènes + references/glyphes.md pour la banque.
- Compositions éprouvées : orbite (cercle dashed 474 px, héros au centre, satellites sur le cercle) ; frise (satellite — pointillé — héros — pointillé — satellite, sur ligne d'horizon) ; jauge (messages qui tombent dans une jauge 576×83 remplie à ~78% en jaune) ; couches (3 cartes au trait 486×106 empilées décalées, celle du milieu en jaune) ; hiérarchie (héros en haut, pointillés en éventail vers 3 petits carrés).

## 9 · Le duel (examples/duel.html)
- Deux demi-ciels (voir references/rampes.md), trait vertical crème 6 px, pastille vs 115 px.
- Chaque camp : une tuile 148 px (outil) OU un glyphe 205 px (approche), centré à (25%, 46%) et (75%, 46%). Jamais tuile d'un côté et glyphe de l'autre sans raison.
- Étoiles côté nuit uniquement.
