---
name: review-pr
description: >-
  Review avant merge d'une branche ou d'une PR, dans n'importe quel repo — gate du repo, puis
  agent revieweur adversarial sur le diff avec la checklist AVQN (secrets, base partagée,
  invariants du repo), tri des findings, corrections réelles, verdict prêt-à-merger. Mode léger
  par défaut (1 agent) ; mode chantier (3 lentilles parallèles) pour le calibre L. Utilisé par
  dev (étape auto-review) et invocable seul (« review cette PR », « regarde la branche avant
  merge »).
---

# Review PR — le filet avant le FF merge

Charge d'abord `travailler-sur-un-repo`. Un merge `main` **livre** — ce que le `## Livrer` du repo
déclare (preview, prod…). La review est donc le **dernier filet avant du live**. Elle cherche les
vrais défauts — pas la conformité cosmétique.

## Entrée

- Branche courante : `git diff origin/main...HEAD` (+ `git log origin/main..HEAD`).
- Numéro de PR : `gh pr diff <n>` + `gh pr view <n>`.
- Contexte à rassembler : la spec (issue/conversation), le `CLAUDE.md` du repo, le diff complet.

## Déroulé

1. **Gate d'abord** : la commande `## Gate` du repo. Rouge → stop, corrige avant toute review
   (on ne review pas du cassé).
2. **Agent `revieweur`** sur le diff, avec dans son prompt : le diff (ou comment l'obtenir),
   la spec, le chemin du `CLAUDE.md` du repo, et la checklist ci-dessous.
3. **Trier les findings** : bloquant (bug réel, secret, invariant violé) / majeur (dette qui
   mord bientôt) / mineur (au goût). Vérifie chaque bloquant toi-même — un finding plausible
   n'est pas un finding confirmé.
4. **Corriger réellement** les bloquants et majeurs fondés, re-gate, re-passe le point touché.
5. **Verdict explicite** : « prêt à merger » ou la liste bloquante. Pas d'entre-deux.

## Checklist AVQN (en plus des bugs)

- **Secrets** : aucune valeur d'env/token/clé dans le diff, les tests, les logs.
- **Base partagée** (quand le repo touche le Postgres central — cf. son `CLAUDE.md`) : le schéma
  auth vendoré ne se migre JAMAIS depuis un autre repo qu'avqn-os ; toute migration sur une base
  logique partagée est rétro-compatible ou signalée.
- **Contrat du repo** : gate respectée, style du repo, et ses invariants propres — ex.
  redirects SEO obligatoires (product-site-avqn), wording figé (barometre-ia), valeurs de marque
  jamais dupliquées (styleguide).
- **Docs à l'état cible** : pas de « désormais / au lieu de » dans une doc modifiée.
- **Périmètre** : le diff fait ce que la spec demande, rien de plus (pas de refacto opportuniste
  non demandé).

## Mode chantier (calibre L)

Trois agents `revieweur` **en parallèle**, une lentille chacun :
1. **Correctness** — bugs, cas limites, concurrence, erreurs silencieuses.
2. **Sécurité & secrets** — fuites, authz, surfaces exposées, données de la base partagée.
3. **Contrat & méthode** — checklist AVQN, critères d'acceptation de la spec, docs.

Croise les verdicts : un finding signalé par deux lentilles = poids fort ; chaque bloquant reste
à confirmer par lecture directe avant correction.

## Garde-fous

- La review **modifie le code**, pas le verdict : pas de « noté pour plus tard » sur un bloquant.
- Pas de review sur gate rouge ; pas de merge sur verdict non rendu.
- Le revieweur est adversarial mais les corrections restent minimales (pas de réécriture).
