---
name: repurposer
description: >-
  Tirer une série de vidéos en préproduction d'un enregistrement long — déposer le rush,
  lire son transcript, écrire le plan de série et le critiquer, puis poser chaque morceau :
  ses extraits cadrés et son intention. À charger dès que la demande porte sur un long form,
  un webinaire, un enregistrement d'écran ou une conférence à découper en plusieurs shorts.
couche: recette
moment: >-
  Un long form à découper — webinaire, conférence, enregistrement d'écran : N vidéos en préproduction, une par propos autonome.
famille: video-contentos
---

# Repurposer un long form

Un long form d'une heure donne une dizaine de vidéos. Chacune est une vidéo
Contentos à part entière : son slug, ses prises, son intention — et elle
s'arrête là, en préproduction, où l'auteur viendra écrire son script. Le rush,
lui, est déposé une seule fois et sert à toutes.

Quatre temps, qui ne se doublent pas : **déposer et lire**, **planifier**,
**critiquer le plan**, **poser morceau par morceau**. Le plan critiqué fait foi
pour la pose ; sans lui, chaque morceau se décide seul et la série se répète.

## Ce que l'auteur demande commande la série

Ce que l'auteur a dit fait foi, et se demande avant de lire le rush. Il peut
nommer **le compte** de vidéos, **l'angle** à tenir, **la plateforme**, **le
registre**, ce qu'il faut éviter. Chacun de ces points remplace ce que tu aurais
décidé seul, et se recopie tel quel en tête du plan de série.

**Ce qu'il n'a pas dit, demande-le avant de lire une heure de transcript.** Tu
es dans une conversation : une question posée maintenant coûte trente secondes,
une série découpée sur le mauvais angle coûte la journée.

**Un compte demandé est un compte tenu.** « Fais-moi douze vidéos » donne douze
entrées au plan, pas dix ni quinze — si la matière n'en porte pas douze qui
tiennent debout, tu en fabriques autant que possible et **tu dis pourquoi le
compte n'y est pas**, à l'auteur, avant de poser quoi que ce soit. Tu ne combles jamais un
compte avec un short qui n'a pas de propos.

**Un compte flou reste un choix.** « Quelques vidéos », « une petite série » :
propose un nombre, dis ce qui l'a décidé — le nombre de propos autonomes que le
rush porte, pas une cible ronde —, et laisse l'auteur trancher.

**Sans compte du tout**, c'est la matière qui décide : autant de vidéos que de
propos autonomes. Un long form d'une heure en donne une dizaine, mais c'est un
ordre de grandeur constaté, jamais une règle.

## 1. Déposer le rush et le lire

```
deposer_rush { nom, url }      un fichier accessible par son adresse
deposer_rush { nom, video }    le slug d'une vidéo finalisée ou publiée
lister_rushes
voir_rush { slug, de?, a? }
```

**Regarde d'abord `lister_rushes`** : la matière est souvent déjà là. Un partage
depuis le téléphone dépose un rush et s'arrête, et c'est précisément à ce
moment-ci qu'on le reprend.

Sinon, `deposer_rush` nomme **exactement une origine** : `url`, ou `video`. Le rush entre en
`recu`, puis le serveur le rapatrie, le sonde et le transcrit. Il passe `pret`
quand tout est là. **Rien ne se lit avant `pret`** : un transcript absent n'est
pas un rush court. Vérifie par `voir_rush`, et laisse le temps qu'il faut à une
heure de parole.

`voir_rush { slug, de, a }` rend le transcript lisible de la fenêtre demandée —
des lignes `m:ss  texte`, par phrases. C'est ce qui se lit. Sans `de` ni `a`, il
rend tout le rush ; au-delà de ce qui se lit d'un coup, il coupe et dit dans
`coupe` avec quel `de` redemander la suite. `url_verbatim` porte le mot à mot
daté : télécharge-le quand une borne se joue à la demi-seconde, pas avant.

Deux mentions de la fiche changent le travail. **`sans_parole`** : ni transcript
ni verbatim, donc la matière se choisit sur les planches d'images et toute la
parole vient de prises générées. **`sans_image`** : l'inverse, rien à cadrer.

