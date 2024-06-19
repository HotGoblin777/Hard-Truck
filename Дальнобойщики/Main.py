from prettytable import PrettyTable
import json
import Towns
import Products
import time
from tqdm import tqdm

def buy_car(player, cars, car):
        Market = PrettyTable()
        Market.field_names = [' ', 'Машина', 'Скорость(км/ч)', 'Грузоподъёмность(кг)', 'Объём бака(лит)', 'Цена($)']
        Market.add_rows(cars)
        print(Market)
        car_choice = int(input('Выбери машину: '))
        if player['Money'] >= cars[car_choice][5] and not (car_choice in player['Car']):
                player['Money'] -= cars[car_choice][5]
                player['Car'].append(car_choice)
                file_of_players = open('file_of_players.txt', 'w')
                json.dump(player, file_of_players)
                file_of_players.close()
                car = cars[car_choice]
                print('покупка прошла успешно')
        elif car_choice in player['Car']:
            print('У вас уже есть этот автомобиль')
        else:
            print('Недостаточно средств')

def ride(car, product=['', 0, 0, '']):
        LIST = PrettyTable()
        LIST.field_names = [' ', 'Город', 'Расстояние']
        LIST.add_rows(Towns.list)
        print(LIST)
        choice_town = int(input('Куда едем: '))
        print(Towns.list[choice_town])
#        time_limit = Towns.list[choice_town][2] // car[2]
#        time.sleep(time_limit)
        for i in tqdm(range(Towns.list[2])):
            time.sleep(10 / car[2])
        print('вы приехали')
        player['Town'] = choice_town
        if product[3] == Towns.list[choice_town][1]:
            player['Money'] += product[1]
            car[3] += product[2]

def buy_product(player):
    list = Products.Update()
    products_Town1 = PrettyTable()
    products_Town1.field_names = ['Товар', 'Цена($)', 'Вес(кг)', 'Место доставки']
    products_Town1.add_rows(list)
    print(products_Town1)
    choice_product = int(input())
    if player['Car'] == 0:
        print('У вас нет машины!')
    elif car[3] >= list[choice_product - 1][2]:
        car[3] -= list[choice_product - 1][2]
        global product
        product = list[choice_product - 1]
        print('Вы выбрали заказ: '
              f'{products_Town1[choice_product - 1]}')
    else:
        print('Слишком большой вес')


def Town(choice, player):
        while choice == 'выход':
                file_of_players = open('file_of_players.txt', 'w')
                json.dump(player, file_of_players)
                file_of_players.close()
                print('Спасибо за игру')
                break
        else:
                if choice == 'обо мне':
                    print(player)
                elif choice == 'продать машину':
                    player['Money'] += car[5] * 0.8
                    print(f"у вас теперь {player['Money']} денег")
                    player['Car'] = 0
                elif choice == 'купить машину':
                    buy_car(player, cars, car)
                elif choice == 'выбрать заказ':
                    buy_product(player)
                elif choice == 'поехали':
                    ride(car, product)
                Town(input().lower(), player)

StartMenu = PrettyTable()
StartMenu.field_names = ['Опции', ' ']
StartMenu.add_rows([
        ['Начать новую игру', 1],
        ['Продолжить', 2],
        ['Настройки', 3],
])
print(StartMenu)
choice = input()

if choice == '1':
        player = {
                'Name': input('Введите имя '),
                'Country': input('Из какой вы страны '),
                'Money': 50000,
                'Skill': 0,
                'Workers': [''],
                'Car': [0, ],
                'Town': 0
        }
        file_of_players = open('file_of_players.txt', 'w')
        json.dump(player, file_of_players)
        file_of_players.close()
elif choice == '2':
        file_of_players = open('file_of_players.txt', 'r')
        player = json.load(file_of_players)
        file_of_players.close()
        cars_file = open('Cars_file.txt', 'r')
        cars = json.load(cars_file)
        cars_file.close()
        CARS = PrettyTable()
        CARS.field_names = [' ', 'Машина', 'Скорость(км/ч)', 'Грузоподъёмность(кг)', 'Объём бака(лит)', 'Цена($)']
        for i in range(len(player['Car'])):
            CARS.add_row(cars[player['Car'][i]])
        print(CARS)
        car_choice = int(input('Какой хотите выбрать автомобиль: '))
        global car
        car = cars[car_choice]
        Town(input().lower(), player)