---
name: ecrire-mes-ressources
description: >-
  Socle des règles de contenu d'Autonomes, le site de formation de Manu pour les
  non-techniques. À charger AVANT d'écrire, réécrire, raccourcir ou juger le contenu d'une
  ressource Autonomes (tuto, fiche, cheatsheet, exercice), même si Manu dit seulement
  « rédige-moi la fiche », « c'est trop long » ou « rends ça plus clair ». Porte
  l'adresse (tu), le lecteur cible, la chasse au fluff et au bullshit marketing, la
  structure par format, les longueurs, l'usage des modules et des images. Les recettes
  creer-une-ressource et relire-une-ressource le chargent d'abord.
  NE COUVRE PAS le titre (titrer-une-ressource), la cover, la fabrication des
  images, ni la mécanique du MCP.
---

# Écrire mes ressources

Autonomes apprend à des gens qui ne savent pas coder à se servir de Claude Code, du terminal, de n8n, d'un serveur. Le lecteur type est indépendant ou salarié, curieux, pressé, et un peu inquiet de casser quelque chose. Il ne lit pas pour le plaisir : il lit pour faire, ou pour comprendre une chose précise, puis il retourne à son travail.

Tout dans ce socle découle de ça. Chaque phrase qui ne l'aide pas à faire ou à comprendre lui coûte du temps et de la confiance.

## Charger d'abord la voix

Les règles non négociables d'`ecrire-comme-manu` s'appliquent telles quelles : orthographe impeccable, jamais de tiret cadratin ni demi-cadratin, jamais de « , et », aucun tic IA (« Ce n'est pas X. C'est Y. », punchlines, questions rhétoriques auto-répondues, phrases-pivot « ça change tout »), aucun connecteur soutenu, aucun adjectif gonflé. Charger ce socle-là si ce n'est pas déjà fait.

Ce qui change pour Autonomes : **on tutoie**, toujours, sans exception, dans toutes les ressources. Les ressources déjà en ligne vouvoient encore : elles seront migrées, on ne s'aligne pas sur elles. Le registre est plus sobre que dans les emails ou la newsletter de Manu : pas d'anecdote d'ouverture obligatoire, pas de mouvement de pensée en quatre temps. On entre directement dans le sujet. Les emojis : au plus un, en fin de ressource, jamais dans une étape.

## Les trois mots : clair, simple, direct

**Clair** : le lecteur ne doit jamais avoir à deviner. Un mot technique est expliqué la première fois qu'il apparaît, en une phrase, entre parenthèses ou en apposition (« un dépôt, c'est le dossier de ton projet chez GitHub »), ou remplacé par un mot courant. Si l'explication demande un paragraphe, c'est qu'il manque une fiche : on la lie plutôt que de l'écrire ici.

