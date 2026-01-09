import pygame
from entities.entity import Entity


class Enemy(Entity):
    def __init__(self, x, y):
        # On initialise comme une Entité avec une vitesse différente
        super().__init__(x, y, speed=2)
        # Image ennemie
        # self.image = pygame.image.load("assets/enemy.png")

    def move(self):
        #deplacement
        self.rect.y += self.speed