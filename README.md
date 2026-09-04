# AVQN — Skills

Marketplace de plugins Claude qui regroupe les skills AVQN. Deux plugins :

- **`avqn-skills`** — tout le craft métier, en trois familles : le **cycle de vie du client**
  sur AVQN OS (`os.avqn.ch`), le **contenu Autonomes** (ressources et blog, images comprises)
  et la **vidéo Contentos**. Chaque famille a son socle d'écriture et ses recettes.
- **`avqn-dev`** — la méthode de dev : triage par calibre, cycle jusqu'au FF merge, chantier,
  review, aperçu, démarrage local, onboarding de repo, secrets, écriture et relecture de
  skills — et ses sous-agents. Elle découvre le contrat de chaque repo (`CLAUDE.md`) et marche
  en local comme en session cloud.

## Installer dans Claude

### Depuis claude.ai (Extensions → Marketplaces)

1. **Ajouter une marketplace** avec le dépôt `a-v-q-n/skills`.
2. Installer **avqn-skills** et/ou **avqn-dev** dans la liste.

### Depuis Claude Code (CLI)

```bash
/plugin marketplace add a-v-q-n/skills
/plugin install avqn-skills@avqn
/plugin install avqn-dev@avqn
```

Dans un repo de la flotte, `.claude/settings.json` déclare la marketplace et le plugin —
c'est ce qui rend la méthode disponible en session cloud :

```json
{ "extraKnownMarketplaces": { "avqn": { "source": { "source": "github", "repo": "a-v-q-n/skills" } } },
  "enabledPlugins": { "avqn-dev@avqn": true } }
```

Mettre à jour après un push :

```bash
/plugin marketplace update avqn
```

## Structure

```
.claude-plugin/marketplace.json     Catalogue de la marketplace « avqn »
plugins/
├── avqn-skills/                     Le business
│   ├── .claude-plugin/plugin.json   Manifeste du plugin
│   └── skills/<nom-du-skill>/       Un skill = un dossier (socle ou recette)
└── avqn-dev/                        La méthode de dev
    ├── .claude-plugin/plugin.json
    ├── agents/                      Sous-agents (revieweur, verificateur)
    └── skills/<nom-du-skill>/
```

## Ajouter un skill

1. `/new-skill <nom>` — scaffolde le dossier et un `SKILL.md` pré-rempli.
2. Rédiger le skill (corps + `references/`/`templates/` au besoin). Son frontmatter porte
   `couche` (socle ou recette), `moment` (une phrase) et, dans `avqn-skills`, `famille` :
   c'est lui qui alimente la table ci-dessous.
3. `python3 scripts/skills.py readme` — la table se régénère entre les marqueurs.
4. `/check-skills` — valider, puis commiter et pousser.

Les skills du dossier `skills/` sont découverts automatiquement — rien à déclarer.
Pas de champ `version` : chaque commit poussé est une version (SHA git) et la mise à jour
se propage seule côté claude.ai (au besoin, « Mettre à jour » / `/plugin marketplace update
avqn` force le rafraîchissement). La méthodologie complète est dans `CLAUDE.md`.

<!-- skills:début -->

## Skills disponibles — `avqn-skills`

Trois familles. Dans chacune, un **socle** porte le craft transverse et les **recettes** vont
de bout en bout en le chargeant.

### Cycle de vie du client — AVQN OS

| Skill | Couche | Moment |
| :---- | :----- | :--- |
| `consigner-un-contact` | socle | L'entrée au CRM : chercher avant de créer, coordonnées structurées, organisation, affiliation, fiche courte. |
| `deposer-un-brouillon-email` | socle | La plomberie du brouillon : trouver le fil hors INBOX, répondre au bon message, contrôler le destinataire. |
| `ecrire-comme-manu` | socle | La voix de Manu : essence, règles non négociables, lexique, adresse. Chargé par toutes les recettes du cycle. |
| `accueillir-une-prise-de-contact` | recette | Quelqu'un contacte AVQN : enquêter, consigner, ouvrir le deal, répondre. |
| `debriefer-un-rendez-vous` | recette | Le call est passé : le débrief trié dans tout l'OS — note, fiches, deal, tâches, agenda, temps. |
| `ecrire-un-email-de-prospection` | recette | La prospection à froid : brief minimal, personnalisation réelle, objet, cadence des relances. |
| `emettre-une-offre` | recette | Accord de vive voix : devis, validation, PDF, email d'accompagnement. |
| `envoyer-une-facture` | recette | Un jalon se facture : pièce, proforma relu, émission, PDF QR, email d'envoi. |
| `preparer-un-rendez-vous` | recette | Un call approche : le dossier relu et condensé en brief. Lecture seule. |
| `relancer-un-prospect` | recette | Le prospect reste silencieux : timing, ton, relance dans le fil, sortie propre. |
| `relancer-une-facture` | recette | Une facture reste impayée : vérifier le paiement, palier de relance, brouillon. |

