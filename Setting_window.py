from Window import Pra_window
import pygame
import Variables as var
from Music import *


def print_text(message, x, y, font_color=(0, 0, 0), font_type='Marta_Decor_Two.ttf', font_size=20):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    var.screen.blit(text, (x, y))


def print_text_in_button(message, x, y, button_width, button_height, font_color=(0, 0, 0),
                         font_type='Marta_Decor_Two.ttf', font_size=20):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    var.screen.blit(text,
                    (x + button_width // 2 - text.get_width() // 2, y + button_height // 2 - text.get_height() // 2))


class Settings(Pra_window):
    def __init__(self):
        self.col_par = 1

    def first_update(self):
        self.button = Button(200, 50)
        self.button_set = Button(200, 50)
        self.update()

    def update(self):
        var.screen.fill((30, 30, 30))
        self.button.draw(40, var.SCREEN_HEIGHT - self.button.height - 40, 'Назад в меню')
        self.button_set.draw(var.SCREEN_WIDTH // 2 - self.button_set.width - 10,
                             var.SCREEN_HEIGHT // (self.col_par + 1) - self.button_set.height, 'Подсказки')
        if var.podskazki:
            print_text('Подсказки включены', var.SCREEN_WIDTH // 2 + 10,
                       var.SCREEN_HEIGHT // (self.col_par + 1) - self.button_set.height // 4 * 3, (0, 200, 140),
                       font_size=20)
        else:
            print_text('Подсказки выключены', var.SCREEN_WIDTH // 2 + 10,
                       var.SCREEN_HEIGHT // (self.col_par + 1) - self.button_set.height // 4 * 3, (0, 200, 140),
                       font_size=20)


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
                # Действия в зависимости от нажатой кнопки
                if text == 'Назад в меню':
                    var.name = 'Главное меню'
                    var.CHANGE_WINDOW = True
                if text == 'Подсказки':
                    var.podskazki = not var.podskazki
        else:
            pygame.draw.rect(var.screen, self.active_color, (x, y, self.width, self.height))
        print_text_in_button(text, x, y, self.width, self.height, font_size=35)
