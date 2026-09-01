# Mécanique des ressources Autonomes (MCP « Autonomes - Blog »)

Référence technique pour construire une ressource. Tout ce qui est décrit ici a été observé sur les ressources en ligne en août 2026 ; ce qui n'a pas été observé est signalé.

## Modèle

Une **ressource** (tuto, fiche, cheatsheet ou exercice) contient un **arbre de pages** ordonné. Chaque page contient des **modules** ordonnés par `position`. Une ressource publiée est indexable et son corps entier est servi ; sans compte, seul l'échantillon d'entrée s'affiche ; un compte ouvre tout le catalogue.

Chaque ressource a une page racine de slug `contenu` dont le titre est celui de la ressource. Une fiche, une cheatsheet ou un exercice tient dans cette seule page. Un tuto met son intro dans la page racine et une sous-page par étape ou notion (`parentId` = id de la page racine).

## Outils

| Outil | Rôle | Paramètres utiles |
|---|---|---|
| `ressources_list` | Catalogue : id, slug, titre, published, archived, pinnedAt, tags | aucun |
| `ressources_get` | Une ressource avec son arbre de pages et leurs modules | `idOrSlug` |
| `ressources_create` | Crée la ressource, en brouillon si `published` n'est pas passé | `title` (requis), `slug`, `description`, `tags[]`, `coverImageUrl` |
| `ressources_update` | Métadonnées : `title`, `description`, `slug`, `tags`, `coverImageUrl`, `published`, `archived`, `pinned` | `id` (requis) |
| `ressources_delete` | Supprime la ressource et son arbre ; `confirmSlug` doit répéter le slug | `id`, `confirmSlug` |
| `ressources_add_page` | Ajoute une page ; `parentId` pour une sous-page ; `position` dans la fratrie | `resourceId`, `title`, `slug`, `parentId`, `position` |
| `ressources_update_page` | Titre, slug, position, parent d'une page | `pageId` |
| `ressources_delete_page` | Supprime la page et ses modules | `pageId` |
| `ressources_add_modules` | Ajoute une liste de modules à une page, dans l'ordre donné | `pageId`, `modules[]` = `{ type, content }` |
| `ressources_update_module` | Contenu, position ou type d'un module | `moduleId` |
| `ressources_delete_module` | Supprime un module | `moduleId` |
| `ressources_stats` | Une ligne par ressource : vues anonymes, vues identifiées, inscrits, conversion | aucun |
| `ressources_readers` | Qui a lu ou s'est inscrit via cette ressource | `idOrSlug` |

Les outils de suppression sont destructifs : ne les appeler que sur demande explicite de Manu.

`ressources_create` ne semble pas créer la page racine : vérifier avec `ressources_get` et l'ajouter si besoin.

## Formes de contenu des modules

Observées sur les ressources en ligne. Le média est toujours référencé par URL publique (R2, via la Médiathèque).

```json
{ "type": "text",       "content": { "markdown": "…" } }
{ "type": "heading",    "content": { "text": "…", "level": 2 } }
{ "type": "image",      "content": { "url": "https://…", "alt": "…", "caption": "…" } }
{ "type": "video",      "content": { "url": "https://player.mediadelivery.net/embed/…", "caption": "…" } }
{ "type": "callout",    "content": { "tone": "info" | "warn" | "success", "markdown": "…" } }
{ "type": "code",       "content": { "code": "…", "language": "bash", "filename": "CLAUDE.md" } }
{ "type": "prompt",     "content": { "title": "…", "prompt": "…" } }
{ "type": "accordion",  "content": { "open": false, "title": "…", "markdown": "…" } }
{ "type": "steps",      "content": { "steps": [ { "title": "…", "markdown": "…" } ] } }
{ "type": "comparison", "content": { "columns": [ { "title": "…", "markdown": "…" } ] } }
{ "type": "cta",        "content": { "url": "https://…", "label": "…" } }
```

