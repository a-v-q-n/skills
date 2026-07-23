# AVQN — Skills

Marketplace de plugins Claude qui regroupe les skills AVQN. Un seul plugin,
`avqn-skills`, embarque toutes les recettes maison.

## Installer dans Claude

### Depuis claude.ai (Extensions → Marketplaces)

1. **Ajouter une marketplace** avec le dépôt `a-v-q-n/skills`.
2. Installer le plugin **avqn-skills** dans la liste.

### Depuis Claude Code (CLI)

```bash
/plugin marketplace add a-v-q-n/skills
/plugin install avqn-skills@avqn
```

Mettre à jour après un push :

```bash
/plugin marketplace update avqn
```

## Structure

```
.claude-plugin/marketplace.json     Catalogue de la marketplace « avqn »
plugins/
└── avqn-skills/
    ├── .claude-plugin/plugin.json   Manifeste du plugin
    └── skills/
        └── <nom-du-skill>/          Un skill = un dossier (socle ou recette)
```

## Ajouter un skill

1. `/new-skill <nom>` — scaffolde le dossier et un `SKILL.md` pré-rempli.
2. Rédiger le skill (corps + `references/`/`templates/` au besoin) et l'ajouter à la
   table ci-dessous.
3. Bumper la `version` (même valeur dans `plugin.json` et dans l'entrée `avqn-skills`
   de `marketplace.json`).
4. `/check-skills` — valider, puis commiter et pousser.

Les skills du dossier `skills/` sont découverts automatiquement — rien à déclarer.
Le numéro de `version` déclenche la mise à jour côté claude.ai (bouton « Mettre à jour »
/ `/plugin marketplace update avqn`). La méthodologie complète est dans `CLAUDE.md`.

## Skills disponibles

| Skill | Couche | Rôle |
| :---- | :----- | :--- |
| `ecrire-comme-manu` | socle | La voix de Manu : essence, règles non négociables, lexique, adresse. Chargé par les skills d'écriture. |
| `ecrire-pour-linkedin` | recette | Rédige un post LinkedIn dans la voix de Manu. |
| `ecrire-pour-threads` | recette | Rédige un post Threads (court, spontané, chaînable) dans la voix de Manu. |
| `ecrire-une-ressource` | recette | Rédige une ressource pédagogique (module, leçon, support) dans la voix de Manu. |
| `produire-un-visuel-avqn` | socle | La charte visuelle AVQN + l'acte de base (composer un HTML on-charte → rendre → vérifier). Chargé par les recettes visuelles. |
| `creer-un-visuel-social` | recette | Visuels réseaux sociaux (formats, gabarits, carrousel). Charge le socle visuel. |
| `creer-une-cover-ressource` | recette | Bannière 16:9 d'une ressource, portée par une accroche-objectif. Charge le socle visuel. |
| `piloter-avqn-os` | socle | La grammaire des objets d'AVQN OS (parties, rôles dérivés, projet pivot, carnet), le réflexe recall/contexte et les invariants. Chargé par les recettes de l'OS. |
| `tenir-le-crm` | recette | Annuaire, affiliations, deals et interlocuteurs. Charge le socle OS. |
| `gerer-les-taches` | recette | Capture, postures d'engagement, facettes, projets. Charge le socle OS. |
| `tenir-le-carnet` | recette | Notes du carnet, liens typés, fils de relation. Charge le socle OS. |
| `suivre-le-temps` | recette | Saisies, activités, taux dérivé, rapport. Charge le socle OS. |
| `suivre-les-objectifs` | recette | Pilotage : objectifs trimestriels, métriques (jauge/compteur), cibles et mesures. Charge le socle OS. |
| `creer-un-pdf` | mécanique | Assemble N images en un PDF multi-pages. Brand-neutral, appelé par les recettes. |
| `creer-une-illustration-ui` | recette | Maquette filaire qui enseigne un élément d'interface. Charge le socle visuel. |
| `creer-une-facture` | recette | Orchestre la facturation AVQN OS : brouillon, proforma et PDF+QR rendus par le serveur (invoice_render_pdf), émission, envoi, encaissement. |
