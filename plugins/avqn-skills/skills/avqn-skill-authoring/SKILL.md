---
name: avqn-skill-authoring
description: >-
  À utiliser dès qu'on crée, édite ou publie un skill AVQN — la marketplace « avqn » du dépôt
  a-v-q-n/skills, plugins avqn-skills et avqn-dev — depuis n'importe quelle surface : une session
  de dev attachée au dépôt, ou une conversation qui écrit par le secteur `skill_` d'AVQN OPS.
  Porte l'architecture AVQN (socle vs recettes, le critère skill-ou-référence, les familles et
  leurs socles) et les conventions maison : anatomie (SKILL.md + references/templates/examples/
  assets), frontmatter en français (name, description à déclencheurs, couche, moment, famille),
  divulgation progressive, README généré, publication sans champ version (le SHA git fait foi).
  NE COUVRE PAS l'écriture du contenu métier d'un skill donné, la séquence de création
  (creer-un-skill), ni sa relecture (relire-un-skill).
couche: socle
moment: >-
  Les conventions d'écriture d'un skill AVQN : socle ou recette, anatomie, frontmatter,
  publication.
famille: outillage
---

# Écrire un skill AVQN

Produire un skill de la marketplace `avqn` : le bien classer, lui donner la bonne anatomie et le
bon frontmatter, puis le publier proprement. L'architecture d'ensemble et le périmètre vivent dans
le `CLAUDE.md` du dépôt `a-v-q-n/skills` ; ce skill l'applique au geste de création, et se charge
aussi depuis une session qui n'a pas ce dépôt sous la main.

## 1. Classer d'abord : socle ou recette ?

Avant d'écrire une ligne, situer le skill.

- **Recette** — une action de bout en bout (`emettre-une-offre`, `envoyer-une-facture`, `dev`).
  Elle orchestre : elle route, appelle les outils MCP, et compose le socle.
- **Socle** — un *craft* transverse réutilisé par plusieurs recettes (`ecrire-comme-manu`,
  `travailler-sur-un-repo`).

Puis trancher skill-à-part contre simple fichier avec **le critère** :

> Usage indépendant (invoqué seul, ou réutilisé par plusieurs recettes) → **skill**.
> Sinon → **fichier `references/`** du parent.

Ne pas créer par anticipation : un format ou un canal devient un skill le jour où on en écrit
un vrai, pas avant.

## 2. Le métier générique

Pour l'artisanat — une `description` qui déclenche, doser la divulgation progressive, vérifier
avant de livrer — s'appuyer sur **`superpowers:writing-skills`**. Ce skill-ci ne le redocumente
pas ; il ajoute la couche AVQN.

## 3. Quel plugin ?

Deux plugins, et le choix se fait **avant** d'écrire : il fixe le frontmatter et le socle que le
skill composera.

- **`avqn-skills`** — le métier d'AVQN (un client, du contenu, une vidéo), **et l'outillage des
  skills eux-mêmes** (`avqn-skill-authoring`, `creer-un-skill`, `relire-un-skill`). **Tout skill
  de ce plugin porte une `famille`**, et compose le socle de cette famille — l'outillage compris.
- **`avqn-dev`** — la méthode de dev sur un dépôt (calibre, cycle, review, secrets). Pas de
  `famille` ; le socle est `travailler-sur-un-repo`.

| `famille` | Socle que composent ses recettes |
| :-------- | :------------------------------- |
| `cycle-client` | `ecrire-comme-manu` |
| `contenu-autonomes` | `ecrire-mes-ressources` (+ `titrer-une-ressource`) |
| `video-contentos` | `ecrire-mes-videos` |
| `outillage` | `avqn-skill-authoring` |

## 4. Emplacement et anatomie

Le skill vit dans `plugins/<plugin>/skills/<nom>/`. Le `<nom>` est en kebab-case et devient le
`name` du frontmatter (identiques). Depuis une session attachée au dépôt, scaffolder avec
`/new-skill <nom>`.

