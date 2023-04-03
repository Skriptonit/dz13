# Задание 1
# Создайте функцию calculate, которая принимает у пользователя два числа и операцию,
# а выдает результат операции.
# Обязательно: воспользуйтесь функциями exec или eval
#



#С помощью eval
# print ("Введите первое число: ")
# a = int (input())
# print ("Введите второе  число: ")
# b = int (input())
#
# def calculate (a,b,s):
#     if s =="+":
#         return (eval(f'{a}{s}{b}'))
#     if s =="-":
#         return (eval(f'{a}{s}{b}'))
#     if s =="*":
#         return (eval(f'{a}{s}{b}'))
#     if s =="/":
#         if b==0:
#             return "На 0 делить нельзя дурачок !"
#         else :
#             return (eval(f'{a}{s }{b}'))
# print ("Введите знак операции:")
# s=input()
# print (calculate (a, b, s))

#C помощью exec
# print ("Введите первое число: ")
# a = int (input())
# print ("Введите второе  число: ")
# b = int (input())
#
# def calculate (a,b,s):
#     if s =="+":
#          exec(f'print({a}{s}{b})')
#     if s =="-":
#          exec(f'print({a}{s}{b})')
#     if s =="*":
#          exec(f'print({a}{s}{b})')
#     if s =="/":
#         if b==0:
#             return "На 0 делить нельзя дурачок !"
#         else :
#              exec(f'print({a}{s}{b})')
# print ("Введите знак операции:")
# s=input()
# print (calculate (a, b, s))
