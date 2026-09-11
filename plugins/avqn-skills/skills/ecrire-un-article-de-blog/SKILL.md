---
name: ecrire-un-article-de-blog
description: >-
  À utiliser dès que Manu veut écrire un article du blog Autonomes à partir de n'importe
  quelle matière : une vidéo Contentos publiée, une actu à couvrir, une idée en une phrase,
  des notes, un raté qui mérite d'être raconté. Même s'il dit seulement « fais-moi
  l'article », « on passe la vidéo en article » ou « écris un papier sur X ». Porte la
  séquence et les jalons : choisir le type (fiche ou actu), proposer l'angle et le plan,
  faire valider, écrire, faire valider, construire l'article via le MCP Autonomes en
  brouillon, publier sur feu vert. À utiliser aussi par la routine de rédaction du dépôt
  redaction-routine, en mode routine : sans humain dans la boucle, les deux jalons de
  validation deviennent une porte qualité tenue par un second agent, et la publication
  suit. Charge d'abord le socle ecrire-comme-manu pour la voix. NE COUVRE PAS la cover
  (composer-une-cover-d-article), les ressources d'apprentissage (creer-une-ressource) ni
  la vidéo source (Contentos).
couche: recette
moment: >-
  De la matière à l'article publié : type, angle, plan, écriture, construction en brouillon.
famille: contenu-autonomes
---

# Écrire un article de blog

Le blog raconte ce que Manu construit avec l'IA : ce qui marche, ce qui casse, et ce que ça
change pour quelqu'un qui n'est pas développeur. Le lecteur est celui d'Autonomes —
curieux, pressé, non technique — et l'article lui parle en **tu**, à la première personne
de Manu.

**Charger d'abord le socle** : `ecrire-comme-manu` porte la voix, les règles non
négociables et la checklist anti-tics. Ce skill-ci ajoute ce qui fait un article : le type,
l'angle, l'anatomie, la construction dans Autonomes.

## Les deux types

