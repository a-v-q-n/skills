---
name: raconter-une-histoire
description: Fabriquer une vidéo verticale « histoire racontée » avec Contentos — une fable, une nouvelle, un conte écrit par Manu — en voix off et en images peintes montées comme une BD animée (caméra qui bouge, planches, phrase suspendue). À utiliser dès que Manu colle une histoire et veut la vidéo. Tout passe par le connecteur Contentos et la Médiathèque ; rien ne se monte à la main.
couche: recette
moment: >-
  La vidéo verticale « histoire racontée » : voix off et images peintes montées en BD animée.
famille: video-contentos
---

# Raconter une histoire

Une histoire racontée, c'est une voix qui lit un texte, et des images qui le portent — jamais une
succession de plein cadres, jamais une captation. Le montage se fait dans Contentos, par le pipe
ordinaire : de la matière dans la vidéo, un script, `lancer_production`. Ce skill dit comment
préparer cette matière et écrire ce script pour que la routine monte une BD animée.

**L'histoire est à Manu.** Elle arrive écrite. Tu ne la réécris pas, tu ne la raccourcis pas, tu ne
choisis pas sa durée : c'est le texte qui décide combien de temps dure la vidéo, et le montage
s'adapte. Ce que tu décides, c'est le découpage en plans et le geste visuel de chacun.

## Le geste, dans l'ordre

