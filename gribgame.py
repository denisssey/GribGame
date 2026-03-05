import pygame
import sys

pygame.init()

# Определение размеров экрана
display_width = 1920
display_height = 1080
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('GribGame')

# Загрузка фона главного меню
background_image = pygame.image.load('assets/images/menu2.jpg').convert()
background_image = pygame.transform.scale(background_image,
                                          (display_width, display_height))  # Масштабирование изображения

# Цвета
white = (255, 255, 255)
yellow = (255, 255, 0)

# Загрузка музыки
pygame.mixer.music.load('assets/sounds/Purrple Cat - Moonlit Walk .mp3')
pygame.mixer.music.set_volume(0.5)  # Громкость музыки

# Загрузка иконки приложения
icon = pygame.image.load('assets/images/icon.jpg')
# Загрузка иконки для отображения лого в панели задач
pygame.display.set_icon(icon)

# Загрузка изображения главного героя
main_hero_image = pygame.image.load('assets/images/Main_hero.png').convert_alpha()
main_hero_image = pygame.transform.scale(main_hero_image, (80, 90))

mob_image = pygame.image.load('assets/images/mob_1lvl.png').convert_alpha()
mob_image = pygame.transform.scale(mob_image, (75, 75))  # Масштабирование моба до нужного размера

door_image = pygame.image.load('assets/images/door.png').convert_alpha()
door_image = pygame.transform.scale(door_image, (100, 100))

score1_image = pygame.image.load('assets/images/score1.png').convert_alpha()
score1_image = pygame.transform.scale(score1_image, (45, 45))

score2_image = pygame.image.load('assets/images/score2.png').convert_alpha()
score2_image = pygame.transform.scale(score2_image, (55, 55))

lives_images = pygame.image.load('assets/images/lives.png').convert_alpha()
lives_images = pygame.transform.scale(lives_images, (45, 45))

music_playing = False
lives = 3
score = 0  # Глобальная переменная для очков


def play_music():
    pygame.mixer.music.play(-1)  # Воспроизведение музыки бесконечно
    global music_playing
    music_playing = True


def stop_music():
    pygame.mixer.music.stop()
    global music_playing
    music_playing = False


