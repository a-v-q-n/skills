---
name: relire-un-skill
description: >-
  À utiliser pour relire un skill AVQN (marketplace « avqn » — plugins avqn-skills et avqn-dev)
  contre les règles de la maison et rendre un rapport : un skill publié, un skill en cours
  d'écriture, ou un lot (« audite les skills »). Même si Manu dit seulement « relis-moi ce
  skill », « il est bon ? », « pourquoi ce skill ne se déclenche jamais », « qu'est-ce qui cloche
  dans emettre-une-offre ». Passe d'abord la conformité (`skill_check`), puis juge ce qu'aucun
  linter ne tranche : la description qui déclenche et sa limite, skill-ou-references, le socle de
  la bonne famille, le poids du corps, la mécanique serveur redocumentée. Lecture seule : n'écrit
  jamais dans le dépôt. Charge d'abord avqn-skill-authoring. NE COUVRE PAS l'écriture ou la
  correction du skill (avqn-skill-authoring), ni la relecture d'une ressource Autonomes.
couche: recette
moment: >-
  Le crible d'un skill : conformité, puis déclenchement, classement, composition, poids. Lecture
  seule.
---

# Relire un skill

Commencer par charger **`travailler-sur-un-repo`** (le socle de la famille dev : calibre, contrat
du dépôt, surface) puis **`avqn-skill-authoring`** (le socle dont ce skill est le crible). Un
rapport ne cite jamais une règle qui n'est pas dans l'un des deux — ou dans le `CLAUDE.md` du
dépôt `skills`.

Ce skill prend un skill, le passe contre les règles de la maison, et rend à Manu un rapport court
qui dit ce qui tient, ce qui casse, et par quoi commencer. Il ne corrige rien : la correction est
un autre geste, sur décision de Manu.

Il sert à deux moments. Avant publication, sur un skill fraîchement écrit, pour attraper ce que
l'auteur ne voit plus. Après, sur un skill publié qui ne se déclenche pas, ou qu'on soupçonne
d'avoir dérivé.

## 1. La conformité d'abord

Trois chemins vers la même vérité — marketplace et `plugin.json` valides, frontmatter complet,
`name` égal au dossier, aucun champ `version`, table du README à jour. Prendre le premier
disponible :

1. `skill_check` (connecteur AVQN OPS), quand la conversation n'a pas le dépôt sous la main ;
2. `/check-skills`, depuis une session attachée au dépôt `skills` ;
3. `python3 scripts/skills.py check` dans un clone du dépôt.

Aucun des trois n'est joignable — pas de connecteur `ops`, pas de dépôt — alors **le dire et
continuer** : le rapport s'ouvre sur « Conformité : non vérifiée, ni `skill_check` ni le dépôt
n'étaient joignables », et porte sur les six questions seules. Un rapport de jugement sans la
conformité vaut mieux que pas de rapport ; un rapport qui tait le trou ne vaut rien.

C'est binaire et ça se règle sans discussion : ce que la conformité rend est **rapporté tel
quel**, en tête du rapport, jamais reformulé en jugement. Le reste de la relecture porte sur ce
qu'aucune ligne de Python ne tranche.

## 2. Charger la matière

