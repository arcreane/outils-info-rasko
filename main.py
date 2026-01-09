import pygame
import sys
from entities.player import Player
from entities.enemy import Enemy

# Iinit pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Projet Rasko - Architecture Test")

# test architect création class
player = Player(400, 300)
enemy = Enemy(100, 100)

print("Architecture chargée avec succès !")
print(f"Joueur créé à la position : {player.rect}")

# Boucle de jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # écran noir
    screen.fill((0, 0, 0))

    # plus tard: player.draw(screen))

    pygame.display.flip()

pygame.quit()
sys.exit()