**Simple** : entre deux formulations, la plus courte. Une phrase, une idée. Des verbes concrets (« clique », « tape », « ouvre ») plutôt que des nominalisations (« procéder à l'ouverture »).

**Direct** : on dit quoi faire, on montre l'écran, on passe à la suite. Le pourquoi tient en une phrase, et seulement quand il évite une erreur. « Coche Add README, sinon Claude ne trouvera rien à cloner à l'étape 3 » suffit ; le paragraphe sur ce qu'est une branche n'a pas sa place ici.

## La chasse au fluff

Le tuto « setup Claude, GitHub, Vercel » faisait 10 000 mots pour six étapes. La vidéo n8n en fait 900 pour cinq. Le deuxième est le modèle. Ce qui gonflait le premier, et qu'on ne fait plus :

- **Les justifications avant l'action.** Trois phrases pour expliquer pourquoi on commence par GitHub avant le premier clic. Le lecteur veut cliquer ; on lui dit où.
- **Les métaphores et l'ambiance.** « Il y a ce mur », « ce guide construit ce pont », « l'atelier qu'on prépare avant de faire venir l'artisan ». C'est du remplissage qui sonne marketing. On coupe.
- **Les annonces et les rappels.** « Avant ça, deux pages courtes… ne les sautez pas », « on y reviendra à l'étape 4 », « comme on l'a vu ». Une idée n'est dite qu'une fois, à l'endroit où le lecteur en a besoin.
- **Les doublons.** Le README expliqué dans l'étape, puis dans un callout de 90 mots, puis dans un accordion. Une fois, au bon endroit.
- **Les pages avant la première action.** « Comment fonctionne le système », « Ce qu'il te faut avant de commencer » : deux pages avant l'étape 1. Les prérequis tiennent en trois lignes dans l'intro ; le fonctionnement s'explique en un schéma, ou pas du tout.
- **La description à la place de l'image.** « Dans la colonne de gauche, à côté de Top repositories, le bouton vert New » : une capture annotée le montre en une seconde. Le texte dit l'action, l'image montre où.
- **Le dépannage en bloc final.** Une page « Quand ça coince » de 700 mots en fin de parcours. L'erreur fréquente se signale à l'étape où elle arrive, en une ligne, dans un callout `warn`.
- **Le bullshit marketing.** « Le setup professionnel », « une fois pour toutes », « le prix d'une installation qu'on ne refait jamais », promesses chiffrées non tenues. On dit ce que le lecteur obtient, combien de temps ça prend, ce que ça coûte. Rien de plus.

Test à chaque paragraphe : si on le supprime, le lecteur perd-il quelque chose pour faire ou comprendre ? Non : on le supprime.

## Les quatre types

Une ressource a un type, et un seul, qui dit ce que le lecteur fait avec :

| Type | Ce que c'est | Ce que le lecteur fait |
|---|---|---|
| **tuto** | un guide, une procédure qui aboutit à un résultat | il fait, en suivant |
| **fiche** | un contexte détaillé : une notion, une pratique, un outil, un modèle à copier | il comprend |
| **cheatsheet** | une liste d'éléments à retrouver | il retrouve |
| **exercice** | une tâche à accomplir soi-même, avec un résultat attendu | il s'entraîne |

Le test pour choisir : qu'est-ce que le lecteur fait quand il a fini de lire ? Il a un résultat à l'écran (tuto), il a compris une chose (fiche), il a trouvé ce qu'il cherchait (cheatsheet), il a produit quelque chose par lui-même (exercice). Un guide en dix pages reste un tuto ; il n'y a pas de type « cours ». Un prompt ou un CLAUDE.md à copier est une fiche dont le cœur est un module `prompt` ou `code`. Le type est aussi ce qui donne la rampe de ciel de la cover (`composer-une-cover-de-ressource`).

## Structure par type

**Fiche**. Une seule page, 500 à 900 mots, 6 à 9 modules. Ouverture en deux ou trois phrases qui disent de quoi on parle et pourquoi ça compte pour le lecteur, sans titre au-dessus. Puis des sections `heading` niveau 2 qui portent chacune une idée. Fermeture courte : le réflexe à retenir en une phrase, et le lien vers la ressource suivante.

**Tuto**. Une page d'intro de 100 à 150 mots : ce que tu obtiens à la fin (une liste de 2 à 4 points), le temps que ça prend, ce qu'il te faut (une ligne), la vidéo si elle existe. Puis une sous-page par étape, titrée par l'action seule (« Créer le dépôt », « Connecter Claude à GitHub » ; jamais « Étape 1 — … », l'ordre des pages donne déjà le numéro et le tiret est interdit), 200 à 400 mots chacune, avec un module `steps` pour la procédure, une image par écran que le lecteur voit, et au plus un callout `warn` pour l'erreur fréquente de l'étape. Un tuto complet tient en 2 000 à 3 000 mots ; au-delà, il y a du fluff ou deux tutos.

Quand la procédure est portée par une vidéo, le texte ne la répète pas : il donne les repères (les étapes avec le minutage), les valeurs à copier, les erreurs fréquentes. C'est le modèle de la ressource n8n.

Un tuto long qui enchaîne des notions plutôt que des écrans (« Bien commencer avec Claude Code ») garde la même forme : intro courte, une sous-page par notion construite comme une fiche courte, et reste sous 4 000 mots ; sinon on le découpe en deux tutos.

**Cheatsheet**. Des tableaux `élément / ce que c'est` ou `commande / ce qu'elle fait`, groupés par contexte, une ligne d'intro, pas de prose entre les tableaux. Une seule page.

