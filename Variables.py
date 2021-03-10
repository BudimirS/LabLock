import sqlite3
import pygame

FONT_SIZE = 18
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
FPS = 60
WIN = False
POLE_SIZE = [[7, 5], [14, 10], [21, 15]]
COLOR_VALUE = {
    'r': 'red',
    'g': 'green',
    'b': 'blue',
    'o': 'orange',
    't': 'turquoise',
    'y': 'yellow'
}
CON = sqlite3.connect('data_base.db')
CUR = CON.cursor()
COLOR_ACTIVE = pygame.Color(41, 150, 150)
COLOR_INACTIVE = pygame.Color(9, 190, 150)
pygame.init()
FONT = pygame.font.Font(None, 32)
name = 'Главное меню'
CHANGE_WINDOW = False
GATES_MOVI = 0  # -1 - открытие ворот, 0 - стоят, 1 - закрытие ворот
podskazki = True
FILENAME = 'pole/Pole3.txt'
lab_hard = 2
lab_w = 5
lab_h = 5
lab_col = 3
set_in = None
Chellenge = False
kol_chel = 1
max_kol_chel = 9
sum_time = 0
time_for_ur = 0
start_time = 0
