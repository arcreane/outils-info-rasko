import pygame
import sys
from settings import *
from entities.player import Player
from entities.enemy import Enemy


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Projet Rasko - V1 Complet")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 24)  # Police pour le score

    # Groupes de sprites
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()  # Groupe spécifique pour les tirs
    enemies = pygame.sprite.Group()  # Groupe spécifique pour les ennemis

    # Création du joueur
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)
    all_sprites.add(player)

    # Variables de jeu
    score = 0
    last_enemy_spawn = 0  # Pour gérer le temps d'apparition

    running = True
    while running:
        #Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Tirer avec ESPACE
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = player.shoot()
                    if bullet:  # Si le tir est réussi (cooldown ok)
                        all_sprites.add(bullet)
                        bullets.add(bullet)

        # Spawn des ennemis (Automatique avec le temps)
        now = pygame.time.get_ticks()
        if now - last_enemy_spawn > ENEMY_SPAWN_RATE:
            last_enemy_spawn = now
            enemy = Enemy()  # Crée un ennemi position aléatoire
            all_sprites.add(enemy)
            enemies.add(enemy)

        # Maj
        all_sprites.update()

        # Collisions
        # Balles touche Ennemis (True, True veut dire : tuer balle, tuer ennemi)
        hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
        for hit in hits:
            score += 10  # On gagne 10 points
            print(f"Ennemi détruit ! Score: {score}")

        # Ennemis touche Joueur
        hits_player = pygame.sprite.spritecollide(player, enemies, False)
        if hits_player:
            print("GAME OVER ! Touche par un ennemi.")
            running = False  # Fin du jeu simple pour l'instant

        # Dessin
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # affiche score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()