**Exercice**. Une seule page, 300 à 800 mots. Dans l'ordre : ce que tu vas produire et le temps que ça prend (deux phrases) ; ce qu'il te faut (une ligne, avec le lien vers le tuto ou la fiche qui prépare) ; la consigne, en un module `steps` court ou un `prompt` de départ ; le résultat attendu, montré par une image ; et une fermeture qui donne une variante pour aller plus loin. L'exercice ne réexplique rien : il renvoie à la fiche qui explique.

## Les modules

Chaque module a un rôle. Les utiliser pour ce rôle, pas pour varier la mise en page.

- `text` : la prose. Paragraphes de une à trois phrases. Les sections d'une fiche se marquent avec `## ` dans le markdown ou avec un module `heading` niveau 2 ; ne pas mélanger les deux dans une même ressource.
- `steps` : toute procédure. Chaque étape a un titre qui dit l'action et un corps de une à quatre phrases. Une étape, un geste.
- `image` : un écran à voir, un schéma qui remplace un paragraphe. Toujours avec `alt` (ce que montre l'image, pour qui ne la voit pas) et une `caption` d'une ligne qui dit où regarder. Dans un tuto, viser une image pour 80 à 120 mots.
- `callout` : `info` pour le temps, le coût, un prérequis ; `warn` pour l'erreur fréquente ; `success` pour le réflexe à garder. Au plus un par page ; s'il en faut trois, le texte est mal construit.
- `prompt` : un texte à copier tel quel dans Claude. Titre court, prompt complet, jamais tronqué.
- `code` : une commande ou un fichier à copier, avec `language` et `filename` quand il y en a un.
- `accordion` : seulement pour une bifurcation réelle (Mac ou Windows, avec ou sans compte) ou une définition que certains lecteurs connaissent déjà. Jamais pour cacher du texte qu'on n'a pas voulu couper.
- `comparison` : deux ou trois options côte à côte, quand la question du lecteur est « lequel ». Titres courts, corps de trois phrases.
- `video` : l'embed, avec une caption qui dit la durée.
- `cta` : au plus un, en fin de ressource, vers une suite concrète (le tuto suivant, l'exercice, la communauté). Jamais vers une offre commerciale dans une ressource d'apprentissage.
- `quote`, `file`, `embed`, `gallery` : rares, seulement s'il n'y a pas plus simple.

## Le maillage

Chaque ressource cite ses voisines par lien interne `/r/slug`, dans le texte, là où la notion apparaît : la fiche qui explique un mot, le tuto ou l'exercice qui met en pratique, la cheatsheet à garder ouverte. Deux à quatre liens par ressource, jamais une liste de liens en fin de page.

## La description

La description d'une ressource fait deux ou trois phrases : ce qu'elle contient, ce que le lecteur saura faire ou aura à la fin, le temps que ça prend. Pas de promesse, pas de « complet », pas de question rhétorique. Elle sert dans le catalogue et dans les partages.

## Checklist avant de rendre la main

- [ ] Tutoiement du début à la fin
- [ ] Chaque mot technique expliqué à sa première apparition, ou lié à sa fiche
- [ ] Aucune métaphore, aucune phrase d'ambiance, aucune annonce, aucun rappel
- [ ] Chaque idée dite une seule fois
- [ ] Le pourquoi tient en une phrase et évite une erreur ; sinon supprimé
- [ ] Un seul type, choisi par ce que le lecteur fait ; longueur dans la fourchette du type, et si dépassement, couper avant de découper
- [ ] Une image par écran dans un tuto, avec alt et caption
- [ ] Au plus un callout par page, accordions seulement pour une bifurcation
- [ ] L'erreur fréquente signalée à l'étape, pas dans une page à part
- [ ] Deux à quatre liens internes dans le texte
- [ ] Les règles d'`ecrire-comme-manu` : zéro tiret cadratin, zéro « , et », zéro tic IA, orthographe parfaite
- [ ] Au plus un emoji, en fin de ressource

## Boucle d'amélioration

Quand Manu coupe, reformule ou refuse un passage, chercher la règle qui aurait évité la correction et l'ajouter ici avec un exemple avant/après. Ce socle a commencé par le diagnostic d'un tuto trop long ; il grandit à chaque relecture.
