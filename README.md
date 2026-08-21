# AVQN — Skills

Marketplace de plugins Claude qui regroupe les skills AVQN. Deux plugins :

- **`avqn-skills`** — le craft du business : la voix de Manu, les canaux d'écriture, et les
  recettes qui orchestrent AVQN OS (`os.avqn.ch`) au fil du cycle de vie du client.
- **`avqn-dev`** — la méthode de dev : triage par calibre, cycle jusqu'au FF merge, chantier,
  review, aperçu, démarrage local, onboarding de repo, secrets — et ses sous-agents. Elle
  découvre le contrat de chaque repo (`CLAUDE.md`) et marche en local comme en session cloud.

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
2. Rédiger le skill (corps + `references/`/`templates/` au besoin) et l'ajouter à la
   table ci-dessous.
3. `/check-skills` — valider, puis commiter et pousser.

Les skills du dossier `skills/` sont découverts automatiquement — rien à déclarer.
Pas de champ `version` : chaque commit poussé est une version (SHA git) et la mise à jour
se propage seule côté claude.ai (au besoin, « Mettre à jour » / `/plugin marketplace update
avqn` force le rafraîchissement). La méthodologie complète est dans `CLAUDE.md`.

## Skills disponibles — `avqn-skills`

Les recettes suivent le cycle de vie du client — un skill par moment, chacun orchestre
AVQN OS et charge la voix.

| Skill | Couche | Moment |
| :---- | :----- | :--- |
| `ecrire-comme-manu` | socle | La voix de Manu : essence, règles non négociables, lexique, adresse. Chargé par toutes les recettes. |
| `accueillir-une-prise-de-contact` | recette | Quelqu'un contacte AVQN : enquêter, consigner au CRM, ouvrir le deal, répondre. |
| `preparer-un-rendez-vous` | recette | Un call approche : le dossier relu et condensé en brief. Lecture seule. |
| `debriefer-un-rendez-vous` | recette | Le call est passé : le débrief trié dans tout l'OS — note, fiches, deal, tâches, agenda, temps. |
| `relancer-un-prospect` | recette | Le prospect reste silencieux : timing, ton, relance dans le fil, sortie propre. |
| `emettre-une-offre` | recette | Accord de vive voix : devis, validation, PDF, email d'accompagnement. |
| `envoyer-une-facture` | recette | Un jalon se facture : pièce, proforma relu, émission, PDF QR, email d'envoi. |
| `relancer-une-facture` | recette | Une facture reste impayée : vérifier le paiement, palier de relance, brouillon. |

## Skills disponibles — `avqn-dev`

Invocation préfixée : `/avqn-dev:dev`, `/avqn-dev:local`…

| Skill | Couche | Rôle |
| :---- | :----- | :--- |
| `travailler-sur-un-repo` | socle | Triage S/M/L, découverte du contrat du repo (Démarrer / Gate / Livrer), signal cloud, mode prudent. Chargé par toutes les recettes de dev. |
| `dev` | recette | Le cycle M jusqu'au FF merge `main` : TDD, aperçu, gate, review, PR, CI verte. |
| `chantier` | recette | La discipline L : brainstorm → spec → plan → étapes → review renforcée. |
| `brainstorm-issue` | recette | De l'idée floue à la spec d'intention dans l'issue GitHub. |
| `review-pr` | recette | Review adversariale avant merge (mode léger / mode chantier). |
| `apercu` | recette | Boucle qualité visuelle locale avant la PR (captures aux breakpoints). |
| `local` | recette | Démarrer un repo (recette dans son CLAUDE.md), socle transverse AVQN, preuve de boot. |
| `new-project` | recette | Onboarder un repo neuf sur la plateforme AVQN (GitHub, Coolify, DNS, squelette, premier deploy). |
| `gerer-les-secrets` | recette | Lire, créer, câbler un secret (coffre BWS en local, broker `ops` partout) sans jamais montrer une valeur. |

| Agent | Rôle |
| :---- | :--- |
| `revieweur` | Reviewer adversarial en lecture seule sur un diff (findings bloquant/majeur/mineur, fichier:ligne, scénario d'échec). |
| `verificateur` | Prouve ou réfute par exécution les affirmations d'un travail « terminé ». |