**Lis par fenêtres**, cinq à dix minutes à la fois, en notant ce qui pourrait
porter un short : un rush lu d'un bloc ne se retient pas. Deux passes, une pour
repérer, une pour borner — et **relis chaque plage retenue avec une minute de
marge de chaque côté**. C'est là que se trouvent la vraie entrée, celle qui
commence une phrase, la chute que tu allais couper, et les raccords qui rendent
un extrait incompréhensible sorti de son contexte.

## 2. Le plan de série

Écris-le dans un fichier de ton scratch. C'est le seul document long de la
préparation, et il se lit deux fois : par la critique, puis par toi à chaque
short.

**La table de décisions vient en tête, et se décide avant le découpage.**
Chaque ligne engage toute la série ; la prendre short par short donne dix
décisions qui se contredisent.

- **Le compte de vidéos**, et d'où il vient : demandé par l'auteur, ou décidé
  sur la matière — et dans ce cas, ce qui l'a décidé.
- **La plateforme**, et ce qu'elle impose.
- **La durée cible** par short, et sa tolérance : **± 30 %**. Au-delà, le short
  se scinde ou se réduit — il ne s'étire pas.
- **Le registre.** Un extrait où l'auteur s'adresse autrement que le reste de la
  série se coupe quand la coupe est bon marché ; un résidu passe au milieu d'un
  tutoriel, jamais dans les vingt premières secondes.
- **La vigilance écran** : le relevé des plages à risque et leur verdict, plage
  par plage. La section 5 dit comment.
- **L'ordre de publication**, et ce qu'il évite : deux shorts du même sujet côte
  à côte, deux shorts qui ouvrent sur la même image.

**Puis une entrée par short**, et elle porte cinq choses :

- **le propos** — une ou deux phrases : ce que ce short avance, tout seul ;
- **l'ouverture** — sur quoi ce short commence, et ce que la matière tient pour
  la tenir ; le texte du hook, lui, s'écrira avec l'auteur ;
- **les extraits** — plage par plage, `m:ss–m:ss`, avec ce qui s'y dit ;
- **le traitement** — le cadrage retenu par plan, et ce qu'il faut éviter de
  montrer ;
- **la durée estimée** — la somme réelle, pas la cible.

**Un short est un propos autonome.** Personne n'a vu le long form, et personne
n'ira le voir. Aucun renvoi (« comme je le disais tout à l'heure »), aucune
suite implicite, aucun pronom qui désigne quelque chose de coupé. Un short qui
n'a pas de propos qu'on peut énoncer en une phrase n'est pas un short : c'est un
morceau.

**L'ouverture est tenue par la matière.** Nomme la phrase du transcript sur
laquelle le short pourra ouvrir. Un morceau dont aucune phrase ne tient
l'ouverture promet ce qu'il ne donnera pas — et c'est un défaut de découpe, pas
un défaut d'écriture : il se répare en bornant autrement, ou en ne retenant pas
le morceau.

## 3. Critiquer le plan

**Montre le plan à l'auteur, et fais-le critiquer à contexte vierge** — un
sous-agent à qui tu donnes le plan et le transcript, rien d'autre : celui qui a
écrit le plan défend ses choix au lieu de les voir. C'est le moment où une série
se répare pour rien, et où elle coûte cher si on le saute. Cinq points, short
par short.

1. **Le propos et les extraits.** Chaque plage existe-t-elle ? Dit-elle vraiment
   ce que le plan prétend ? Les bornes tombent-elles sur une frontière de
   phrase ? On vérifie ligne à ligne contre le transcript, pas de mémoire.
2. **L'ouverture.** La phrase nommée existe-t-elle ? La matière la contredit-elle
   trente secondes plus loin ?
3. **Ce qui manque, ce qui est de trop.** Un passage fort qu'aucun short ne
   prend ; du remplissage qui allonge sans avancer ; un passage assez fort pour
   mériter son propre short au lieu d'être un morceau d'un autre.
4. **La durée réelle.** La somme des plages, **moins les silences**. Un silence
   n'est pas de la matière : 245 secondes de plages brutes dont 46 de silence
   font 199 secondes de parole. Verdict binaire, réaliste ou pas.
5. **Le risque.** Ce qui apparaît à l'écran ; le registre ; la redite avec un
   autre short ; une affirmation périssable — un prix, une version — qui sera
   fausse dans trois mois.

