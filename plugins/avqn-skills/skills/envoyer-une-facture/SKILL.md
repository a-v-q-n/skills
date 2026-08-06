---
name: envoyer-une-facture
description: >-
  À utiliser dès qu'un jalon se facture ou que Manu demande d'envoyer une facture à un
  client : retrouver la ligne d'échéancier, préparer ou reprendre la pièce, faire relire
  le proforma, émettre le jour même, générer le PDF avec QR suisse et préparer l'email
  d'envoi dans la voix de Manu. Charge d'abord le socle ecrire-comme-manu pour l'email.
  NE COUVRE PAS la proposition commerciale en amont (emettre-une-offre), la relance d'un
  impayé (relancer-une-facture) ni la mécanique du domaine, qui vit dans
  grammaire facturation côté serveur.
---

# Envoyer une facture

Une facture part propre ou ne part pas : le bon montant sur la bonne ligne d'échéancier, un
PDF relu à l'œil, un email court qui l'apporte sans commenter. La rigueur ici, c'est ce qui
rend l'encaissement silencieux — et la relance inutile.

**Charger d'abord le skill `ecrire-comme-manu`** pour l'email, et appeler
`grammaire {domaine: "facturation"}` avant la première écriture du domaine : la chaîne
complète (plan, pièce, émission, encaissement) vit là-bas, ce skill n'ajoute que le
jugement et l'email.

Adresse : **tu** — un client qui reçoit une facture est un client établi. Le vous ne se
garde que si toute la relation est restée au vous.

## La séquence

### 1. Partir du plan, jamais de mémoire

`echeancier_a_facturer` dit le geste à faire ; `echeancier_get` sur le projet donne le plan
et son règlement. **Une pièce couvre une ligne d'échéancier, jamais deux.** Si la ligne
attendue n'existe pas, c'est le plan qui se corrige d'abord (`tranche_add`), pas la facture
qui s'invente.

Si la ligne est en `brouillon_pret`, la pièce existe déjà : le geste est **relire et
émettre**, jamais en créer une seconde.

### 2. Préparer la pièce

`invoice_create` — montants en centimes, libellés clairs, snapshot client via `client` —
puis `tranche_update { invoiceId }` pour lier la pièce à sa ligne. L'adresse postale du
client manque ? La chercher (mails, `recall`) ou la demander : sans elle, le QR laisse
« Payable par » vide.

### 3. Relire le proforma avec Manu

`invoice_render_pdf` sur le brouillon rend le proforma filigrané. **Le faire relire à
Manu** : nom, montants, libellés, dates, échéance. Rien ne s'émet sans sa validation
explicite.

### 4. Émettre le jour même

`invoice_issue` pose le numéro et la date d'émission **le jour réel, jamais d'avance**.
Puis `invoice_render_pdf` à nouveau : le PDF final avec QR. **Ouvrir la `pdfUrl` et
vérifier le rendu à l'œil** — c'est ce document qui part chez le client.

### 5. L'email d'envoi

`mail_draft`, dans le fil existant si la conversation en a un — **toujours un brouillon**,
Manu relit et envoie. L'email :

- est court : la facture se comprend toute seule, l'email l'apporte ;
- nomme ce qui est facturé en une phrase humaine (« la facture du solde de ton
  accompagnement »), rappelle l'échéance, mentionne le QR pour le paiement ;
- joint le PDF, nommé `AAAA-MM-JJ-prenom-nom-facture-NNNN.pdf` ;
- ne glisse aucune demande annexe : une facture voyage seule ;
- peut fermer sur une note chaleureuse ancrée dans le travail fait ensemble — c'est aussi
  un message de fin de jalon.

### 6. Après l'envoi

Au retour de Manu : rien à faire côté OS, l'émission a tout posé. À l'arrivée de l'argent :
`paiement_record { invoiceId, paidOn, amountCents }`. Si l'échéance passe sans paiement,
`relancer-une-facture` prend le relais.

## Checklist avant de rendre la main

- [ ] La pièce couvre exactement une ligne d'échéancier, liée par `tranche_update`
- [ ] Aucun brouillon préexistant n'a été doublé
- [ ] Le proforma a été relu et validé explicitement par Manu avant l'émission
- [ ] L'émission date du jour réel ; le PDF final avec QR a été ouvert et vérifié à l'œil
- [ ] L'email est un brouillon court, PDF joint et bien nommé, sans demande annexe
- [ ] Checklist anti-tics du socle `ecrire-comme-manu` passée
