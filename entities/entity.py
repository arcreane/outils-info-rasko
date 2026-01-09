import pygame

class Entity:
    def __init__(self, x, y, speed):
        self.rect = pygame.Rect(x, y, 0, 0) # Position et taille
        self.speed = speed
        self.vie= vie
        self.image= image
        # Tu peux ajouter ici des variables communes (vie, image, etc.)

    def move(self):
        # Logique de déplacement de base (peut être vide pour l'instant)
        pass

    def draw(self, screen):
        # Méthode pour s'afficher (à surcharger par les enfants)
        pass