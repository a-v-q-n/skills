---
name: creer-une-facture
description: >-
  À utiliser dès qu'on prépare, émet, envoie ou encaisse une facture client AVQN, ou qu'on
  pose l'échéancier de règlement d'un projet : orchestre le domaine facturation d'AVQN OS —
  échéancier du projet (une pièce par versement convenu), brouillon (invoice_create), aperçu
  proforma et PDF final générés PAR LE SERVEUR (invoice_render_pdf : corps A4 on-charte +
  QR-facture suisse), émission (invoice_issue), envoi (mail_draft), encaissement
  (paiement_record). Porte le jugement (grain du plan, lignes, libellés, adresses à réclamer,
  relecture), jamais le dessin du document. Charge le socle piloter-avqn-os. NE COUVRE PAS le
  rendu lui-même (fonction serveur invoice_render_pdf) ni le reporting revenu (rubrique
  Facturation du cockpit, lecture seule).
---

# Créer une facture

Commencer par charger **`piloter-avqn-os`** : la grammaire des parties (une personne physique se
facture au même titre qu'une organisation) et les invariants de l'OS y sont posés.

Produire une facture client AVQN de bout en bout. **Le MCP rend, l'agent décide** : les
données ET le dessin du document (PDF A4 on-charte + QR suisse) vivent dans AVQN OS
(specs `avqn-os/docs/specs/2026-07-15-facturation-design.md` et
`2026-07-25-paiements-echelonnes-design.md`) ; ce skill orchestre et garde le jugement —
quel grain d'échéancier, quelles lignes, quels libellés, quoi vérifier.
Ne jamais fabriquer le PDF à la main : `invoice_render_pdf` est la seule voie.

## La grammaire du règlement

Trois questions, trois objets — tout le reste se dérive, jamais ne se saisit :

- **Convenu** → l'échéancier du projet (`avqn_project_tranche`) : une ligne par versement
  convenu, en centimes exacts, date prévue. C'est LA source du « quoi facturer quand » —
  jamais de plan en prose dans une fiche ou un libellé.
- **Facturé** → les pièces : une ligne d'échéancier facturée pointe SA facture émise
  (une pièce couvre une ligne, garde-fou serveur).
- **Encaissé** → les paiements (`paiement_record`) : l'argent réellement arrivé, N par pièce.

Les états se lisent, ne s'écrivent pas. Une ligne du plan se lit en quatre temps —
**à facturer** (aucune pièce, ou pièce annulée) / **brouillon prêt** (la pièce est écrite,
pas émise : ne pas en refaire une) / **facturée** / **payée** ; une facture est *en attente*
tant qu'elle est émise et non soldée, et `paid` n'est qu'un cache de Σ paiements ≥ total.

Où lire : le **calendrier du règlement** (`/facturation/echeancier` du cockpit) montre tous
les plans groupés par projet ; le bloc « À facturer » de la rubrique montre le geste à faire ;
`echeancier_get` rend le plan d'un projet et son règlement dérivé.

## Le grain : une pièce par versement

**Tout étalement convenu s'écrit dans l'échéancier au grain du versement. Chaque ligne
devient UNE facture, émise à son jalon, avec son QR au montant exact. Chaque pièce attend
UN paiement : le sien.** C'est la pratique suisse (acompte, intermédiaire, solde — chaque
versement a sa pièce) et la seule voie d'émission.

- Une pièce ne couvre jamais plusieurs versements ; un versement ne s'étale jamais sur
  plusieurs pièces. Si le serveur refuse un lien (« une pièce par tranche »), c'est le grain
  qui est faux — corriger le plan, pas contourner en prose.
- Les N paiements possibles sur une pièce ne sont **pas** une voie d'émission : c'est
  l'enregistreur des déviations du client (virement partiel). La pièce passe
  « partiellement payée » — la réponse est une relance, jamais une contorsion des pièces.
- Un paiement est un fait immuable : corriger = `paiement_delete` + re-saisir. Une pièce
  porteuse de paiements ne s'annule ni ne se supprime (`paiement_delete` d'abord).

## La chaîne

1. **Poser le plan** — dès l'accord conclu : `avqn-os:tranche_add` sur le projet, une ligne
   par versement (libellé, centimes, date prévue). Relire l'échéancier avec Manu avant de
   facturer quoi que ce soit (`avqn-os:echeancier_get`).
   **Un dossier repris a presque toujours son plan quelque part** : il vit dans la
   proposition ou le contrat envoyé au client, pas dans le mail de facture — qui se contente
   d'un « comme convenu ». Le chercher (`mail_search` sur le fil de la proposition, `recall`)
   avant de demander à Manu, et surtout avant de laisser une tranche sans date : une date
   prévue est un engagement pris, jamais une valeur inventée.
