---
description: Scaffolde un nouveau skill dans plugins/avqn-skills/skills/
argument-hint: <nom-du-skill-en-kebab-case>
---

Crée un nouveau skill nommé `$ARGUMENTS` dans ce repo. Charge d'abord le skill
`avqn-skill-authoring` pour les conventions.

Étapes :

1. **Valider le nom** `$ARGUMENTS` : kebab-case (minuscules, chiffres, tirets), sans
   espace. S'il est absent ou invalide, demander un nom correct et s'arrêter.
2. **Vérifier l'absence de collision** : si `plugins/avqn-skills/skills/$ARGUMENTS/`
   existe déjà, s'arrêter et le signaler.
3. **Créer** `plugins/avqn-skills/skills/$ARGUMENTS/SKILL.md` avec ce gabarit :

   ```markdown
   ---
   name: $ARGUMENTS
   description: >-
     À utiliser dès que … . NE COUVRE PAS … .
   ---

   # <Titre lisible du skill>

   <Une ou deux phrases : ce que le skill produit, et pour qui.>

   ## <Section principale>

   <La recette. Rester concis ; renvoyer vers references/ pour les détails longs.>
   ```

4. **Rappeler** (sans les faire tout de suite) : compléter la `description`
   (déclencheurs + limite), ajouter `references/`/`templates/`/`examples/`/`assets/`
   au besoin, ajouter le skill à la table de `README.md`, puis lancer `/check-skills`
   avant de commiter.

Ne pas créer de dossiers vides — `references/`, `templates/`, etc. s'ajoutent quand
ils servent.