def confirm_exit():
    pygame.mixer.pause()  # Приостанавливаем звук (если играет)
    exit_message = "Вы уверены, что хотите выйти? (Нажмите Y для подтверждения или N для отмены)"
    exit_font = pygame.font.Font(None, 36)
    exit_text = exit_font.render(exit_message, True, (255, 255, 255))
    exit_rect = exit_text.get_rect(center=(display_width // 2, display_height // 2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_n:
                    pygame.mixer.unpause()  # Возобновляем звук
                    return

        display.fill((0, 0, 0))  # Заливаем фон чёрным
        display.blit(exit_text, exit_rect)
        pygame.display.update()


def confirm_exit_to_menu():
    pygame.mixer.pause()  # Приостанавливаем звук (если играет)
    exit_message = "Вы уверены, что хотите выйти в главное меню? (Нажмите Y для подтверждения или N для отмены)"
    exit_font = pygame.font.Font(None, 36)
    exit_text = exit_font.render(exit_message, True, (255, 255, 255))
    exit_rect = exit_text.get_rect(center=(display_width // 2, display_height // 2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    pygame.mixer.unpause()  # Возобновляем звук
                    return False
                elif event.key == pygame.K_n:
                    pygame.mixer.unpause()  # Возобновляем звук
                    return True

        display.fill((0, 0, 0))  # Заливаем фон чёрным
        display.blit(exit_text, exit_rect)
        pygame.display.update()


def confirm_exit_to_main_menu():
    pygame.mixer.pause()  # Приостанавливаем звук (если играет)
    menu_font = pygame.font.Font(None, 100)
    menu_text_font = pygame.font.Font(None, 64)
    menu_text_color = white

    exit_message = menu_font.render('Вы хотите выйти?', True, menu_text_color)
    no_text = menu_text_font.render('Нет (Press N)', True, menu_text_color)
    yes_text = menu_text_font.render('Да (Press Y)', True, menu_text_color)

    exit_message_rect = exit_message.get_rect(center=(display_width // 2, 225))
    no_text_rect = no_text.get_rect(center=(display_width // 2, 750))
    yes_text_rect = yes_text.get_rect(center=(display_width // 2, 540))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                confirm_exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    pygame.mixer.unpause()  # Возобновляем звук
                    return True
                elif event.key == pygame.K_y:
                    pygame.mixer.unpause()  # Возобновляем звук
                    return False

        display.blit(background_image, (0, 0))
        display.blit(exit_message, exit_message_rect)
        display.blit(no_text, no_text_rect)
        display.blit(yes_text, yes_text_rect)

        pygame.display.update()


def main_menu():
    menu_font = pygame.font.Font(None, 150)
    menu_text_font = pygame.font.Font(None, 64)
    menu_text_color = white

    title_text = menu_font.render('GribGame', True, menu_text_color)
    music_toggle_text = menu_text_font.render('Press M to Toggle Music', True, menu_text_color)
    start_text = menu_text_font.render('Press SPACE to Start Game', True, menu_text_color)

    menu_running = True
    clock = pygame.time.Clock()

    while menu_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                confirm_exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu_running = False  # Запуск игры
                elif event.key == pygame.K_m:
                    if music_playing:
                        stop_music()  # Выключить музыку
                    else:
                        play_music()  # Включить музыку
                elif event.key == pygame.K_ESCAPE:
                    confirm_exit()  # Показать запрос на выход
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Левая кнопка мыши
                    x, y = event.pos
                    if 300 <= x <= 1000 and 750 <= y <= 800:
                        if music_playing:
                            stop_music()
                        else:
                            play_music()
                    elif 300 <= x <= 1000 and 540 <= y <= 600:
                        menu_running = False  # Запуск игры

        # Отображение фона главного меню
        display.blit(background_image, (0, 0))

        # Отображение текста меню
        title_rect = title_text.get_rect(center=(display_width // 2, 225))
        music_toggle_rect = music_toggle_text.get_rect(center=(display_width // 2, 750))
        start_rect = start_text.get_rect(center=(display_width // 2, 540))

        display.blit(title_text, title_rect)
        display.blit(music_toggle_text, music_toggle_rect)
        display.blit(start_text, start_rect)

        pygame.display.update()
        clock.tick(60)  # Ограничение на 60 кадров в секунду


def level_1():
    platforms = [
        pygame.Rect(1620, 250, 300, 30),  # Верхняя крайняя правая платформа
        pygame.Rect(0, 250, 1000, 30),  # Верхняя крайняя левая платформа
        pygame.Rect(1185, 250, 250, 30),  # Верхняя платформа посередине
        pygame.Rect(0, 600, 70, 30),  # Переходящая платформа слева между 2 и 3 уровнями
        pygame.Rect(200, 500, 470, 30),  # 2 по уровню, левая
        pygame.Rect(850, 500, 850, 30),  # 2 по уровню, правая
        pygame.Rect(0, 750, 400, 30),  # 3 по уровню, левая
        pygame.Rect(670, 750, 700, 30),  # 3 по уровню, середина
        pygame.Rect(1500, 750, 420, 30),  # 3 по уровню, правая
        pygame.Rect(450, 850, 110, 30),  # Запрыгивание на плафтормы, левая
        pygame.Rect(560, 950, 110, 30)  # Запрыгивание на плафтормы, правая
    ]
    points_score1 = [
        pygame.Rect(200, 215, 20, 20),
        pygame.Rect(800, 215, 20, 20),
        pygame.Rect(1700, 215, 20, 20),
        pygame.Rect(15, 565, 20, 20),
        pygame.Rect(600, 465, 20, 20),
        pygame.Rect(1600, 465, 20, 20),
        pygame.Rect(800, 715, 20, 20),
        pygame.Rect(1600, 715, 20, 20)
    ]
    points_score2 = [
        pygame.Rect(1200, 205, 30, 30),
        pygame.Rect(1100, 455, 30, 30),
        pygame.Rect(200, 705, 30, 30),
    ]
    obstacles = [
        {'rect': pygame.Rect(250, 180, 75, 75), 'speed': 5, 'direction': 1, 'range': (150, 1000)},
        {'rect': pygame.Rect(500, 430, 75, 75), 'speed': 5, 'direction': 1, 'range': (210, 660)},
        {'rect': pygame.Rect(780, 680, 75, 75), 'speed': 5, 'direction': 1, 'range': (670, 1370)}
    ]
    door = pygame.Rect(display_width - 100, display_height - 110, 50, 100)

    return platforms, points_score1, points_score2, obstacles, door, 'assets/images/1lvl.jpg'


def level_2():
    platforms = [
        pygame.Rect(0, 250, 460, 30),  # 1 уровень, левая
        pygame.Rect(660, 250, 1020, 30),  # 1 уровень, правая
        pygame.Rect(1800, 380, 150, 30),  # 1 -> 2, правая
        pygame.Rect(230, 500, 820, 30),  # 2 уровень, левая
        pygame.Rect(1250, 500, 500, 30),  # 2 уровень, правая
        pygame.Rect(0, 620, 110, 30),  # 2 -> 3, левая
        pygame.Rect(0, 750, 450, 30),  # 3 уровень, левая
        pygame.Rect(700, 750, 400, 30),  # 3 уровень, середина
        pygame.Rect(1400, 750, 380, 30),  # 3 уровень, правая
        pygame.Rect(1190, 840, 170, 30),  # 3 между серединой и правой
        pygame.Rect(450, 840, 100, 30),  # подъем на 3 уровень, нижняя, левая
        pygame.Rect(550, 941, 100, 30)
    ]
    points_score1 = [
        pygame.Rect(250, 215, 20, 20),
        pygame.Rect(1250, 215, 20, 20),
        pygame.Rect(1790, 345, 20, 20),
        pygame.Rect(55, 585, 20, 20),
        pygame.Rect(650, 465, 20, 20),
        pygame.Rect(1650, 465, 20, 20),
        pygame.Rect(250, 715, 20, 20),
        pygame.Rect(850, 715, 20, 20)
    ]
    points_score2 = [
        pygame.Rect(900, 455, 30, 30),
        pygame.Rect(850, 205, 30, 30),
        pygame.Rect(1450, 705, 30, 30)
    ]
    obstacles = [
        {'rect': pygame.Rect(750, 185, 25, 25), 'speed': 5, 'direction': 1, 'range': (660, 1650)},
        {'rect': pygame.Rect(500, 435, 25, 25), 'speed': 5, 'direction': 1, 'range': (230, 1020)},
        {'rect': pygame.Rect(1500, 685, 25, 25), 'speed': 5, 'direction': 1, 'range': (1400, 1750)}
    ]
    door = pygame.Rect(display_width - 100, display_height - 110, 50, 100)

    return platforms, points_score1, points_score2, obstacles, door, 'assets/images/2lvl.jpg'


def level_3():
    platforms = [
        pygame.Rect(0, 250, 400, 30),
        pygame.Rect(640, 250, 350, 30),
        pygame.Rect(1320, 250, 595, 30),
        pygame.Rect(400, 380, 155, 30),
        pygame.Rect(640, 500, 770, 30),
        pygame.Rect(1590, 500, 160, 30),
        pygame.Rect(1800, 630, 115, 30),
        pygame.Rect(0, 750, 625, 30),
        pygame.Rect(990, 750, 175, 30),
        pygame.Rect(1330, 750, 175, 30),
        pygame.Rect(1600, 750, 285, 30),
        pygame.Rect(625, 850, 150, 30),
        pygame.Rect(775, 1000, 150, 30)
    ]
    points_score1 = [
        pygame.Rect(355, 215, 20, 20),
        pygame.Rect(1130, 325, 20, 20),
        pygame.Rect(1750, 215, 20, 20),
        pygame.Rect(785, 465, 20, 20),
        pygame.Rect(1640, 465, 20, 20),
        pygame.Rect(450, 715, 20, 20),
        pygame.Rect(1050, 715, 20, 20)
    ]
    points_score2 = [
        pygame.Rect(945, 455, 30, 30),
        pygame.Rect(50, 705, 30, 30),
        pygame.Rect(1550, 1035, 30, 30),
        pygame.Rect(1700, 1035, 30, 30)

    ]
    obstacles = [
        {'rect': pygame.Rect(1500, 185, 25, 25), 'speed': 5, 'direction': 1, 'range': (1320, 1850)},
        {'rect': pygame.Rect(800, 435, 25, 25), 'speed': 5, 'direction': 1, 'range': (645, 1350)},
        {'rect': pygame.Rect(250, 685, 25, 25), 'speed': 5, 'direction': 1, 'range': (0, 550)}
    ]
    door = pygame.Rect(display_width - 100, display_height - 110, 50, 100)

    return platforms, points_score1, points_score2, obstacles, door, 'assets/images/3lvl.jpg'


def game(level_func):
    global lives, score

    platforms, points_score1, points_score2, obstacles, door, background_image_path = level_func()
    background_image = pygame.image.load(background_image_path).convert()
    background_image = pygame.transform.scale(background_image, (display_width, display_height))

    rect_width = 80
    rect_height = 90
    rect_x = 30
    rect_y = 250 - rect_height
    rect_speed = 7
    gravity = 1
    jump_speed = 18
    velocity_y = 0
    is_jumping = False

    game_running = True
    clock = pygame.time.Clock()

    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                confirm_exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_running = confirm_exit_to_main_menu()  # Показать запрос на выход в меню

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            rect_x -= rect_speed
        if keys[pygame.K_d]:
            rect_x += rect_speed
        if keys[pygame.K_SPACE] and not is_jumping:
            velocity_y = -jump_speed
            is_jumping = True

        # Применение гравитации
        velocity_y += gravity
        rect_y += velocity_y

        if rect_x < 0:
            rect_x = 0
        elif rect_x > display_width - rect_width:
            rect_x = display_width - rect_width

        if rect_y >= display_height - rect_height:
            rect_y = display_height - rect_height
            velocity_y = 0
            is_jumping = False

        player_rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
        for platform in platforms:
            if player_rect.colliderect(platform):
                if velocity_y > 0 and player_rect.bottom <= platform.bottom:
                    rect_y = platform.top - rect_height
                    velocity_y = 0
                    is_jumping = False
                elif velocity_y < 0 and player_rect.top >= platform.top:
                    rect_y = platform.bottom
                    velocity_y = gravity
                elif player_rect.right >= platform.left and player_rect.left < platform.left:
                    rect_x = platform.left - rect_width
                elif player_rect.left <= platform.right and player_rect.right > platform.right:
                    rect_x = platform.right

                player_rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

        if player_rect.colliderect(door):
            return True

        for point in points_score1[:]:
            if player_rect.colliderect(point):
                points_score1.remove(point)
                score += 1

        for point in points_score2[:]:
            if player_rect.colliderect(point):
                points_score2.remove(point)
                score += 3

        for obstacle in obstacles:
            if player_rect.colliderect(obstacle['rect']):
                lives -= 1
                if lives == 0:
                    print("Game Over!")
                    return False
                else:
                    rect_x = 30  # Сброс позиции игрока
                    rect_y = 250 - rect_height
                    velocity_y = 0
                    is_jumping = False

        for obstacle in obstacles:
            obstacle['rect'].x += obstacle['speed'] * obstacle['direction']
            if obstacle['rect'].left < obstacle['range'][0] or obstacle['rect'].right > obstacle['range'][1]:
                obstacle['direction'] *= -1

        display.blit(background_image, (0, 0))
        display.blit(main_hero_image, (rect_x, rect_y))

        display.blit(door_image, door)

        for point in points_score1:
            display.blit(score1_image, point.topleft)

        for point in points_score2:
            display.blit(score2_image, point.topleft)

        for obstacle in obstacles:
            display.blit(mob_image, (obstacle['rect'].x, obstacle['rect'].y))

        # Отображение количества жизней
        for i in range(lives):
            x = (display_width - (i + 1) * 45, 10, 30, 30)
            display.blit(lives_images, x)

        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {score}', True, white)
        display.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    while True:
        main_menu()
        lives = 3
        score = 0  # Сброс очков при начале новой игры
        while game(level_1):
            if game(level_2):
                if game(level_3):
                    break