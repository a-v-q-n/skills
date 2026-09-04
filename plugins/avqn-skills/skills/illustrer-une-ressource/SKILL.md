---
name: illustrer-une-ressource
description: >-
  À utiliser pour fabriquer les images du corps d'une ressource Autonomes (tuto, fiche,
  cheatsheet, exercice) : une maquette qui montre un élément d'interface, un schéma qui
  explique un concept, ou une capture d'écran fournie par Manu à enrichir (cadre, flèche,
  numéro, mot, masque). Même s'il dit seulement « il faut une image dans la fiche », « fais-moi
  le schéma du tuto », « annote cette capture » ou « refais les images de la cheatsheet ».
  Pour une ressource Autonomes, jamais pour une vidéo. Porte la
  palette papier d'Autonomes, les trois gabarits HTML, le rendu via la Médiathèque et le
  contrôle visuel obligatoire. Chargé par creer-une-ressource à l'étape des
  images. NE COUVRE PAS la cover (composer-une-cover-de-ressource), les assets vidéo Contentos
  (fabriquer-les-assets) ni la génération d'images par IA.
couche: recette
moment: >-
  Les images du corps : maquette, schéma, capture annotée — palette papier, gabarits HTML, rendu
  Médiathèque.
famille: contenu-autonomes
---

# Illustrer une ressource

Une image dans une ressource sert à une chose : montrer ce que le texte ne devrait pas avoir à décrire. Le socle `ecrire-mes-ressources` demande une image par écran dans un tuto et un schéma à la place d'un paragraphe d'explication. Ce skill fabrique ces images, dans le même code couleur que les covers, sur fond papier.

Trois modes, un gabarit HTML par mode, un seul pipeline : composer le HTML, le rendre en PNG via la Médiathèque, regarder le résultat, corriger, livrer l'URL.

## Les trois modes

| Mode | Quand | Gabarit |
|---|---|---|
| **Maquette d'interface** | montrer un élément d'écran en général (une barre latérale, une modale, un menu déroulant), sans capture réelle | `assets/maquette.html` |
| **Schéma de concept** | expliquer comment des choses s'articulent (un fichier lu par plusieurs projets, un flux entre services, avant/après) | `assets/schema.html` |
| **Capture annotée** | Manu fournit une capture d'écran réelle et il faut dire où regarder, dans quel ordre, quoi cacher | `assets/capture.html` |

Le choix est rarement ambigu : s'il y a une capture, c'est le mode 3 ; s'il faut montrer un écran qui n'existe pas encore ou qui vaut pour tous les outils, c'est la maquette ; s'il n'y a pas d'écran du tout, c'est un schéma. Pas de génération d'image par IA : les trois modes couvrent tout ce qu'une ressource Autonomes montre, et une image générée ne tient jamais la palette.

## Ce qui ne change jamais

- **Le papier.** Fond crème #FBF8F1 avec le quadrillage discret, pour les maquettes et les schémas. Une capture garde son propre fond.
- **La palette** de `references/palette.md` : navy pour le trait et le texte, ocre pour ce qu'il faut voir, sable pour le contenu muet, blanc pour les surfaces. Rien d'autre.
- **Le format.** Maquettes et schémas en 1600×900. Une capture garde ses dimensions d'origine (viewport = taille de l'image) ; si elle dépasse 2000 px de large, la recadrer d'abord sur la zone utile avec `media_crop`.
- **Une seule chose à voir par image.** Un cadre ocre, ou une flèche, ou un héros de schéma. Si deux éléments doivent être vus, ce sont deux images, ou un ordre numéroté.
- **Pas de texte qui raconte.** Les mots dans l'image sont des noms (un libellé de bouton, un chemin de fichier, un nom de projet), jamais une phrase d'explication : la phrase est dans la caption, écrite par le socle.
- **Pas de vraie interface reproduite avec de fausses données.** Une maquette a un nom d'entreprise fictif (« Acme »), des barres de remplissage pour le contenu, aucune marque. Une capture réelle masque toute donnée personnelle (nom, email, adresse, montant) avec un `.masque`.
- **L'alt et la caption existent déjà**, écrits dans le fichier de travail par le socle. L'image doit leur correspondre ; si l'image change ce qu'on montre, l'alt change avec.

