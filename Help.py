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


class Help(Pra_window):
    def __init__(self):
        pass

    def first_update(self):
        self.button = Button(200, 50)
        self.update()

    def update(self):
        # Вывод текста
        var.screen.fill((30, 30, 30))
        print_text('Цель игры - вам необходимо как можно быстрее добраться до финиша', 10, 30, (60, 140, 190),
                   font_size=30)
        print_text('Особенности:', 10, 70, (60, 140, 190), font_size=30)
        print_text('В лабиринте присутсвтуют двери разных цветов', 10, 110, (60, 140, 190), font_size=30)
        print_text('игрок может проходить только через двери своего цвета.', 10, 150, (60, 140, 190), font_size=30)
        print_text('При проходе через дверь например,', 10, 190, (60, 140, 190), font_size=30)
        print_text('красного',
                   10 + pygame.font.Font('Marta_Decor_Two.ttf', 30).render('При проходе через дверь например, ', True,
                                                                           (0, 0, 0)).get_width(), 190, (250, 10, 10),
                   font_size=30)
        print_text('цвета, игрок,', 10 + pygame.font.Font('Marta_Decor_Two.ttf', 30).render(
            'При проходе через дверь например, красного ', True, (0, 0, 0)).get_width(), 190, (60, 140, 190),
                   font_size=30)
        print_text('при наличии в данный момент', 10, 230, (60, 140, 190), font_size=30)
        print_text('красного',
                   10 + pygame.font.Font('Marta_Decor_Two.ttf', 30).render('при наличии в данный момент ', True,
                                                                           (0, 0, 0)).get_width(), 230, (250, 10, 10),
                   font_size=30)
        print_text('поменяет его например на',
                   10 + pygame.font.Font('Marta_Decor_Two.ttf', 30).render('при наличии в данный момент красного ',
                                                                           True, (0, 0, 0)).get_width(), 230,
                   (60, 140, 190), font_size=30)
        print_text('зеленый', 10 + pygame.font.Font('Marta_Decor_Two.ttf', 30).render(
            'при наличии в данный момент красного поменяет его например на ', True, (0, 0, 0)).get_width(), 230,
                   (10, 250, 10), font_size=30)
        print_text('и больше не сможет проходить через дверь красного цвета', 10, 270, (60, 140, 190), font_size=30)
        print_text('Профиль:', 10, 310, (60, 140, 190), font_size=30)
        print_text('Показывает лучшее время за которое были пройдены уровни испытаний', 10, 350, (60, 140, 190),
                   font_size=30)
        print_text('Испытания:', 10, 390, (60, 140, 190), font_size=30)
        print_text('Это группа сложных лабиринтов, сгенерированных программой, которые нужно пройти на скорость.', 10,
                   430, (60, 140, 190), font_size=30)
        print_text('Горячии клавиши:', 10, 470, (60, 140, 190), font_size=30)
        print_text('"h" - вызов подсказки во время прохождения лабиринта', 10, 510, (60, 140, 190), font_size=30)
        print_text('"p" - вкл/выкл музыки', 10, 550, (60, 140, 190), font_size=30)
        self.button.draw(40, var.SCREEN_HEIGHT - self.button.height - 40, 'Назад в меню')


class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_color = (41, 150, 150)
        self.active_color = (9, 190, 150)

    def draw(self, x, y, text, action=None):
        # Проверка на нажатие
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(var.screen, self.inactive_color, (x, y, self.width, self.height))
            if click[0] == 1:
                pygame.mixer.Sound.play(button_sound)
                pygame.time.delay(150)
                if text == 'Назад в меню':
                    var.name = 'Главное меню'
                    var.CHANGE_WINDOW = True
        else:
            pygame.draw.rect(var.screen, self.active_color, (x, y, self.width, self.height))
        print_text_in_button(text, x, y, self.width, self.height, font_size=35)
