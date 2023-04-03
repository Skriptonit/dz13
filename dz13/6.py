# Создать функцию alphabet, которая:
# а) выводит буквы английского алфавита и их порядковый номер.
# б) выводит словарь {порядковый номер : буква }
#под а
# def alphabet (alp):
#     for i ,item in enumerate(alp):
#         print (i+1,'-',item)
#
# alp=['A' ,'B' ,'C', 'D' ,'E' ,'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U','V', 'W','X', 'Y', 'Z']
# alphabet(alp)
#под б
# def alphabet (alp):
#     slow={ }
#     for i ,item in enumerate(alp):
#         slow.update({i+1:item})
#     print (slow)
#         # print (i+1,'-',item)
#
# alp=['A' ,'B' ,'C', 'D' ,'E' ,'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U','V', 'W','X', 'Y', 'Z']
# alphabet(alp)
#Либо так :
dct = {key:chr(value) for key, value in zip(range(1, 27), range(97, 123))}
print(dct)
