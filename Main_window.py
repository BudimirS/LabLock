from Window import Pra_window
import sys
import Variables as var
import pygame
from Music import *

count = -1


def print_text(message, x, y, button_width, button_height, font_color=(0, 0, 0), font_type='Marta_Decor_Two.ttf',
               font_size=20):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    var.screen.blit(text,
                    (x + button_width // 2 - text.get_width() // 2, y + button_height // 2 - text.get_height() // 2))


class MainWindow(Pra_window):
    def __init__(self):
        super().__init__()
        self.standart_button_size = [200, 50]

    def first_update(self):
        global count
        var.screen.fill((255, 255, 255))
        if count == 47:
            count = 0
        else:
            count += 1
        # Создаём кнопки
        self.button = Button(*self.standart_button_size)
        self.button2 = Button(*self.standart_button_size)
        self.button3 = Button(*self.standart_button_size)
        self.button4 = Button(*self.standart_button_size)
        self.button6 = Button(*self.standart_button_size)
        self.button7 = Button(20, 20)
        BackGround = Background('data\\' + str(count) + '.gif', [0, 0])
        var.screen.blit(BackGround.image, BackGround.rect)
        self.button.draw(20, 100, 'Играть')
        self.button2.draw(20, 175 + self.standart_button_size[1], "Испытания")
        self.button3.draw(20, 250 + self.standart_button_size[1] * 2, 'Настройки')
        self.button4.draw(20, 325 + self.standart_button_size[1] * 3, 'Рейтинг')
        self.button6.draw(20, 400 + self.standart_button_size[1] * 4, 'Выйти')
        self.button7.draw(var.SCREEN_WIDTH - self.button7.width - 20, 20, '?')

    def update(self):
        global count
        var.screen.fill((255, 255, 255))
        if count == 47:
            count = 0
        else:
            count += 1
        BackGround = Background('data\\' + str(count) + '.gif', [0, 0])
        var.screen.blit(BackGround.image, BackGround.rect)
        self.button.draw(20, 150, 'Играть')
        self.button2.draw(20, 225 + self.standart_button_size[1], "Испытания")
        self.button3.draw(20, 300 + self.standart_button_size[1] * 2, 'Настройки')
        self.button4.draw(20, 375 + self.standart_button_size[1] * 3, 'Рейтинг')
        self.button6.draw(20, 450 + self.standart_button_size[1] * 4, 'Выйти')
        self.button7.draw(var.SCREEN_WIDTH - self.button7.width - 20, 20, '?')


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
                # Смена окна
                if text == 'Играть':
                    var.name = 'Предыгровое меню'
                    var.CHANGE_WINDOW = True
                if text == 'Испытания':
                    var.kol_chel = 0
                    var.Chellenge = True
                    var.name = 'Испытания'
                    var.CHANGE_WINDOW = True
                if text == 'Настройки':
                    var.name = 'Настройки'
                    var.CHANGE_WINDOW = True
                if text == 'Рейтинг':
                    var.name = 'Рейтинг'
                    var.CHANGE_WINDOW = True
                if text == '?':
                    var.name = 'Помощь'
                    var.CHANGE_WINDOW = True
                if text == 'Выйти':
                    sys.exit(1)

        else:
            pygame.draw.rect(var.screen, self.active_color, (x, y, self.width, self.height))
        if len(text) == 1:
            print_text(text, x, y, self.width, self.height, font_size=25)
        else:
            print_text(text, x, y, self.width, self.height, font_size=35)


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.transform.scale(pygame.image.load(image_file), var.SCREEN_SIZE[::-1])
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
