---
name: rescenariser
description: Réordonner le propos d'une vidéo dont la matière est déjà posée —
  relire ce que chaque prise dit, trouver l'ordre qui tient debout, et réécrire
  le script sur les mêmes prises. À charger quand une vidéo en préproduction a
  ses prises mais que son propos ne s'enchaîne pas, qu'elle démarre mal, ou que
  l'auteur veut la raconter autrement sans retourner quoi que ce soit.
couche: recette
moment: >-
  Une vidéo dont la matière est déjà là : son propos réordonné, avec l'auteur.
famille: video-contentos
---

# Rescénariser une vidéo

Une vidéo dont la matière est bonne peut se raconter mal. L'ordre dans lequel
les choses ont été dites n'est presque jamais l'ordre dans lequel elles
s'écoutent : on a commencé par le contexte alors que l'accroche était au milieu,
on a gardé pour la fin ce qui devait ouvrir.

**Rescénariser ne touche pas la matière.** Aucune prise ne bouge, aucune ne se
réextrait, aucun octet ne change. Ce qui change, c'est le script — et c'est
tout.

## Pourquoi c'est gratuit

Le script ne nomme jamais de secondes. Il nomme des **ancres** :

```
@{skill}          le début du mot « skill »
@{2:skill}        dans la deuxième captation — obligatoire dès qu'il y en a
                  plusieurs, un mot dit deux fois n'est pas le même instant
@{"je veux pas".fin}   la fin de la suite de mots
@{prêts +0.4}     décalé de quatre dixièmes
```

Une ancre vise **un mot dans une prise**, désignée par son rang. Donc :

- **les prises sont un tas**, sans ordre propre ;
- **l'ordre du récit vit entièrement dans le script**, et nulle part ailleurs ;
- réordonner le propos = **réécrire le script**, `modifier_video`, et rien
  d'autre.

C'est aussi pourquoi le rang d'une captation ne bouge jamais : les ancres
pointent dessus. Si réordonner voulait dire réordonner les prises, chaque ancre
déjà écrite casserait. Ce n'est pas le cas.

## 1. Relire ce que la matière porte vraiment

```
voir_video { slug }
voir_prise { slug, rang, de?, a? }
```

`voir_video` rend les prises, leur verbatim, leur durée. `voir_prise` rend ce
qu'une prise dit, mot à mot — c'est là que se lisent les ancres possibles.

**Relis avant de proposer quoi que ce soit.** Un ordre qu'on imagine depuis le
script existant reproduit les défauts du script existant : c'est la matière qui
dit ce qui est disponible, pas le texte qu'on avait écrit dessus.

Note, prise par prise : **ce qu'elle avance**, en une phrase. Une vidéo de six
prises tient sur six lignes, et c'est sur ces six lignes que l'ordre se décide —
pas sur le verbatim entier.

## 2. Trouver l'ordre

Trois questions, dans cet ordre :

**Par quoi ça ouvre ?** Les trois premières secondes décident si la suite est
regardée. Cherche la phrase la plus forte de toute la matière — celle qui pose
un enjeu, contredit une évidence, ou nomme un chiffre. Elle est presque jamais
au début : c'est le sujet même de ce skill.

**Qu'est-ce qui doit être compris avant quoi ?** Une affirmation qui suppose une
définition posée plus loin ne tient pas. Note les dépendances réelles — il y en
a moins qu'on croit, et la plupart des « il faut d'abord expliquer que… » sont
des habitudes, pas des nécessités.

**Par quoi ça ferme ?** Une vidéo qui s'arrête parce que la matière s'arrête se
sent. La fin est un choix : la conséquence, la question posée au spectateur, le
retour à l'ouverture.

Ce qui ne trouve pas sa place **ne se case pas**. Un passage qu'aucun ordre
n'accueille est un passage à couper, et le dire vaut mieux que l'enterrer au
milieu.

## 3. Proposer, avant d'écrire

Montre l'ordre retenu à l'auteur — les prises dans leur nouvel enchaînement, une
ligne chacune, avec ce que ça ouvre et ce que ça ferme. Et dis **ce que tu
proposes de couper**, séparément : c'est la décision qui se conteste le plus, et
elle se conteste mieux avant que le script soit écrit.

Le propos est le sien. Tu proposes une architecture, tu ne tranches pas ce que
la vidéo dit.

## 4. Réécrire le script

```
modifier_video { slug, script }
```

Le script est **prescriptif** : le montage l'exécute tel quel, il ne l'interprète
pas. Ce qu'il porte, ce sont les ancres qui disent quel morceau de quelle prise
se joue, et dans quel ordre.

- **Une ancre par borne**, entrée et sortie de chaque passage retenu.
- **`@{rang:mot}` dès qu'il y a plus d'une prise.** Sans le rang, un mot dit dans
  deux prises est un pari.
- **Vérifie chaque mot cité contre le verbatim**, pas contre ta mémoire du
  transcript. Une ancre qui ne résout pas arrête le montage.
- **Une répétition se numérote** : `@{skill#2}` pour le deuxième « skill ».

Le reste du script — ce qui s'affiche, ce qui s'entend par-dessus — se décide
avec l'auteur comme d'habitude. Rescénariser pose l'ossature, pas l'habillage.

## Ce qui ne se fait pas

- **Aucune prise ne se réextrait.** Si l'ordre demande une matière qui n'existe
  pas, c'est une matière à tourner, pas un script à forcer.
- **Aucun rang ne bouge.** `renommer_captation` change un nom, jamais un rang.
- **Rien ne se resserre ici.** Si une prise traîne, c'est `resserrer_prise`, et
  ça se juge à l'oreille, par l'auteur.
- **Le script ne se réécrit pas sur une vidéo sortie de préproduction.** Une
  vidéo en montage ou en revue exécute un script scellé ; le rescénariser
  reviendrait à changer le contrat sous le monteur.
