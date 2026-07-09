# Catalogue des gabarits — covers ressources

**Index des gabarits de bannière.** Choisir d'après la **nature du contenu** (colonne « Cas d'usage »), pas d'après l'esthétique — l'esthétique est commune à tous (la charte du socle `produire-un-visuel-avqn`). Tous en 16:9 (1280×720).

| Gabarit (fichier) | Cas d'usage (nature du contenu) | Ambiance | État |
|---|---|---|---|
| `cover-defaut.html` | Cours / tuto (défaut) — objet fenêtre code | nocturne | seed clonable |
| *(à décliner)* | Le sujet est un fichier — fiche document à onglet | clair ou nocturne | depuis le seed |
| *(à décliner)* | Le sujet est une interaction — boîte de dialogue | nocturne | depuis le seed |
| *(à décliner)* | Automatisation n8n — ligne de workflow + node | nocturne | depuis le seed |
| *(à décliner)* | Comprendre / conceptuel — accroche en escalier | clair | depuis le seed |
| *(à décliner)* | Fondations — type fantôme géant | clair | depuis le seed |
| *(à décliner)* | Cheatsheet — badge type + plaque + tapisserie | nocturne ou clair | depuis le seed |

On ne crée un gabarit que le jour où on produit une vraie cover de cette nature — on documente **le contexte d'usage** (`SKILL.md`, section « Le climat + l'objet central »), pas l'exemple par anticipation.

---

## Anatomie d'un gabarit

Chaque `.html` est autonome (fonts Google en `@import`, tout le CSS inline) et suit la même ossature :

- un conteneur `.c` en `var(--W)` × `var(--H)` = 1280×720 ;
- les tokens de marque en `:root` (issus de la charte du socle `produire-un-visuel-avqn`, §10) ;
- une ambiance du socle posée sur `.c` (papier quadrillé, ou nocturne + `::after` vignette) ;
- un en-tête de commentaire : le cas d'usage, ce qui est **figé**, ce qu'on **remplace**, les marges de sécurité, le `wait_for` conseillé ;
- l'**accroche** (le seul texte, un seul fragment `.acc`) et l'**objet central** selon la nature.

## Ajouter un gabarit

1. Copier `cover-defaut.html` comme point de départ.
2. Garder l'ossature (`.c`, tokens `:root`, ambiance, en-tête de commentaire, marges 8 %).
3. Respecter le socle : un seul vermillon porteur, la serif porte / le mono recule, filets pour séparer, beaucoup d'air, ni cadre à ombre dure ni arrondi, coins libres.
4. Changer l'objet central pour qu'il reflète la **nature** du contenu (voir `SKILL.md`).
5. Le rendre (`media_render_html`, 1280×720) et **vérifier à l'œil**.
6. Ajouter une ligne au tableau ci-dessus.