Puis un regard d'ensemble : deux shorts qui se partagent le même plan (l'un des
deux le perd), le compte qui ne tombe pas juste — **contre ce que l'auteur a
demandé quand il a nommé un nombre**, contre la matière sinon —, les collisions
de sujet. À
chercher en premier, parce que ce sont les défauts qui reviennent : **les bornes
qui coupent les chutes**, **le silence compté comme matière**, **les durées
sous-évaluées d'un quart à moitié**, **le registre qui change au milieu**.

## 4. Poser un morceau

Dans cet ordre, pour chacun. **Relis `lister_videos`** avant de nommer : un
titre proche d'un autre déjà au backlog se voit à la publication, pas avant.

```
nouvelle_video { idee, titre?, slug? }
extraire_prise { slug, rush, de, a, nom?, cadrage: { mode, x?, zone?, boite_y? }, fond? }
```

**Les extraits deviennent les prises**, dans l'ordre où le morceau se déroulera :
chaque appel en pose une sur la vidéo, avec sa provenance, et le serveur la fait
recadrer, transcoder et dater. Nomme-la — un rang seul ne dit rien quand il y en
a huit.

**Aucune prise générée.** Le morceau n'a pas de hook en voix de synthèse, pas de
liaison, pas d'avatar : ce que tu poses est de la matière d'origine, et rien
d'autre. Ce qui manquera se fabriquera avec l'auteur, quand le script sera
décidé.

Deux refus coûtent un aller-retour : la vidéo doit être en **préproduction
ouverte** et le rush `pret`, et la fenêtre doit tenir dans la durée du rush. La
section 6 dit ce qu'elle a le droit de mesurer.

## 5. Cadrer, et vérifier ce qu'on montre

Une source 16:9 ne tient pas dans un cadre 9:16. Le mode décide de ce qu'on voit
et de ce qui se lit, et il se choisit **par plan**, pas par short.

| Mode | Ce qu'il fait | Ce qu'il sert |
|---|---|---|
| `plein` | une fenêtre verticale de la source, agrandie pour couvrir tout le cadre — aucun fond visible | un terminal, une colonne, un panneau de chat : une zone étroite où se passe l'action |
| `carre` | un carré pleine hauteur de la source, à l'échelle 1, posé sur le fond | montrer une interface sans perte de netteté — le défaut |
| `zone` | un rectangle choisi, agrandi pour remplir la largeur, posé sur le fond | **lire** une ligne d'interface, et éviter ce qu'on ne veut pas montrer |
| `large` | la source entière réduite en bande, posée sur le fond | une vue d'ensemble, une disposition — jamais pour lire |

`x` centre la fenêtre des modes `plein` et `carre` dans la source ; sans lui,
c'est le milieu. `zone` prend un rectangle par son **centre** et sa taille en
pixels source (`{ x, y, largeur, hauteur }`) : seize pixels de côté au moins, et
il doit tenir dans la source — le serveur le vérifie avant d'appeler la ferme.

**`carre` montre, `zone` fait lire.** En `carre`, un texte d'interface de
quatorze pixels dans la source en fait toujours quatorze : illisible sur un
téléphone. Une zone de quatre cents à neuf cents pixels de large l'agrandit
assez pour qu'on lise la ligne.

`boite_y` place le haut de la boîte dans le cadre. Les défauts sont bons : ils
laissent libres les bandes du haut et du bas, où vivront les titres et les
sous-titres. Ne les touche que pour une raison qui s'énonce. `fond` vaut
`nocturne` par défaut, et c'est le bon : **les boîtes d'écran vivent sur le fond
nocturne**, un écran clair sur un fond papier ne se détachant pas, et les
sous-titres blancs y étant ternes.

### Choisir la zone, et confirmer ce qui apparaît

```
regarder { rush, instants: [ ... ], colonnes?, largeur?, reprendre? }
```

Rend une planche JPEG des images aux instants demandés : c'est comme ça qu'on
choisit un cadrage, et comme ça qu'on vérifie. **L'`url` est signée et ne
s'ouvre pas toute seule** — télécharge la planche dans ton scratch, puis ouvre
le fichier :

```bash
curl -sS -o planche.jpg "<url>"
```

**Rien n'est inscrit sur les vignettes.** Elles se lisent en grille, de gauche à
droite, dans l'ordre exact des `instants` demandés : c'est ta liste qui date les
images, et elle revient dans la réponse. Cent instants au plus, six colonnes et
270 pixels de large par défaut — une planche trop grande se refuse en disant
quoi baisser.

