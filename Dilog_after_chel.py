from Window import Pra_window
import pygame
import sqlite3
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


name = ''


class Dilog(Pra_window):
    def __init__(self):
        super().__init__()

    def first_update(self):
        # Первое обновление
        self.input_box1 = InputBox(var.SCREEN_WIDTH // 2, var.SCREEN_HEIGHT // 64 * 30, 140, 32, 'Имя')
        self.input_boxes = [self.input_box1]
        self.button = Button(200, 50)
        self.button_play = Button(200, 50)

    def update(self):
        # Обновления в игре
        for box in self.input_boxes:
            box.update()
        var.screen.fill((30, 30, 30))
        for box in self.input_boxes:
            box.draw(var.screen)
        # Кнопки на экране
        self.button.draw(40, var.SCREEN_HEIGHT - 40 - self.button.height, 'Выйти')
        self.button_play.draw(var.SCREEN_WIDTH - 40 - self.button_play.width,
                              var.SCREEN_HEIGHT - 40 - self.button_play.height, 'Сохранить')
        print_text('Имя', var.SCREEN_WIDTH // 2 + 10, var.SCREEN_HEIGHT // 64 * 30, (60, 140, 190), font_size=30)

    def window_event(self, k):
        # Отслеживание нажатий клавиатуры
        for box in self.input_boxes:
            box.handle_event(k)

    def mouse_event(self, pos):
        # If the user clicked on the input_box rect.
        for box in self.input_boxes:
            if box.rect.collidepoint(pos):
                # Toggle the active variable.
                box.active = not box.active
            else:
                box.active = False
            # Change the current color of the input box.
            box.color = var.COLOR_ACTIVE if box.active else var.COLOR_INACTIVE


class InputBox:
    def __init__(self, x, y, w, h, name):
        self.rect = pygame.Rect(x - w - 10, y, w, h)
        self.color = var.COLOR_INACTIVE
        self.text = ''
        self.name = name
        self.active = False
        self.txt_surface = var.FONT.render(self.text, True, self.color)

    def handle_event(self, k):
        if self.active:
            if pygame.key.name(k) == 'return':
                self.text = ''
            elif pygame.key.name(k) == 'backspace':
                self.text = self.text[:-1]
            else:
                if self.name == 'Имя':
                    if len(self.text) < 8 and pygame.key.name(k).isalnum() and len(pygame.key.name(k)) == 1:
                        self.text += pygame.key.name(k)
            self.txt_surface = var.FONT.render(self.text, True, self.color)
            global name
            name = self.text

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width
        self.rect.x = var.SCREEN_WIDTH // 2 - width - 10

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)


class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_color = (41, 150, 150)
        self.active_color = (9, 190, 150)

    def draw(self, x, y, text, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(var.screen, self.inactive_color, (x, y, self.width, self.height))
                if click[0] == 1:
                    pygame.mixer.Sound.play(button_sound)
                    pygame.time.delay(150)
                    # Смена окна при нажатии кнопки
                    if text == 'Выйти':
                        var.name = 'Главное меню'
                        var.CHANGE_WINDOW = True
                    elif text == 'Сохранить':
                        # Работа с бд
                        con = sqlite3.connect('data_base.db')
                        cur = con.cursor()
                        cur.execute("""INSERT INTO Records(Name, Time) VALUES(?, ?)""", (name, round(var.sum_time, 3)))
                        con.commit()
                        var.name = 'Главное меню'
                        var.CHANGE_WINDOW = True
                    var.sum_time = 0
                    var.time_for_ur = 0
            else:
                pygame.draw.rect(var.screen, self.active_color, (x, y, self.width, self.height))
        else:
            pygame.draw.rect(var.screen, self.active_color, (x, y, self.width, self.height))
        print_text_in_button(text, x, y, self.width, self.height, font_size=35)
