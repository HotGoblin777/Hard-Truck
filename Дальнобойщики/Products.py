from random import randrange
import Towns


def Update():
    number = randrange(3, 7)
    LIST = [['Бананы', randrange(3, 9), randrange(200, 601)],
            ['Трактор', randrange(10, 21), randrange(2000, 7001)],
            ['Молоко', randrange(5, 13), randrange(200, 601)],
            ['Пшено', randrange(3, 9), randrange(400, 801)],
            ['Стекло', randrange(7, 15), randrange(800, 1001)],
            ['Трубы', randrange(8, 17), randrange(1000, 5001)],
            ['Дерево', randrange(7, 13), randrange(1000, 4001)],
            ['Нефть', randrange(9, 19), randrange(600, 3001)],
            ['Яблоки', randrange(3, 9), randrange(200, 601)],
            ['Кран', randrange(15, 27), randrange(3000, 9001)]]
    Towns.Update()
    list = [];  i = 1; j = 0;  counter = []
    while i <= number:
        town = randrange(0, 2);   choice = randrange(0, 10)
        if choice not in counter:
            list.append(j, [LIST[choice][0], LIST[choice][1] * Towns.list[town][2], LIST[choice][2], Towns.list[town][1]])
            counter.append(choice)
            j += 1
        else:
            number += 1
        i += 1
    return list