- Un skill publié : `skill_get` (le `SKILL.md` et l'arbre de ses fichiers annexes) ; à défaut,
  lire `plugins/<plugin>/skills/<nom>/` depuis un clone du dépôt.
- Un skill en cours d'écriture : lire le fichier tel quel.
- Un lot : `skill_list` pour l'inventaire — ou l'arborescence de `plugins/*/skills/` — puis le
  contenu de chaque skill retenu.

Lire le skill **en entier**, fichiers `references/` compris — un défaut de composition ne se voit
que là.

## 3. Les six questions

Dans cet ordre. Chacune cite le passage fautif (dix mots suffisent) et dit ce qu'il faudrait.

1. **La `description` déclenche-t-elle ?** Elle est le seul texte qui décide du chargement. Elle
   porte les mots que Manu emploie vraiment (« relis-moi ça », « on candidate », « il est bon ? »),
   pas le vocabulaire interne du skill. Une description qui décrit le contenu au lieu de nommer
   l'occasion ne se déclenche jamais.
2. **Pose-t-elle sa limite ?** Un « NE COUVRE PAS … » explicite, qui nomme le skill voisin vers
   lequel renvoyer. Sans limite, deux skills se disputent la même conversation. Vérifier aussi
   que la limite est **juste** : elle exclut ce que le skill ne fait pas, pas ce qu'il fait.
3. **Est-ce un skill, ou un `references/` déguisé ?** Le critère est l'usage indépendant : on
   l'invoque seul, ou plusieurs recettes le réutilisent. Un bloc qui ne sert qu'à un seul parent
   est un fichier de ce parent — le dire, et nommer le parent.
4. **La recette charge-t-elle le socle de *sa* famille ?** `ecrire-comme-manu` pour le cycle
   client, `ecrire-mes-ressources` (+ `titrer-une-ressource`) pour le contenu Autonomes,
   `ecrire-mes-videos` pour la vidéo, `travailler-sur-un-repo` pour la méthode de dev. La voix
   écrite, la voix des ressources et la voix parlée sont trois crafts distincts : charger le socle
   d'une autre famille est un défaut bloquant, pas une approximation.
5. **Le corps tient-il ?** Sous 500 lignes, les détails longs poussés en `references/` — et les
   références **à un niveau**, jamais une référence qui en appelle une autre. Un corps qui déborde
   se relit en cherchant ce qui part en `references/`, pas en coupant.
6. **Redocumente-t-il la mécanique du serveur ?** Le fonctionnement des objets d'AVQN OS (partie,
   deal, projet, facture, note…) vit dans `grammaire {domaine}` côté serveur et se périme ici. Un
   skill porte le craft et le jugement ; il cite les outils par leur nom d'usage
   (`invoice_render_pdf`) sans réexpliquer le domaine.

Puis les points que la conformité couvre déjà, et qu'on ne recontrôle pas à la main : `name` en
kebab-case sans accent identique au dossier, `couche`/`moment` présents, absence de `version`.
S'ils remontent de l'étape 1, ils s'ouvrent le rapport ; sinon on n'en parle pas.

## 4. Le rapport

Toujours ce format, en français, sans « Salut Manu » ni formule de fin :

```
## <nom-du-skill> (<plugin>, <couche>)

**Conformité.** <vert, ou la liste brute de ce que skill_check remonte>

**Verdict.** <une phrase : publier, retoucher, ou repenser le découpage>

**Ce qui casse, par ordre d'importance.**
1. <la règle> : <citation courte> → <ce qu'il faudrait>
2. …
(5 points au plus ; le reste va dans « aussi »)

**Aussi.** <les points mineurs, en une ligne chacun>

**À garder.** <ce qui est juste et se recopie tel quel>

**Déclenchement.** <ok, ou la description corrigée, réécrite en entier>

**Par où commencer.** <le premier geste, en une phrase>
```

Cinq points forts au plus : un rapport de trente lignes ne sert à personne. Quand la
`description` ne va pas, la **réécrire en entier** dans « Déclenchement » — c'est le seul endroit
où le rapport propose du texte fini, parce que c'est le texte qui décide de tout le reste.

Pour un lot (« audite les skills »), un rapport par skill dans le même message, précédé d'un
tableau d'une ligne par skill : nom, plugin, couche, lignes, verdict.

## Ce qui reste toujours vrai

- **Lecture seule.** Aucun `skill_upsert`, aucun `skill_delete`, aucune écriture de fichier, même
  pour « juste corriger la description ». La correction est un autre geste, sur décision de Manu.
- Chaque point cite la règle qu'il applique (`avqn-skill-authoring` ou le `CLAUDE.md` du dépôt).
  S'il n'y a pas de règle, c'est un avis, et il se présente comme tel, à la fin.
- Une règle qui manque au socle et qui aurait attrapé un défaut réel s'ajoute au socle, avec
  l'exemple — dans un autre geste, signalé en fin de rapport.
