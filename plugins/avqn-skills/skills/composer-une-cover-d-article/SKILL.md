---
name: composer-une-cover-d-article
description: >-
  À utiliser dès qu'un article du blog Autonomes a besoin de sa cover (image d'en-tête,
  vignette de partage), même si Manu dit seulement « la cover de l'article », « la vignette
  du blog » ou « l'image pour le blog ». Compose un HTML 1600×900 puis un PNG via la
  Médiathèque. Un thème commun (ciel bleu #BFD7FF, noir, jaune, Anton, ombres
  dures, parfois le visage de Manu) et une composition improvisée à chaque fois : chaque
  cover est unique. Trois variantes, validation de Manu, PNG posé sur l'article.
  NE COUVRE PAS les covers des ressources (composer-une-cover-de-ressource) ni les images
  dans le corps de l'article.
---

# Covers des articles du blog

Une cover de blog se voit dans un fil, entre deux autres posts, par quelqu'un qui ne sait rien du sujet. Elle doit arrêter le pouce et se comprendre seule, comme une miniature d'Hugo Décrypte : gros, net, un mot qui saute. Et elle ne doit jamais ressembler à une cover de ressource (ciels dégradés, glyphes au trait, papier crème).

Le thème est fixe. La composition, non. Deux covers du blog ne se ressemblent pas : l'une a un mot énorme et rien d'autre, l'autre un visage qui prend la moitié, la troisième une capture penchée avec trois mots en coin. Ce skill donne les ingrédients et le goût ; il ne donne pas de gabarit à remplir.

## Article ou ressource ?

Les ressources ont leurs propres covers (`composer-une-cover-de-ressource`), et les deux
systèmes visuels n'ont rien en commun. Si Manu dit seulement « fais la cover » sans dire de
quoi, poser la question en une ligne avant de composer.

## Le thème (ce qui ne change pas)

- 1600×900, ciel bleu `#BFD7FF` avec un grain léger. Trois couleurs : le bleu, le noir `#0B0F1A`, le jaune `#F5B326`. Le blanc seulement comme surface d'un objet. Pas de rouge, pas d'ocre, pas de dégradé, pas de photo de fond, pas de logo.
- Le texte en Anton, capitales. Les objets avec un bord noir épais et une ombre dure, un peu penchés. Le sticker jaune bordé de noir. Le visage détouré avec son contour noir. C'est cette matière commune qui fait la famille.
- Rien qui ne serve pas le choc : pas de sous-titre, pas de phrase secondaire, pas de date, pas de marque.
- Ce qui est montré est vrai : le mot du sticker et le texte crié tiennent leurs promesses une fois l'article lu.

## Les ingrédients (ce qu'on combine)

`exemples/ingredients.css` contient les pièces, avec leurs fourchettes : le texte (120 à 260 px, à gauche, à droite, centré, en haut, en bas, penché ou non, un à cinq mots, un groupe en jaune ou tout en jaune), le sticker (80 à 220 px, de -8 à 8 degrés, jaune ou noir, facultatif), l'objet ou la capture (n'importe quelle taille, n'importe où, même coupé par un bord), le visage (entier dans le cadre, à droite ou à gauche ou au centre, petit ou géant), le chiffre (300 à 420 px). Une cover en prend deux ou trois. Jamais tout.

Les trois fichiers HTML dans `exemples/` sont des covers qui ont plu à Manu, à lire pour attraper le goût : la matière, les épaisseurs, la façon dont un sticker mord sur un bord. Ils ne sont pas à remplir. En copier la structure, jamais la composition.

## Le texte crié

Deux à cinq mots, ou aucun. Il n'est pas le titre de l'article : la cover dit le choc, le titre dit le fait, les deux se complètent. Il se comprend sans contexte par quelqu'un qui ne connaît pas l'outil : pas de « session », « MCP », « prompt système », « déploiement » ; des mots de la vie. Test avant de rendre : le lire seul, à voix haute, en imaginant ne rien savoir. Si une question vient (« c'est quoi une session ? », « et alors ? »), c'est raté.

Exemples validés : DEUX CLAUDE QUI BOSSENT ENSEMBLE (article : Claude Code sait parler à ses autres sessions), MONTAGE VIDÉO / AUTONOME (article : j'ai automatisé mon montage vidéo). Exemples refusés : TES SESSIONS SE PARLENT (jargon), CLAUDE NE DEMANDE PLUS RIEN (répète le titre), TU DISAIS OUI SANS LIRE (phrase plate ; là, l'objet seul avec STOP disait tout, sans texte).

Le mot du sticker vient de `references/mots-cta.md` (STOP, ENFIN, TESTÉ, PIÈGE…) ou d'ailleurs s'il est plus juste ; jamais INCROYABLE, SECRET, ULTIME. Ne pas reprendre le même mot que la cover précédente.

## Improviser

Avant de composer, regarder les cinq dernières covers du blog (`article_list`, puis les `imageUrl`) et faire autre chose : si la dernière avait le texte à gauche et un objet à droite, mettre le texte en plein centre, ou un visage à gauche, ou un seul mot géant. Quelques leviers, à mélanger : un mot seul en 260 px qui remplit la largeur ; le texte sur l'objet plutôt qu'à côté ; l'objet énorme et coupé par le bas ; le visage à gauche et le texte qui descend en escalier à droite ; le sticker qui devient le seul texte ; le chiffre qui prend tout ; deux objets face à face ; un texte penché de 3 degrés ; un texte en deux colonnes. Le résultat doit rester lisible en vignette de 400 px de large : c'est la seule limite à l'improvisation.

Le visage apparaît quand l'article est Manu (un test, un récit, un raté, un avis). Les détourés sont dans la collection **Visages** de la Médiathèque ; choisir l'expression qui va avec le propos. Le visage est toujours entier dans le cadre, jamais coupé sur les côtés ni en haut, et le texte va là où il reste de la place, du côté où il regarde.

## Pipeline

1. **Brief** : titre, chapô, ce que raconte l'article en une phrase. En tirer le choc à montrer, le mot du sticker s'il y en a un, et l'élément visuel (objet, capture, visage, chiffre). Regarder les dernières covers pour ne pas refaire la même.
2. **Trois variantes**, composées différemment (pas trois placements du même texte : trois idées). Un fichier HTML par variante, `ingredients.css` copié en ligne dans le `<style>`, polices via Google Fonts (`Anton`, et `Schibsted Grotesk` si un objet imite une interface).
3. **Rendre** avec `media_render_html` (1600×900, `wait_for` 2000 ms, `name` = `blog-<slug>-<a|b|c>`, `tags` = `["blog", "<slug>"]`).
4. **Regarder chaque rendu** avec `media_view_image`, et corriger avant de montrer : un texte qui touche un objet, un visage coupé, un sticker qui cache le sens de l'objet (les boutons, la ligne de commande), une capitale accentuée qui mord la ligne du dessus, un mot replié. Ce qui n'a pas été regardé n'est pas fini.
5. **Présenter** les trois à Manu, une ligne par variante. Il choisit ou retouche ; retoucher la variante choisie.
6. **Livrer** : `article_update` avec `imageUrl` et un `imageAlt` d'une phrase ; garder le HTML de la variante retenue dans le dossier de travail de l'article.

## Boucle d'amélioration

Quand Manu corrige, la correction va dans ce fichier si elle vaut pour toutes les covers (une règle de goût), dans `ingredients.css` si c'est une pièce (une taille, une ombre), dans `exemples/` si c'est une cover réussie qui mérite d'être un modèle de plus. Un exemple de plus vaut mieux qu'une règle de plus.