1. **Lire l'histoire en entier**, repérer ses battements : les lieux qu'elle installe, les choses
   qu'elle énumère, les phrases qu'elle veut faire entendre seules, les bascules — et **le hook** :
   la vidéo est un TikTok, elle n'ouvre jamais sur son titre. Elle ouvre sur une action forte
   prise vers la fin de l'histoire (pas la chute — un morceau de la fin qui donne envie : la cour
   qui déborde de girouettes, Baldur qui entre dans le cercle), puis vient la carte de titre, puis
   l'histoire commence à son début. Le hook se lit avec sa phrase, à la voix, comme le reste.

   **La seconde une décide de tout, et elle se construit à trois voix, ensemble :**
   - **un texte hook à l'écran** — `@raconter-hook` : une amorce en petites capitales
     (« L'histoire d'un forgeron ») et la phrase-tease en grand, qui n'est PAS le titre mais ce
     qui intrigue (« dont la forge s'est mise à travailler toute seule »), avec le mot-clé
     accentué (`accent: "toute seule"`). Elle annonce, elle ne raconte pas.
   - **une caméra directe** — le plan du hook porte une `camera` avec une `duree` courte (1,2 à
     1,8 s) : un recul ou une poussée franche, joué pendant que le texte frappe — jamais la
     dérive lente du reste du récit.
   - **un son fort sur la première image** — le foley du gabarit (un braam) l'apporte ; dès que
     la banque du conte existe, un coup de tambour grave généré par `generer_son`.
   Piste pour plus tard, à ne pas faire aujourd'hui : transformer la première image en vraie
   vidéo (image-to-video) — coûteux par vidéo, à éprouver un jour sur le hook seul.
2. **Ouvrir la vidéo** — `nouvelle_video` (idée = l'histoire en une phrase, titre = le sien).
3. **La voix** — `generer_prise` avec le clone de Manu (voix `mzrxp21l4T3YCuOE8UaZ`), `registre:
   "conte"` (plus lent, plus posé), le texte tel quel — le hook d'abord, puis le titre s'il se
   dit, puis l'histoire —, un `<break time="0.6s" />` entre deux paragraphes et `0.3s`–`0.4s`
   avant une parole rapportée, `silence_fin` 1,5. Un texte de plus de 3 000 caractères se coupe en plusieurs prises,
   au paragraphe. Quand la prise est `traitee`, `voir_prise` donne le transcript horodaté : c'est là
   que tu lis combien dure chaque phrase — les durées des plans en découlent, tu ne les estimes pas.
4. **Découper en plans** — un plan par phrase, ou par battement quand une phrase en porte deux.
   À chaque plan, un geste de la grammaire (ci-dessous), et jamais le même geste deux fois de suite.
5. **Les images** — dans la Médiathèque (`media_generate_image`), une par plan ou par case, au format
   que le geste demande, avec la facture et le personnage verrouillé (ci-dessous). Regarde chaque
   image (`media_view_image`) : une image ratée se regénère, elle ne se garde pas.
6. **Les ranger** — `creer_asset` avec l'url de la Médiathèque, `video` = le slug de la vidéo, un
   `slug` court qui dit la chose (`forge-seuil`, `caisse-pleine`), un `quoi` qui décrit l'image et un
   `quand` qui dit sur quelle phrase elle sert.
7. **Les sons** — ce que la scène doit faire entendre : `generer_son` (texte en anglais, 0,5 à 30 s,
   réservé à la vidéo), un par bruit du récit. La musique vient de la librairie.
8. **Le script** — `modifier_video` avec la ligne FORMAT et la source `sequences.json` explicite
   (ci-dessous). La routine transcrit cette source telle quelle ; ce qui n'y est pas n'existe pas.
9. **La couverture** — la vidéo ne se finalisera pas sans vignette. Générer la couverture dans
   la Médiathèque (l'image du hook retravaillée, ou une image dédiée : la scène la plus forte,
   sans texte — la plateforme pose le titre du post) et la déposer par `deposer_couverture`.
10. **Lancer** — `lancer_production`. Si une image ou un son est encore `en_attente`, la vidéo
    attend seule que tout soit prêt.
11. **Revue** — la vidéo remonte en `revue` avec son rendu ; Manu la regarde sur sa page.

## La grammaire des gestes

Chaque plan porte un geste, et le geste dit quel format d'image générer.

| Geste | Ce qu'il montre | Comment il s'écrit | Image |
|---|---|---|---|
| **établir** | une image pleine, la caméra la parcourt avec une intention : elle part d'un détail et recule, s'approche d'une chose que la voix nomme, ou traverse une scène large | `fond: { "image": "<slug>" }` + `camera: { "de": {x, y, zoom}, "a": {x, y, zoom}, "ease" }` (voir « La caméra ») ; sans `camera`, l'image dérive lentement | **9:16** pour un léger zoom ou un plan qui tient ; **16:9** pour un travelling latéral |
| **planche** | une page de BD façon webtoon : deux à cinq cases bord à bord, séparées d'une gouttière blanche, la caméra plonge dans la première, voyage jusqu'à chacune sur son mot, puis recule sur la planche entière | `@raconter-planche`, `image1..5`, `entree2..5` en `{ "sur": "mot" }`, `mise` (voir « La planche »), `mouvementK` seulement s'il raconte | une image par case, au format que la mise donne à la case (voir « La planche »). 5 à 10 s : ~1,2 s par case, 0,7 s de voyage, 1,3 s de recul |
| **suspendre** | le temps s'arrête sur une phrase : voile d'encre, trait vermillon, les mots un à un en serif italique | `@raconter-suspendre`, `sur` le premier mot de la phrase, `texte` = la phrase | aucune — le fond de la scène (une image ou un nocturne) |
| **hook** | la seconde une : l'amorce en petites capitales et la phrase-tease en grand or, le mot-clé en vermillon — jamais le titre | `@raconter-hook`, `avant`, `texte`, `accent` — sur la première image, avec sa caméra directe ; son tambour est dans sa fiche | aucune — sur l'image du hook |
| **titre** | la carte de titre, après le hook : le décor du récit voilé derrière, le titre en Cinzel or qui se resserre, une ligne dessous | `@raconter-titre`, `image` (le décor, souvent celle du hook), `titre`, `ligne` — une scène à elle, 3,5 à 5 s | une **9:16** du récit en décor |
| **récitatif** | le cartouche de BD dans un coin haut : une marque de temps ou de lieu que le récit pose sans la dire | `@raconter-recitatif`, `texte` (2 à 8 mots), `coin: droit` au besoin, avec la scène ou `sur` un mot | aucune — sur une image ou une planche |
| **onomatopée** | le mot du bruit — CLANG — en vermillon nu, gros, qui apparaît d'un coup sur l'image | `@raconter-onomatopee`, `mot`, `x`/`y`, `sur` le mot qui le dit ; **un par vidéo au plus** | aucune — sur une image, jamais sur du texte |
| **accumuler** | des cartes carrées qui s'ajoutent une à une sur leurs mots | `@raconter-accumuler` | **1:1** |
| **opposer** | deux cartes 16:9, haut et bas, chacune de son côté | `@raconter-opposer` | **16:9** |

`accumuler` et `opposer` sont le même geste — des cartes qui se posent. Ils servent une fois par
vidéo au plus, pour une énumération ou un face-à-face ; le reste du récit se raconte avec la caméra
et les planches. Pas de bulles de dialogue : la voix dit les répliques, une bulle peinte par-dessus
ferait pastiche. Le récitatif sert aux marques de temps (« Neuf jours plus tard »), l'onomatopée à
un vrai son de l'histoire, et à un seul.

### La caméra

Sur un plan dont le fond est une image, `camera` dit où l'on regarde et comment on y va :

```json
"camera": { "de": { "x": 50, "y": 74, "zoom": 1.35 }, "a": { "x": 50, "y": 48, "zoom": 1 }, "ease": "douce" }
```

- `x`, `y` : le point de l'image qu'on regarde, en pour-cent de sa largeur et de sa hauteur — il
  est placé au centre du cadre, et la caméra s'arrête au bord quand l'image n'a plus de quoi
  couvrir. `zoom` : 1 = l'image couvre exactement le cadre ; plus, on s'approche. Jamais moins.
- `de` obligatoire ; sans `a`, la caméra tient son cadrage toute la scène. `ease` : `douce`
  (défaut) ou `lineaire` pour un travelling à vitesse constante. Sans rien d'autre, le mouvement
  dure toute la scène ; `"sur": "<mot>"` le fait **attendre puis partir sur ce mot** — la caméra
  tient sur `de`, et s'approche quand la voix nomme la chose —, `"duree"` borne sa longueur.
  C'est la ponctuation la plus forte du format : un zoom qui part sur « Une caisse entière ».
- **Une image 9:16** : partir d'un détail (`zoom` 1,3 sur le bas) et reculer, ou l'inverse — jamais
  au-delà de 1,4, l'image ramollit. **Une image 16:9** : la traverser, `x` de 15 à 85 à `zoom` 1,
  `lineaire` — c'est un vrai travelling, qui utilise tous les pixels de l'image.
- La caméra dit une intention : elle va vers ce que la voix nomme, ou s'en éloigne pour montrer
  l'ensemble. Un mouvement sans raison se voit comme un tic.

### La planche

`mise` choisit la composition sur le rythme de la phrase ; chaque mise dit le format d'image de
chaque case, dans l'ordre :

| Cases | `mise` | Quand | Formats des cases |
|---|---|---|---|
| 2 | `empilees` (défaut) | deux moments qui se suivent | 16:9, puis 1:1 |
| 2 | `cote-a-cote` | deux choses face à face | 9:16, 9:16 |
| 2 | `diagonale` | une bascule, une rupture | 16:9, 16:9 |
| 3 | `large-et-deux-hautes` (défaut) | un lieu, puis deux détails | 16:9, 9:16, 9:16 |
| 3 | `trois-bandes` | une action qui se suit | 16:9, 16:9, 16:9 |
| 3 | `grande-et-deux-petites` | un moment et ses détails | 1:1, 1:1, 1:1 |
| 3 | `diagonale` | de la vitesse, une chute | 16:9, 16:9, 16:9 |
| 4 | `briques` (défaut) | quatre temps d'une scène | 9:16, 9:16, 9:16, 9:16 |
| 4 | `grille` | une énumération régulière | 9:16 × 4 |
| 4 | `diagonale` | une action qui dévale | 16:9, 1:1, 1:1, 16:9 |
| 5 | `une-grande-quatre-petites` (défaut) | un lieu et ce qu'il contient | 1:1, puis 1:1 × 4 |
| 5 | `bandes-et-duo` | un récit en cinq temps | 16:9, 9:16, 9:16, 16:9, 16:9 |

**Les cases sont fixes.** Une case bouge seulement quand ça raconte — `mouvementK` : `zoom` (on
s'approche de ce que la voix nomme), `recul`, `gauche` / `droite` (on traverse un décor), `haut` /
`bas` (on suit un geste). Une case sur trois au plus ; une planche dont toutes les cases bougent
brouille la lecture. La caméra, elle, bouge toujours : plongée, voyages, recul.

`page: encre` fait les gouttières d'encre pour une planche de nuit ; par défaut elles sont
blanches. `recul: 0` laisse la caméra sur la dernière case au lieu de reculer.

**La phrase suspendue** va à la phrase que l'histoire veut faire entendre : une parole rapportée, une
pensée, la chute d'un paragraphe. Pas plus d'une par paragraphe ; jamais une phrase de plus de
vingt mots.

## Les images

### La facture

Toute image de l'histoire commence par la même phrase, recopiée mot pour mot — c'est elle qui fait
qu'une image ressemble aux autres :

> Textured gouache painting, storybook illustration, thick opaque brushstrokes, rich earthy palette —
> indigo night, ochre gold, terracotta, deep umber, cream highlights — warm glowing light, mythic
> atmosphere inspired by West African oral tales and Yoruba iconography, painterly, no outlines.
> Full bleed, the painting fills the entire image edge to edge: no border, no frame, no white margin,
> no vignette, no paper edge.

Puis la scène : ce qu'on voit, où, dans quelle lumière, le cadrage (wide / medium / close-up, the
angle). Et pour finir, toujours : `No text, no letters, no writing.`

**Aucun cadre dans l'image.** Le modèle aime poser une marge crème ou un liseré autour d'une peinture
« storybook » ; à l'écran, ce liseré se voit dès que la caméra bouge. La phrase « full bleed… no
paper edge » est là pour ça — si une image en porte quand même un, on la regénère.

**Le personnage est verrouillé deux fois.** D'abord par une phrase, la même dans chaque prompt
où il apparaît — pour « La forge et le tambour » : *an old broad-shouldered Black blacksmith,
bald, with a short grey beard, bare chest, wearing a plain ochre cloth apron tied at the waist,
barefoot* — écrite avant la première image, jamais changée. Ensuite par **l'édition d'image** :
générer UNE image maîtresse du personnage (`media_generate_image`), la regarder, et dériver
toutes ses autres scènes par `media_edit_image` depuis cette source — « keep the exact same
character and the exact same gouache style, now show him… » — c'est ce qui garde le même homme
d'un bout à l'autre (éprouvé : Baldur assis dans sa cour → Baldur au bord du fleuve, même
visage, même tablier). Préférer quand même les vues de dos et de trois quarts, et garder les
gros plans de visage pour un seul moment.

**Décrire l'objet, pas la métaphore.** « Des clous alignés comme des soldats » donne des petits
bonshommes. Écrire *plain iron nails with flat heads, standing upright in straight rows* — et
`no figures, no people` quand une image humaine traîne dans la phrase. Ne rien demander qui ait un
référent réel (une marque, un logo, un écran) : il sera faux.

### Le format, par geste

- **9:16** — un fond qui tient ou que la caméra zoome un peu ; c'est le format par défaut.
- **16:9** — un travelling latéral, une case large de planche, une carte d'`opposer`. Une image
  large traversée de gauche à droite utilise tous ses pixels ; c'est la seule façon de faire un
  vrai travelling sans agrandir.
- **1:1** — une case carrée, une carte d'`accumuler`.

La Médiathèque génère en 1K (768 × 1376, 1376 × 768, 1024 × 1024) : un plein cadre 9:16 est
agrandi d'un tiers à l'écran, ça passe en gouache ; un zoom au-delà de ×1,4 dans une image ne
passe plus. Quand un plan veut s'approcher d'un détail, générer le détail comme une image à part
plutôt que zoomer.

## L'atmosphère

Toute histoire porte, en tête de source, une couche qui la tient dans la même nuit :

```json
"atmosphere": { "gabarit": "raconter-atmosphere", "params": { "grain": 0.5, "vignette": 0.6, "lueur": "feu" } }
```

Un grain de film qui vit, un vignettage qui ferme les bords, et une lueur selon le récit — `feu`
pour une forge, une cuisine, une veillée (chaude, elle palpite depuis le bas) ; `lune` pour la
nuit dehors, un fleuve (froide, lente, depuis le haut) ; vide pour le jour. `grain` 0,4 à 0,6,
`vignette` 0,5 à 0,7 : au-delà, ça se voit comme un filtre.

## La respiration

Un conte a son timing, et c'est le script qui le donne, pas la voix :

- `"pause": 1.2` sur un plan : la scène dure 1,2 s de plus après la phrase, sans un mot — la voix
  se tait, l'image tient, la musique respire dans le silence. Une pause après une chute de
  paragraphe, avant une bascule, après la phrase suspendue. Jamais plus de 2 s.
- `"transition": "noir"` sur un plan : la scène se ferme au noir et la suivante s'ouvre depuis le
  noir — le passage d'un chapitre, un saut dans le temps (« Neuf jours plus tard »). Avec une
  `pause`, la respiration est noire : c'est le geste le plus fort, deux ou trois fois par histoire,
  pas plus. Sans `transition`, coupe nette.

Pas d'autre transition : ni fondu enchaîné, ni effet. Une coupe, ou le noir.

## Le son

- **La musique** est **une seule**, pour toute l'histoire, composée **par sections qui suivent
  ses chapitres** : `generer_musique` avec `styles` (globaux, en anglais — toujours
  « instrumental, no vocals ») et `eviter` (toujours « vocals, singing, lyrics »), puis
  `sections` — une par mouvement du récit, avec sa durée prise sur le verbatim (3 à 120 s
  chacune) et ses styles propres : « calme, tambour à peine là, 20 s » ; « tension, cordes
  basses, 15 s » ; « retombée, presque silence, 25 s » ; « le tambour reprend, 30 s ». La somme
  fait la longueur de la voix, pauses comprises. Le thème appartient au récit — pour « La forge
  et le tambour », un tambour à trois temps, lent, ouest-africain, clairsemé. Deux morceaux
  différents cassent l'envoûtement ; un seul, qui monte, retombe et se tait, construit l'arc.
  `boucle: false` dans la source quand la musique fait la longueur de la vidéo. À défaut, la
  librairie : `profondeur` (gravité calme),
  `respiration` (douceur, finit presque en silence), `confidence` (sincérité), `nappe-suspension`
  (mystère, sans pulsation). En tête de source : `"musique": { "asset": "<slug>", "boucle": true,
  "ducking": true }`. Le niveau ne s'écrit pas — la bande son le cale sous la voix, et le relâche
  dans les pauses.
- **Pas de son de coupe** (`cut`) : une histoire ne « whoosh » pas entre deux images.
- **La banque du conte, en librairie** — à réutiliser avant d'en générer : `tambour-grave` (le
  battement qui ouvre — le hook et le titre le posent déjà par leur fiche), `feu-foyer` (lit de
  crépitement de 12 s), `marteau-enclume` (la sonnerie claire du fer, pour un CLANG). Ce qui
  manque au récit se fabrique par `generer_son`, en anglais, un par bruit : *old wooden crate
  dropped on packed earth* ; *slow hand drum, three-beat rhythm, distant* ; *wind over a river at
  dusk*. Le serveur mesure l'attaque et le gain : rien à régler. Un son se pose dans le plan sur
  son mot : `"sons": [{ "sfx": "<slug>", "sur": "<mot>" }]` — c'est le pic qui tombe sur le mot.
  Un son par battement au plus ; deux pics au même instant s'additionnent.
- **Une ambiance** (le feu sous toute une scène) se pose comme un son, avec un niveau écrit et la
  durée de la scène : `{ "sfx": "feu-foyer", "a": 0, "gain": -14, "duree": <durée du plan> }` —
  bas, c'est un décor, pas un accent. Une par scène au plus, pas sur les planches.
- Les autres sons de la librairie sont tech (glitchs, whooshs, braams) : ils ne servent pas ici.

## Les sous-titres

Le script les choisit, en tête de source : `"sous_titres": "sous-titre-conte"` — serif italique,
minuscules, crème sur une bande d'encre — ou `"aucun"`. Sans rien, ce sont les sous-titres de la
charte tech, en capitales : pas pour une histoire. La ligne des sous-titres passe sur les images et
sur les cases basses d'une planche ; sa bande d'encre la rend lisible partout.

## Le script

`modifier_video` reçoit un texte libre. Il commence par la ligne FORMAT — voix off seule, la prise,
la musique, les sous-titres, le ton — puis dit le montage plan par plan, et finit par la source
`sequences.json` complète, dans un bloc ` ```json `. La routine transcrit cette source ; les
lignes qui la précèdent sont pour l'humain qui relit.

Ce qu'un plan porte, dans la source :

```json
{ "dit": "Le texte de la phrase, exactement comme la voix le dit.",
  "fond": { "image": "forge-seuil" },
  "poser": [ { "gabarit": "raconter-suspendre", "sur": "Il me faudrait",
               "params": { "texte": "Il me faudrait des clous. Une caisse entière.", "voile": 0.6 } } ],
  "sons": [ { "sfx": "marteau-enclume", "sur": "marteau" } ] }
```

- `dit` est copié du texte lu, sans le raccourcir : ce sont ses premiers et derniers mots qui bornent
  le plan dans la voix.
- `fond` : `{ "image": "<slug>" }` (plein cadre, 9:16 ou 16:9), ou `"nocturne"` sous des cartes.
  Jamais `"papier"` sous un texte crème.
- Un gabarit entre avec la scène, ou `sur` un mot du plan. Ses images s'écrivent `{ "asset":
  "<slug>" }` ; un instant interne (l'entrée d'une carte, la bascule) s'écrit `{ "sur": "<mot>" }`
  et la routine le convertit en secondes. `duree` ne s'écrit pas : l'instance dure jusqu'à la coupe.
- `voile` : 0 sur un nocturne, 0,45 à 0,6 sur une image.

Une séquence par paragraphe (`nom` court), un plan par phrase, `prise` = le rang de la voix.

## Le rythme

- La voix fait le temps : un plan dure ce que sa phrase dure. Une phrase de six mots ne portera
  pas une planche à trois cases — lui donner une image et la caméra.
- Un geste par battement, et le suivant différent. La caméra qui bouge est le geste par défaut du
  récit ; la planche, celui de l'énumération et de l'action ; la phrase suspendue, celui du silence.
- Entre deux plans, la routine coupe net. Ce sont les images et la musique qui lient, pas des
  transitions.
- Un paragraphe = une séquence ; une séquence s'ouvre en général sur un plan établi (la caméra sur
  une image pleine) avant de se resserrer.
- L'ordre de la vidéo : **le hook** (une ou deux phrases fortes prises vers la fin, sur une image
  qui frappe), **le titre** (`@raconter-titre`, 3 à 4 s, souvent avec `transition: noir` avant),
  **l'histoire** depuis son début. La phrase du hook revient à sa place dans le récit, plus tard :
  le spectateur la reconnaît, c'est voulu.

## Ce qui ne se fait pas

- Réécrire, résumer ou « adapter » l'histoire. Couper une phrase en deux plans sans que la voix
  marque la pause.
- Poser un plan sans image (un `fond` nocturne nu pendant qu'on raconte).
- Une image avec un cadre, une marge, un liseré, du texte ; un personnage décrit autrement que par
  sa phrase.
- Estimer une durée à la place du verbatim ; écrire un niveau sonore ; mettre un son de coupe.
- Monter quoi que ce soit à la main : tout ce qui n'est pas dans la source n'existe pas pour la
  routine, et rien ne se corrige après `lancer_production` — sauf par une revue sur la page de la
  vidéo, qui relance une reprise.
