import pygame
import sys
from settings import *
from entities.player import Player
from entities.enemy import Enemy
from ui.menu import MainMenu
from ui.hud import HUD


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Projet Rasko - V1 Complet")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 24)  # Police pr score

    # État du jeu
    game_state = "menu"
    main_menu = MainMenu()
    hud = HUD()

    # Groupes sprites
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()  #grp pour tirs
    enemies = pygame.sprite.Group()  # Groupe pr ennemis

    # Création du joueur
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)
    all_sprites.add(player)

    # Variable de jeu
    score = 0
    last_enemy_spawn = 0  # Pour gére le temps d'apparition

    running = True
    while running:
        #Gestion des events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Si Menu
            if game_state == "menu":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    game_state = "playing"
                    # Reset variables
                    player.current_hp = player.max_hp
                    score = 0
                    enemies.empty()
                    bullets.empty()

            # Si Jeu
            elif game_state == "playing":
                # Tirer avec ESPACE
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bullet = player.shoot()
                        if bullet:  #tir réussi (cooldown ok)
                            all_sprites.add(bullet)
                            bullets.add(bullet)

        # Logique
        if game_state == "menu":
            main_menu.draw(screen)

        elif game_state == "playing":
            # Spawn des ennemis auto
            now = pygame.time.get_ticks()
            if now - last_enemy_spawn > ENEMY_SPAWN_RATE:
                last_enemy_spawn = now
                enemy = Enemy()  # creer enemie pose random
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

            # Ennemis touche Joueur (Dégâts)
            hits_player = pygame.sprite.spritecollide(player, enemies, True) # True pour supprimer ennemi
            for hit in hits_player:
                player.damage(20)
                print(f"Aie! Vie: {player.current_hp}")
                if player.current_hp <= 0:
                    print("GAME OVER ! Touche par un ennemi.")
                    game_state = "menu"  # Retour au menu

            # Dessin
            screen.fill(BLACK)
            all_sprites.draw(screen)

            # affiche HUD (remplace ancien affichage score)
            hud.draw(screen, score, player)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()