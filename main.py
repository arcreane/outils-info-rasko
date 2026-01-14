import pygame
import sys
import random
from settings import *
from entities.player import Player
from entities.enemy import Enemy
from entities.bonus import Bonus
from ui.menu import MainMenu
from ui.hud import HUD


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Projet Rasko - V2 avec bonus et hud")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 24)  # Police pr score

    # État du jeu
    game_state = "menu"
    main_menu = MainMenu()
    hud = HUD()

    # Groupe sprites
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()  # grp pour tirs
    enemies = pygame.sprite.Group()  # Groupe pr ennemis
    bonuses = pygame.sprite.Group()  # <--- Groupe pr bonus

    # Création du joueur
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)
    all_sprites.add(player)

    # Variable de jeu
    score = 0
    last_enemy_spawn = 0  # Pour gére le temps d'apparition
    last_bonus_spawn = 0  # <-Timer pour bonus

    running = True
    while running:
        # Gestion des events
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
                    bonuses.empty()  # <- Reset bonus

            # Si Jeu
            elif game_state == "playing":
                # Tirer avec ESPACE
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bullet = player.shoot()
                        if bullet:  # tir réussi (cooldown ok)
                            all_sprites.add(bullet)
                            bullets.add(bullet)

        # Logique
        if game_state == "menu":
            main_menu.draw(screen)

        elif game_state == "playing":
            now = pygame.time.get_ticks()

            # Spawn des ennemis auto
            if now - last_enemy_spawn > ENEMY_SPAWN_RATE:
                last_enemy_spawn = now
                enemy = Enemy()  # creer enemie pose random
                all_sprites.add(enemy)
                enemies.add(enemy)

            # Spawn des BONUS toutes les 20-30 sec)
            if now - last_bonus_spawn > random.randint(20000, 30000):
                last_bonus_spawn = now
                bonus = Bonus()
                all_sprites.add(bonus)
                bonuses.add(bonus)

            # Maj
            all_sprites.update()

            # Collisions Tirs -> Ennemis
            hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
            for hit in hits:
                score += 10  # Win 10 points

            # Collisions Joueur -> recup bonus
            hits_bonus = pygame.sprite.spritecollide(player, bonuses, True)
            for bonus in hits_bonus:
                if bonus.type == "health":
                    player.heal(30)  # Rend 30 PV
                elif bonus.type == "score":
                    score += 50  # Bonus de points

            # Ennemis touche Joueur (Degats)
            hits_player = pygame.sprite.spritecollide(player, enemies, True)  # True pour supprimer ennemi
            for hit in hits_player:
                player.damage(20)
                if player.current_hp <= 0:
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