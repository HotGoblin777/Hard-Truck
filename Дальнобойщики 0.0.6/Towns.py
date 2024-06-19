import json
from prettytable import PrettyTable
import math

file_of_players = open('file_of_players.txt', 'r')
player = json.load(file_of_players)
file_of_players.close()

list = []

TOWNS = [['Южный', 0, 2000],   # Название, х, у
         ['Алмазный', 2000, 0],
         ['Ключи', 100, 100],
         ['Боровое', 1700, 1500]
         ]
def Update(i=0, j=1):
    while i < len(TOWNS):
        if i != player['Town']:
            list.append([j, TOWNS[i][0], math.ceil(math.hypot(TOWNS[player['Town']][1] - TOWNS[i][1], TOWNS[player['Town']][2] - TOWNS[i][2]))])
            i += 1
            j += 1
        else:
            i += 1
    return list


