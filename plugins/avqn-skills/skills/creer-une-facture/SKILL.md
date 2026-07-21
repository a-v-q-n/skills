---
name: creer-une-facture
description: >-
  À utiliser dès qu'on prépare, émet, envoie ou encaisse une facture client AVQN : orchestre
  le domaine facturation d'AVQN OS — brouillon (invoice_create), aperçu proforma et PDF final
  générés PAR LE SERVEUR (invoice_render_pdf : corps A4 on-charte + QR-facture suisse),
  émission (invoice_issue), envoi (mail_draft), encaissement (invoice_mark_paid). Porte le
  jugement (lignes, libellés, adresses à réclamer, relecture), jamais le dessin du document.
  Charge le socle piloter-avqn-os. NE COUVRE PAS le rendu lui-même (fonction serveur invoice_render_pdf) ni le reporting
  revenu (rubrique Facturation du cockpit, lecture seule).
---

# Créer une facture

Commencer par charger **`piloter-avqn-os`** : la grammaire des parties (une personne physique se
facture au même titre qu'une organisation) et les invariants de l'OS y sont posés.

Produire une facture client AVQN de bout en bout. **Le MCP rend, l'agent décide** : les
données ET le dessin du document (PDF A4 on-charte + QR suisse) vivent dans AVQN OS
(spec `avqn-os/docs/specs/2026-07-15-facturation-design.md`) ; ce skill orchestre et
garde le jugement — quelles lignes, quels libellés, quel échéancier, quoi vérifier.
Ne jamais fabriquer le PDF à la main : `invoice_render_pdf` est la seule voie.

## La chaîne

1. **Préparer** — retrouver le client (`contexte` / `recall`), réunir lignes et montants
   (en **centimes** : 180.00 CHF → 18000). Adresse postale du client inconnue ? La demander
   à Manu ou la chercher (mails) : sans elle le QR laisse « Payable par » vide — valide,
   mais moins pratique pour le client.
2. **Créer le brouillon** — `avqn-os:invoice_create` (lignes libres, snapshot client
   structuré via `client` si l'adresse est connue).
3. **Aperçu AVANT d'émettre** — `avqn-os:invoice_render_pdf` sur le brouillon → proforma
   filigrané (sans QR). **Relire avec Manu** : nom, montants, libellés, dates. C'est ce qui
   évite d'émettre un numéro pour rien.
4. **Émettre** — validation explicite de Manu, puis `avqn-os:invoice_issue` (numérote
   `AAAA-NNN`, fige le snapshot, pose les dates).
5. **PDF final** — `avqn-os:invoice_render_pdf` → corps + partie paiement QR, `pdfUrl` posé
   automatiquement. **Vérifier le rendu à l'œil** (ouvrir l'URL) avant l'envoi.
6. **Envoyer** — brouillon email via `avqn-os:mail_draft`, PDF joint ; relecture et envoi
   par Manu.
7. **Encaisser** — au paiement reçu, `avqn-os:invoice_mark_paid { paidAt }`.

## Corrections et numérotation

Le régime d'éditabilité est **souple** par défaut : `invoice_update` corrige contenu,
dates et **numéro** à tout statut (re-générer le PDF ensuite — l'ancien fichier ne bouge
pas, l'URL change). Une annulée se supprime (`invoice_delete`) ou se renumérote : aucun
numéro n'est jamais brûlé. La séquence auto (`invoice_issue`) = max de l'année + 1 —
vérifier `invoice_list` avant d'émettre si l'historique n'est pas encore importé.

## Reprise d'historique

Une facture déjà envoyée hors système s'importe telle quelle :
`invoice_create { status: "sent"|"paid", number, issueDate, paidAt?, lines, client }` —
elle se fige à la création avec le numéro du document réel.

## Émetteur

Les coordonnées AVQN (adresse, IBAN PostFinance, mention TVA) vivent dans le **profil
émetteur de l'OS** : `avqn-os:invoice_issuer_get` pour lire, `invoice_issuer_update` pour
corriger. Rien n'est codé en dur ici.

## Outils MCP (AVQN OS, domaine facturation)

- `invoice_create` / `invoice_update` / `invoice_issue` / `invoice_delete` — le cycle des données.
- `invoice_render_pdf` — LE rendu (proforma sur brouillon, QR sur émise). Jamais de PDF à la main.
- `invoice_mark_paid` / `invoice_cancel` — encaissement, annulation.
- `invoice_get` / `invoice_list` — lecture (filtres statut, client, année, retard).
- `invoice_issuer_get` / `invoice_issuer_update` — le profil émetteur.
- `mail_draft` — le brouillon d'envoi au client.
