from random import randint
import Variables
from Game_window import *
from Setting_window import *
from Setting_befor_game_window import *
from Setting_in_game import *
from Main_window import *
from Dilog_after_chel import *
import pygame
from Music import *
import time
from Help import *
from Rating import *


def load_image(name, colorkey=None):
    # Загрузка изображения
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        return '0'
    image = pygame.image.load(fullname)
    return image


def main():
    pygame.init()
    pygame.display.set_caption('Labyrinth')
    Variables.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    Variables.SCREEN_SIZE = Variables.SCREEN_HEIGHT, Variables.SCREEN_WIDTH = [Variables.screen.get_height(),
                                                                               Variables.screen.get_width()]
    # Створки ворот
    gate_left = load_image('Gate_left.png')
    gate_left = pygame.transform.scale(gate_left, (Variables.SCREEN_WIDTH // 2, Variables.SCREEN_HEIGHT))
    gate_reight = load_image('Gate_reight.png')
    gate_reight = pygame.transform.scale(gate_reight, (
    int((Variables.SCREEN_WIDTH // 2 + 1) / (gate_reight.get_width() - 310) * gate_reight.get_width()),
    Variables.SCREEN_HEIGHT))
    gate_standart_pos = [-gate_reight.get_width() - 5, 0, Variables.SCREEN_WIDTH + 1,
                         Variables.SCREEN_WIDTH - gate_reight.get_width() - 4]
    gate_pos = [-gate_reight.get_width() - 5, Variables.SCREEN_WIDTH + 1]
    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()
    # Создаём начальное окно
    Variables.window = MainWindow()
    running = True
    Variables.window.first_update()
    while running:
        if Variables.GATES_MOVI == 0:
            # Основные события
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if var.set_in is None:
                        Variables.window.window_event(event.key)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if var.set_in is None:
                        if event.button == 1:
                            Variables.window.mouse_event(event.pos)
        # Если изменяем окно
        if Variables.CHANGE_WINDOW:
            Variables.GATES_MOVI = 1
            Variables.FPS = 100
        # Движение ворот к центру
        if Variables.GATES_MOVI == 1:
            if gate_pos[0] == gate_standart_pos[0]:
                door()
            if gate_pos[0] + 80 >= gate_standart_pos[1]:
                gate_pos[0] += 5
                gate_pos[1] -= 5
            else:
                gate_pos[0] += 17
                gate_pos[1] -= 17
            if gate_pos[0] >= gate_standart_pos[1]:
                gate_pos[0] = gate_standart_pos[1]
                gate_pos[1] = gate_standart_pos[3]
                change_window()
                Variables.CHANGE_WINDOW = False
                try:
                    var.screen.blit(gate_left, (gate_pos[0], 0))
                    var.screen.blit(gate_reight, (gate_pos[1], 0))
                except Exception:
                    pass
                pygame.display.flip()
                pygame.time.delay(1000)
                Variables.GATES_MOVI = -1
        # Открытие ворот
        elif Variables.GATES_MOVI == -1:
            if gate_pos[0] == gate_standart_pos[1]:
                door()
            if gate_pos[0] + 20 >= gate_standart_pos[1]:
                gate_pos[0] -= 7
                gate_pos[1] += 7
            elif gate_pos[0] + 40 >= gate_standart_pos[1]:
                gate_pos[0] -= 14
                gate_pos[1] += 14
            elif gate_pos[0] + 80 >= gate_standart_pos[1]:
                gate_pos[0] -= 28
                gate_pos[1] += 28
            else:
                gate_pos[0] -= 35
                gate_pos[1] += 35
            if gate_pos[0] <= gate_standart_pos[0]:
                gate_pos[0] = gate_standart_pos[0]
                gate_pos[1] = gate_standart_pos[2]
                Variables.GATES_MOVI = 0
                Variables.FPS = 60
        if Variables.GATES_MOVI != 1:
            # Проверка на паузу
            if var.set_in is None:
                Variables.window.update()
            else:
                Variables.set_in.update()
        try:
            # Отрисовка ворот
            var.screen.blit(gate_left, (gate_pos[0], 0))
            var.screen.blit(gate_reight, (gate_pos[1], 0))
        except Exception:
            pass
        pygame.display.flip()
        clock.tick(Variables.FPS)
    pygame.quit()


def change_window():
    # Смена окна
    if Variables.name == 'Главное меню':
        Variables.window = MainWindow()
    elif Variables.name == 'Настройки':
        Variables.window = Settings()
    elif Variables.name == 'Предыгровое меню':
        Variables.window = Pre_game_setting()
    elif Variables.name == 'Игра':
        Variables.window = Pole([var.lab_w, var.lab_h], var.lab_col)
    elif Variables.name == 'Помощь':
        Variables.window = Help()
    elif Variables.name == 'Испытания':
        Variables.window = Pole([randint(6, 8), randint(6, 8)], randint(2, 5))
    elif Variables.name == 'Установка результата':
        Variables.window = Dilog()
    elif Variables.name == 'Рейтинг':
        Variables.window = Rating()
    Variables.window.first_update()


if __name__ == '__main__':
    main()
