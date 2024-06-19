from prettytable import PrettyTable
import json
import Towns
import Products
import time
from tqdm import tqdm
from colorama import init, Fore
from Workers import Start
from threading import Thread
init(autoreset=True)

def MyCars(player, cars, choiceble=True):
    CARS = PrettyTable()
    CARS.field_names = ['Машина', 'Скорость(км/ч)', 'Грузоподъёмность(кг)', 'Объём бака(лит)', 'Цена($)']
    for i in player['Car']:
        CARS.add_row(cars[i][1:6])
    print(CARS)
    del CARS
    if choiceble == True:
        car_choice = int(input(Fore.BLUE + "Какой хотите выбрать автомобиль: "))
        car = cars[player['Car'][car_choice]][:]
        del car_choice
        return car
def workers(worker, player, pay=0):
    while True:
        time.sleep(300)
        for i in worker:
            player['Money'] += i[3]
            pay += i[3]
        print(f"Вы получили от рабочих {pay}$")



def buy_car(player, cars, car):
        print(Fore.LIGHTGREEN_EX + f"У вас на счету {player['Money']}$")
        Market = PrettyTable()
        Market.field_names = [' ', 'Машина', 'Скорость(км/ч)', 'Грузоподъёмность(кг)', 'Объём бака(лит)', 'Цена($)']
        Market.add_rows(cars)
        print(Market)
        cars_choice = int(input(Fore.BLUE + "Выбери машину: "))
        if player['Money'] >= cars[cars_choice][5] and not (cars_choice in player['Car']):
                player['Money'] -= cars[cars_choice][5]
                player['Car'].append(cars_choice)
                file_of_players = open('file_of_players.txt', 'w')
                json.dump(player, file_of_players)
                file_of_players.close()
                car = cars[cars_choice]
                print(Fore.GREEN + "покупка прошла успешно")
        elif cars_choice in player['Car']:
            print(Fore.YELLOW + "У вас уже есть этот автомобиль")
        else:
            print(Fore.RED + "Недостаточно средств")

def buy_workers(player):
    print(Fore.LIGHTGREEN_EX + f"У вас на счету {player['Money']}$")
    OAO = PrettyTable();   file = open('file_of_workers.txt', 'r')
    workers = json.load(file);    file.close()
    OAO.field_names = ['Имя', 'Машина', 'Стоимость', 'Отдаёт($)']
    OAO.add_rows(workers)
    print(OAO)
    work_choice = int(input(Fore.BLUE + "Выбери рабочего: "))
    if player['Money'] >= workers[work_choice - 1][2] and not (work_choice in player['Workers']):
        player['Money'] -= cars[work_choice - 1][2]
        player['Workers'].append(work_choice)
        file_of_players = open('file_of_players.txt', 'w')
        json.dump(player, file_of_players)
        file_of_players.close()
        print(Fore.GREEN + "выбор был произведён")
    elif work_choice in player['Worker']:
        print(Fore.YELLOW + "У вас уже есть этот рабочий")
    else:
        print(Fore.RED + "Недостаточно средств")

def ride(car):
        Towns.Update()
        LIST = PrettyTable()
        LIST.field_names = [' ', 'Город', 'Расстояние']
        LIST.add_rows(Towns.list)
        print(LIST)
        choice_town = int(input(Fore.BLUE + "Куда едем: "))
        print(Towns.list[choice_town - 1])
        del LIST
#        time_limit = Towns.list[choice_town][2] // car[2]
#        time.sleep(time_limit)
        speed = round(10 / car[2], 2)
        tut = car[2] / 4
        for i in tqdm(range(Towns.list[choice_town - 1][2]), leave=True):
            time.sleep(speed)
            if i % tut == 0:
                car[4] -= 1
                print(f'\t {car[4]}л')
        print(Fore.CYAN + "Вы приехали")
        del speed, tut
        player['Town'] = Towns.list[choice_town - 1][0]
        if product[3] == Towns.list[choice_town - 1][1]:
            player['Money'] += product[1]
            car[3] += product[2]
            print(Fore.GREEN + f"Стало у вас на счету {player['Money']}$")

