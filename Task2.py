# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
#  За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?


#- ответ - 20 шт

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""
import random
from pickle import FALSE, TRUE

#ход игрока или бота
def turn (player):
    global count
    if player == "bot":
        if mode ==2:
            b = random.randint(1,28)
            if count < b: b = random.randint(1,count)           
        
        if mode ==3:
            b = count%29     # так победим
            if b==0: b=1      
        print (f'бот взял {b} шт.')
        count -=b
        if count == 0:
            print ('Бот выиграл и забрал все конфеты')
            return "win"
    else:
        print (f'осталось {count} шт.')
        print(f"Ход игрока {player}")
        
        a = int(input ('возьмите число конфет от 1 до 28 - '))
        while a < 1 or a > 28 or a > count: a = int(input(" введите корректное количество конфет: "))
           
        count -= a
        if count == 0 :
            print (f'Игрок {player} выиграл и забрал все конфеты')
            return "win"

count = 2021 #число конфет
mode = 0 #режим игры 

while mode < 1 or mode > 3:
      mode = int (input ("выберете режим игры от 1 до 3-х\n1- против человека 2- против бота 3- против умного бота "))
player1 = input ("Введите имя игрока ")
if mode == 2 or mode ==3 : player2 = 'bot'
else: player2 =input ("Введите имя 2-го игрока ")
if random.randint(1,10)>5:#кто ходит первым?
  temp = player1
  player1 = player2
  player2 = temp
# началась игра
while TRUE:
    if turn (player1)== "win" : break
    if turn (player2)== "win" : break




