---
name: creer-une-ressource
description: >-
  À utiliser dès que Manu veut créer une ressource Autonomes (tuto, fiche, cheatsheet,
  exercice) à partir de n'importe quelle matière : une idée en une phrase, une
  vidéo tournée, des notes, un article, un PDF, une transcription. Même s'il dit seulement
  « fais-moi une fiche sur X », « on met la vidéo n8n en ressource » ou « écris le tuto ».
  Porte la séquence et les jalons : choisir le format, proposer le plan, faire valider,
  écrire, faire valider, titrer, illustrer, construire pages et modules via le MCP
  Autonomes, relire, publier sur feu vert. Charge d'abord ecrire-mes-ressources pour le
  contenu et titrer-une-ressource pour le titre. NE COUVRE PAS les règles
  d'écriture elles-mêmes (ecrire-mes-ressources), la relecture d'une ressource existante
  (relire-une-ressource) ni les articles du blog.
couche: recette
moment: >-
  De la matière à la ressource publiée : format, plan, écriture, titre, images, pages et modules.
famille: contenu-autonomes
---

# Créer une ressource

Ce skill est une recette : il déroule la séquence et tient les jalons. Il ne porte aucune règle d'écriture, elles vivent dans `ecrire-mes-ressources`, ni de règle de titre, elles vivent dans `titrer-une-ressource`. Charger ces deux socles avant de commencer. La mécanique du MCP (outils, formes des modules, tags, slug) est dans `references/mcp-ressources.md`, à lire au moment de construire.

Deux jalons structurent le travail, et rien n'est écrit dans Autonomes avant le second. Manu relit vite et corrige précisément ; ce qui lui coûte, c'est de découvrir une ressource construite sur un mauvais plan. D'où l'ordre : plan validé, texte validé, puis seulement la construction.

## 1. Comprendre la matière

Lire ou écouter tout ce que Manu fournit. Si c'est une vidéo, en tirer les étapes avec leur minutage, les valeurs à copier (commandes, réglages, prix), les moments où ça coince. Si c'est une idée en une phrase, poser à Manu les deux ou trois questions qui manquent (à qui ça s'adresse, ce que le lecteur doit savoir faire à la fin, ce qu'il a déjà sous la main), pas plus.

Appeler `ressources_list` pour voir ce qui existe : la nouvelle ressource doit se ranger dans le catalogue, lier ses voisines, ne pas doublonner.

## 2. Jalon 1 : le format et le plan

Proposer à Manu, en un message court :

- le **type** (tuto, fiche, cheatsheet, exercice), choisi par ce que le lecteur fera avec, et pourquoi celui-là ;
- la **promesse** en une phrase, dans les mots du lecteur : « à la fin, tu sais … » ;
- le **plan** : pour une fiche, les sections ; pour un tuto, la page d'intro puis une ligne par étape ou par sous-page ; pour une cheatsheet, les groupes de tableaux ; pour un exercice, la consigne et le résultat attendu. Marquer sur le plan chaque **image attendue** (quel écran, quel schéma) et chaque **valeur à copier** ;
- les **tags** selon la taxonomie (voir la référence) et les **liens internes** prévus ;
- deux ou trois **candidats de titre** selon `titrer-une-ressource`.

Attendre la validation. Manu corrige souvent le plan d'un mot ; c'est le moment le moins cher pour le faire.

## 3. Jalon 2 : le texte

Écrire la ressource complète selon `ecrire-mes-ressources`, module par module, dans un seul fichier Markdown de travail où chaque module est annoté par son type (`[text]`, `[steps]`, `[image: ce qu'elle montre]`, `[callout warn]`…). Ce fichier est ce que Manu relit : le lui envoyer en entier, avec la description et le titre retenu.

Quand le texte décrit une interface, une commande ou un prix, vérifier dans la documentation du jour plutôt que de mémoire, et lister à Manu en fin de message les deux ou trois points qu'il doit confirmer sur son propre écran (libellés en français, ce que montre réellement `/mcp`…). C'est lui qui a l'interface sous les yeux.

Passer la checklist du socle avant d'envoyer. Compter les mots par page et le dire : Manu a l'œil sur la longueur.

Le message à Manu est un message de travail, pas un email : pas de « Salut Manu », pas de formule de clôture, pas d'emoji. Le plan, le texte, les points à vérifier, et c'est tout.

Attendre la validation. Reprendre chaque correction dans le fichier, et noter celles qui révèlent une règle manquante pour l'ajouter au socle.

## 4. Les images

Une fois le texte validé, traiter les images marquées dans le plan avec `illustrer-une-ressource` : une maquette pour un élément d'interface, un schéma pour un concept, une capture annotée quand Manu fournit l'écran réel. Demander à Manu ses captures en une fois, avec la liste des écrans attendus, plutôt qu'une par une.

La cover suit `composer-une-cover-de-ressource` (trois variantes, validation de Manu, PNG versé à la Médiathèque et posé sur la ressource) : le charger une fois le titre retenu, puisque la cover le porte.

Chaque image a son `alt` et sa `caption` déjà écrits dans le fichier de travail.

## 5. Construire dans Autonomes

Lire `references/mcp-ressources.md`, puis :

1. `ressources_create` avec le titre, le slug, la description, les tags, la cover si elle existe. **Sans `published`** : la ressource naît en brouillon.
2. `ressources_get` pour vérifier la page racine ; l'ajouter avec `ressources_add_page` (slug `contenu`, titre = titre de la ressource) si elle n'y est pas.
3. Pour un tuto en plusieurs pages, `ressources_add_page` pour chaque sous-page, avec `parentId` = page racine et `position` dans l'ordre du plan.
4. `ressources_add_modules` page par page, dans l'ordre du fichier de travail, en respectant les formes de contenu de la référence.
5. `ressources_get` en fin de construction et comparer au fichier de travail : nombre de modules, ordre, aucun texte tronqué, chaque image avec son URL.

Donner à Manu le lien de prévisualisation et le récapitulatif : pages, modules, mots, images.

## 6. Relire et publier

Passer `relire-une-ressource` sur la ressource construite et transmettre son rapport à Manu avec le lien de prévisualisation. Un point qui casse se corrige avant de proposer la publication.

Publier (`ressources_update` avec `published: true`) **seulement sur le feu vert explicite de Manu**, jamais parce que la construction est finie. Épingler en vitrine (`pinned: true`) seulement s'il le demande. Rappeler qu'une ressource publiée est indexable et que son slug devient une adresse : on ne le change plus après.

## Ce qui reste toujours vrai

- Rien n'est écrit dans Autonomes avant le jalon 2.
- Le slug se choisit une fois, court, sans mot vide, dérivé du titre.
- Les liens internes pointent vers des slugs qui existent (vérifier dans `ressources_list`).
- Une correction de Manu qui révèle une règle va dans le socle, pas seulement dans le texte.
