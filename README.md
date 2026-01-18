#Projet Rasko - Shooter Arcade
Shooter arcade développé avec Pygame intégrant un système de vagues, des bonus aléatoires et une interface utilisateur complète (HUD).

 #But du jeu
L'objectif est de réaliser le meilleur score possible tout en gérant sa survie :

Combat : Éliminez les ennemis pour gagner des points (+10 pts par ennemi).

Survie : Évitez les collisions qui retirent 20 PV. La partie s'arrête si la barre de vie tombe à zéro.

Bonus : Collectez les items qui apparaissent périodiquement pour vous soigner ou booster votre score.

Ambiance : Une musique de fond tourne en continu dès le lancement du jeu pour une immersion totale.

 #Commandes
ENTRÉE : Lancer la partie.

ESPACE : Tirer.

FLÈCHES : Déplacer le vaisseau.

 Règles d'équipe
#Pour assurer la stabilité du projet, l'équipe suit ces règles de workflow :

Main Stable : Interdiction de push directement sur la branche main.

Organisation : Une tâche = une carte Trello.

Commits Clairs : Pas trop de détails, ou alors les mettre en description.

Pull avant Push : Toujours récupérer le travail des autres avant d'envoyer les git push.

 #Architecture du projet
Le projet est structuré en modules pour séparer les responsabilités :

entities/ : Contient les êtres vivants (Joueur, Ennemis, Bonus).

weapons/ : Contient la gestion des armes et projectiles.

ui/ : Interface utilisateur (Menu, HUD).

main.py : Script principal gérant la boucle de jeu et la machine à états.

settings.py : Toutes les constantes globales du jeu.