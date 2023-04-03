# Задание 4
# Создайте функцию cesar, которая возвращает зашифрованную строку шифром Цезаря со сдвигом на 3.
# Саму строку запросите у пользователя.
# Шифр Цезаря — это вид шифра подстановки, в котором каждый символ в открытом тексте заменяется символом,
# находящимся на некотором постоянном числе позиций левее или правее него в алфавите.
# Например, в шифре со сдвигом вправо на 3, А была бы заменена на Г, Б станет Д, и так далее.


al="12345678901234567890абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
def cesar (stroka):
     key= 3
     str_now=stroka.lower()
     p= " "

     for letter in str_now :
         position = al.find(letter)
         new_position=position+key
         if letter in al:
             p=p+al[new_position]
         else :
             p=p+letter
     print("Ваш шифр милорд :")
     return (p)

print("Введите строку Господин  :")
stroka= input()
print (cesar(stroka))