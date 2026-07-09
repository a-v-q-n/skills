# Catalogue des gabarits

**Index vivant des gabarits.** Pour faire évoluer la liste : ajouter/retirer une ligne ici, et créer/supprimer le `.html` correspondant. Un gabarit = un fichier autonome. Rien d'autre à toucher.

Choisir d'après la **forme du contenu** (colonne « Cas d'usage »), pas d'après l'esthétique — l'esthétique est commune à tous (la charte du socle `produire-un-visuel-avqn`).

| Gabarit (fichier) | Cas d'usage | Mode | Format natif | Suit aussi |
|---|---|---|---|---|
| `social-statement.html` | Une prise de position / une idée en une phrase | clair | 4:5 | 1:1 · 9:16 |
| `social-manifeste.html` | La même idée, en emphase maximale sur l'encre à lueur | nocturne | 9:16 | 4:5 |
| `social-chiffre.html` | Un résultat chiffré brut (le chiffre fait le hook) | clair | 1:1 | 4:5 |
| `social-liste.html` | N étapes / N erreurs / N principes | clair | 4:5 | 9:16 |
| `social-citation.html` | La parole de quelqu'un d'autre (jamais l'opérateur) | nocturne | 4:5 | 9:16 |
| `social-terminal.html` | Post technique (commande, recette n8n, Claude Code) | nocturne | 16:9 | 4:5 |
| `social-carrousel-cover.html` | Slide 1 d'un carrousel (« Faites défiler ») | clair | 4:5 | 1:1 · 9:16 |
| `social-image-editorial.html` | Image IA « anticipation douce » en grand + titre serif | clair | 4:5 | — |

**Changer de format** = passer `width`/`height` à `media_render_html` (+ `--W`/`--H` alignés dans `:root`). Les gabarits en flux (statement, manifeste, liste, citation, carrousel-cover) suivent proprement ; les gabarits à positionnement plus tenu (chiffre, terminal, image-éditorial) demandent de vérifier quelques offsets sur un autre ratio, puis de re-rendre et **vérifier à l'œil**.

En carrousel, **alterner clair / nocturne** donne le rythme.

---

## Anatomie d'un gabarit

Chaque `.html` est autonome (fonts Google en `@import`, tout le CSS inline) et suit la même ossature :

- un conteneur `.c` aux dimensions `var(--W)` × `var(--H)` (le format) ;
- les tokens de marque en `:root` (issus de la charte du socle `produire-un-visuel-avqn`, §10) ;
- l'ambiance posée sur `.c` (papier quadrillé, ou nocturne + `::after` vignette) ;
- un en-tête de commentaire qui dit : le cas d'usage, ce qui est **figé**, ce qu'on **remplace**, le `wait_for` conseillé ;
- des placeholders textuels à remplacer (**retours à la ligne à la main**, un seul fragment `.acc`).

## Ajouter un gabarit

1. Copier le `.html` le plus proche comme point de départ.
2. Garder l'ossature (`.c`, tokens `:root`, ambiance, en-tête de commentaire).
3. Respecter le socle : un seul vermillon porteur, la serif porte / le mono recule, filets pour séparer, beaucoup d'air, ni cadre à ombre dure ni arrondi.
4. Le rendre (`media_render_html`) et **vérifier à l'œil**.
5. Ajouter une ligne au tableau ci-dessus.

## Conventions de nommage

`social-<forme>.html`. Le préfixe est réseau-agnostique : un même fichier se décline sur LinkedIn / Instagram / Threads par le format, tant que le reflow suffit.
