import pygame
from entities.entity import Entity  # On importe la classe mère

class Player(Entity):
    def __init__(self, x, y):
            #appel parent (Entity)
        super().__init__(x, y, speed=5)
        # Ici tu mets le code spécifique au Player (chargement image, etc.)
        # self.image = pygame.image.load(...)
        # self.rect = self.image.get_rect(topleft=(x, y))

    def move(self):
        # Ici tu mets la logique des touches (keyboard input) pour bouger
        pass