def buy_product(player):
    list = Products.Update()
    products_Town1 = PrettyTable()
    products_Town1.field_names = ['Товар', 'Цена($)', 'Вес(кг)', 'Место доставки', 'Расстояние']
    products_Town1.add_rows(list)
    print(products_Town1)
    choice_product = int(input())
    if player['Car'] == 0:
        print("У вас нет машины!")
    elif car[3] >= list[choice_product - 1][2]:
        car[3] -= list[choice_product - 1][2]
        global product
        product = list[choice_product - 1]
        print(f"Вы выбрали заказ: {products_Town1[choice_product - 1]}")
    else:
        print("Слишком большой вес")


def Town(player, car, worker):
        while True:
                choice = input('Команды: Выбрать заказ, поехали, заправить машину, продать машину, купить машину, выбрать работника, выбрать машину, обо мне, о рабочих, выход ').lower()
                if choice == 'выбрать заказ':
                    buy_product(player)
                elif choice == 'поехали':
                    if car == 0:
                        print("У вас нет машины")
                    elif input(f"Вы уверены что хотите ехать если у вас {car[4]} л в баке: д/н  ") == 'д':
                        ride(car)
                elif choice == 'заправить машину':
                    print(f"Всего в баке: {cars[car[0]][4]}, а сейчас: {car[4]}")
                    cho = int(input("Сколько заправить(1л = 8$)? "))
                    if cho + car[4] <= cars[car[0]][4]:
                        player['Money'] -= cho * 8
                        car[4] += cho
                        print(Fore.RED + "Вы потратили {cho * 8}$")
                        del cho
                    else:
                        print(Fore.LIGHTRED_EX + "перебор!")
                elif choice == 'продать машину':
                    MyCars(player, cars, choiceble=False)
                    car_choice = int(input(Fore.BLUE + "Какой хотите продать автомобиль: "))
                    if player['Car'][car_choice] != car[0]:
                        player['Money'] += cars[player['Car'][car_choice]][5] * 0.8
                        print(Fore.LIGHTGREEN_EX + f"у вас теперь {player['Money']} денег")
                        del player['Car'][car_choice]
                    else:
                        print(Fore.RED + "Вы сейчас в этой машине и мы не можем её купить")
                elif choice == 'купить машину':
                    buy_car(player, cars, car)
                elif choice == 'выбрать рабочего':
                    buy_workers(player)
                elif choice == 'поменять машину':
                    car = MyCars(player, cars)
                elif choice == 'обо мне':
                    print(Fore.CYAN + f"Имя: {player['Name']}, Страна: {player['Country']}, Деньги: {player['Money']}$")
                elif choice == 'о рабочих':
                    Work = PrettyTable()
                    Work.field_names = ['Имя', 'Машина', 'Отдаёт($)']
                    for i in worker:
                        Work.add_row([i[0], i[1], i[3]])
                    print(Fore.CYAN + f'{Work}')
                    del Work, workers
                elif choice == 'выход':
                    file_of_players = open('file_of_players.txt', 'w')
                    json.dump(player, file_of_players)
                    file_of_players.close()
                    print(Fore.LIGHTCYAN_EX + "Спасибо за игру")
                    break
                else:
                    print("Нет такой команды")

StartMenu = PrettyTable()
StartMenu.field_names = [' ', 'Опции']
StartMenu.add_rows([
        [1, 'Начать новую игру'],
        [2, 'Продолжить'],
        [3, 'Настройки'],
])
print(StartMenu)
del StartMenu
choice = input()

if choice == '1':
        player = {
                'Name': input('Введите имя '),
                'Country': input('Из какой вы страны '),
                'Money': 50000,
                'Workers': [],
                'Car': [0],
                'Town': 0
        }
        file_of_players = open('file_of_players.txt', 'w')
        json.dump(player, file_of_players)
        file_of_players.close()
        Start()
elif choice == '2':
        file_of_players = open('file_of_players.txt', 'r')
        player = json.load(file_of_players)
        file_of_players.close()
        cars_file = open('Cars_file.txt', 'r')
        cars = json.load(cars_file)
        cars_file.close()
        car = MyCars(player, cars)
        file = open('file_of_workers.txt', 'r')
        work = json.load(file)
        file.close();   worker = []
        for i in player['Workers']:
            worker.append(work[i])
        Thread(target=workers, args=(worker, player)).start()
        del choice
        Town(player, car, worker)