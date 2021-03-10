import time

next_visit = []


def find_way(pole, posled, x1, y1, x2, y2):
    # Шлавный цикл для нахождения пути
    way = []
    for i in pole:
        way.append([])
        for j in i:
            way[-1].append([])
    global next_visit
    way[y1][x1] = [str(x1) + ',' + str(y1) + ',' + posled[0]]
    next_visit.append([x1, y1])
    waves(pole, way, posled)
    return way[y2][x2]


def waves(pole, way, posled):
    # функция, вызываемая рекурсивно
    time.sleep(0)
    global next_visit
    k = next_visit[0]
    for i in range(len(pole[k[1]][k[0]])):
        for j in range(len(way[k[1]][k[0]])):
            if way[k[1]][k[0]][j][-1] == pole[k[1]][k[0]][i]:
                if i % 2 == 0:
                    delt = i - 1
                    if str(k[0]) + ',' + str(k[1] + delt) not in way[k[1]][k[0]][j]:
                        if (way[k[1]][k[0]][j][:-2] + '-{},{},{}'.format(k[0], k[1] + delt,
                                                                         next_col(posled, way[k[1]][k[0]][j][-1]))
                                not in way[k[1] + delt][k[0]]):
                            way[k[1] + delt][k[0]].append(way[k[1]][k[0]][j][:-2] +
                                                          '-{},{},{}'.format(k[0], k[1] + delt,
                                                                             next_col(posled, way[k[1]][k[0]][j][-1])))
                            next_visit.append([k[0], k[1] + delt])
                else:
                    delt = -i + 2
                    if str(k[0] + delt) + ',' + str(k[1]) not in way[k[1]][k[0]][j]:
                        if way[k[1]][k[0]][j][:-2] + \
                                '-{},{},{}'.format(k[0] + delt, k[1], next_col(posled, way[k[1]][k[0]][j][-1])) \
                                not in way[k[1]][k[0] + delt]:
                            way[k[1]][k[0] + delt].append(way[k[1]][k[0]][j][:-2] +
                                                          '-{},{},{}'.format(k[0] + delt, k[1],
                                                                             next_col(posled, way[k[1]][k[0]][j][-1])))
                            next_visit.append([k[0] + delt, k[1]])
            elif pole[k[1]][k[0]][i] == 'n':
                if i % 2 == 0:
                    delt = i - 1
                    if str(k[0]) + ',' + str(k[1] + delt) not in way[k[1]][k[0]][j]:
                        if way[k[1]][k[0]][j][:-2] + \
                                '-{},{},{}'.format(k[0], k[1] + delt, way[k[1]][k[0]][j][-1]) \
                                not in way[k[1] + delt][k[0]]:
                            way[k[1] + delt][k[0]].append(way[k[1]][k[0]][j][:-2] +
                                                          '-{},{},{}'.format(k[0], k[1] + delt,
                                                                             way[k[1]][k[0]][j][-1]))
                            next_visit.append([k[0], k[1] + delt])
                if i % 2 == 1:
                    delt = -i + 2
                    if str(k[0] + delt) + ',' + str(k[1]) not in way[k[1]][k[0]][j]:
                        if way[k[1]][k[0]][j][:-2] + \
                                '-{},{},{}'.format(k[0] + delt, k[1], way[k[1]][k[0]][j][-1]) \
                                not in way[k[1]][k[0] + delt]:
                            way[k[1]][k[0] + delt].append(way[k[1]][k[0]][j][:-2] +
                                                          '-{},{},{}'.format(k[0] + delt, k[1],
                                                                             way[k[1]][k[0]][j][-1]))
                            next_visit.append([k[0] + delt, k[1]])
    del next_visit[0]
    if len(next_visit) != 0:
        waves(pole, way, posled)


def next_col(posl, ind):
    # Следующий цвет
    ind = posl.index(ind)
    ind += 1
    if ind >= len(posl):
        ind = 0
    return posl[ind]
