---
name: degrossir
description: Tirer une vidéo propre d'une captation tournée d'un jet — repérer
  les faux départs et les redites dans le transcript, ne garder que les
  tentatives qui portent, poser les prises dans l'ordre et resserrer leur
  parole. À charger quand la matière est une captation courte filmée au
  téléphone, une prise de parole reprise plusieurs fois, un enregistrement où
  l'auteur s'est repris — et qu'il doit en sortir une seule vidéo.
---

# Dégrossir une captation

Une captation tournée d'un jet contient une vidéo et son brouillon, mélangés.
L'auteur a commencé, s'est arrêté, a repris ; il a dit la même chose deux fois,
mieux la seconde ; il a hésité, cherché son mot, toussé. **Tout ça est dans le
même fichier, et rien ne le sépare.**

Dégrossir, c'est retirer ce qui n'était pas destiné à rester, et poser ce qui
reste dans l'ordre. Il en sort **une seule vidéo**, en préproduction, dont le
script s'écrira ensuite avec l'auteur.

Ce n'est pas `repurposer`. Là, une matière porte plusieurs propos et on en tire
plusieurs vidéos. Ici, une matière porte **un** propos, dit maladroitement, et
on en tire la meilleure version.

## Ce que tu peux juger, et ce que tu ne peux pas

Tu lis. Tu ne peux pas entendre.

**Ce qui se lit dans le transcript**, et que tu tranches seul :

- un **faux départ** — une phrase abandonnée, une reprise annoncée (« non,
  attends », « je reprends », « alors, alors ») ;
- une **redite** — le même propos deux fois, et la seconde est presque toujours
  la meilleure : l'auteur venait de s'entendre le dire ;
- un **hors-sujet** — une parenthèse qui n'avance pas le propos ;
- une **hésitation qui mange une phrase** — pas un « euh », qui ne se coupe pas
  au montage, mais dix secondes à chercher un mot ;
- **l'ordre** — deux passages qui gagnent à être intervertis.

**Ce qui ne se lit pas**, et qui revient à l'auteur :

- une prise **molle** — le texte est le même, la diction non ;
- une **voix qui casse**, un souffle, un bruit de fond, un scooter ;
- ce qui **sonne** juste entre deux tentatives dont le texte est identique.

Quand deux tentatives disent la même chose avec les mêmes mots, **ne choisis
pas**. Dis à l'auteur qu'il y en a deux, donne-lui les deux fenêtres et les
liens, et laisse-le écouter. Choisir sur le texte en croyant choisir sur le son
est la seule faute qui ne se voit pas.

## 1. Lire, et cartographier les tentatives

```
lister_rushes
voir_rush { slug, de?, a? }
```

La matière est souvent déjà là : un partage depuis le téléphone dépose un rush
et s'arrête. Sinon, `deposer_rush { nom, url }`.

Rien ne se lit avant que le rush soit `pret` : le serveur le rapatrie, le sonde
et le transcrit. Un transcript absent n'est pas une captation muette.

Une captation courte se lit **d'un bloc** — c'est la différence avec un long
form. Puis relève, ligne par ligne, **ce que chaque passage tente**. Une
captation de quatre minutes donne typiquement six à douze tentatives, dont la
moitié sont des reprises de la précédente.

Écris cette carte : `m:ss–m:ss`, ce qui s'y dit, et son verdict — *garder*,
*redite de la précédente*, *faux départ*, *à trancher par l'auteur*. C'est le
seul document, et il tient en un écran.

## 2. Décider, avec l'auteur

Montre la carte. C'est court à lire, et c'est là que l'auteur voit ce qu'il a
fait — il ne s'en souvient pas, il était en train de parler.

Trois choses se tranchent là :

- **les tentatives à garder**, quand deux disent la même chose ;
- **l'ordre**, s'il ne suit pas celui de la captation ;
- **ce qui manque** — un propos que la captation n'a pas dit et qu'il faudra
  tourner, ou faire dire.

Ne pose rien avant. Une prise extraite puis supprimée coûte un aller-retour et
un rang qui ne se rendra pas.

