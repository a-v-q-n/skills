---
name: preparer-une-video
description: >-
  À utiliser dès que Manu veut créer une vidéo Contentos à partir de n'importe quelle
  matière : un PDF, un article, une simple idée dite en une phrase, un sujet à creuser par
  la recherche, des notes, un rush. Porte la méthode de préparation : analyser la matière à
  fond, extraire les idées fortes, proposer des hooks, bâtir un plan séquencé où chaque
  passage a son asset, et valider étape par étape avant de rien verrouiller. Charge d'abord
  le socle ecrire-mes-videos pour la voix. NE COUVRE PAS la fabrication des gabarits et
  images (fabriquer-les-assets), la voix off (produire-la-vo) ni le script de montage final
  (scripter-le-montage).
---

# Préparer une vidéo

Ce skill est une recette : il mène de la matière brute au script validé, jalon par jalon.
Il ne porte aucune règle de voix, elles vivent dans `ecrire-mes-videos` — le charger avant
d'écrire la moindre ligne destinée à être dite.

## La matière peut être n'importe quoi

Le point d'entrée est libre, et la recette s'adapte :

- **Un document** (PDF, article, deck, notes) : le lire EN ENTIER avant tout. L'analyse
  d'abord, les idées ensuite.
- **Une simple idée** (« je veux faire une vidéo sur X ») : creuser le sujet — recherche
  web, docs, ce que l'OS sait — jusqu'à avoir une matière assez profonde pour une vidéo qui
  apprend quelque chose.
- **Un rush ou une matière brute Contentos** : partir de ce qu'il contient.
- **Un mélange** : tout est bon à prendre.

Le critère de sortie est le même dans tous les cas : pouvoir énumérer les idées fortes —
celles qui changent la façon de voir le sujet, pas un résumé.

## La séquence

1. **Analyser la matière** et restituer à Manu ce qu'on en retient, en quelques idées
   fortes numérotées. C'est la base de la discussion.
2. **Clarifier les choix de cadrage** : le hook (en proposer 3-4, styles différents, avec
   une recommandation), le format et la durée visée, s'il faut citer la source ou se
   réapproprier le contenu.
3. **Ouvrir la vidéo tôt** (`nouvelle_video` avec idée + titre + slug parlant) : le slug
   sert à réserver les assets dès leur création.
4. **Bâtir le plan séquencé** : chaque séquence = un passage de VO + l'asset qui l'illustre
   (gabarit animé, image, insert). Le cœur du propos reçoit l'asset le plus travaillé.
   Vérifier dans `lister_assets` ce que la librairie couvre déjà avant de prévoir du neuf.
5. **Faire valider le plan** avant toute production d'asset.
6. **Valider le ton** sur un échantillon (le hook suffit) avant d'écrire le script entier —
   Manu itère sur la formulation, et chaque correction vaut règle pour la suite.
7. **Écrire le script complet** et le présenter dans la conversation.

## Les garde-fous

- **Le script se verrouille à l'envoi** : `modifier_video` avec le champ `script` ferme le
  script et le fait partir à la fabrique. Ne JAMAIS le poser sans le OK explicite de Manu
  sur le texte intégral.
- **Valider par étapes**, jamais en bloc : le plan, puis le ton, puis le script. Ça évite
  de refaire trois fois.
- **Pas de template de vidéo** : le nombre de séquences, la durée, la structure viennent de
  la matière et du format choisi — pas d'un moule.
- Ordres de grandeur utiles (à adapter, pas à imposer) : ~150 mots par minute de VO ; un
  format 3 min ≈ 450 mots ; un hook = 2 phrases.

## Ce qui suit

Une fois le script validé : `fabriquer-les-assets` pour les gabarits et images,
`produire-la-vo` pour les prises, `scripter-le-montage` pour le script final lié et le
découpage des plans.

## Checklist avant de rendre la main

- [ ] La matière a été lue ou creusée en entier, les idées fortes restituées à Manu
- [ ] Le hook retenu vient d'un choix de Manu parmi plusieurs propositions
- [ ] Le plan séquencé est validé : chaque séquence a son passage de VO et son asset
- [ ] La librairie a été consultée (`lister_assets`) avant de prévoir un asset neuf
- [ ] Le ton a été validé sur un échantillon avant le script entier
- [ ] Le script complet a été validé par Manu — et rien n'a été posé dans `modifier_video`

## Boucle d'amélioration

Quand Manu corrige une formulation, la correction vaut règle pour tout le reste du script.
Si elle vaut au-delà de cette vidéo, elle se capitalise : dans `ecrire-mes-videos` si c'est
la voix, ici si c'est la méthode.
