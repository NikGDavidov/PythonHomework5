
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


txt = input("Введите текст через пробел:\n")
del_flag = "абв"
lst = [i for i in txt.split() if del_flag not in i]
txt_after_del = " ".join(lst)
print(f'{txt}->{txt_after_del}')