## 3. Poser les prises

```
lister_videos
nouvelle_video { idee, titre?, slug? }
extraire_prise { slug, rush, de, a, nom?, cadrage: { mode, x? }, fond? }
```

**Dans l'ordre où la vidéo se déroulera**, pas dans celui de la captation. Le
rang d'une prise ne bouge jamais après coup — c'est par lui que les ancres du
script la désigneront (`@{2:mot}`) —, donc l'ordre se décide maintenant.

Nomme chaque prise par ce qu'elle dit, pas par sa fenêtre : « le vrai coût »
vaut mieux que « 2:14–2:48 » quand il y en a six.

**Une captation téléphone est déjà verticale** : le mode `plein` la rend telle
quelle. Les autres modes servent une source large et n'ont rien à faire ici. Si
la captation a été tournée à l'horizontale, `repurposer` porte la table des
cadrages.

**Aucune prise générée.** Pas de hook en voix de synthèse, pas de liaison, pas
d'avatar : ce que tu poses est la matière d'origine. Ce qui manque se fabriquera
avec l'auteur, quand le script sera décidé.

## 4. Les bornes

Les mêmes règles que partout, et elles se ratent au même endroit :

- **Sur un silence, jamais au milieu d'un mot.** Le premier et le dernier mot de
  l'extrait doivent être entiers.
- **Le `fin` d'un mot du verbatim absorbe souvent la pause qui le suit** : une
  borne posée juste après le dernier mot peut le perdre. Quelques dixièmes de
  marge.
- **Relis ce qui suit ta borne de fin.** Une chute tronquée est le défaut le plus
  fréquent — la captation s'arrête au milieu de l'idée qu'elle venait de poser.
- **Une borne de début tombe au début d'une phrase**, pas sur un fragment.
- **Coupe le faux départ, pas la respiration qui le suit.** Un extrait qui
  démarre pile sur la première syllabe s'entend comme une coupe.

Après extraction, relis le verbatim de la prise dans `voir_video` : le premier
et le dernier mot y sont, ou la borne est à reprendre.

## 5. Resserrer la parole

```
resserrer_prise { slug, rang }
resserrer_prise { slug, rang, defaire: true }
```

Une captation où l'auteur cherche ses mots porte des blancs que le montage ne
comblera pas. `resserrer_prise` les ramène à une pause courte : aucun mot ne
disparaît, seuls les silences se raccourcissent, et les ancres du script
survivent — elles visent des mots, pas des secondes.

**Deux choses à savoir avant de le proposer.**

Sur une prise qui porte de l'image, **chaque jointure est un saut visible** : le
son et l'image se coupent aux mêmes instants, sinon ils se décalent. Sur de la
parole face caméra c'est le geste ordinaire, mais ça se regarde.

Et **c'est à l'oreille que ça se juge**, donc pas par toi. Propose-le, dis ce
que ça change, donne les deux liens que `voir_video` rend — `url_livraison` et
`url_avant_resserrage` — et laisse l'auteur écouter. `defaire` remet la prise
comme elle était.

Ne le lance pas sur toutes les prises d'office. Une prise déjà nette n'y gagne
rien, et le resserrage lui coûte une génération d'encodage.

## 6. L'intention

Le dernier geste est d'écrire l'`idee` de la vidéo, par `modifier_video`. C'est
ce que l'auteur lira pour écrire son script, et c'est tout ce qu'il aura de ce
travail :

- **le propos** — ce que cette vidéo avance, en une phrase ;
- **les prises posées** — leur rang, ce qui s'y dit, d'où elles viennent dans la
  captation ;
- **la durée** mesurée, pas estimée ;
- **ce qui a été jeté, et pourquoi** — c'est ce qu'il ne peut pas deviner, et ce
  qu'il voudra peut-être récupérer ;
- **ce qui reste à trancher** — les tentatives que tu n'as pas départagées faute
  d'oreille, les graphies que la transcription écorche.

**Le `script` reste vide**, et la vidéo reste en préproduction. Ce qu'elle dira,
mot à mot, se décide ensuite avec l'auteur.