2. **Préparer la pièce du jalon** — retrouver le client (`contexte` / `recall`), les lignes
   et montants (en **centimes** : 180.00 CHF → 18000). Adresse postale du client inconnue ?
   La demander à Manu ou la chercher (mails) : sans elle le QR laisse « Payable par » vide —
   valide, mais moins pratique pour le client.
3. **Créer le brouillon et le lier à sa ligne** — `avqn-os:invoice_create` (lignes libres,
   snapshot client structuré via `client` si l'adresse est connue), puis
   `avqn-os:tranche_update { invoiceId }` : le brouillon prépare la ligne, seule l'émission
   la solde.
4. **Aperçu AVANT d'émettre** — `avqn-os:invoice_render_pdf` sur le brouillon → proforma
   filigrané (sans QR). **Relire avec Manu** : nom, montants, libellés, dates. C'est ce qui
   évite d'émettre un numéro pour rien.
5. **Émettre** — validation explicite de Manu, puis `avqn-os:invoice_issue` (numérote
   `AAAA-NNN`, fige le snapshot, pose les dates).
6. **PDF final** — `avqn-os:invoice_render_pdf` → corps + partie paiement QR, `pdfUrl` posé
   automatiquement. **Vérifier le rendu à l'œil** (ouvrir l'URL) avant l'envoi.
7. **Envoyer** — brouillon email via `avqn-os:mail_draft`, PDF joint ; relecture et envoi
   par Manu.
8. **Encaisser** — à chaque arrivée réelle d'argent : `avqn-os:paiement_record
   { invoiceId, paidOn, amountCents }`. `invoice_mark_paid` est le sucre qui solde le
   restant en un geste. Le statut `paid` se dérive seul.

## Ce qui se prépare, ce qui se pose au jalon

Une pièce **naît** à son émission : c'est `invoice_issue` qui pose le numéro et la date
d'émission, le jour réel, jamais d'avance. Émettre en avance inscrirait dans les livres une
créance qui n'existe pas encore, et un changement de plan se paierait alors en annulations
au lieu d'une simple suppression de brouillon.

Se prépare donc à l'avance, sans rien engager : le brouillon (lignes, snapshot client), son
**échéance** (`dueDate` — posée sur le brouillon, elle est conservée par l'émission), le
**jalon** de la tranche (`expectedOn` = le jour où la pièce doit partir), et le proforma
relu. Quand le jalon est lointain, **poser une tâche datée** (`task_create` avec
`scheduledFor`, rattachée au projet) : elle dort jusqu'au jour dit puis remonte seule.

## Corrections et numérotation

Le régime d'éditabilité est **souple** par défaut : `invoice_update` corrige contenu,
dates et **numéro** à tout statut (re-générer le PDF ensuite — l'ancien fichier ne bouge
pas, l'URL change). Une annulée se supprime (`invoice_delete`) ou se renumérote : aucun
numéro n'est jamais brûlé. La séquence auto (`invoice_issue`) = max de l'année + 1 —
vérifier `invoice_list` avant d'émettre si l'historique n'est pas encore importé.

## Reprise d'historique

Une facture déjà envoyée hors système s'importe telle quelle :
`invoice_create { status: "sent"|"paid", number, issueDate, lines, client }` — elle se fige
à la création avec le numéro du document réel. Si elle est payée, enregistrer son ou ses
paiements (`paiement_record`) : l'invariant « toute pièce payée porte ses encaissements »
vaut aussi pour l'historique.

## Émetteur

Les coordonnées AVQN (adresse, IBAN PostFinance, mention TVA) vivent dans le **profil
émetteur de l'OS** : `avqn-os:invoice_issuer_get` pour lire, `invoice_issuer_update` pour
corriger. Rien n'est codé en dur ici.

## Outils MCP (AVQN OS, domaine facturation)

- `tranche_add` / `tranche_update` / `tranche_delete` — l'échéancier du projet (le plan).
- `echeancier_get` — le plan + son règlement dérivé, en une lecture.
- `invoice_create` / `invoice_update` / `invoice_issue` / `invoice_delete` — le cycle des pièces.
- `invoice_render_pdf` — LE rendu (proforma sur brouillon, QR sur émise). Jamais de PDF à la main.
- `paiement_record` / `paiement_list` / `paiement_delete` — les encaissements (les faits).
- `invoice_mark_paid` / `invoice_cancel` — le sucre du solde, l'annulation.
- `invoice_get` / `invoice_list` — lecture (filtres statut, client, année, retard) ; les
  pièces exposent paiements et solde.
- `invoice_issuer_get` / `invoice_issuer_update` — le profil émetteur.
- `mail_draft` — le brouillon d'envoi au client.
