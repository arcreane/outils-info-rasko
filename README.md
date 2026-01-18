Shooter arcade développé avec Pygame, intégrant une gestion dynamique d'entités (joueur, ennemis, bonus) et une interface utilisateur complète.

 But du jeu
L'objectif est de réaliser le score le plus élevé tout en gérant sa survie :

Élimination : Chaque ennemi détruit rapporte 10 points.

Survie : Une collision avec un ennemi retire 20 PV. Le jeu se termine à 0 PV.

Bonus : Des items apparaissent périodiquement (20-30s) pour restaurer la vie (Cœur) ou augmenter le score (Étoile).

Ambiance : Une musique de fond tourne en boucle durant toute la session de jeu.

 Commandes
Action	Touche
Démarrer	ENTRÉE (depuis le menu)
Déplacement	FLÈCHES DIRECTIONNELLES
Tirer	ESPACE

Exporter vers Sheets

 Règles d'équipe
Main Stable : Interdiction de push directement sur main.

Une Tâche = une carte Trello.

Commits Clairs : Titre explicite (ajouter les détails en description si nécessaire).

Pull avant Push : Toujours récupérer le travail des autres avant d'envoyer les git push.

 Architecture du projet
Le projet est structuré de manière modulaire :

entities/ : Classes des entités (Joueur, Ennemis, Bonus).

weapons/ : Logique des projectiles et armements.

ui/ : Composants d'interface (Menu principal, HUD).

main.py : Point d'entrée, boucle de jeu et gestionnaire d'états.

settings.py : Constantes globales (dimensions, couleurs, fréquences de spawn).

