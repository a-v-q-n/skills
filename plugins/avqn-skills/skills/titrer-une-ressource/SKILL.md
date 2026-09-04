---
name: titrer-une-ressource
description: >-
  À utiliser dès qu'il faut trouver, proposer, vérifier ou corriger le titre d'une ressource
  Autonomes (tuto, fiche, cheatsheet, exercice), que la ressource soit à créer
  ou déjà en ligne, et même si Manu ne dit pas « titre » mais « comment on l'appelle »,
  « retitre-moi ça » ou « c'est bon ce titre ? ». Porte la règle de Manu : un titre simple,
  descriptif, compris par un néophyte, sans formule accrocheuse ni sous-titre. À charger
  aussi par toute recette qui crée ou révise une ressource Autonomes avant de poser le
  titre. NE COUVRE PAS le contenu de la ressource, sa description, ses tags ni les titres
  d'articles du blog ou de vidéos Contentos.
couche: socle
moment: >-
  Le titre : simple, descriptif, compris par un néophyte, sans accroche ni sous-titre.
famille: contenu-autonomes
---

# Titrer une ressource

Autonomes est le site de formation de Manu pour les non-développeurs : des gens qui découvrent Claude Code, le terminal, n8n, l'auto-hébergement. Une ressource y est un tuto (un guide, parfois en plusieurs pages, souvent en vidéo), une fiche (un contexte détaillé : une notion, une pratique, un outil), une cheatsheet (une liste à retrouver) ou un exercice (une tâche à faire soi-même).

Le titre est ce qui fait qu'un lecteur clique ou passe son chemin. Mais ce lecteur ne sait pas encore ce qu'est Vercel, `/init` ou Coolify. Un titre qui accroche un développeur le laisse froid ; un titre qui joue l'effet de style lui cache ce qu'il va vraiment obtenir. Manu veut donc des titres qui ressemblent à une table des matières de manuel : plats, honnêtes, lisibles par quelqu'un qui débute.

## La règle

**Un titre dit ce que le lecteur va savoir faire ou comprendre, dans ses mots à lui, sans effet de style.**

Trois conséquences :