- **Fiche** (tag `type:fiche`) : une notion, une méthode, un système que Manu a monté.
  L'article apprend quelque chose de durable. Souvent tiré d'une vidéo Contentos (tag
  `source:<slug-video>`, la vidéo embarquée en tête d'article).
- **Actu** (tag `type:actu`) : une nouveauté et ce qu'elle change. La colonne vertébrale
  qui marche : ce qui change, les faits (chiffres et sources liées), puis « faut-il t'en
  occuper maintenant ? » — avec une vraie réponse, y compris « rien, tu peux ignorer ».

Dans les deux cas, l'honnêteté prime sur l'effet : les chiffres citent leur source, les
réserves se disent (« ces chiffres viennent d'Anthropic, qui est juge et partie »), et un
raté de Manu se raconte comme un raté.

## La matière

Une vidéo Contentos est la matière la plus fréquente : l'article se **réapproprie** le
propos à l'écrit, il ne transcrit pas la VO. Reprendre les idées fortes, les réorganiser
pour la lecture, ajouter ce que la vidéo n'avait pas la place de dire. Pour une actu,
vérifier les faits du jour (dates, versions, chiffres) dans les sources plutôt que de
mémoire, et lier ces sources dans le texte.

## La séquence

1. **Jalon 1 : l'angle et le plan.** Proposer à Manu en un message court : le type (fiche
   ou actu), l'angle en une phrase, le plan (les sections `heading` niveau 2), deux ou
   trois candidats de titre et de chapô, les tags (`niveau:`, `outil:`, `type:`, `source:`
   s'il y a une vidéo) et les liens internes prévus. Attendre la validation.
2. **Jalon 2 : le texte.** Écrire l'article complet dans un fichier de travail, chaque
   module annoté par son type (`[text]`, `[heading]`, `[callout warn]`, `[comparison]`,
   `[video]`, `[cta]`). L'envoyer en entier à Manu, sans « Salut Manu » ni formule de
   clôture. Attendre la validation ; capitaliser les corrections qui révèlent une règle.
3. **Construire.** `article_create` avec titre, slug, chapô, tags et **rubrique**
   (`categorieSlug` : `actualites` pour une actu, la rubrique du geste pour une fiche) —
   l'article naît en brouillon, jamais publié d'office. Puis `article_add_modules` dans
   l'ordre du fichier, et relire le résultat (`article_get`) contre le fichier de travail.
4. **La cover.** Une fois le titre arrêté, `composer-une-cover-d-article` prend le relais
   (trois variantes, validation, `imageUrl` et `imageAlt` posés sur l'article).
5. **Publier** (`article_publish`) seulement sur le feu vert explicite de Manu. Le slug
   est une adresse : on ne le change plus après.

## Mode routine

Quand c'est la routine de rédaction du dépôt `a-v-q-n/redaction-routine` qui écrit —
elle le dit en tête de sa marche — il n'y a personne pour valider, et la séquence change
sur trois points, rien d'autre :

- **Les jalons 1 et 2 n'attendent personne.** L'angle, le plan, le titre et le chapô se
  décident depuis la matière de l'issue et `strategie.md` du dépôt ; le texte s'écrit en
  entier dans le fichier de travail, comme au jalon 2.
- **La porte qualité remplace la validation.** Un second agent, qui n'a vu ni les sources
  ni le raisonnement, note l'article sur dix points (la grille est dans
  `routines/redaction.md` du dépôt : réponse complète, apport introuvable ailleurs,
  tutoiement, chaque chiffre sourcé, zéro tic du socle, titre en langage de requête, fin
  qui ouvre, rubrique et tags cohérents, longueur qui suit le sujet, lisible par un
  non-dev). Sous huit, une réécriture puis un second passage ; toujours sous huit, ou un
  échec sur les chiffres ou la lisibilité, l'article ne sort pas et le sujet retourne au
  stock. La porte est la validation : ce qu'elle refuse, Manu l'aurait refusé.
- **La publication suit la porte**, sans feu vert : `article_publish` dès que l'article
  a sa cover (composée en mode routine, une variante contrôlée) et que `article_get` ne
  rend aucun manque. Manu relit après coup ; un article qu'il dépublie est un signal que
  le bilan du dépôt enregistre.

Tout le reste tient : la voix du socle, les deux types, l'anatomie, le maillage, le CTA
seulement quand une ressource approfondit, le slug qu'on ne change plus.

## L'anatomie

- **Le titre** dit le fait, sans vendre. Contrairement aux ressources, un deux-points est
  permis (« Projet ou skill : lequel créer en premier ») et la première personne aussi
  (« J'ai automatisé mon montage vidéo »). Jamais de promesse gonflée ni de clickbait.
- **Le chapô** fait deux ou trois phrases sobres : ce que l'article contient, pourquoi ça
  compte pour le lecteur. C'est lui qu'on voit dans le catalogue et les partages.
- **L'ouverture** entre dans le sujet par le concret : la situation que le lecteur
  reconnaît, ou ce que Manu vient de vivre. Pas de rampe de lancement.
- **Le corps** : des sections `heading` niveau 2 qui portent chacune une idée, des
  paragraphes d'une à trois phrases, 500 à 900 mots au total. Un `callout` (`tip` ou
  `warn`) au plus pour LA chose à retenir ; un `comparison` quand la question du lecteur
  est « lequel des deux ».
- **Le maillage** : deux à quatre liens dans le texte — les articles voisins en lien
  relatif (`/slug`), les sources externes citées là où le fait apparaît.
- **La fin** : un module `cta` au plus, vers la ressource Autonomes qui approfondit, avec
  `?src=blog:<slug>` dans l'URL. Pas de conclusion qui résume : le dernier paragraphe
  ouvre sur la suite (la lecture qui complète, le geste à faire).

## Checklist avant de rendre la main

- [ ] Le type est choisi (fiche ou actu) et la structure suit celle du type
- [ ] Tutoiement du début à la fin, première personne de Manu assumée
- [ ] Chaque chiffre et chaque nouveauté a sa source, liée dans le texte
- [ ] Titre factuel, chapô en deux ou trois phrases sobres, 500 à 900 mots
- [ ] Deux à quatre liens dans le texte, un CTA au plus avec son `?src=blog:`
- [ ] Checklist anti-tics du socle `ecrire-comme-manu` passée
- [ ] La rubrique est posée (`categorieSlug`) : sans elle, l'article n'apparaît dans aucun hub
- [ ] L'article est né en brouillon ; publication sur feu vert explicite — ou, en mode
      routine, après la porte qualité

## Boucle d'amélioration

Ce skill est jeune : il vient des premiers articles publiés, pas encore de dizaines de
relectures. Quand Manu coupe, reformule ou refuse un passage, chercher la règle qui aurait
évité la correction et l'ajouter ici avec un exemple avant/après ; une question de voix va
dans `ecrire-comme-manu`. Un article publié par la routine que Manu dépublie ou corrige
vaut une relecture de la grille de la porte : ce qu'elle a laissé passer devient un point
de plus, ou un point plus dur.
