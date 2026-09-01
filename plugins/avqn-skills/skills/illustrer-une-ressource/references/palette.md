# La palette « papier » des illustrations Autonomes

Les illustrations vivent dans le corps d'une page claire. Elles reprennent la palette du skill `composer-une-cover-de-ressource`, mais toujours sur sa **rampe claire** : jamais de ciel sombre dans le corps d'une ressource, la cover s'en charge.

| Rôle | Couleur | Hex |
|---|---|---|
| Le papier (fond) | crème | #FBF8F1 |
| Le quadrillage du papier | navy à 5,5 % | rgba(22,35,63,.055), pas de 40 px |
| Le trait, le texte, l'autorité | navy | #16233F |
| Le texte secondaire | navy à 60-75 % | rgba(22,35,63,.6) à .75 |
| L'accent, ce qu'il faut voir | ocre | #E8763A |
| La surface d'une fenêtre, d'une boîte | blanc | #FFFFFF |
| Le contenu « muet » (barres de remplissage) | sable | #E9E2D3, foncé #D6CDBA |
| Le masque d'une donnée personnelle | sable | #E9E2D3 |
| Un état actif, un bouton principal dans une maquette | navy plein, texte crème | #16233F / #FBF8F1 |
| Le soleil, un signal rare | jaune | #F5B326, au plus un par image, jamais pour signaler une erreur |

Ce qu'on ne fait pas : du rouge pour une erreur (l'ocre suffit), du vert pour un succès, un dégradé, une ombre portée dure, une photo, un emoji, un logo dans un schéma. Les logos d'outils n'apparaissent que dans une maquette, quand l'écran réel en montre un, et sous forme de tuile monogramme (un carré navy avec l'initiale) plutôt que du vrai logo.

## Typographie

- Texte d'interface et texte courant : Schibsted Grotesk (Google Fonts, `https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@400;500;700`), 400 pour le courant, 700 pour les titres. Le rendu attend le chargement de la police : passer `wait_for` à 1500 ms au minimum.
- Étiquettes, chemins, commandes, numéros : mono (`ui-monospace, Menlo, monospace`). Une étiquette d'élément est en capitales, lettrage espacé (.14em), ocre, précédée d'un carré ocre de 12 px.

## Traits et épaisseurs (au format 1600×900)

- Bord d'une fenêtre ou d'une boîte : 2 px navy (3 px pour le héros d'un schéma), rayon 10-12 px, ombre douce `0 10px 40px rgba(22,35,63,.08-.10)`.
- Cadre « ce qu'il faut voir » : 4 px ocre dans une maquette, 5 px ocre avec halo crème de 4 px sur une capture.
- Connecteur neutre : 4 px navy, pointillé 10/14, bouts ronds. Flèche de mouvement : 5 px ocre (7 px sur une capture), tête pleine ocre.
- Glyphe au trait : même épaisseur visuelle que sur les covers, ≈ 8 px : `stroke-width = 8 × 24 ÷ largeur affichée` (glyphe de 110 px → 1,75 ; de 80 px → 2,4 ; de 48 px → 4). C'est ce que font les gabarits. Un seul accent ocre par glyphe.

## Les glyphes

La banque de glyphes (24 objets en SVG viewBox 24) vit dans le skill `composer-une-cover-de-ressource`, fichier `references/glyphes.md`. La charger de là : mêmes codes, en remplaçant TRAIT par `#16233F` et ACCENT par `#E8763A`. L'étendre suit les mêmes règles : un objet du quotidien reconnaissable, des formes simples, un accent au plus.
