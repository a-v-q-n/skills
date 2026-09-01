---
name: relire-une-ressource
description: >-
  À utiliser pour relire une ressource Autonomes (tuto, fiche, cheatsheet, exercice) contre
  les règles de la maison et rendre un rapport : une ressource en ligne ou archivée
  (par slug ou id), ou un fichier de travail avant construction. Même si Manu dit
  seulement « relis-moi ça », « c'est bon ? », « qu'est-ce qui cloche dans cette fiche »,
  « audite les ressources » ou « qu'est-ce qu'on garde de l'ancienne ». Lecture seule :
  ce skill n'écrit jamais dans Autonomes. Charge d'abord ecrire-mes-ressources et
  titrer-une-ressource. NE COUVRE PAS la réécriture elle-même
  (creer-une-ressource) ni la relecture d'un article de blog.
---

# Relire une ressource

Ce skill est le crible. Il prend une ressource, la passe contre le socle `ecrire-mes-ressources` et la règle de titre de `titrer-une-ressource`, et rend à Manu un rapport court qui dit ce qui tient, ce qui casse, et par quoi commencer. Il ne corrige rien : la correction passe par la recette de création, sur décision de Manu.

Il sert à deux moments. Avant la construction, sur le fichier de travail du jalon 2, pour attraper ce que l'auteur ne voit plus. Après, sur une ressource en ligne ou archivée, pour décider ce qu'on garde quand on la refait.

## 1. Charger la matière

- Une ressource en ligne ou archivée : `ressources_get` avec le slug ou l'id. Si le résultat est trop gros pour la fenêtre, il est enregistré dans un fichier : c'est ce fichier qu'on lit et qu'on donne au script.
- Un fichier de travail : le lire tel quel.
- Charger les deux socles (`ecrire-mes-ressources`, `titrer-une-ressource`) si ce n'est pas déjà fait. Le rapport ne cite jamais une règle qui n'y est pas.

## 2. Compter avant de juger

Lancer `scripts/stats.py` sur le JSON (ou le fichier de travail). Il sort les mots par page, les modules par type, le ratio image/mots, les tirets cadratins, les « , et », l'adresse (tu/vous), les motifs suspects, les liens internes et les titres de pages. Ces chiffres ouvrent le rapport : ils sont incontestables et ils disent souvent l'essentiel avant toute lecture.

Ne pas recopier la sortie brute : en tirer les trois ou quatre nombres qui comptent (« 9 400 mots pour un tuto, plafond 3 000 », « 27 accordions », « 0 lien interne », « 292 vous »).

## 3. Lire, page par page

Lire la ressource en entier, avec la checklist du socle en tête. Pour chaque page, noter ce qui accroche, en citant le passage (dix mots suffisent) : une justification avant l'action, une métaphore, une annonce ou un rappel, un doublon, un callout de trop, un accordion qui cache du texte non coupé, un mot technique non expliqué, une description à la place d'une image, une promesse marketing.

Vérifier aussi ce que le script ne voit pas :

- **Le titre** contre la règle de titrage : un néophyte comprend-il ce qu'il obtient ? Proposer le titre corrigé s'il ne passe pas.
- **Le type** : est-ce bien un tuto, une fiche, une cheatsheet ou un exercice, et la structure suit-elle celle du type ?
- **La description** : deux ou trois phrases qui disent le contenu, le résultat et le temps, sans promesse.
- **Les tags** : un `niveau:`, un `pilier:`, un `type:` de la taxonomie (tuto, fiche, cheatsheet, exercice), des `outil:` seulement pour l'outil sujet.
- **Les liens internes** : pointent-ils vers des slugs qui existent (`ressources_list`) ? Y en a-t-il deux à quatre, dans le texte ?
- **Les images** : chaque écran a-t-il la sienne ? Ont-elles un alt et une caption ? Sont-elles dans la palette papier ?
- **Ce qui vaut la peine d'être gardé** : les passages justes, les valeurs à copier vérifiées, les erreurs fréquentes bien placées. Une relecture qui ne dit que ce qui casse fait recommencer de zéro ce qui était bon.

## 4. Le rapport

Toujours ce format, en français, sans « Salut Manu » ni formule de fin :

```
## <titre de la ressource> (<slug>, <type>)

**En chiffres.** <3 ou 4 nombres qui comptent, avec le plafond du type>

**Verdict.** <une phrase : garder, retoucher, ou refaire depuis la matière>

**Ce qui casse, par ordre d'importance.**
1. <règle> : <citation courte> → <ce qu'il faudrait>
2. …
(5 points au plus ; le reste va dans « aussi »)

**Aussi.** <les points mineurs, en une ligne chacun>

**À garder.** <les passages, valeurs, images qui survivent tels quels>

**Titre, description, tags.** <ok, ou la version corrigée>

**Par où commencer.** <le premier geste, en une phrase>
```

Cinq points forts au plus : un rapport de trente lignes ne sert à personne. Si la ressource casse partout, le verdict est « refaire depuis la matière » et le rapport dit ce qu'on récupère plutôt que de lister chaque phrase.

Pour un lot (« audite les ressources »), un rapport par ressource dans le même message, précédé d'un tableau d'une ligne par ressource : slug, type, mots, verdict.

## Ce qui reste toujours vrai

- Lecture seule. Aucun `ressources_update`, `ressources_add_*`, `ressources_delete_*`, même pour « juste corriger le titre ». La correction est un autre geste, sur décision de Manu.
- Chaque point cite la règle du socle qu'il applique. S'il n'y a pas de règle, c'est un avis, et il se présente comme tel, à la fin.
- Une règle qui manque au socle et qui aurait attrapé un défaut réel s'ajoute au socle, avec l'exemple.