### Contenu Autonomes — ressources et blog

| Skill | Couche | Moment |
| :---- | :----- | :--- |
| `ecrire-mes-ressources` | socle | Les règles de contenu d'Autonomes : adresse, lecteur cible, chasse au fluff, structure par format, longueurs. |
| `titrer-une-ressource` | socle | Le titre : simple, descriptif, compris par un néophyte, sans accroche ni sous-titre. |
| `composer-une-cover-d-article` | recette | La cover 1600×900 : thème commun, composition improvisée, trois variantes puis pose. |
| `composer-une-cover-de-ressource` | recette | La vignette 1280×720 : rampes de ciel, recettes de composition, glyphes, trois variantes puis pose. |
| `creer-une-ressource` | recette | De la matière à la ressource publiée : format, plan, écriture, titre, images, pages et modules. |
| `ecrire-un-article-de-blog` | recette | De la matière à l'article publié : type, angle, plan, écriture, construction en brouillon. |
| `illustrer-une-ressource` | recette | Les images du corps : maquette, schéma, capture annotée — palette papier, gabarits HTML, rendu Médiathèque. |
| `relire-une-ressource` | recette | Relecture contre les règles de la maison, en ligne ou sur fichier de travail. Lecture seule. |

### Vidéo Contentos

| Skill | Couche | Moment |
| :---- | :----- | :--- |
| `ecrire-mes-videos` | socle | La voix parlée : hook et bridge, vraies phrases, liste noire des tics IA. |
| `fabriquer-les-assets` | recette | Le visuel : gabarits HTML animés et images générées, charte, aperçu de contrôle. |
| `preparer-une-video` | recette | De la matière au plan séquencé : idées fortes, hooks, chaque passage avec son asset. |
| `produire-la-vo` | recette | La voix off et l'avatar : découpage en prises, écriture pour l'oreille, voix clonée. |
| `raconter-une-histoire` | recette | La vidéo verticale « histoire racontée » : voix off et images peintes montées en BD animée. |
| `scripter-le-montage` | recette | Le script de montage final : séquences, plans, liens `#prise` et `@asset`. |

## Skills disponibles — `avqn-dev`

Invocation préfixée : `/avqn-dev:dev`, `/avqn-dev:local`…

| Skill | Couche | Moment |
| :---- | :----- | :--- |
| `avqn-skill-authoring` | socle | Les conventions d'écriture d'un skill AVQN : socle ou recette, anatomie, frontmatter, publication. |
| `travailler-sur-un-repo` | socle | Triage S/M/L, découverte du contrat du repo (Démarrer / Gate / Livrer), signal cloud, mode prudent. Chargé par toutes les recettes de dev. |
| `apercu` | recette | Boucle qualité visuelle locale avant la PR (captures aux breakpoints). |
| `brainstorm-issue` | recette | De l'idée floue à la spec d'intention dans l'issue GitHub. |
| `chantier` | recette | La discipline L : brainstorm → spec → plan → étapes → review renforcée. |
| `dev` | recette | Le cycle M jusqu'au FF merge `main` : TDD, aperçu, gate, review, PR, CI verte. |
| `gerer-les-secrets` | recette | Lire, créer, câbler un secret (coffre BWS en local, broker `ops` partout) sans jamais montrer une valeur. |
| `local` | recette | Démarrer un repo (recette dans son CLAUDE.md), socle transverse AVQN, preuve de boot. |
| `new-project` | recette | Onboarder un repo neuf sur la plateforme AVQN (GitHub, Coolify, DNS, squelette, premier deploy). |
| `relire-un-skill` | recette | Le crible d'un skill : conformité, puis déclenchement, classement, composition, poids. Lecture seule. |
| `review-pr` | recette | Review adversariale avant merge (mode léger / mode chantier). |

<!-- skills:fin -->

## Agents — `avqn-dev`

| Agent | Rôle |
| :---- | :--- |
| `revieweur` | Reviewer adversarial en lecture seule sur un diff (findings bloquant/majeur/mineur, fichier:ligne, scénario d'échec). |
| `verificateur` | Prouve ou réfute par exécution les affirmations d'un travail « terminé ». |
