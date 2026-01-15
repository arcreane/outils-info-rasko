[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/lCgyrFil)

# Projet Rasko - V2

Shooter arcade développé avec Pygame. Cette version intègre un système de vagues, des bonus aléatoires et une interface utilisateur complète (HUD).

## 🎯 But du jeu
L'objectif est de réaliser le **meilleur score** possible tout en gérant sa survie :
* **Combat** : Éliminez les ennemis pour gagner des points (**+10 pts** par ennemi).
* **Survie** : Évitez les collisions qui retirent **20 PV**. La partie s'arrête si la barre de vie tombe à zéro.
* **Bonus** : Collectez les items qui apparaissent périodiquement pour vous soigner ou booster votre score.
* **Ambiance** : Une musique de fond tourne en continu dès le lancement du jeu pour une immersion totale.

## 🕹️ Commandes
* **ENTRÉE** : Lancer la partie
* **ESPACE** : Tirer
* **FLÈCHES** : Déplacer le vaisseau

## 👥 Règles d'équipe
1. **Main Stable** : Interdiction de push directement sur `main`.
2. **Une Tâche = une carte Trello**.
3. **Commits Clairs** : pas trop de détail ou alors mettre en description.
4. **Pull avant Push** : Toujours récupérer le travail des autres avant d'envoyer les git push.

## 🏗️ Architecture du projet
Le projet est désormais structuré en modules :
- `entities/` : Contient les êtres vivants (Joueur, Ennemis, Bonus).
- `weapons/` : Contient la gestion des armes.
- `ui/` : Interface utilisateur (Menu, HUD).
- `main.py` : Point d'entrée et chef d'orchestre.
- `settings.py` : Toutes les constantes globales.
