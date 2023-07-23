import pygame
import random
from PlayerShip import PlayerShip
from bullet import Bullet
import enemy
from enemy_bullet import Enemy_bullet
from enemy_bullet import Enemy_bullet_trace
import power_item
pygame.init()
pygame.mixer.init()
# load screen
screen = pygame.display.set_mode((480, 640))
bg = pygame.image.load("MiniPixelPack/Space_BG (2 frames) (64 x 64).png")
bg = pygame.transform.scale(bg, (480, 640))
screen.blit(bg, (0, 0))
clock = pygame.time.Clock()

s_rect = screen.get_rect()
player_ship = PlayerShip("ship_image.png", s_rect)

# Load the sound effect
shoot_sound = pygame.mixer.Sound("8-Bit Sound Library/Wav/Shoot_01.wav")
shoot_sound.set_volume(0.1)
death_sound = pygame.mixer.Sound("8-Bit Sound Library/Wav/Hero_Death_00.wav")
death_sound.set_volume(0.5)
explosion_sound = pygame.mixer.Sound(
    "8-Bit Sound Library/Wav/Explosion_00.wav")
explosion_sound.set_volume(0.1)
achievement_sound = pygame.mixer.Sound(
    "8-Bit Sound Library\Wav\Jingle_Achievement_00.wav")
achievement_sound.set_volume(0.5)
# load bgm

music_files = [
    '01. A Dream that is more Scarlet than Red.mp3',
    '02. A Soul that is Red, like a Ground Cherry.mp3',
    '03. Apparitions Stalk the Night.mp3',
    '04. Lunate Elf.mp3',
    '05. Tomboyish Girl in Love.mp3',
    '06. Shanghai Teahouse ~ Chinese Tea.mp3',
    '07. Shanghai Alice of Meiji 17.mp3',
    '08. Voile, the Magic Library.mp3',
    "09. Locked Girl ~ The Girl's Secret Room.mp3",
    '10. The Maid and the Pocket Watch of Blood.mp3',
    '11. Lunar Clock ~ Luna Dial.mp3',
    '12. The Young Descendant of Tepes(1).mp3',
    '12. The Young Descendant of Tepes.mp3',
    '13. Septette for a Dead Princess.mp3',
    '14. The Centennial Festival for Magical Girls.mp3',
    '15. U.N. Owen was Her.mp3',
    '16. An Eternity that is More Transient than Scarlet.mp3',
    '17. Crimson Tower ~ Eastern Dream....mp3']
music_file = random.choice(music_files)
pygame.mixer.music.load("bgm/" + music_file)

# enemy groups
all_sprites = pygame.sprite.Group()
bullets_sprites = pygame.sprite.Group()
# player
PlayerShip_sprites = pygame.sprite.Group()
PlayerShip_sprites.add(player_ship)

# player bullets
bullets = pygame.sprite.Group()  # in milliseconds
last_bullet_time = pygame.time.get_ticks()

#items

items = pygame.sprite.Group()
item_timer = pygame.time.get_ticks()

def update_all(group):
    for e in group:
        e.update()


def add_alan(num=3, s_rect=s_rect):
    alans = []
    for i in range(num):
        alan = enemy.Alan(s_rect)
        alan.name = 'alan' + str(i)
        alans.append(alan)
    return alans


def add_bon(num=3, s_rect=s_rect):
    bon = []
    for i in range(num):
        b = enemy.Bon(s_rect)
        b.name = 'bon' + str(i)
        bon.append(b)
    return bon


def add_lip(num=3, s_rect=s_rect):
    lips = []
    for i in range(num):
        l = enemy.Lips(s_rect)
        l.name = 'lip' + str(i)
        lips.append(l)
    return lips


def fire_enemy_bullet(all_sprites, bullets_sprites, bullet_speed, interval_bon, interval_lip):
    current_time = pygame.time.get_ticks()
    for sprite in all_sprites:
        prob = 0.6
        if (isinstance(sprite, enemy.Bon) and (current_time - sprite.last_shot) > interval_bon) and random.random() > prob:
            sprite.last_shot = current_time
            bullet = Enemy_bullet(sprite.rect.centerx,
                                  sprite.rect.bottom, bullet_speed)
            bullets_sprites.add(bullet)

        elif (isinstance(sprite, enemy.Lips) and (current_time - sprite.last_shot) > interval_lip) and random.random() > prob:
            sprite.last_shot = current_time
            bullet = Enemy_bullet_trace(
                sprite.rect.centerx, sprite.rect.bottom, bullet_speed, player_ship)
            bullets_sprites.add(bullet)


def render_lives(screen, font, x, y, lives):
    text = font.render("LIVES:" + str(lives), True, (255, 255, 255))
    screen.blit(text, (x, y))


def add_all_to_group(group):
    for e in group:
        all_sprites.add(e)


