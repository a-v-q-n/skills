# Les rampes de ciel

Dégradé à 165° obligatoire. Le type de la ressource (tag `type:` dans Autonomes) impose la rampe.

| Type de ressource | Rampe | Stops | Tonalité |
|---|---|---|---|
| Tuto | Nuit d'aube | #16233F 0% → #5D3E6B 60% → #C95B7E 100% | sombre |
| Fiche | Plein jour | #F5B326 0% → #F8C64B 45% → #FBEBC4 100% | claire |
| Cheatsheet | Aube bleue | #16233F 0% → #3D5A9E 55% → #6E8FE8 100% | sombre |
| Exercice | Couchant ocre | #E8763A 0% → #C95B7E 55% → #5D3E6B 100% | sombre |
| (réserve, aucun type) | Crépuscule | #C95B7E 0% → #8A4468 45% → #16233F 100% | sombre |

Anciens noms : pastille → fiche ; parcours → tuto ; modèle → fiche ; retour d'expérience → article de blog, pas de cover ressource.

## Ce que le type de rampe change

- Sombre : traits et fenêtres crème, accents jaunes #F5B326, étoiles autorisées (2 max), halo possible.
- Claire (plein jour) : traits navy #16233F, accents ocre #E8763A, pas d'étoiles, pas de halo (arc au trait navy à la place).

## Le duel — exception unique

Le duel n'utilise pas la rampe du type : il assemble deux demi-ciels — gauche linear-gradient(165deg,#16233F 0%,#5D3E6B 100%), droite linear-gradient(165deg,#F8C64B 0%,#FBEBC4 100%) — séparés par un trait crème vertical de 6 px et une pastille « vs » (cercle crème 115 px, mono 40 px, navy). Chaque camp suit les règles de contraste de son demi-ciel.
