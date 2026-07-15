---
name: creer-une-facture
description: >-
  À utiliser dès qu'on prépare, émet, envoie ou encaisse une facture client AVQN : pilote le
  domaine facturation d'AVQN OS (invoice_create → invoice_issue → invoice_mark_paid), remplit
  le gabarit A4 on-charte (templates/facture.html) pour produire un PDF texte, archive le PDF
  sur la facture et prépare l'email d'envoi. Porte les conventions du document (formats
  suisses, mention TVA, coordonnées émetteur). NE COUVRE PAS le reporting revenu (rubrique
  Facturation du cockpit, lecture seule) ni les visuels rendus en image (produire-un-visuel-avqn).
---

# Créer une facture

Produire une facture client AVQN de bout en bout : les **données** vivent dans AVQN OS
(domaine `facturation`, spec `avqn-os/docs/specs/2026-07-15-facturation-design.md`), le
**document** sort du gabarit `templates/facture.html`. Une facture est un **document texte**
(sélectionnable, archivable) — jamais une image : on ne passe pas par `media_render_html`,
le PDF est généré directement depuis le HTML rempli.

## La chaîne

1. **Créer** — `avqn-os:invoice_create` (lignes libres : label, quantité, unité, prix
   unitaire en centimes). Relire le brouillon avec Manu avant toute émission.
2. **Émettre** — `avqn-os:invoice_issue` : attribue le numéro et fige tout (snapshot client,
   lignes, montants). Irréversible — jamais sans validation explicite.
3. **Produire le PDF** — `avqn-os:invoice_get`, remplir le gabarit (placeholders `{{…}}`,
   un `<tr>` par ligne), générer le PDF, **vérifier à l'œil** (alignements, montants,
   coupures) avant de livrer.
4. **Archiver** — déposer le PDF à un emplacement stable (médiathèque) et poser l'URL via
   `avqn-os:invoice_update { pdfUrl }`.
5. **Envoyer** — brouillon email via `avqn-os:mail_draft`, PDF joint ; relecture et envoi
   par Manu.
6. **Encaisser** — au paiement reçu, `avqn-os:invoice_mark_paid { paidAt }`.

## Conventions du document

- **Dates** au format suisse `JJ.MM.AAAA` (ex. `15.07.2026`).
- **Montants** avec apostrophe pour les milliers et deux décimales : `1'890.00`. La devise
  s'affiche via le libellé du total (`Total CHF`). Les centimes de l'OS se divisent par 100.
- **Échéance** : 30 jours après émission, sauf accord contraire porté sur la facture.
- **TVA** : non assujetti — la mention figée du pied de page suffit, aucun taux n'apparaît.
- **Charte** : papier écru, Instrument Serif qui porte (numéro, total), Geist/Geist Mono en
  appui, **un seul vermillon** (l'eyebrow « Facture »). On remplit le gabarit, on ne le
  redessine pas.

## Émetteur

L'identité, l'adresse et l'IBAN vivent **dans le gabarit**, pas dans l'OS : AVQN — Emmanuel
Bernard, Av. Charles Dickens 10, 1006 Lausanne ; compte PostFinance IBAN
CH10 0900 0000 1686 7016 2 (bénéficiaire « Bernard Emmanuel David — AVQN »). Ces coordonnées
se maintiennent dans `templates/facture.html` (la référence bancaire vit dans la note carnet
« Admin » de l'OS). Avant l'envoi, vérifier qu'aucun placeholder `{{…}}` ne reste dans le
document.

## QR-facture (plus tard)

La partie paiement normalisée (récépissé + Swiss QR Code) occupera les 105 mm du bas de
page ; le gabarit lui réserve l'emplacement. Le jour venu, elle se génère depuis les données
de la facture (lib `swissqrbill`) — rien d'autre ne change.

## Outils MCP (AVQN OS)

- `invoice_create` / `invoice_update` — brouillon (contenu) ; `pdfUrl` et `notes` à tout moment.
- `invoice_issue` — émission : numérote et fige.
- `invoice_mark_paid` / `invoice_cancel` — cycle de vie post-émission.
- `invoice_get` / `invoice_list` — lecture (filtres statut, client, année, retard).
- `mail_draft` — le brouillon d'envoi au client.
