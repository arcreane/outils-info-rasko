import pygame
import sys
# On importe les classes depuis nos nouveaux modules
from entities.player import Player


def main():
    # 1. INITIALISATION CENTRALISÉE
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Mon Projet Structuré")
    clock = pygame.time.Clock()

    # Création des instances d'objets (POO)
    player = Player(400, 300)