Trois réponses : l'`url` quand l'image est là ; `en_cours` avec le
`reessayer_dans_s` avant de redemander ; `echoue` avec son motif. Un refus ne se
rejoue pas seul, parce qu'il est déterministe le plus souvent — une source sans
image ne guérit pas. Quand le motif ressemble à une panne de passage,
`reprendre: true` relance.

**Sur chaque plage retenue, confirme image par image qu'aucun secret
n'apparaît** — une image toutes les une à deux secondes, sur toute la plage. Ce
que tu cherches : une clé d'API, un jeton, un mot de passe, une adresse e-mail,
une bulle de trousseau, un identifiant ou un secret client, une liste de dépôts
privés, un nom de client. Un enregistrement d'écran d'une heure en contient,
toujours.

**On cadre ailleurs, on ne floute jamais.** Un floutage qui glisse d'une image
sur une clé reste un floutage qui glisse, et c'est exactement ce que les gens
remarquent. Quand aucune fenêtre ne convient, la plage ne se montre pas : la
voix se pose sur un autre plan, ou sur ce que le monteur composera.

**Cadrer hors du secret t'appartient, et à personne d'autre.** Le monteur
regarde les images de ses plans d'écran et, s'il y voit passer quelque chose, il
reborne le plan ou le supprime et l'écrit en rétro — il ne floute pas et il ne
peut pas recadrer ta prise. Un secret que tu laisses entrer coûte donc un plan,
au mieux ; au pire il part avec la version. Le relevé se fait **une fois pour
toute la série**, dans la table de décisions, et il l'emporte sur ce qu'une
ligne de plan dirait de plus permissif.

Un doute se tranche avec l'auteur : lui seul sait si ce nom de client peut
sortir.

## 6. Les bornes

- **Sur un silence, jamais au milieu d'un mot.** Le premier et le dernier mot
  de l'extrait doivent être entiers.
- **Le `fin` d'un mot du verbatim absorbe souvent la pause qui le suit.** Une
  borne posée juste après le dernier mot peut le perdre. Prends une marge de
  quelques dixièmes.
- **Relis la minute qui suit ta borne de fin.** Une chute tronquée est le défaut
  le plus fréquent, et le plus visible : le short s'arrête au milieu de l'idée
  qu'il venait de poser.
- **Un extrait qui commence par un fragment est perdu**, même audible : personne
  ne sait de quoi il parle. Recule la borne au début de la phrase.
- **Une fenêtre fait entre 0,6 et 600 secondes**, et le tool refuse en dehors.
  Mais **le plancher utile est 0,7 s**, pas 0,6 : un plan tient au moins vingt
  images à trente par seconde, parce que la ferme abandonne un rendu dont un
  clip capture moins de 95 % de ses images et qu'un clip en perd une à
  l'extraction. Un extrait de 0,65 s passe le tool et ne se monte pas. En
  pratique, un extrait qui dit quelque chose dure plusieurs secondes.

Après extraction, relis le verbatim de la prise dans `voir_video` : le premier
et le dernier mot y sont, ou la borne est à reprendre. C'est ce verbatim-là qui
alimente l'intention — ce qui se dit dans chaque prise, l'auteur ne l'a pas
sous les yeux. Un rush dont plus aucune prise ne sort s'efface par
`supprimer_rush`, avec l'aval de l'auteur.

## 7. L'intention du morceau

Le dernier geste sur un morceau est d'écrire son intention dans son `idee`, par
`modifier_video`. C'est ce que l'auteur lira pour écrire le script, et c'est tout
ce qu'il aura de ton travail : le propos en une phrase, l'angle et le registre,
les prises posées avec leur rang et ce qui s'y dit, la durée mesurée, et ce qu'il
faut éviter.

Trois choses méritent d'y être nommées parce que toi seul les as vues :
**la nature de chaque plan** — une boîte d'écran vit sur le fond nocturne, et les
bandes au-dessus et au-dessous sont de l'habillage à remplir, pas du vide ;
**la phrase d'ouverture** que la matière tient ; et **les graphies** que la
transcription écorche, une marque, un nom propre, un sigle.

**Le `script` reste vide**, et la vidéo reste en préproduction. Un morceau posé,
tu passes au suivant : la série se dérushe morceau par morceau, jamais toutes les
extractions d'un côté et toutes les intentions de l'autre. Un défaut trouvé sur
le premier se répare sur les neuf autres.