pygame.mixer.music.load("bgm/" + music_file)
pygame.display.set_caption("To the stars")
font = pygame.font.Font(None, 20)
score = 0
# main loop
running = True
paused = False
level = 1
timer = pygame.time.get_ticks()
while running:
    screen.blit(bg, (0, 0))
    render_lives(screen, font, 10, 600, player_ship.lives)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused = not paused

    # leveling
    if level == 1:

        bullet_interval = 500
        enemy_interval = 2000
        B_bullet_interval = 2000
        L_bullet_interval = 3000
        E_bullet_speed = 5
        alan_num = 4
        bon_num = 0
        lip_num = 0

    if level == 1 and score > 2000:
        level = 2
        bullet_interval = 300
        B_bullet_interval = 1800
        L_bullet_interval = 2700
        E_bullet_speed = 5.5
        bon_num += 3

        achievement_sound.play()

    if level == 2 and score > 5000:
        level = 3
        bullet_interval = 150
        enemy_interval -= 200
        B_bullet_interval = 1600
        L_bullet_interval = 2400
        E_bullet_speed = 6
        lip_num += 3
        bon_num += 3
        achievement_sound.play()

    if level == 3 and score > 10000:
        level = 4
        bullet_interval = 80
        enemy_interval -= 200
        B_bullet_interval = 1600
        L_bullet_interval = 2400
        E_bullet_speed = 6
        lip_num += 2
        bon_num += 2
        achievement_sound.play()

    if level == 4:
        insane = score//10000 - 1
        old_insane = 0
        if old_insane - insane > 0:
            enemy_interval = int(enemy_interval*0.85)
            B_bullet_interval = int(B_bullet_interval*0.85)
            L_bullet_interval = int(L_bullet_interval*0.85)
            E_bullet_speed *= 1.1
            lip_num += 2
            bon_num += 2
            old_insane += 1

    if (not paused) and player_ship.lives:
        # Collision Detection ---------------------------------
        collisions = pygame.sprite.groupcollide(
            bullets, all_sprites, True, True)
        if collisions:
            score += 100
            explosion_sound.play()



        collided_enemies = pygame.sprite.spritecollide(
            player_ship, all_sprites, False)
        Enemy_bullet_player_collision = pygame.sprite.spritecollide(
            player_ship, bullets_sprites, False)
        if collided_enemies or Enemy_bullet_player_collision:
            player_ship.hit()

        item_collision = pygame.sprite.spritecollide(player_ship, items,True)

        if item_collision:
            for e in all_sprites:
                score += 100
                e.explode()
                explosion_sound.play()
        # shooting --------------------------------------------
        current_time = pygame.time.get_ticks()
        if current_time - last_bullet_time >= bullet_interval:
            last_bullet_time = current_time
            bullet = Bullet(player_ship.rect.x +
                            player_ship.rect.width // 2, player_ship.rect.y)
            bullets.add(bullet)
            shoot_sound.play()

        # new enemy

        if current_time - timer >= enemy_interval:
            timer = current_time
            add_all_to_group(add_alan(alan_num))
            add_all_to_group(add_bon(bon_num))
            add_all_to_group(add_lip(lip_num))
        
        # drop items --------------------------------

        if current_time - item_timer >= 30000:
            item_timer = current_time
            item = power_item.power_item(s_rect)
            items.add(item)
        

    # updates
        fire_enemy_bullet(all_sprites, bullets_sprites,
                          E_bullet_speed, B_bullet_interval, L_bullet_interval)

        player_ship.update()  # player
        PlayerShip_sprites.draw(screen)

        all_sprites.draw(screen)  # enemy
        update_all(all_sprites)

        bullets.draw(screen)  # player b
        update_all(bullets)

        bullets_sprites.draw(screen)  # enemy b
        update_all(bullets_sprites)

        items.draw(screen)
        items.update()

        pygame.display.update()
        score_text = font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(score_text, (0, 0))
        pygame.display.flip()
        if not pygame.mixer.music.get_busy():
            music_file = random.choice(music_files)
            pygame.mixer.music.load("bgm/" + music_file)
            pygame.mixer.music.set_volume(0.6)
            pygame.mixer.music.play(-1)

        clock.tick(60)

        if player_ship.lives == 0:
            death_sound.play()
            # Display game over screen
            game_over_font = pygame.font.Font(None, 48)
            game_over_text = game_over_font.render(
                "Game Over", True, (255, 255, 255))
            screen.blit(game_over_text, (screen.get_width(
            )/2 - game_over_text.get_width()/2, screen.get_height()/2 - game_over_text.get_height()/2))
            score_font = pygame.font.Font(None, 36)
            score_text = score_font.render(
                "Score: " + str(score), True, (255, 255, 255))
            screen.blit(score_text, (screen.get_width(
            )/2 - score_text.get_width()/2, screen.get_height()/2 + score_text.get_height()))

            if score < 1000:
                result_font = pygame.font.Font(None, 24)
                result_text = result_font.render(
                    "Keep trying!", True, (255, 255, 255))
                screen.blit(result_text, (screen.get_width(
                )/2 - result_text.get_width()/2, screen.get_height()/2 + 2*score_text.get_height()))
            else:
                result_font = pygame.font.Font(None, 24)
                if level == 1:
                    result_text = result_font.render(
                        "You have reached level 1!", True, (255, 255, 255))
                elif level == 2:
                    result_text = result_font.render(
                        "You have reached level 2!", True, (255, 255, 255))
                elif level == 3:
                    result_text = result_font.render(
                        "You have reached level 3!", True, (255, 255, 255))
                elif level == 4:
                    result_text = result_font.render(
                        f"You have reached insane {insane}!", True, (255, 255, 255))
                screen.blit(result_text, (screen.get_width(
                )/2 - result_text.get_width()/2, screen.get_height()/2 + 2*score_text.get_height()))


            pygame.display.update()


pygame.quit()
