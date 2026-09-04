---
name: fabriquer-les-assets
description: >-
  À utiliser pour créer le visuel d'une vidéo Contentos : gabarits HTML animés (graphes,
  schémas, cartes) et images générées. Porte les réflexes (réutiliser la librairie avant de
  créer, apprendre la charte en lisant un gabarit existant), les conventions techniques
  (GSAP, marge sûre, nocturne/papier), l'aperçu de contrôle obligatoire et les règles des
  images (métaphores, jamais d'UI réelle). NE COUVRE PAS le plan de la vidéo
  (preparer-une-video), le montage (scripter-le-montage) ni les images d'une ressource
  Autonomes, qui ont leur propre charte (illustrer-une-ressource).
couche: recette
moment: >-
  Le visuel : gabarits HTML animés et images générées, charte, aperçu de contrôle.
famille: video-contentos
---

# Fabriquer les assets

Ce skill fabrique les gabarits animés et les images d'une vidéo, à partir du plan validé.
Deux réflexes avant tout geste : la librairie d'abord, la charte sur pièce.

## Réflexe 1 : la librairie d'abord

Avant de créer quoi que ce soit, `lister_assets` (type html pour les gabarits). La
librairie couvre déjà les besoins récurrents : accroches (phrase-bloc, deux-lignes),
désignation (mot-cle, badge, annotation), énumérations (liste-points, pile-items),
chapitres (ecran-section, titre-chapitre), CTA (abonne-toi, commente, bookmark), inserts
(image-cadree, citation, terminal-tape). Un récap de fin = `pile-items` en mode coche, pas
un gabarit neuf.

On ne crée un gabarit que pour ce que la librairie ne sait pas dire — typiquement les
visualisations propres au sujet (une courbe, un plan, une jauge, un schéma).

## Réflexe 2 : apprendre la charte sur pièce

Avant d'écrire le premier gabarit d'une session, ouvrir un gabarit existant proche
(`voir_asset` puis télécharger son corps) et en reprendre les conventions. Ne jamais écrire
de tête.

## La charte, en résumé

- Couleurs par variables : `--bg` (papier crème), `--fg` (encre, qui sert aussi de fond
  nocturne), `--primary` (vermillon), `--secondary` (teal). Polices : `--display` (Archivo
  Black, la frappe), `--caption` (petites capitales espacées), et Instrument Serif pour les
  citations.
- **Plein cadre** (le gabarit occupe sa scène) : fond nocturne quadrillé, opaque dès la
  première image, lueur vermillon qui respire — comme `ecran-section`. Jamais papier en
  plein cadre : les sous-titres perdent leur contraste.
- **Overlay** (l'A-roll reste visible) : cartes et pastilles papier bordées d'encre, ombre
  dure décalée (un objet derrière, jamais un flou).
- Le contenu vit au-dessus de la bande basse des sous-titres (padding bas ~15cqh) et dans
  la marge sûre (`--marge`, 11%).

## Les conventions techniques

- Un `<template>` avec un commentaire d'intention en tête et un commentaire
  `<!-- exemples {...} -->` qui donne des valeurs de démonstration aux trous.
- Racine : `<div id="root" data-composition-id="slug" data-width="1080" data-height="1920"
  data-duration="{{duree}}">` avec `container-type: size` ; tailles en cqw/cqh.
- Chaque trou `{{cle}}` du corps DOIT être déclaré dans `params.params` du tool, sinon
  refus.
- Animation GSAP : timeline `paused: true` enregistrée dans `window.__timelines["slug"]`.
  État de repos = caché en CSS (`opacity: 0; visibility: hidden`), révélé par `fromTo` avec
  `immediateRender: false`. Sortie du bloc à `duree - 0.3` ; en plein cadre, le fond couvre
  jusqu'à la coupe.
- JAMAIS de `transform` CSS sur un élément dont gsap anime x/y/scale — conflit, le lint
  refuse. Tout viser par sélecteur `#id` (les ids sont préfixés au montage).
- Tracés SVG : mesurer avec `getTotalLength()` au montage et animer `strokeDashoffset` —
  jamais de longueur codée en dur.
- Texte variable en une ligne : la mesure en pixels fixe + `document.fonts.ready` pour
  tenir la marge sûre (reprendre le bloc `poserLeTitre` d'un gabarit existant).
- `foley` dans params : un whoosh discret sur la coupe suffit (`whoosh-ample` plein cadre,
  `whoosh-doux-1` overlay).

## L'aperçu de contrôle — obligatoire

Après chaque `creer_gabarit`, `apercevoir_gabarit` et REGARDER la planche : débordements de
texte au bord du cadre, libellés rognés, lisibilité, timing des entrées. Corriger en
réécrivant le gabarit entier (même slug = remplacement) et re-vérifier. Un gabarit n'est
fini qu'après un aperçu propre. Consigner les pièges trouvés dans le champ `comment`.

## Les images générées

`generer_image`, réservée à la vidéo (param `slug`). Les règles :

- Le sujet se RÉDIGE : la scène, ce qu'on y voit, le fond — pas le style, que le serveur
  pose.
- Des métaphores visuelles, jamais un référent réel : pas de logo, pas de marque, pas
  d'interface d'un outil (le modèle en fabrique un faux qui décrédibilise tout). Un sujet
  qui EST un écran se couvre de faux texte — changer de métaphore.
- Pas de texte porteur de sens dans l'image : le texte, c'est l'affaire des gabarits.
- Vérifier le rendu (`voir_asset` quand `pret`, télécharger, regarder) avant de considérer
  l'image bonne.

Exemples de métaphores qui ont marché : le sablier dont le sable s'évapore (ce qui expire),
le rouleau de papier interminable qui déborde d'un bureau (l'historique qui pèse).

## Checklist avant de rendre la main

- [ ] La librairie a été consultée avant toute création, rien de doublonné
- [ ] La charte a été apprise sur un gabarit existant, pas écrite de tête
- [ ] Chaque trou `{{cle}}` est déclaré dans `params.params`
- [ ] Plein cadre en nocturne, overlay en papier, contenu dans la marge sûre
- [ ] L'aperçu de chaque gabarit a été regardé, corrigé, re-regardé jusqu'à propre
- [ ] Les images générées : métaphores sans référent réel, rendu vérifié à l'œil
- [ ] Les pièges rencontrés sont consignés dans le champ `comment` du gabarit

## Boucle d'amélioration

Quand Manu corrige un asset, chercher la règle qui aurait évité la correction : une règle
de charte ou de technique s'ajoute ici, un piège propre à un gabarit va dans son champ
`comment`. Les gabarits de la librairie sont la mémoire du style.
