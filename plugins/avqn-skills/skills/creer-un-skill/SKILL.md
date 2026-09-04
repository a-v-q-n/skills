---
name: creer-un-skill
description: >-
  À utiliser dès qu'un skill AVQN doit être posé, modifié ou retiré de la marketplace « avqn »
  (dépôt a-v-q-n/skills, plugins avqn-skills et avqn-dev) — même si Manu dit seulement « crée-moi
  un skill pour… », « fais-en un skill », « on en fait une recette », « ajoute ça à
  emettre-une-offre », « ce skill ne sert plus », ou raconte un geste qu'il refait souvent. Porte
  la séquence et les jalons : capter l'intention (souvent déjà dans la conversation), choisir le
  plugin, trancher skill ou pas, écrire le brouillon, éprouver le déclenchement sur de vraies
  phrases, poser par le secteur `skill_` d'AVQN OPS, faire relire, publier. Charge d'abord
  avqn-skill-authoring. NE COUVRE PAS les conventions elles-mêmes (avqn-skill-authoring), le
  crible d'un skill existant (relire-un-skill), ni le contenu métier du skill à écrire, qui vient
  de Manu.
couche: recette
moment: >-
  De l'intention au skill publié : capter, choisir le plugin, écrire, éprouver le déclenchement,
  poser, faire relire.
famille: outillage
---

# Créer un skill

Commencer par charger **`avqn-skill-authoring`** — les conventions : classement, plugins,
anatomie, frontmatter, publication. Ce skill ne les redit pas ; il porte la **séquence** et les
**jalons de validation**.

Trois gestes vivent ici : poser un skill neuf (§1 à §6), en modifier un, en retirer un (§7).

## 1. Capter l'intention

Le skill est souvent déjà là, sous les yeux : Manu vient de faire le geste, ou de le décrire.
Tirer de la conversation ce qu'elle contient déjà — les outils appelés, leur ordre, les
corrections de Manu en cours de route, ce qui entrait et ce qui sortait — **avant** de poser la
moindre question. Interviewer sur ce qu'on a sous les yeux fait perdre confiance.

Puis combler les trous, et seulement eux :

- Quel **moment** déclenche ce skill ? Pas ce qu'il fait — quand il sert.
- Quelles **phrases** Manu dirait vraiment pour l'appeler.
- Ce qu'il **rend** à la fin, et à qui.
- Où il **s'arrête**, et quel skill voisin prend le relais.

## 2. Choisir le plugin, puis la famille

Ce choix vient **avant** l'écriture : il fixe le frontmatter et le socle que le skill composera.
Se tromper ne range pas mal — ça produit un skill qui charge le mauvais socle.

- Le skill sert le **métier** (un client, du contenu, une vidéo) ou **l'outillage des skills**
  eux-mêmes → `avqn-skills`. Il porte alors une `famille`, et composera son socle :
  `cycle-client` → `ecrire-comme-manu`, `contenu-autonomes` → `ecrire-mes-ressources`
  (+ `titrer-une-ressource`), `video-contentos` → `ecrire-mes-videos`, `outillage` →
  `avqn-skill-authoring`.
- Il sert la **méthode de dev** sur un dépôt → `avqn-dev`, sans `famille`, socle
  `travailler-sur-un-repo`.

## 3. Trancher : skill, `references/`, ou rien

Le critère skill-ou-référence vit dans le socle. La question en amont est autre : **est-ce que ce
geste s'est produit pour de vrai, plus d'une fois ?** Un skill écrit par anticipation ne se
déclenche jamais, et sa description encombre celle des autres.

Passer `skill_list` sur le plugin retenu au §2 : voir qui couvre déjà ce terrain.

Trois issues :

- un moment récurrent, avec son craft à lui → **un skill** ;
- un détail d'un skill qui existe → un fichier `references/` de ce parent, ou une section de son
  corps → c'est le geste « modifier » (§7) ;
- une fois, sans lendemain → **rien**. On le fait à la main et on passe.

Annoncer la décision à Manu, avec sa raison, avant d'écrire une ligne.

## 4. Écrire le brouillon

**La `description` d'abord**, le corps ensuite : c'est elle qui décide du chargement, donc de
tout le reste. Le corps porte la séquence et les jalons — pas un cours sur le domaine.

Le brouillon se lit **dans la conversation**, jamais dans le dépôt. Manu valide avant qu'on pose
quoi que ce soit.

## 5. Éprouver le déclenchement

Avant de poser, pas après. Écrire **2 ou 3 phrases que Manu dirait vraiment** — sa formulation à
lui, dans son registre, surtout pas une paraphrase de la description.

Pour chacune, deux questions :

1. La `description` la capte-t-elle ?
2. Un skill voisin la capterait-il **mieux** ? (`skill_list` pour les voir tous.)

Quand un voisin gagne, c'est que la frontière est floue : corriger le `NE COUVRE PAS` **des
deux** skills, pas d'un seul. Et corriger la description, jamais les phrases de test — une phrase
qu'on reformule pour qu'elle passe ne prouve rien.

## 6. Poser, faire relire, publier

Par le secteur `skill_` d'AVQN OPS, qui marche depuis n'importe quelle conversation ; à défaut,
depuis une session attachée au dépôt.

1. `skill_upsert` avec `dry_run: true` — le rapport complet, sans une ligne écrite.
2. Le même appel sans `dry_run`.
3. Le serveur régénère la table du README et **refuse le commit** si la conformité tombe : ce
   qu'il rend en `problemes` se corrige, ce qu'il rend en `avertissements` traînait déjà ailleurs.
4. Garder l'URL du commit qu'il rend — c'est la trace de l'écriture.

Puis passer le skill à **`relire-un-skill`** et traiter son rapport avant d'annoncer que c'est
fini. La conformité est binaire, la qualité ne l'est pas.

Le push **est** la publication : ni CI, ni image, ni déploiement. Dire à Manu que le nouveau skill
n'apparaîtra pas dans la conversation en cours — le jeu de skills est figé à l'ouverture d'une
session.

## 7. Modifier, retirer

**Modifier** — `skill_get` d'abord, **toujours**. Le serveur refuse de lui-même ce qui doit
l'être ; ce piège-là, non : `skill_upsert` remplace le dossier en entier, et une annexe qu'on ne
renvoie pas dans `fichiers` disparaît sans un mot. Si la `description` bouge, rejouer §5 — c'est
le déclenchement qui change.

**Retirer** — avant `skill_delete`, chercher qui cite ce skill : les voisins le nomment dans leur
`NE COUVRE PAS`, les recettes le nomment dans leur composition. Corriger ces renvois d'abord,
sinon on laisse des pointeurs morts qui survivront des mois.

Changer un skill de plugin n'est pas un geste : c'est une pose dans le plugin d'arrivée, puis une
suppression dans celui de départ — dans cet ordre, pour qu'il ne manque jamais.

## Ce qui reste toujours vrai

- La `description` avant le corps, et le corps sert la description — pas l'inverse.
- Rien ne se pose sans que Manu ait lu le brouillon.
- Un skill naît d'un geste déjà fait, jamais d'une anticipation.
- Le dépôt `skills` est **public** : aucun secret, aucun nom de client, aucun montant, aucune
  donnée d'affaire dans un skill. Les exemples s'inventent.
