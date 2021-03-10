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


class Pre_game_setting(Pra_window):
    def __init__(self):
        super().__init__()

    def first_update(self):
        # Создание input_box и кнопок
        self.input_box1 = InputBox(var.SCREEN_WIDTH // 2, var.SCREEN_HEIGHT // 64 * 10, 140, 32, 'Размер лабиринта')
        self.input_box2 = InputBox(var.SCREEN_WIDTH // 2, var.SCREEN_HEIGHT // 64 * 15, 140, 32,
                                   'Количество цветов дверей')
        self.input_box3 = InputBox(var.SCREEN_WIDTH // 2, var.SCREEN_HEIGHT // 64 * 20, 140, 32, 'Сложность')
        self.input_boxes = [self.input_box1, self.input_box2, self.input_box3]
        self.button = Button(200, 50)
        self.button_play = Button(200, 50)

    def update(self):
        for box in self.input_boxes:
            box.update()
        var.screen.fill((30, 30, 30))
        for box in self.input_boxes:
            box.draw(var.screen)
        self.button.draw(40, var.SCREEN_HEIGHT - 40 - self.button.height, 'Назад в меню')
        self.button_play.draw(var.SCREEN_WIDTH - 40 - self.button_play.width,
                              var.SCREEN_HEIGHT - 40 - self.button_play.height, 'Играть')
        # Выводим текст
        print_text('Размер лабиринта', var.SCREEN_WIDTH // 2 + 10, var.SCREEN_HEIGHT // 64 * 10, (60, 140, 190),
                   font_size=30)
        print_text('Количество цветов дверей', var.SCREEN_WIDTH // 2 + 10, var.SCREEN_HEIGHT // 64 * 15 + 2,
                   (60, 140, 190), font_size=30)
        print_text('Сложность', var.SCREEN_WIDTH // 2 + 10, var.SCREEN_HEIGHT // 64 * 20 + 4, (60, 140, 190),
                   font_size=30)
        print_text('Количество цветов  показывает сколько',
                   var.SCREEN_WIDTH // 2 - pygame.font.Font('Marta_Decor_Two.ttf', 20).render(
                       'Пример - 64. Это создаст лабиринт 6 клеток в длинну и 4 в высоту', True,
                       (0, 0, 0)).get_width() // 2, var.SCREEN_HEIGHT // 64 * 25 + 20, (60, 140, 190), font_size=20)
        print_text('будет различных по цвету дверей в одном лабиринте',
                   var.SCREEN_WIDTH // 2 - pygame.font.Font('Marta_Decor_Two.ttf', 20).render(
                       'Пример - 64. Это создаст лабиринт 6 клеток в длинну и 4 в высоту', True,
                       (0, 0, 0)).get_width() // 2, var.SCREEN_HEIGHT // 64 * 25 + 50, (60, 140, 190), font_size=20)
        print_text('------------------------------------------------------',
                   var.SCREEN_WIDTH // 2 - pygame.font.Font('Marta_Decor_Two.ttf', 20).render(
                       'Пример - 64. Это создаст лабиринт 6 клеток в длинну и 4 в высоту', True,
                       (0, 0, 0)).get_width() // 2, var.SCREEN_HEIGHT // 64 * 25 + 80, (250, 140, 200), font_size=30)
        print_text('Размер лабиринта устанавливает размер игрового поля',
                   var.SCREEN_WIDTH // 2 - pygame.font.Font('Marta_Decor_Two.ttf', 20).render(
                       'Пример - 64. Это создаст лабиринт 6 клеток в длинну и 4 в высоту', True,
                       (0, 0, 0)).get_width() // 2, var.SCREEN_HEIGHT // 64 * 25 + 110, (60, 140, 190), font_size=20)
        print_text('Указывается в формате "xy" где x длинна ,а y высота',
                   var.SCREEN_WIDTH // 2 - pygame.font.Font('Marta_Decor_Two.ttf', 20).render(
                       'Пример - 64. Это создаст лабиринт 6 клеток в длинну и 4 в высоту', True,
                       (0, 0, 0)).get_width() // 2, var.SCREEN_HEIGHT // 64 * 25 + 140, (60, 140, 190), font_size=20)
        print_text('Пример - 64. Это создаст лабиринт 6 клеток в длинну и 4 в высоту',
                   var.SCREEN_WIDTH // 2 - pygame.font.Font('Marta_Decor_Two.ttf', 20).render(
                       'Пример - 64. Это создаст лабиринт 6 клеток в длинну и 4 в высоту', True,
                       (0, 0, 0)).get_width() // 2, var.SCREEN_HEIGHT // 64 * 25 + 170, (60, 140, 190), font_size=20)

    def window_event(self, k):
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
        # Задание базовых значений
        if self.name == 'Размер лабиринта':
            var.lab_h = 5
            var.lab_w = 5
            self.text = '55'
        elif self.name == 'Количество цветов дверей':
            var.lab_col = 3
            self.text = '3'
        elif self.name == 'Сложность':
            var.lab_hard = 2
            self.text = '2'
        self.txt_surface = var.FONT.render(self.text, True, self.color)

    def handle_event(self, k):
        if self.active:
            if pygame.key.name(k) == 'return':
                self.text = ''
            elif pygame.key.name(k) == 'backspace':
                self.text = self.text[:-1]
            else:
                if pygame.key.name(k).isdigit():
                    # Обновление значений
                    if self.name == 'Размер лабиринта':
                        if int(pygame.key.name(k)) > 2 and int(pygame.key.name(k)) < 10 and len(self.text) < 2:
                            self.text += pygame.key.name(k)
                            if len(self.text) == 2:
                                var.lab_h = int(self.text[0])
                                var.lab_w = int(self.text[1])
                    elif self.name == 'Количество цветов дверей':
                        if int(pygame.key.name(k)) > 1 and int(pygame.key.name(k)) < 7 and len(self.text) < 1:
                            self.text += pygame.key.name(k)
                            var.lab_col = int(self.text)
                        if len(self.text) == 0:
                            var.lab_col = None
                    elif self.name == 'Сложность':
                        if int(pygame.key.name(k)) > 0 and int(pygame.key.name(k)) < 3 and len(self.text) < 1:
                            self.text += pygame.key.name(k)
                            var.lab_hard = int(self.text)
                        if len(self.text) == 0:
                            var.lab_hard = None
                            # Re-render the text.
            self.txt_surface = var.FONT.render(self.text, True, self.color)
            if self.name == 'Размер лабиринта':
                if len(self.text) != 2:
                    var.lab_w = None
            elif self.name == 'Количество цветов дверей':
                if len(self.text) == 0:
                    var.lab_col = None
            elif self.name == 'Сложность':
                if len(self.text) == 0:
                    var.lab_hard = None

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
                    # Смена окна
                    if text == 'Назад в меню':
                        var.name = 'Главное меню'
                        var.CHANGE_WINDOW = True
                    elif (text == 'Играть' and not var.lab_col is None and
                          not var.lab_w is None and not var.lab_hard is None):
                        var.name = 'Игра'
                        var.CHANGE_WINDOW = True
            else:
                pygame.draw.rect(var.screen, self.active_color, (x, y, self.width, self.height))
        else:
            pygame.draw.rect(var.screen, self.active_color, (x, y, self.width, self.height))
        print_text_in_button(text, x, y, self.width, self.height, font_size=35)
