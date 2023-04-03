#Задача 5
# Создайте функцию countdown, которая принимает список рандомных чисел от 0 до 10,
# а возвращает каждый элемент этого списка в порядке обратного отсчета, а после 0 - слово " Пуск!".
def coutdown (rand ):
    zero=0
    ind = (rand .index(0))#находим индекс для 0
    srez = rand [:ind +1]#срез до нуля
    x=(sorted(srez,reverse=True))
    return (*x,"Пуск!")#вывод итого

from random import sample#создаем рандом чисел от 0 до 10
rand = sample (range (0,10),10)
print (rand )#вывод рандомных чисел
print (coutdown(rand))
