"""
че такое while?

Цикл while (“пока”) позволяет выполнить одну и ту же последовательность действий, 
пока проверяемое условие истинно.
При выполнении цикла while сначала проверяется условие. 
Если оно ложно, то выполнение цикла прекращается и управление передается на следующую инструкцию 
после тела цикла while

i = 1
while i <= 10:
    print(i ** 2)
    i += 1
выведет 
1
4
9
16
25
36
49
64
81
100
"""

"""
Исполнитель Редактор получает на вход строку цифр и преобразовывает её. 
Редактор может выполнять две команды, в обеих командах v и w обозначают цепочки символов.
1. заменить (v, w)
2. нашлось (v)

Первая команда заменяет в строке первое слева вхождение цепочки v на цепочку w. 
Если цепочки v в строке нет, эта команда не изменяет строку. 
Вторая команда проверяет, встречается ли цепочка v в строке исполнителя Редактор. 
Дана программа для исполнителя Редактор:


НАЧАЛО
ПОКА нашлось (2222) ИЛИ нашлось (666)
  ЕСЛИ нашлось (2222)
    ТО заменить (2222, 6)
    ИНАЧЕ заменить (666, 2)
  КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
КОНЕЦ

Какая строка получится в результате применения приведённой выше программы к строке, 
состоящей из 13 идущих подряд цифр 6? В ответе запишите полученную строку.
"""

s = '6'*13  #состоящей из 13 идущих подряд цифр 6.'' нужны,ведь без них будет просто 78

while ('2222' in s) or ('666' in s): #условие 
    if '2222' in s:
        s = s.replace('2222', '6', 1) #Третий параметр в функции replace обозначает, что замену нужно производить один раз! первое слева вхождение цепочки v на цепочку w
    else:
        s = s.replace('666', '2', 1)  #Третий параметр в функции replace обозначает, что замену нужно производить один раз

print(s) # ответ 66  p.s. Если оно ложно, то выполнение цикла прекращается и управление передается на следующую инструкцию после тела цикла while

"""
666 666 666 666 6
2   2   2   2   6
6               6
66
вот и все .!.
"""