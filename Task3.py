# Создайте программу для игры в ""Крестики-нолики"".

from pickle import FALSE, TRUE
#ход игрока
def turn (player):

 while TRUE:
    i = int(input (f"ход {player}. Введите номер поля по горизонтали от 0 до 2-х "))
    j = int (input ("Введите номер поля по горизонтали от 0 до 2-х " ))
    if i>=0 and i<=2 :
        if  j>=0 and j<=2:
             if matrix[i][j] == " ": break
 matrix[i][j]=player

# выводим матрицу на консоль после каждого хода
def printMatrix ( matrix ): 
   for i in range ( len(matrix) ): 
      print( matrix[i])

# проверяем на выигрыш
def check(player):

  ln=len(matrix)
  row = len(matrix[0])
# по горизонтали
  for i in range (ln):
    j=0
    while j<row:
        if matrix[i][j] == player:
            if j==row-1: 
                return TRUE
            j=j+1
            
        else: break
# по вертикали
  for i in range (row):
    j=0
    while j<ln:
        if matrix[j][i] == player:
            if j==ln-1: 
                return TRUE
            j=j+1
            
        else: break
        
# по диагоналям
  for i in range (row):
    if not (matrix[i][i] == player): break
    if i == row -1: return TRUE
  for i in range (row):
    if not (matrix[i][row-1-i] == player): break
    if i == row -1: return TRUE
  return FALSE


player = "X"
matrix = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
while TRUE:
  turn (player)
  printMatrix(matrix)
  if check(player) == TRUE: 
    print (f'{player} победили. Игра окончена.')
    break
  if player == "X":player ="0"
  else: player ="X"