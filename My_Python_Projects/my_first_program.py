import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zombie Shooter")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Настройки игрока
player_width = 50
player_height = 50
player_x = WIDTH // 2
player_y = HEIGHT - 70
player_speed = 5

# Настройки пуль
bullets = []
bullet_width = 5
bullet_height = 10
bullet_speed = 7

# Настройки зомби
zombies = []
zombie_width = 40
zombie_height = 40
zombie_speed = 2
spawn_rate = 50  # Чем меньше, тем чаще появляются зомби

# Шрифт
font = pygame.font.Font(None, 36)

# Счёт и уровень оружия
score = 0
weapon_level = 1
weapon_damage = 10  # Базовый урон


# Функция для создания зомби
def spawn_zombie():
    x = random.randint(0, WIDTH - zombie_width)
    zombies.append([x, 0])

# Функция сброса игры
def reset_game():
    global player_x, player_y, bullets, zombies, score, weapon_level, weapon_damage
    player_x = WIDTH // 2
    player_y = HEIGHT - 70
    bullets = []
    zombies = []
    score = 0
    weapon_level = 1
    weapon_damage = 10

# Основной игровой цикл
running = True
game_over = False
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    if not game_over:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Стрельба
                    bullets.append([player_x + player_width // 2, player_y])

        # Движение игрока
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
            player_x += player_speed

        # Движение пуль
        for bullet in bullets[:]:
            bullet[1] -= bullet_speed
            if bullet[1] < 0:
                bullets.remove(bullet)

        # Появление зомби
        if random.randint(1, spawn_rate) == 1:
            spawn_zombie()

        # Движение зомби
        for zombie in zombies[:]:
            zombie[1] += zombie_speed
            if zombie[1] > HEIGHT:
                game_over = True  # Игра окончена, если зомби дошли до низа

        # Проверка столкновений (пуля — зомби)
        for bullet in bullets[:]:
            for zombie in zombies[:]:
                if (zombie[0] < bullet[0] < zombie[0] + zombie_width and
                    zombie[1] < bullet[1] < zombie[1] + zombie_height):
                    zombies.remove(zombie)
                    bullets.remove(bullet)
                    score += 1

                    # Прокачка оружия каждые 10 очков
                    if score % 10 == 0 and score > 0:
                        weapon_level += 1
                        weapon_damage += 5

        # Отрисовка игрока
        pygame.draw.rect(screen, GREEN, (player_x, player_y, player_width, player_height))

        # Отрисовка пуль
        for bullet in bullets:
            pygame.draw.rect(screen, WHITE, (bullet[0], bullet[1], bullet_width, bullet_height))

        # Отрисовка зомби
        for zombie in zombies:
            pygame.draw.rect(screen, RED, (zombie[0], zombie[1], zombie_width, zombie_height))

        # Отображение счёта и уровня оружия
        score_text = font.render(f!Счёт: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        
        weapon_text = font.render(f"Уровень оружия: {weapon_level} (Урон: {weapon_damage})", True, GREEN)
        screen.blit(weapon_text, (10, 50))

    else:
        # Экран окончания игры
        game_over_text = font.render("Игра окончена! Нажми R для перезапуска", True, RED)
        screen.blit(game_over_text, (WIDTH // 2 - 250, HEIGHT // 2))
        final_score = font.render(f"Твой счёт: {score}", True, WHITE)
        screen.blit(final_score, (WIDTH // 2 - 100, HEIGHT // 2 + 40))

        # Перезапуск по клавише R
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            reset_game()
            game_over = False

    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()
Как запустить
Установите Pygame (если ещё не установлен):

pip install pygame
Сохраните код в файл zombie_shooter.py.

Запустите:

python zombie_shooter.py
Как играть
Стрелки ←→ — движение игрока.

Пробел — выстрел.

R — перезапуск после проигрыша.

Что можно улучшить
Добавить разные типы оружия.

Ввести уровни/волны зомби.

Добавить звуки и спрайты вместо прямоугольников.

Реализовать сохранение лучшего счёта.

Добавить анимированных зомби и пули.

Алиса старается, но может ошибаться —
import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zombie Shooter")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Настройки игрока
player_width = 50
player_height = 50
player_x = WIDTH // 2
player_y = HEIGHT - 70
player_speed = 5

# Настройки пуль
bullets = []
bullet_width = 5
bullet_height = 10
bullet_speed = 7

# Настройки зомби
zombies = []
zombie_width = 40
zombie_height = 40
zombie_speed = 2
spawn_rate = 50  # Чем меньше, тем чаще появляются зомби

# Шрифт
font = pygame.font.Font(None, 36)

# Счёт и уровень оружия
score = 0
weapon_level = 1
weapon_damage = 10  # Базовый урон


# Функция для создания зомби
def spawn_zombie():
    x = random.randint(0, WIDTH - zombie_width)
    zombies.append([x, 0])

# Функция сброса игры
def reset_game():
    global player_x, player_y, bullets, zombies, score, weapon_level, weapon_damage
    player_x = WIDTH // 2
    player_y = HEIGHT - 70
    bullets = []
    zombies = []
    score = 0
    weapon_level = 1
    weapon_damage = 10

# Основной игровой цикл
running = True
game_over = False
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    if not game_over:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Стрельба
                    bullets.append([player_x + player_width // 2, player_y])

        # Движение игрока
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
            player_x += player_speed

        # Движение пуль
        for bullet in bullets[:]:
            bullet[1] -= bullet_speed
            if bullet[1] < 0:
                bullets.remove(bullet)

        # Появление зомби
        if random.randint(1, spawn_rate) == 1:
            spawn_zombie()

        # Движение зомби
        for zombie in zombies[:]:
            zombie[1] += zombie_speed
            if zombie[1] > HEIGHT:
                game_over = True  # Игра окончена, если зомби дошли до низа

        # Проверка столкновений (пуля — зомби)
        for bullet in bullets[:]:
            for zombie in zombies[:]:
                if (zombie[0] < bullet[0] < zombie[0] + zombie_width and
                    zombie[1] < bullet[1] < zombie[1] + zombie_height):
                    zombies.remove(zombie)
                    bullets.remove(bullet)
                    score += 1

                    # Прокачка оружия каждые 10 очков
                    if score % 10 == 0 and score > 0:
                        weapon_level += 1
                        weapon_damage += 5

        # Отрисовка игрока
        pygame.draw.rect(screen, GREEN, (player_x, player_y, player_width, player_height))

        # Отрисовка пуль
        for bullet in bullets:
            pygame.draw.rect(screen, WHITE, (bullet[0], bullet[1], bullet_width, bullet_height))

        # Отрисовка зомби
        for zombie in zombies:
            pygame.draw.rect(screen, RED, (zombie[0], zombie[1], zombie_width, zombie_height))

        # Отображение счёта и уровня оружия
        score_text = font.render(f!Счёт: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        
        weapon_text = font.render(f"Уровень оружия: {weapon_level} (Урон: {weapon_damage})", True, GREEN)
        screen.blit(weapon_text, (10, 50))

    else:
        # Экран окончания игры
        game_over_text = font.render("Игра окончена! Нажми R для перезапуска", True, RED)
        screen.blit(game_over_text, (WIDTH // 2 - 250, HEIGHT // 2))
        final_score = font.render(f"Твой счёт: {score}", True, WHITE)
        screen.blit(final_score, (WIDTH // 2 - 100, HEIGHT // 2 + 40))

        # Перезапуск по клавише R
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            reset_game()
            game_over = False

    pygame.display.flip()
    clock.tick(60)  # 60 FPS