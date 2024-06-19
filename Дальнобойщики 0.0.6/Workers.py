from random import randint
import json
file = open('Cars_file.txt', 'r')
cars = json.load(file)
file.close()
names = ['Гриша', 'Гена', 'Николай', 'Женя', 'Саня', 'Лена', 'Анастасия', 'Алиса', 'Евгений', 'Миша']
workers = []
def Start():
    for i in range(randint(3, 8)):
        car = cars[randint(1, 5)][:]
        workers.append([names[randint(0, 10)], car[1], car[5] + randint(2000, 7001), (car[3] + randint(200, 701)) * car[2] // 60])
    file_of_workers = open('file_of_workers.txt', 'w')
    json.dump(workers, file_of_workers)
    file_of_workers.close()

