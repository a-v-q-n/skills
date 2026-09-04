---
description: Scaffolde un nouveau skill dans plugins/avqn-skills/skills/
argument-hint: <nom-du-skill-en-kebab-case>
---

Crée un nouveau skill nommé `$ARGUMENTS` dans ce repo. Charge d'abord le skill
`avqn-dev:avqn-skill-authoring` pour les conventions et l'architecture.

Étapes :

1. **Valider le nom** `$ARGUMENTS` : kebab-case (minuscules, chiffres, tirets), sans
   espace, verbe d'action en tête (`écrire-…`, `créer-…`). S'il est absent ou invalide,
   demander un nom correct et s'arrêter.
2. **Classer le skill** : socle ou recette ? Appliquer le critère de `CLAUDE.md`
   (usage indépendant → skill ; sinon → fichier `references/` d'un parent). Si le bloc ne
   mérite pas un skill à part, le signaler et proposer le `references/` correspondant plutôt
   que de scaffolder.
3. **Vérifier l'absence de collision** : si `plugins/avqn-skills/skills/$ARGUMENTS/`
   existe déjà, s'arrêter et le signaler.
4. **Créer** `plugins/avqn-skills/skills/$ARGUMENTS/SKILL.md` avec ce gabarit :

   ```markdown
   ---
   name: $ARGUMENTS
   description: >-
     À utiliser dès que … . NE COUVRE PAS … .
   couche: recette
   moment: >-
     <Une phrase : le moment où ce skill sert. C'est la colonne « Moment » du README.>
   famille: cycle-client
   ---

   # <Titre lisible du skill>

   <Une ou deux phrases : ce que le skill produit, et pour qui.>

   ## <Section principale>

   <La recette. Rester concis ; renvoyer vers references/ pour les détails longs.>
   ```

   `couche` vaut `socle` ou `recette` ; `famille` vaut `cycle-client`, `contenu-autonomes`
   ou `video-contentos` (un skill d'`avqn-dev` n'en porte pas). Si c'est une **recette** qui
   compose un socle, ajouter en tête du corps la ligne de composition : « Commencer par
   charger `<socle>` » (ex. `écrire-comme-manu`).

5. **Rappeler** (sans les faire tout de suite) : compléter la `description`
   (déclencheurs + limite), ajouter `references/`/`templates/`/`examples/`/`assets/`
   au besoin, régénérer la table (`python3 scripts/skills.py readme`), passer le
   skill à `avqn-dev:relire-un-skill`, puis lancer `/check-skills` avant de commiter.
   Pas de version à bumper : chaque commit poussé se propage seul.

Ne pas créer de dossiers vides — `references/`, `templates/`, etc. s'ajoutent quand
ils servent. Ne jamais éditer la table du `README.md` à la main : elle se régénère.
