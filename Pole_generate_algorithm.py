import random


def generate_random_pole(width, height, colvo_col, levl):  # width, height, colvo colors, level(1, 2, 3)
    col = ['r', 'b', 'g', 'o', 't', 'y']  # red, blue, green, orange, light blue, yellow
    if colvo_col < 2:
        return 'Error'
    if width < 3:
        return 'Error'
    if height < 3:
        return 'Error'
    x = 0  # position hero x
    y = 0  # position hero y
    d = 0  # color door
    pole = []
    for i in range(height):
        a = []
        for j in range(width):
            b = []
            c1 = 'n'  # c1 - вверх
            c2 = 'n'  # c2 - вправо
            c3 = 'n'  # c3 - вниз
            c4 = 'n'  # c4 - влево
            if i == 0:
                c1 = 's'
            if j == 0:
                c4 = 's'
            if j == width - 1:
                c2 = 's'
            if i == height - 1:
                c3 = 's'
            b.append(c1)
            b.append(c2)
            b.append(c3)
            b.append(c4)
            a.append(b)
        pole.append(a)
    if levl == 1:
        while x != width - 1 or y != height - 1:
            a = random.randint(1, 2)  # 1 - Вниз, 2 - Влево
            if a == 1:
                if y != height - 1:
                    pole[y][width - x - 1][2] = col[d]
                    pole[y + 1][width - x - 1][0] = col[d]
                    d += 1
                    if d == colvo_col:
                        d = 0
                    y += 1
            if a == 2:
                if x != width - 1:
                    pole[y][width - x - 1][3] = col[d]
                    pole[y][width - x - 2][1] = col[d]
                    d += 1
                    if d == colvo_col:
                        d = 0
                    x += 1
        for i in range(height):
            for j in range(width):
                for k in range(4):
                    if pole[i][j][k] == 'n':
                        a = random.randint(0, colvo_col * 2 - 1)
                        if a != colvo_col * 2 - 1:
                            if k == 1:
                                pole[i][j][k] = col[(a // 2)]
                                pole[i][j + 1][3] = col[(a // 2)]
                            if k == 2:
                                pole[i][j][k] = col[(a // 2)]
                                pole[i + 1][j][0] = col[(a // 2)]
    if levl == 2:
        b = random.randint(1, 2)  # 1 - Вверх, 2 - Вправо
        if b == 1:
            e = random.randint(1, width - 2)
            if y != height - 1:
                pole[y][width - x - 1][2] = col[d]
                pole[y + 1][width - x - 1][0] = col[d]
                d += 1
                if d == colvo_col:
                    d = 0
                y += 1
        if b == 2:
            e = random.randint(1, height - 2)
            if x != width - 1:
                pole[y][width - x - 1][3] = col[d]
                pole[y][width - x - 2][1] = col[d]
                d += 1
                if d == colvo_col:
                    d = 0
                x += 1
        while x != width - 1 or y != height - 1:
            if b == 1:
                a = random.randint(1, 2)  # 1 - Вниз, 2 - Влево
                if a == 1:
                    if y != height - 1:
                        pole[y][width - x - 1][2] = col[d]
                        pole[y + 1][width - x - 1][0] = col[d]
                        d += 1
                        if d == colvo_col:
                            d = 0
                        y += 1
                if a == 2:
                    if x != width - 1:
                        pole[y][width - x - 1][3] = col[d]
                        pole[y][width - x - 2][1] = col[d]
                        d += 1
                        if d == colvo_col:
                            d = 0
                        x += 1
                    if x == e:
                        if y != 0:
                            y -= 1
                            pole[y][width - x - 1][2] = col[d]
                            pole[y + 1][width - x - 1][0] = col[d]
                            d += 1
                            if d == colvo_col:
                                d = 0
                            pole[y][width - x - 1][3] = col[d]
                            pole[y][width - x - 2][1] = col[d]
                            x += 1
                            d += 1
                            if d == colvo_col:
                                d = 0
            if b == 2:
                a = random.randint(1, 2)  # 1 - Вниз, 2 - Влево
                if a == 1:
                    if y != height - 1:
                        pole[y][width - x - 1][2] = col[d]
                        pole[y + 1][width - x - 1][0] = col[d]
                        d += 1
                        if d == colvo_col:
                            d = 0
                        y += 1
                    if y == e:
                        if x != 0:
                            x -= 1
                            pole[y][width - x - 1][3] = col[d]
                            pole[y][width - x - 2][1] = col[d]
                            d += 1
                            if d == colvo_col:
                                d = 0
                            pole[y][width - x - 1][2] = col[d]
                            pole[y + 1][width - x - 1][0] = col[d]
                            y += 1
                            d += 1
                            if d == colvo_col:
                                d = 0
                if a == 2:
                    if x != width - 1:
                        pole[y][width - x - 1][3] = col[d]
                        pole[y][width - x - 2][1] = col[d]
                        d += 1
                        if d == colvo_col:
                            d = 0
                        x += 1
        for i in range(height):
            for j in range(width):
                for k in range(4):
                    if pole[i][j][k] == 'n':
                        a = random.randint(0, colvo_col * 2 - 1)
                        if a != colvo_col * 2 - 1:
                            if k == 1:
                                pole[i][j][k] = col[(a // 2)]
                                pole[i][j + 1][3] = col[(a // 2)]
                            if k == 2:
                                pole[i][j][k] = col[(a // 2)]
                                pole[i + 1][j][0] = col[(a // 2)]
    return pole, col[:colvo_col]
