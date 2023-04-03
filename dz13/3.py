# Задание 3
# Создайте функцию honest, которая принимает произвольный список,
# а возвращает список, состоящий только из четных элементов.
# Список от 0 до 20 создайте любым способом.

def honest (messi):
    return [ronaldy for ronaldy in messi if not ronaldy % 2]

spisok = []
for i in range(21):
    spisok.append(i)
    messi=spisok
print(honest(messi))