- **`SKILL.md`** (requis) — la recette, concise (sous 500 lignes). Frontmatter puis corps.
- **`references/`** — détails chargés à la demande, **à un niveau** depuis `SKILL.md`.
- **`templates/`** — artefacts à remplir. **`examples/`** — sorties de référence.
  **`assets/`** — fichiers statiques.

N'ajouter que les dossiers utiles ; seul `SKILL.md` est obligatoire.

## 5. Frontmatter

Cinq clés, dont quatre obligatoires partout. Le frontmatter n'est plus une formalité : c'est lui
qui déclenche le skill **et** qui alimente la table du `README.md`.

| Clé | Obligatoire | Ce qu'elle porte |
| :-- | :---------- | :--------------- |
| `name` | oui | Identique au dossier, kebab-case, verbe d'action en tête, sans accent — minuscules, chiffres, tirets seulement. |
| `description` | oui | Français, 3e personne. Déclencheurs (« À utiliser dès que… ») **et** limite (« NE COUVRE PAS… »). Le seul texte qui décide du déclenchement. |
| `couche` | oui | `socle` ou `recette`. Le classement de l'étape 1, rendu lisible par la machine. |
| `moment` | oui | Une phrase : le moment où ce skill sert. C'est la colonne « Moment » de la table du README. |
| `famille` | dans `avqn-skills` | `cycle-client`, `contenu-autonomes`, `video-contentos` ou `outillage` — elle décide du socle (§3). Obligatoire sur tout skill d'`avqn-skills` ; les skills d'`avqn-dev` n'en portent pas, et la gate refuse les deux fautes. |

`moment` et `description` s'écrivent en bloc replié (`>-`) : une phrase avec un « : » casse un
scalaire YAML simple.

Jamais de champ `version` — ni ici, ni dans un `plugin.json`, ni dans l'entrée marketplace : une
version épinglerait le plugin, alors que chaque commit poussé fait version par son SHA git.

## 6. Corps et composition

Concis, état-cible : décrire ce qui est, sans « désormais » ni « au lieu de ». `SKILL.md` porte
l'essentiel et renvoie vers `references/` pour le reste.

Une **recette compose le socle de sa famille** — et jamais celui d'une autre : écrire en tête du
corps, noir sur blanc, « commencer par charger `ecrire-comme-manu` » (cycle client),
`ecrire-mes-ressources` (+ `titrer-une-ressource`) pour le contenu Autonomes, `ecrire-mes-videos`
pour la vidéo, `avqn-skill-authoring` pour l'outillage des skills, `travailler-sur-un-repo` pour
la méthode de dev.

Les outils MCP se citent par leur nom d'usage (`invoice_render_pdf`) avec une formulation
française de l'usage ; la mécanique d'un domaine AVQN OS vit dans `grammaire {domaine}` côté
serveur et ne se redocumente pas.

## 7. Publier

1. La table du `README.md` **se régénère** — `avqn-skills` regroupée par famille, `avqn-dev` en
   table plate, entre les marqueurs `<!-- skills:début -->` et `<!-- skills:fin -->`. On ne
   l'édite jamais à la main : pour changer une ligne, changer le `moment`, la `couche` ou la
   `famille` du skill. Écrire par le secteur `skill_` la régénère seul.
2. La gate : `skill_check` depuis n'importe quelle conversation, `/check-skills` depuis une
   session attachée au dépôt.
3. Commit 🤖 + push sur `main`. Le push **est** la publication : ni CI, ni image, ni déploiement.
4. La mise à jour se propage seule ; au besoin, forcer côté client : « Mettre à jour » sur le
   plugin, ou `/plugin marketplace update avqn` en CLI.

La séquence complète — de l'intention au skill publié — vit dans **`creer-un-skill`**. Avant de
considérer un skill fini, le passer à **`relire-un-skill`** : la conformité est binaire, la
qualité ne l'est pas.
