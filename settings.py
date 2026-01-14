# settings.py
import pygame

# Dim de l'écran
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# settings joueurs
PLAYER_SPEED = 5
PLAYER_WIDTH = 75
PLAYER_HEIGHT = 75


# Tir
BULLET_SPEED = 7
BULLET_WIDTH = 5
BULLET_HEIGHT = 10
BULLET_COLOR = (255, 255, 0) # Jaune

# Ennemi
ENEMY_SPEED = 3
ENEMY_WIDTH = 50
ENEMY_HEIGHT = 50
ENEMY_COLOR = (255, 0, 0) # Rouge
ENEMY_SPAWN_RATE = 1500 # ennemie toute les 1,5 sec