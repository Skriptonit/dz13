# Задание 7
# Пусть дана функция, которая спрашивает имя пользователя.
# def get_name( ):
#   name = input('Введите имя')
#   return name
# Создайте декоратор hello, который дополнительно будет выводить приветствие: "Привет, <имя>!"
def hello(ronaldy ):
    def messi ():
        name = ronaldy ()
        print ("Привет ,",name,"!")
    return messi
@hello
def get_name ():
    print ("Введите имя :")
    name = input ()
    return name
get_name()
