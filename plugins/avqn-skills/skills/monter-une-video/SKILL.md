---
name: monter-une-video
description: >-
  À utiliser pour monter une vidéo Contentos dont le script est écrit et la matière prête :
  traduire le script en source de montage, la faire dériver, corriger ce que la dérivation
  refuse, puis lancer le rendu. Porte la forme de la source (séquences, plans, ancres de
  texte), la boucle courte de correction et la lecture de la table des scènes. NE COUVRE PAS
  l'écriture du script (scripter-le-montage), la génération de la voix (produire-la-vo) ni
  celle des gabarits et images (fabriquer-les-assets).
couche: recette
moment: >-
  Le script est écrit et la matière est là : la vidéo se monte et part au rendu.
famille: video-contentos
---

# Monter une vidéo

Le montage arrive décidé. Le script porte les mots retenus, dans l'ordre, et la mise en
scène plan par plan. **Tu ne le reconçois pas — tu le retrouves dans la matière et tu le
transcris.**

Une seule chose se décide ici, et c'est tout le travail : **où chaque plan tombe vraiment**.
Les secondes du script sont une estimation que la voix ne tient jamais ; c'est le texte dit
qui date un plan.

## Les deux verbes

`monter` traduit ta source en projet déposé et rend la table des scènes. Il ne rend rien.
`rendre_version` lance le rendu quand la table te convient.

## La boucle

1. **Lis la matière.** `voir_video` donne le script, les captations et leur verbatim.
2. **Écris la source** — la transcription du script, en séquences et en plans.
3. **`monter`.** Il refuse en nommant ce qui cloche : un plan qu'il ne retrouve pas dans le
   verbatim, un gabarit hors de son format, un asset absent.
4. **Corrige la source, rejoue.** Rien d'autre ne s'édite : tout dérive de la source, et une
   retouche posée sur un produit se perdrait à la dérivation suivante.
5. **`rendre_version`** quand la table des scènes tient debout.

## La source

Une tête, puis des séquences de plans. Chaque plan dit le texte qu'il prononce ; c'est cette
suite de mots qui le date, retrouvée dans le verbatim de sa prise.

```json
{
  "video": "le-slug",
  "sous_titres": "sous-titre",
  "sequences": [
    { "nom": "hook", "prise": 1, "plans": [
      { "dit": "Les mots exacts que dit ce plan.",
        "cadrage": { "zoom": 1.3, "y": 28 } } ] }
  ]
}
```

Les plans d'une même prise se cherchent **dans l'ordre**, chacun après le précédent : c'est
ce qui lève l'ambiguïté d'une phrase répétée sans qu'on ait à compter les occurrences.

## Lire la table des scènes

C'est le produit du montage, et la seule chose à juger. Elle donne la durée réelle de chaque
scène — donc ce que le script avait mal estimé. Une scène beaucoup plus longue que prévu
n'est pas une erreur de dérivation : c'est la voix qui a pris son temps.

## Ce qui ne se fait pas ici

- **Rien ne se fabrique.** Le script, les gabarits, les images, les sons arrivent faits. Ce
  qu'une promesse du script ne trouve pas dans la matière ne s'invente pas.
- **Aucune coupe pour corriger le propos.** Ce qui te semble fautif se dit à Manu, jamais par
  une coupe silencieuse.
