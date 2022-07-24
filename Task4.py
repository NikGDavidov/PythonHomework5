#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

#функция сжатия
def rle(txt):
    count = 1
    rle = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            rle = rle+ str(count) + txt[i]
            count = 1

    if count >1 or not (txt[-1] == txt[-2]): #после выхода из цикла записываем последние символы
        rle = rle + str(count) + txt[-1]
    return rle

#функция восстановления
def unDoRle(txt):
    num = ''
    unRle = ''
    for i in range(len(txt)):
        if txt[i].isdigit():
            num = num + txt[i] # считываем цифры перед символом, потом преобразуем в число
        else:
            unRle = unRle+ txt[i]*int(num) #добавляем к результату символ num раз
            num = ''
    return unRle


txt = input("Введите текст ")
txtRle = rle(txt)
print(f"Текст после сжатия: {txtRle}")
print(f"Текст после восстановления: {unDoRle(txtRle)}")