Non observés, forme à vérifier sur un brouillon avant usage : `quote`, `file`, `embed`, `gallery`. Le serveur revalide le contenu à chaque écriture ; une forme fausse renvoie une erreur, elle ne casse rien.

Le markdown des modules `text`, `callout`, `steps`, `accordion`, `comparison` accepte les titres `## `, le gras, les listes, les tableaux, les blocs de code et les liens internes `/r/slug`.

## Tags

Quatre axes, chaque ressource en porte un par axe (l'axe `outil` peut en avoir plusieurs, ou aucun pour une ressource de fondations) :

| Axe | Valeurs en usage | Rôle |
|---|---|---|
| `niveau:` | `debutant` | Niveau requis. Seul `debutant` existe pour l'instant. |
| `pilier:` | `fondations`, `construire`, `automatiser` | Le grand chapitre du site. |
| `outil:` | `claude-code`, `n8n`, `coolify`, `opencode` | L'outil au cœur de la ressource. Ajouter une valeur seulement si l'outil est vraiment le sujet. |
| `type:` | `tuto`, `fiche`, `cheatsheet`, `exercice` | Ce que le lecteur fait avec : il suit un guide, il comprend un contexte, il retrouve un élément, il s'entraîne. Un seul par ressource. Pas de `cours` (un guide long est un tuto), pas de `pastille` (ancien nom de la fiche). |

Le `type:` donne aussi la rampe de ciel de la cover : tuto = nuit d'aube, fiche = plein jour, cheatsheet = aube bleue, exercice = couchant ocre (voir `composer-une-cover-de-ressource`).

Créer une nouvelle valeur d'axe (un pilier `heberger`, un outil `nextcloud`) est une décision de Manu : la proposer, ne pas l'inventer en silence. Les quatre valeurs de `type:` sont fermées.

Les ressources archivées portent encore les anciens tags (`type:pastille`) : elles servent de matière pour les refaire, pas de modèle.

## Slug

Dérivé du titre, en minuscules, sans accents, mots séparés par des tirets, sans mots vides (le, la, de, avec, votre) : « Installer n8n sur votre propre serveur » → `installer-n8n-propre-serveur`. Court, lisible, stable : d'autres ressources y pointent par `/r/slug`, on ne le change plus une fois publié.

Les sous-pages ont aussi un slug, dérivé de leur titre (`creer-le-depot`, `connecter-claude-github`).

## Description

Deux ou trois phrases : ce que contient la ressource, ce que le lecteur saura faire ou aura à la fin, le temps que ça prend. Voir `ecrire-mes-ressources`.

## Cover

`coverImageUrl` accepte une URL publique. Les covers existantes sont hébergées sur le R2 de la Médiathèque (`pub-….r2.dev/images/…` ou `/uploads/manu/…`). Toutes les ressources n'en ont pas.

## Séquence de construction

1. `ressources_create` (title, slug, description, tags, coverImageUrl) sans `published`.
2. `ressources_get` → si pas de page racine, `ressources_add_page` (slug `contenu`, titre = titre de la ressource).
3. Sous-pages : `ressources_add_page` avec `parentId` et `position` 0, 1, 2…
4. `ressources_add_modules` page par page, tous les modules d'une page en un appel, dans l'ordre.
5. `ressources_get` de contrôle : compter, comparer au fichier de travail.
6. `ressources_update` `published: true` sur feu vert de Manu ; `pinned: true` sur demande.

## Médiathèque (images)

Serveur « AVQN Médiathèque » : `media_upload` / `media_request_upload` + `media_finalize_upload` pour une capture fournie, `media_import_from_url` pour une image déjà en ligne, `media_generate_image` (IA) ou `media_render_html` (rendu d'un HTML) pour une image créée, `media_crop` / `media_resize` / `media_optimize` pour retravailler, `media_get_image` pour l'URL publique. Ranger les images d'une ressource dans une collection (`media_create_collection`) nommée par le slug de la ressource.
