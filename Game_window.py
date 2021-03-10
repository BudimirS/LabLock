from Window import Pra_window
import Variables as var
import Pole_generate_algorithm as pga
from Setting_in_game import *
from Path_algorithm import *
import pygame
import keyboard
from random import randint
import os


def print_text(message, x, y, font_color=(0, 0, 0), font_type='Marta_Decor_Two.ttf', font_size=20):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    var.screen.blit(text, (x, y))


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        return '0'
    image = pygame.image.load(fullname)
    return image


def next_col(posl, ind):
    ind = posl.index(ind)
    ind += 1
    if ind >= len(posl):
        ind = 0
    return posl[ind]


class Pole(Pra_window):
    # size - размеры игрового поля (в клетках)
    def __init__(self, size, colors):
        super().__init__()
        # Базовые параметра
        self.height = size[1]
        self.width = size[0]
        self.cell_size = min([int((var.SCREEN_HEIGHT * 0.89) // self.height),
                              int(var.SCREEN_WIDTH // self.width)])
        if not var.Chellenge:
            self.board, colors = pga.generate_random_pole(self.width, self.height, colors, var.lab_hard)
        else:
            self.board, colors = pga.generate_random_pole(self.width, self.height, colors, randint(1, 2))
        self.left = (var.SCREEN_WIDTH - self.cell_size * self.width) // 2
        self.top = var.SCREEN_HEIGHT * 0.1
        self.colors = colors
        keyboard.add_hotkey('h', self.hot_key_for_help)
        self.win = False
        try:
            self.ways = find_way(self.board, self.colors, self.width - 1, 0, 0, self.height - 1)
        except Exception:
            self.ways = []

    def first_update(self):
        # Первоначальное обновление
        var.screen.fill('black')
        self.all_cells_sprites = pygame.sprite.Group()
        self.all_doors = pygame.sprite.Group()
        self.hero_sprites = pygame.sprite.Group()
        self.hero = Hero(self.width - 1, 0, self.board, self.hero_sprites, self.cell_size, self.left, self.top,
                         [self.height, self.width], self.colors)
        self.draw_cells()
        self.draw_doors()
        self.all_cells_sprites.draw(var.screen)
        self.hero_sprites.draw(var.screen)
        self.all_doors.draw(var.screen)

    def update(self):
        # Засекаем время
        if var.start_time == 0:
            var.start_time = time.time()
        var.time_for_ur = time.time() - var.start_time
        var.screen.fill('black')
        self.hero_sprites.update(-1)
        self.all_cells_sprites.draw(var.screen)
        # Отрисовка линии пути
        for i in range(1, len(self.hero.hero_way)):
            x1 = self.left + self.hero.hero_way[i - 1][1] * self.cell_size + self.cell_size // 2
            y1 = self.top + self.hero.hero_way[i - 1][0] * self.cell_size + self.cell_size // 2
            x2 = self.left + self.hero.hero_way[i][1] * self.cell_size + self.cell_size // 2
            y2 = self.top + self.hero.hero_way[i][0] * self.cell_size + self.cell_size // 2
            if i == 1:
                pygame.draw.line(var.screen, var.COLOR_VALUE[self.hero.colors_posled[i - 1]], (x1, y1),
                                 (x1 + (x2 - x1) // 2, y1 + (y2 - y1) // 2), self.cell_size // 10)
                pygame.draw.line(var.screen, var.COLOR_VALUE[self.hero.colors_posled[i]],
                                 (x1 + (x2 - x1) // 2, y1 + (y2 - y1) // 2), (x2, y2), self.cell_size // 10)
            else:
                x3 = x1 if y1 != y2 else x1 + ((x1 - x2) // abs(x1 - x2)) * self.cell_size // 20
                if x2 > x1:
                    x3 += 1
                y3 = y1 if x1 != x2 else y1 + ((y1 - y2) // abs(y1 - y2)) * self.cell_size // 20
                if y2 > y1:
                    y3 += 1
                pygame.draw.line(var.screen, var.COLOR_VALUE[self.hero.colors_posled[i - 1]], (x3, y3),
                                 (x3 + (x2 - x3) // 2, y3 + (y2 - y3) // 2), self.cell_size // 10)
                pygame.draw.line(var.screen, var.COLOR_VALUE[self.hero.colors_posled[i]],
                                 (x3 + (x2 - x3) // 2, y3 + (y2 - y3) // 2), (x2, y2), self.cell_size // 10)
        self.hero_sprites.draw(var.screen)
        self.all_doors.draw(var.screen)
        # Надписи Старт и Финиш
        message = pygame.font.Font('Marta_Decor_Two.ttf', 32 + (9 - self.height) * 2).render('Финиш', True,
                                                                                             (60, 140, 190))
        print_text('Финиш', self.left + self.cell_size // 2 - message.get_width() // 2,
                   self.top + self.cell_size * self.height - self.cell_size // 5 - message.get_height() // 2,
                   font_color=(255, 255, 255), font_type='Marta_Decor_Two.ttf', font_size=32 + (9 - self.height) * 2)
        message = pygame.font.Font('Marta_Decor_Two.ttf', 32 + (9 - self.height) * 2).render('Старт', True,
                                                                                             (60, 140, 190))
        print_text('Старт', self.left + self.cell_size * self.width - self.cell_size // 2 - message.get_width() // 2,
                   self.top + self.cell_size // 5 - message.get_height() // 2, font_color=(255, 255, 255),
                   font_type='Marta_Decor_Two.ttf', font_size=32 + (9 - self.height) * 2)
        if self.hero.hero_way[-1][1] == 0 and self.hero.hero_way[-1][0] == self.height - 1:
            self.win = True
        message = pygame.font.Font('Marta_Decor_Two.ttf', 32 + (9 - self.height) * 2).render(
            str(round(var.sum_time + var.time_for_ur, 1)), True, (60, 140, 190))
        print_text(str(round(var.sum_time + var.time_for_ur, 1)), var.SCREEN_WIDTH - 100 - message.get_width() // 2, 20,
                   font_color=(255, 255, 255), font_type='Marta_Decor_Two.ttf', font_size=32 + (9 - self.height) * 2)
        self.hero_sprites.update(-2)

    def window_event(self, key_press):
        # Реакция на нажатие клавиш
        if key_press == pygame.K_LEFT:
            self.hero_sprites.update(3)
        if key_press == pygame.K_RIGHT:
            self.hero_sprites.update(1)
        if key_press == pygame.K_UP:
            self.hero_sprites.update(0)
        if key_press == pygame.K_DOWN:
            self.hero_sprites.update(2)
        if key_press == pygame.K_ESCAPE:
            var.sum_time += var.time_for_ur
            var.start_time = 0
            var.set_in = Set_in_game()
            var.set_in.first_update()

    def draw_cells(self):
        # Отрисовка клеток поля
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                name = ''
                for k in self.board[i][j]:
                    if k != 's':
                        name += '1'
                    else:
                        name += '0'
                alpha = 0
                im = load_image(name + ".png")
                while im == '0':
                    name = name[1:] + name[0]
                    im = load_image(name + ".png")
                    alpha -= 90
                cell = pygame.sprite.Sprite(self.all_cells_sprites)
                cell.image = pygame.transform.scale(im, (self.cell_size, self.cell_size))
                cell.rect = im.get_rect()
                cell.rect.x = int(self.left + self.cell_size * j)
                cell.rect.y = int(self.top + self.cell_size * i)
                cell.image = pygame.transform.rotate(cell.image, alpha)

    def draw_doors(self):
        # Отрисовка Дверей
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                for k in range(len(self.board[i][j])):
                    dor = self.board[i][j][k]
                    if dor == 's' or dor == 'n':
                        continue
                    if k == 3 or k == 1:
                        alpha = -90
                    if k == 0 or k == 2:
                        alpha = 0
                    if k < 2:
                        dor += '1'
                    else:
                        dor += '2'
                    im = load_image(dor + ".png")
                    cell = pygame.sprite.Sprite(self.all_doors)
                    im_height = self.cell_size // 5
                    im_width = self.cell_size // 12
                    cell.image = pygame.transform.scale(im, (im_height, im_width))
                    cell.rect = im.get_rect()
                    if k == 0:
                        cell.rect.x = int(self.left + self.cell_size * j + self.cell_size / 5 * 2)
                        cell.rect.y = int(self.top + self.cell_size * i)
                    elif k == 1:
                        cell.rect.x = int(self.left + self.cell_size * (j + 1) - im_width)
                        cell.rect.y = int(self.top + self.cell_size * i + self.cell_size / 5 * 2)
                    elif k == 2:
                        cell.rect.x = int(self.left + self.cell_size * j + self.cell_size / 5 * 2)
                        cell.rect.y = int(self.top + self.cell_size * (i + 1) - im_width)
                    else:
                        cell.rect.x = int(self.left + self.cell_size * j)
                        cell.rect.y = int(self.top + self.cell_size * i + self.cell_size / 5 * 2)
                    cell.image = pygame.transform.rotate(cell.image, alpha)

    def hot_key_for_help(self):
        # Вызов подсказки
        if var.GATES_MOVI == 0 and self.hero.hero_way[-1] != [self.height - 1,
                                                              0] and var.podskazki and not var.Chellenge:
            hero_way = ''
            for i in self.hero.hero_way:
                hero_way += str(i[1]) + ',' + str(i[0]) + '-'
            hero_way = hero_way[:-1]
            way = ''
            while hero_way not in way:
                for way in self.ways:
                    if hero_way in way:
                        break
                if hero_way not in way:
                    hero_way = '-'.join(hero_way.split('-')[:-1])
            way = way[:-2]
            sled = way.split(hero_way)[1].split('-')[1][::-1].split(',')
            hero_way = [int(h) for h in hero_way.split('-')[-1][::-1].split(',')]
            self.hero.hero_way = self.hero.hero_way[:self.hero.hero_way.index(hero_way) + 1]
            self.hero.colors_posled = self.hero.colors_posled[:self.hero.hero_way.index(hero_way) + 1]
            if int(sled[0]) == self.hero.hero_way[-1][0]:
                napr = self.hero.hero_way[-1][1] - int(sled[1]) + 2
            else:
                napr = -self.hero.hero_way[-1][0] + int(sled[0]) + 1
            self.hero_sprites.update(napr)


class Hero(pygame.sprite.Sprite):
    image = load_image("hero.png")

    def __init__(self, x, y, pole, group, height, left, top, size, colors):
        super().__init__(group)
        self.pole = pole
        self.image = pygame.transform.scale(Hero.image, (height // 5, height // 5))
        self.height = height
        self.left = left
        self.top = top
        self.colors = colors
        self.rect = self.image.get_rect()
        self.rect.x = self.left + x * self.height + self.height // 5 * 2
        self.rect.y = self.top + y * self.height + self.height // 5 * 2
        self.travel = False
        self.proid_put = 0
        self.del_put = 15
        self.per_po = 'x'
        self.hero_way = [[y, x]]
        self.colors_posled = [colors[0]]
        self.nazad = False
        self.size = size

    def update(self, napr):
        if napr >= -1 or self.travel:
            # Если герой перемещается
            if self.travel:
                if not self.nazad:
                    self.rect.y += (self.hero_way[-1][0] - self.hero_way[-2][0]) * self.height // self.del_put
                    if self.proid_put + 1 == self.del_put:
                        self.rect.y = self.top + self.hero_way[-1][0] * self.height + self.height // 5 * 2
                    self.rect.x += (self.hero_way[-1][1] - self.hero_way[-2][1]) * self.height // self.del_put
                    if self.proid_put + 1 == self.del_put:
                        self.rect.x = self.left + self.hero_way[-1][1] * self.height + self.height // 5 * 2
                    self.proid_put += 1
                    if self.proid_put == self.del_put:
                        self.proid_put = 0
                        self.travel = False
                else:
                    self.rect.y += (self.hero_way[-2][0] - self.hero_way[-1][0]) * self.height // self.del_put
                    if self.proid_put + 1 == self.del_put:
                        self.rect.y = self.top + self.hero_way[-2][0] * self.height + self.height // 5 * 2
                    self.rect.x += (self.hero_way[-2][1] - self.hero_way[-1][1]) * self.height // self.del_put
                    if self.proid_put + 1 == self.del_put:
                        self.rect.x = self.left + self.hero_way[-2][1] * self.height + self.height // 5 * 2
                    self.proid_put += 1
                    if self.proid_put == self.del_put:
                        self.proid_put = 0
                        self.travel = False
                        del self.hero_way[-1]
                        del self.colors_posled[-1]
                        self.nazad = False
            elif napr == -1:
                return
            # Если нет перемещения
            elif not self.travel:
                self.travel = True
                if napr % 2 == 0:
                    if [self.hero_way[-1][0] + int(str(napr - 1)[:-1] + '1'),
                        self.hero_way[-1][1]] not in self.hero_way[: -2]:
                        if [self.hero_way[-1][0] + int(str(napr - 1)[:-1] + '1'),
                            self.hero_way[-1][1]] in self.hero_way:
                            self.nazad = True
                        else:
                            if (self.colors_posled[-1] == self.pole[self.hero_way[-1][0]][self.hero_way[-1][1]][napr] or
                                    self.pole[self.hero_way[-1][0]][self.hero_way[-1][1]][napr] == 'n'):
                                self.hero_way.append(
                                    [self.hero_way[-1][0] + int(str(napr - 1)[:-1] + '1'), self.hero_way[-1][-1]])
                                self.nazad = False
                            else:
                                self.travel = False
                    else:
                        self.travel = False
                else:
                    if [self.hero_way[-1][0],
                        self.hero_way[-1][1] + int(str(-(napr - 2))[:-1] + '1')] not in self.hero_way[: -2]:
                        if [self.hero_way[-1][0],
                            self.hero_way[-1][1] + int(str(-(napr - 2))[:-1] + '1')] in self.hero_way:
                            self.nazad = True
                        else:
                            if (self.colors_posled[-1] == self.pole[self.hero_way[-1][0]][self.hero_way[-1][1]][napr] or
                                    self.pole[self.hero_way[-1][0]][self.hero_way[-1][1]][napr] == 'n'):
                                self.hero_way.append(
                                    [self.hero_way[-1][0], self.hero_way[-1][1] + int(str(-(napr - 2))[:-1] + '1')])
                                self.nazad = False
                            else:
                                self.travel = False
                    else:
                        self.travel = False
                if (self.hero_way[-1][1] >= self.size[-1] or self.hero_way[-1][0] >= self.size[0] or
                        self.hero_way[-1][1] < 0 or self.hero_way[-1][0] < 0):
                    self.travel = False
                    del self.hero_way[-1]
                    self.nazad = False
                else:
                    if not self.nazad and self.travel:
                        self.colors_posled.append(self.pole[self.hero_way[-2][0]][self.hero_way[-2][1]][napr])
                        if self.colors_posled[-1] == 'n':
                            self.colors_posled[-1] = self.colors_posled[-2]
                        else:
                            self.colors_posled[-1] = next_col(self.colors, self.colors_posled[-1])
        elif napr == -2:
            self.check_for_win()

    def check_for_win(self):
        # Проверка на победу
        if self.hero_way[-1] == [self.size[0] - 1, 0]:
            self.print_win_text()
            pygame.display.flip()
            pygame.time.delay(1500)
            if not var.Chellenge:
                var.name = 'Предыгровое меню'
                var.CHANGE_WINDOW = True
                var.sum_time = 0
                var.time_for_ur = 0
                var.start_time = 0
            else:
                var.kol_chel += 1
                var.sum_time += var.time_for_ur
                var.time_for_ur = 0
                var.start_time = 0
                if var.kol_chel <= var.max_kol_chel:
                    var.name = 'Испытания'
                    var.CHANGE_WINDOW = True
                else:
                    var.Chellenge = False
                    var.name = 'Установка результата'
                    var.CHANGE_WINDOW = True

    def print_win_text(self, font_color=(255, 0, 0), font_type='Marta_Decor_Two.ttf', font_size=300):
        # Вывести текст победы
        im = load_image('zatemnenie.png')
        im = pygame.transform.scale(im, var.SCREEN_SIZE[::-1])
        var.screen.blit(im, (0, 0))
        font_type = pygame.font.Font(font_type, font_size)
        text = font_type.render('You win', True, font_color)
        var.screen.blit(text, (
        var.SCREEN_WIDTH // 2 - text.get_width() // 2, var.SCREEN_HEIGHT // 2 - text.get_height() // 2))
