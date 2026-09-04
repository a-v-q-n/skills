---
name: scripter-le-montage
description: >-
  À utiliser pour écrire le script de montage final d'une vidéo Contentos et le poser dans
  la fiche — le dernier geste avant la production. Porte la syntaxe des liens (#prise,
  @asset), le découpage en séquences et en plans, le montage dynamique (cuts, splits en
  volet), le découpage du hook en trois plans et les règles de composition de la librairie.
  NE COUVRE PAS l'écriture du texte de la VO (preparer-une-video + socle ecrire-mes-videos)
  ni la génération des prises (produire-la-vo).
couche: recette
moment: >-
  Le script de montage final : séquences, plans, liens `#prise` et `@asset`.
famille: video-contentos
---

# Scripter le montage

Ce skill écrit le script lié et le pose dans la fiche. C'est le dernier geste : tout ce qui
précède (texte validé, prises traitées, gabarits vérifiés) doit être en place, parce que
poser le script le verrouille.

## La forme du script

Le champ `script` de `modifier_video` n'impose aucune forme, mais celle qui marche :

- Un en-tête d'une ligne : format, durée visée, quelles prises portent quoi, le ton.
- Une section par SÉQUENCE avec son timing indicatif, la prise qui la porte, les assets
  accrochés à leur verbatim (« @quota-burn plein cadre (~10 s) sur "la bonne question n'est
  jamais…" »), puis le texte entre guillemets.
- Les liens : `#rang` pour une prise (#1, #2), `@slug` pour un asset ou un gabarit
  (@quota-burn, @phrase-bloc). La fiche les rend cliquables — TOUT ce qui existe se lie.

## Le hook : trois plans, jamais deux

La première séquence (hook + bridge) se découpe TOUJOURS en trois plans minimum — le rythme
des premières secondes décide de la rétention, et un hook laissé en deux plans mous
(l'accroche, puis « le reste ») gaspille le meilleur moment de la vidéo. Le patron :

1. **L'accroche pure** (2-3 s) : plein cadre serré sur le visage, le gabarit d'accroche
   par-dessus (@deux-lignes ou @phrase-bloc), @riser-hook sous la montée et un drop sur la
   chute de la première phrase. Le plan se termine à la frontière de cette phrase, pas
   ailleurs.
2. **Le bridge en split** (3-5 s) : bascule en volet — @panneau-concept nomme le concept en
   haut pendant que l'auteur vit dans le panneau bas (la scène se monte en volet, c'est sa
   raison d'être). C'est la respiration qui installe le sujet.
3. **La promesse** (3-5 s) : retour plein cadre par un cut franc, et un @badge ou @mot-cle
   qui pop sur le mot qui paie (« à la fin », « gratuit », « dès demain »).

Chaque coupe tombe sur une frontière de phrase du verbatim — le lire avant de découper.
2 à 4 secondes par plan sur un hook ; si un plan dépasse, il se coupe.

## Le montage dynamique

Un long passage face caméra ne reste jamais un seul plan. Le découper en PLANS à
l'intérieur de la séquence, chacun avec son timing et son verbatim :

- Alterner split screen et plein cadre : un split en volet (l'habillage en volet haut, la
  prise recadrée sous la couture — `@panneau-concept` est fait pour ça), un cut plein
  cadre, un retour en split avec autre chose en haut (une image de la vidéo, par exemple).
- Les cuts tombent sur des frontières de phrase — le verbatim de la prise fait foi, pas
  l'estimation.
- Les gabarits plein cadre (visualisations) occupent leur scène entière, posés sur le
  passage exact qu'ils illustrent — le verbatim cité dans le script fait foi.
- Un plan de plus de ~10 s sans événement visuel (pop, tracé, bascule) est un plan à
  redécouper — sauf si un gabarit anime déjà son intérieur (ses t1/t2/t3 calés sur les mots
  comptent comme des événements).

## Les règles de composition de la librairie

- Un seul CTA par scène, jamais deux de la famille (abonne-toi, commente, bookmark).
- Les gabarits d'accroche (phrase-bloc, deux-lignes, rangee-logos) : une instance par
  vidéo, dans les premières secondes, jamais en chapitre.
- `panneau-concept` : une instance par vidéo, et sa scène DOIT se monter en volet.
- Deux gabarits qui occupent la même zone ne coexistent pas (mot-cle et carte-outil se
  partagent le tiers haut).
- Un même asset ne se répète pas d'une séquence à l'autre sans raison — s'il a servi au
  hook, le noter dans le script pour ne pas le rejouer plus loin.
- `ecran-section` / `titre-chapitre` : un ou deux par vidéo, sur les vraies bascules du
  propos.

## Le verrouillage

Poser le `script` via `modifier_video` FERME le script : il part à la fabrique et ne se
rouvre pas. C'est donc le dernier geste, quand tout est en place : prises traitées,
gabarits vérifiés à l'aperçu, images prêtes, texte validé par Manu. Le titre, l'idée et la
description restent modifiables après.

Si Manu demande un changement de structure APRÈS un premier envoi (nouveau découpage du
hook, asset déplacé), reposer le script entier mis à jour — et vérifier que la modification
passe encore avant de la promettre.

## Après

La production se lance depuis la fiche ou via `lancer_production` — sur demande de Manu
uniquement.

## Checklist avant de rendre la main

- [ ] Prises traitées, gabarits vérifiés à l'aperçu, images prêtes, texte validé par Manu
- [ ] Le hook tient en trois plans minimum, 2 à 4 secondes chacun
- [ ] Chaque coupe tombe sur une frontière de phrase du verbatim, relu avant découpage
- [ ] Aucun plan de plus de ~10 s sans événement visuel (hors gabarit animé)
- [ ] Les règles de la librairie sont respectées (CTA, instances uniques, zones, répétitions)
- [ ] Tout ce qui existe est lié (#prise, @asset), l'en-tête d'une ligne est posé
- [ ] Le script n'a été posé dans `modifier_video` qu'avec le feu vert explicite de Manu

## Boucle d'amélioration

Après la vidéo, penser à la rétro (`deposer_retro`) : ce qui a marché ou raté nourrit les
skills. Une règle de montage qui se confirme (un rythme, un patron de plans) s'ajoute ici ;
une règle de gabarit va dans `fabriquer-les-assets`.
