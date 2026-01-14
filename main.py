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
    # Initialisation du mixeur de son (optionnel mais recommandé)
    pygame.mixer.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Projet Rasko - V2 avec bonus et hud")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 24)

    # --- GESTION DE LA MUSIQUE ---
    try:
        # Remplace "musique_fond.mp3" par le chemin exact de ton fichier
        pygame.mixer.music.load("musique_fond.mp3")
        # Le paramètre -1 permet de répéter la musique à l'infini
        pygame.mixer.music.play(loops=-1)
        # Optionnel : Ajuster le volume (entre 0.0 et 1.0)
        pygame.mixer.music.set_volume(0.5)
    except pygame.error as e:
        print(f"Erreur lors du chargement de la musique : {e}")
    # -----------------------------

    # État du jeu
    game_state = "menu"
    main_menu = MainMenu()
    hud = HUD()

    # Groupe sprites
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    bonuses = pygame.sprite.Group()

    # Création du joueur
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)
    all_sprites.add(player)

    # Variable de jeu
    score = 0
    last_enemy_spawn = 0
    last_bonus_spawn = 0

    running = True
    while running:
        # Gestion des events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if game_state == "menu":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    game_state = "playing"
                    player.current_hp = player.max_hp
                    score = 0
                    enemies.empty()
                    bullets.empty()
                    bonuses.empty()

            elif game_state == "playing":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bullet = player.shoot()
                        if bullet:
                            all_sprites.add(bullet)
                            bullets.add(bullet)

        # Logique
        if game_state == "menu":
            main_menu.draw(screen)

        elif game_state == "playing":
            now = pygame.time.get_ticks()

            if now - last_enemy_spawn > ENEMY_SPAWN_RATE:
                last_enemy_spawn = now
                enemy = Enemy()
                all_sprites.add(enemy)
                enemies.add(enemy)

            if now - last_bonus_spawn > random.randint(20000, 30000):
                last_bonus_spawn = now
                bonus = Bonus()
                all_sprites.add(bonus)
                bonuses.add(bonus)

            all_sprites.update()

            hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
            for hit in hits:
                score += 10

            hits_bonus = pygame.sprite.spritecollide(player, bonuses, True)
            for bonus in hits_bonus:
                if bonus.type == "health":
                    player.heal(30)
                elif bonus.type == "score":
                    score += 50

            hits_player = pygame.sprite.spritecollide(player, enemies, True)
            for hit in hits_player:
                player.damage(20)
                if player.current_hp <= 0:
                    game_state = "menu"

            screen.fill(BLACK)
            all_sprites.draw(screen)
            hud.draw(screen, score, player)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()