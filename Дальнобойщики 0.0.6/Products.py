from random import randrange
import Towns


def Update():
    Towns.Update()
    number = randrange(3, 7)
    LIST = [['Бананы', randrange(2, 4), randrange(200, 601)],
            ['Трактор', randrange(9, 15), randrange(2000, 7001)],
            ['Молоко', randrange(3, 8), randrange(200, 601)],
            ['Пшено', randrange(2, 4), randrange(400, 801)],
            ['Стекло', randrange(6, 10), randrange(800, 1001)],
            ['Трубы', randrange(6, 11), randrange(1000, 5001)],
            ['Дерево', randrange(5, 9), randrange(1000, 4001)],
            ['Нефть', randrange(7, 13), randrange(1000, 5001)],
            ['Яблоки', randrange(2, 4), randrange(200, 601)],
            ['Кран', randrange(12, 19), randrange(3000, 9001)]]
    list = [];  i = 1;   counter = []
    while i <= number:
        town = randrange(0, 3);   choice = randrange(0, 10)
        if choice not in counter:
            list.append([LIST[choice][0], LIST[choice][1] * Towns.list[town][2], LIST[choice][2], Towns.list[town][1], Towns.list[town][2]])
            counter.append(choice)
        else:
            number += 1
        i += 1
    return list


