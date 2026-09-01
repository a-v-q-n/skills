---
name: produire-la-vo
description: >-
  À utiliser pour générer la voix off d'une vidéo Contentos et, quand le plan le prévoit,
  la cloner en avatar — après validation du script par Manu. Porte le découpage en prises
  selon le montage, l'écriture pour l'oreille (respirations, breaks), la voix clonée de
  Manu et le choix d'avatar selon le registre. Charge d'abord le socle ecrire-mes-videos si
  le texte doit encore être ajusté. NE COUVRE PAS l'écriture du script (preparer-une-video)
  ni son verrouillage dans la fiche (scripter-le-montage).
---

# Produire la VO

Ce skill transforme un script validé en prises audio, et en avatar quand le plan le
prévoit. Rien ne se génère avant la validation du texte intégral par Manu : la prise coûte,
et surtout le ton se corrige sur le texte, pas sur l'audio. Si le texte doit encore bouger,
charger `ecrire-mes-videos` d'abord.

## Découper selon le montage, pas selon le texte

Le nombre de prises vient du plan de montage : chaque passage qui vit différemment à
l'écran mérite sa prise. Le cas type — le hook en avatar (Manu à l'image) et le corps en
voix off — fait DEUX prises : on ne clone en avatar que la prise du hook, pas trois minutes
de vidéo. Une prise = 3000 caractères max ; un corps plus long se découpe aux frontières
naturelles des séquences.

## Écrire pour l'oreille

Le texte des prises reprend le script validé, avec les ajustements oral :

- `<break time="0.4s" />` entre deux idées qui s'opposent ou se répondent,
  `<break time="0.6s" />` entre deux séquences. Une pause par respiration voulue — jamais
  une par virgule.
- Les tirets cadratins du texte écrit deviennent des phrases séparées (la synthèse les lit
  mal).
- Les chiffres et symboles restent tels quels si la synthèse les dit bien en français
  (8%, 100%) — au doute, les écrire en toutes lettres.

## La voix

`lister_voix` et prendre la voix clonée de Manu (« Emmanuel Bernard », catégorie
professional). Modèle par défaut du serveur, sauf raison contraire. `generer_prise` rend la
prise `recue` ; attendre `traitee` (visible dans `voir_video`) avant toute suite. Vérifier
au passage la durée obtenue contre le plan (~150 mots/min) : un gros écart signale un texte
à retailler.

## L'avatar

`cloner_prise` ne vaut que sur une prise sonore déjà `traitee`, et REMPLACE l'audio comme
matière de la prise. `lister_avatars` donne les looks de Manu ; le choix suit le registre
et le cadre :

- Un hook qui frappe : « Manu expressif ».
- Un passage posé : « Manu naturel vertical ».
- Les looks « horizontal » ne servent que si le plan le demande explicitement (insert 16:9,
  split).

La génération d'avatar prend quelques minutes : re-vérifier `voir_video` jusqu'à `traitee`
avec `a_image: true`. Si Manu n'aime pas le rendu, on regénère cette prise-là, pas tout.

## Checklist avant de rendre la main

- [ ] Le texte intégral des prises a été validé par Manu avant toute génération
- [ ] Le découpage en prises suit le plan de montage, aucune prise ne dépasse 3000 caractères
- [ ] Les breaks sont posés sur les respirations voulues, les cadratins convertis en phrases
- [ ] Voix « Emmanuel Bernard », chaque prise attendue jusqu'à `traitee`
- [ ] La durée de chaque prise colle au plan (~150 mots/min), sinon signalé à Manu
- [ ] L'avatar suit le registre (expressif pour le hook, naturel pour le posé), vérifié rendu
- [ ] Une prise ratée se regénère seule, le reste n'a pas bougé

## Boucle d'amélioration

Quand Manu refuse un rendu (intonation, débit, break mal placé), chercher ce qui dans le
texte de la prise l'a produit et l'ajouter ici comme règle d'écriture pour l'oreille ; une
question de formulation va dans `ecrire-mes-videos`.