## Le vocabulaire des annotations (capture et maquette)

- `.cadre` : ce qu'il faut voir. Un par image, deux au maximum s'ils sont numérotés.
- `.numero` : l'ordre des gestes, quand l'étape du tuto en enchaîne plusieurs sur le même écran. Cercle ocre, chiffre mono crème, posé à gauche ou au-dessus de l'élément, jamais dessus.
- `.fleche` : un mouvement (glisser, aller de ce champ à ce bouton). Pas pour « regarde ici » : c'est le rôle du cadre.
- `.texte` : un mot ou un libellé posé à côté (« Add README sur On »). Jamais une phrase.
- `.masque` : un rectangle sable qui cache une donnée personnelle.
- `.etiquette` (maquette) : le nom de l'élément en mono capitales ocre, relié au cadre par un fil.

## Pipeline

1. **Lire le brief** : dans le plan validé de la ressource, chaque image attendue est décrite (quel écran, quel élément, quel schéma) avec son alt et sa caption. S'il manque l'un des trois, poser une question, pas plus. Pour une capture, récupérer le fichier de Manu (pièce jointe ou URL) et le déposer dans la Médiathèque (`media_upload` en base64, ou `media_request_upload` puis `media_finalize_upload` pour un gros fichier) afin d'avoir une URL publique et ses dimensions (`media_get_image`).
2. **Choisir le mode** et copier le gabarit correspondant. Ne pas réinventer la géométrie : remplacer le contenu, garder les classes, les épaisseurs et les couleurs.
3. **Composer.** Maquette : construire l'écran avec les composants du gabarit (nav, cartes, barres), poser le cadre et l'étiquette. Schéma : un héros, deux ou trois satellites au plus, des connecteurs, les glyphes de la banque du skill covers. Capture : mettre l'image en fond, poser les annotations en px.
4. **Repérer sur une capture.** Les coordonnées ne se devinent pas. Faire un premier rendu avec `.grille` en `display:block` (quadrillage de 100 px numéroté), le regarder avec `media_view_image`, lire les coordonnées de l'élément, puis remettre la grille en `display:none`.
5. **Rendre** avec `media_render_html` (width et height = ceux du gabarit ou de la capture, `wait_for` 1500 ms pour la police, `name` = `<slug-ressource>-<n>-<sujet>`, `tags` = `["autonomes", "<slug-ressource>"]`, format png).
6. **Regarder le résultat** avec `media_view_image`. C'est obligatoire : un cadre décalé de 20 px, une police non chargée, un texte qui déborde, ça ne se voit pas dans le HTML. Corriger et re-rendre jusqu'à ce que l'image montre exactement ce que l'alt décrit.
7. **Livrer** à Manu l'URL publique de chaque image avec, en une ligne, ce qu'elle montre. Une variante par image ; en proposer une seconde seulement si le brief hésitait entre deux façons de montrer. Conserver le HTML source dans le dossier de travail de la ressource pour les retouches.

Quand une ressource entière est à illustrer (« refais les images de la cheatsheet »), traiter les images dans l'ordre des pages, rendre et regarder chacune, et présenter le lot en fin de série plutôt qu'une par une.

## Checklist avant de rendre la main

- [ ] Le bon mode pour ce qu'il y a à montrer ; pas d'image générée par IA
- [ ] Palette papier respectée : navy, ocre, sable, blanc, crème ; pas de rouge, de vert, de dégradé, de logo réel
- [ ] Une seule chose à voir, cadrée en ocre ; les numéros seulement si l'ordre compte
- [ ] Aucune phrase dans l'image, seulement des noms ; aucune donnée personnelle visible sur une capture
- [ ] Police chargée, rien qui déborde, rien de rogné aux bords (marge de 60 px sur une maquette ou un schéma)
- [ ] Le rendu a été regardé, pas seulement généré
- [ ] L'image correspond à l'alt et à la caption du fichier de travail
- [ ] Nom et tags posés dans la Médiathèque, HTML source conservé

## Boucle d'amélioration

Quand Manu corrige une image (trop chargée, mauvais cadrage, un mot en trop), chercher la règle qui aurait évité la correction et l'ajouter ici ou dans le gabarit. Les gabarits sont la mémoire du style : une correction qui vaut pour toutes les images se fait dans le gabarit, pas dans l'image.