1. **Simple et descriptif.** Pas de deux-points suivi d'un sous-titre, pas de promesse gonflée (« le setup complet », « la cheatsheet complète », « qui changent tout »), pas de tournure d'accroche (« Votre site en ligne aujourd'hui »). Le titre nomme l'objet ou l'action, et s'arrête là.
2. **Compris par un néophyte.** Le lecteur doit saisir à quoi ça sert avant de connaître les outils. Un nom d'outil reste dans le titre seulement s'il est le sujet lui-même (Claude Code, n8n, CLAUDE.md, le terminal). Les outils intermédiaires du tuto (Vercel, GitHub, Hetzner, Coolify) n'y ont pas leur place : ils apparaissent dans la description et le contenu. Une commande brute (`/init`, `/clear`) n'est jamais un titre : on nomme ce qu'elle apporte.
3. **Une action quand c'est un tuto.** Un tuto peut commencer par le verbe à l'infinitif de ce que le lecteur va faire : « Installer… », « Créer… », « Mettre en ligne… ». Une fiche nomme plutôt un objet ou un « Comprendre… ». Une cheatsheet nomme simplement la famille de choses qu'elle liste. Un exercice nomme la tâche que le lecteur va accomplir, avec le verbe et le résultat (« Renommer 50 factures avec Claude Code ») ; le mot « exercice » n'a pas besoin d'être dans le titre, le type le dit déjà.

Un superlatif est acceptable quand il décrit une sélection réelle (« les 3 commandes les plus utiles ») : il dit ce qu'il y a dedans. Il est refusé quand il vend (« qui changent tout », « complet », « ultime »).

## Exemples contrastifs

Les titres de gauche sont ceux qui existaient sur Autonomes ; ceux de droite sont validés par Manu ou construits sur le même modèle.

| Avant | Pourquoi ça ne va pas | Après |
|---|---|---|
| Coder et déployer avec Claude : le setup complet | deux-points + sous-titre gonflé, et un néophyte ne voit pas ce qu'il obtient | Créer un site avec Claude et le mettre en ligne |
| Installer Claude Code, GitHub et Vercel | liste d'outils : on ne comprend pas à quoi ça sert | Créer un site avec Claude et le mettre en ligne |
| Les 3 commandes Claude Code qui changent tout | « qui changent tout » est une promesse, pas une description | Les 3 commandes Claude Code les plus utiles |
| /init, /clear et /resume | commandes brutes, illisibles pour un débutant | Les 3 commandes Claude Code les plus utiles |
| Votre setup n8n auto-hébergé : Hetzner + Coolify | deux-points, jargon (« auto-hébergé »), outils intermédiaires | Installer n8n sur votre propre serveur |
| CLAUDE.md : le briefing permanent de votre assistant | deux-points + métaphore d'accroche | Donner de la mémoire à Claude Code avec CLAUDE.md |
| Abonnement ou paiement au token : comprendre la facturation de Claude | trop long, le deux-points coupe en deux titres | Comprendre la facturation de Claude |
| Les commandes Claude Code : la cheatsheet complète | « complète » vend, le format n'a pas à être dans le titre | Les commandes Claude Code |
| Votre site en ligne aujourd'hui | accroche, on ne sait pas ce qu'on va faire ni avec quoi | Mettre un site en ligne gratuitement |

Ce qui reste tel quel, parce que c'est déjà juste : « Le terminal expliqué aux non-développeurs », « Le vocabulaire de l'interface », « Les permissions de Claude Code », « Bien commencer avec Claude Code ».

## Processus

1. **Comprendre ce que le lecteur obtient.** Lire la matière (le plan, le contenu, la vidéo, ou la ressource existante via `ressources_get`). Formuler en une phrase, comme si on l'expliquait à un ami qui n'y connaît rien : « à la fin, tu sauras … ». C'est de cette phrase que sort le titre, pas de la liste des outils.
2. **Identifier le type.** Tuto : le titre peut partir d'un verbe. Fiche : un objet ou un « Comprendre … ». Cheatsheet : la famille de choses listées. Exercice : la tâche, verbe et résultat.
3. **Regarder les titres voisins.** `ressources_list` donne l'existant. Le nouveau titre doit s'y ranger sans détonner, ne pas doublonner, et respecter la façon dont les autres nomment le même outil.
4. **Proposer 2 ou 3 candidats à Manu**, du plus sobre au plus explicite, avec en une ligne ce que chacun privilégie. Ne rien écrire dans Autonomes avant son choix. Si le titre est destiné à une ressource déjà en ligne, changer le titre sans toucher au slug, sauf demande explicite : le slug est une adresse que d'autres pages pointent.
5. **Passer la checklist** avant de proposer.

## Checklist avant de rendre la main

- [ ] Un néophyte comprend ce qu'il va savoir faire ou comprendre, sans connaître les outils
- [ ] Aucun deux-points, aucun tiret (cadratin ou demi-cadratin), aucun sous-titre
- [ ] Aucune promesse (« complet », « ultime », « qui change tout », « aujourd'hui », « en 5 minutes ») ni tournure publicitaire (« Votre X », « Le secret de… »)
- [ ] Seuls les outils qui sont le sujet sont nommés ; pas de commande brute
- [ ] Tuto : commence par un verbe à l'infinitif ou nomme l'action ; fiche : nomme l'objet ; cheatsheet : nomme la famille ; exercice : nomme la tâche
- [ ] Court : idéalement moins de 8 mots, en tout cas une seule idée
- [ ] Orthographe et grammaire impeccables, majuscule initiale seulement (pas de Majuscules À Chaque Mot), pas d'emoji
- [ ] Le titre tiendrait dans la table des matières d'un manuel pour débutants sans faire tache

## Boucle d'amélioration

Quand Manu refuse ou corrige un titre, ne pas se contenter de le remplacer : chercher la règle qui manquait, l'ajouter ici avec un exemple avant/après. C'est comme ça que cette règle s'est construite (trois allers-retours sur les mêmes titres) et c'est comme ça qu'elle reste juste.
