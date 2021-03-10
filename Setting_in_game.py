from Window import Pra_window
import Variables as var
import pygame
from Music import *
import os


def print_text(message, x, y, font_color=(60, 140, 190), font_type='Marta_Decor_Two.ttf', font_size=20):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    var.screen.blit(text, (x, y))


def print_text_in_button(message, x, y, button_width, button_height, font_color=(0, 0, 0),
                         font_type='Marta_Decor_Two.ttf', font_size=20):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    var.screen.blit(text,
                    (x + button_width // 2 - text.get_width() // 2, y + button_height // 2 - text.get_height() // 2))


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        return '0'
    image = pygame.image.load(fullname)
    return image


class Set_in_game(Pra_window):
    def __init__(self):
        super().__init__()

    def first_update(self):
        # Загрузка фона и создание кнопок
        im = load_image('zatemnenie.png')
        self.im = pygame.transform.scale(im, var.SCREEN_SIZE[::-1])
        self.button = Button(200, 50)
        self.button_play = Button(200, 50)
        var.screen.blit(self.im, (0, 0))
        self.update()

    def update(self):
        print_text('Пауза', var.SCREEN_WIDTH // 2 - pygame.font.Font('Marta_Decor_Two.ttf', 100).render('Пауза', True, (
        60, 140, 190)).get_width() // 2, 20, font_size=100)
        self.button.draw(var.SCREEN_WIDTH // 2 - self.button.width // 2,
                         var.SCREEN_HEIGHT // 2 - 40 - self.button.height, 'Назад в меню')
        self.button_play.draw(var.SCREEN_WIDTH // 2 - self.button_play.width // 2, var.SCREEN_HEIGHT // 2 + 40,
                              'Продолжить')


class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_color = (41, 150, 150)
        self.active_color = (9, 190, 150)

    def draw(self, x, y, text, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(var.screen, self.inactive_color, (x, y, self.width, self.height))
            if click[0] == 1:
                pygame.mixer.Sound.play(button_sound)
                pygame.time.delay(150)
                if text == 'Назад в меню':
                    var.set_in = None
                    var.name = 'Главное меню'
                    var.CHANGE_WINDOW = True
                    var.Chellenge = False
                    var.sum_time = 0
                    var.time_for_ur = 0
                if text == 'Продолжить':
                    var.set_in = None
        else:
            pygame.draw.rect(var.screen, self.active_color, (x, y, self.width, self.height))
        print_text_in_button(text, x, y, self.width, self.height, font_size=35)
