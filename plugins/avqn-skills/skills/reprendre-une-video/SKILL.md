---
name: reprendre-une-video
description: Tirer une nouvelle vidéo en préproduction d'une vidéo Contentos
  déjà finie — un autre propos, une autre coupe, pour une seule sortie. À
  charger quand la demande porte sur une vidéo existante à reprendre autrement,
  pas sur une matière neuve.
---

# Reprendre une vidéo

Une vidéo finie contient souvent plus qu'un propos. Une qui a marché mérite un
autre angle ; une de trois minutes contient une idée qui tient en quarante
secondes ; une dont l'ouverture a manqué mérite une seconde chance.

La reprise est la même marche qu'un repurpose, pour **une seule sortie**. Le skill `repurposer` porte le détail de chaque geste —
lire un transcript, borner un extrait, cadrer, vérifier ce qui apparaît. Ici,
ce qui change.

## Choisir la source

Une vidéo finie devient un rush en un geste :

```
deposer_rush { nom, video: "<slug de la vidéo>" }
```

La vidéo doit être **`finalisee` ou `publiee`** — c'est son fichier de sortie
que le rush copie, et il n'existe pas avant. Une vidéo encore en montage ou en
revue se reprend par la livraison d'une de ses captations, plus bas. Le serveur
en fait une copie interne, la sonde et la transcrit. C'est le chemin court, et
c'est celui qu'on prend par défaut.

**Regarde d'abord ce que cette vidéo porte dans ses pixels.** Un rendu fini
emporte son habillage : ses sous-titres incrustés, son hook, ses cartes, ses
mots à l'écran. Un extrait les emporte avec lui. Deux conséquences, et elles se
disent dans l'intention : le montage ne devra pas re-sous-titrer par-dessus des
sous-titres qui sont déjà là, et l'habillage d'origine ne doit pas contredire le
nouveau propos — une accroche de l'ancienne vidéo qui réapparaît au milieu de la
nouvelle sonne comme une erreur.

**Quand la parole nue vaut mieux**, prends la livraison d'une captation
d'origine plutôt que le rendu :

```
voir_video { slug }                        → captations[].url_livraison
deposer_rush { nom, url: "<url_livraison>" }
```

C'est l'image et la voix sans un seul élément d'habillage. Le lien est signé
pour une heure : dépose dans la foulée.

## Ce qui reste à décider

Il n'y a pas de série, donc pas de table de décisions à tenir sur dix vidéos.
Les mêmes questions se posent quand même, une fois :

- **Le propos.** Pas celui de la vidéo d'origine. Si le nouveau propos est le
  même dit autrement, il n'y a pas de reprise à faire — il y a un montage à
  refaire, et ce n'est pas ton geste.
- **La durée**, et sa tolérance de ± 30 %.
- **L'ouverture**, et la phrase de la matière qui la tient — c'est presque
  toujours la raison d'être de la reprise.
- **Ce qui apparaît à l'écran**, si la source montre un écran.

## La marche

1. **Lis le transcript** — `voir_rush { slug, de, a }`, par fenêtres, avec une
   minute de marge autour de chaque plage retenue. Le champ `coupe` de la
   réponse dit avec quel `de` redemander la suite.
2. **Écris le plan** : le propos en une phrase, la phrase d'ouverture que la
   matière tient, les extraits bornés, le cadrage, la durée estimée.
3. **Critique-le** — les cinq points de `repurposer`, montrés à l'auteur et
   passés à un sous-agent à contexte vierge. Une reprise rate au
   même endroit qu'un short : une chute tronquée, un silence compté comme
   matière, une ouverture que la matière ne tient pas.
4. **Pose** : `lister_videos` pour ne pas doublonner un titre, `nouvelle_video`,
   les extraits par `extraire_prise`, puis l'intention dans l'`idee`.

La vidéo reste en préproduction : son script s'écrira avec l'auteur.

## Le cadrage d'une source déjà verticale

Une vidéo Contentos est déjà en 9:16. Elle n'a rien à recadrer : le mode `plein`
couvre le cadre et rend l'image telle qu'elle est. Les autres modes existent
pour une source large ; les appliquer à une source verticale rétrécit l'image
sans rien gagner.

## Ce qui ne se fait pas

- **La vidéo d'origine ne se touche pas.** Elle garde son slug, son fichier, sa
  publication. La reprise est une vidéo neuve, avec son propre slug.
- **Le titre de la reprise dit son propos à elle.** Reprendre le titre d'origine
  avec un suffixe donne deux lignes indistinguables au backlog.
- **Une reprise ne renvoie pas à l'originale.** Personne ne l'a vue, et personne
  n'ira la voir. Elle tient seule ou elle ne tient pas.
