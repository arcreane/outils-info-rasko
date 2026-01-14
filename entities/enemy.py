import pygame
from entities.entity import Entity
from settings import *
import random


class Enemy(Entity):
    def __init__(self):
        # ennemie a pose X aléatoire en haut
        x = random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH)
        y = -ENEMY_HEIGHT  # Juste au-dessus de l'écran
        super().__init__(x, y, ENEMY_WIDTH, ENEMY_HEIGHT)
        self.image.fill(ENEMY_COLOR)
        self.speed = ENEMY_SPEED

    def update(self):
        # L'ennemi descend
        self.rect.y += self.speed

        # S'il sort en bas  détruit
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()