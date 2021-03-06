
# ТЕОРИЯ В ТЕТРАДИ 

# Отрицание ¬	          not()
# Логическое умножение ∧  and
# Логическое сложение ∨	  or
# Следование A ⟶ B	     not(A) or B
# Равносильность ≡, ↔, ∼   	  == 
# Cтрогая дизъюнкция ⊕	 A != B 
# Э                       in

#Миша заполнял таблицу истинности логической функции F
#(w → z) ∧ ((y → x) ≡ (z → y)),
#cответствует каждая из переменных w, x, y, z,
# ? ? ? ? F
# 1     0 1
#   0 1   1
# 1 0 0 1 1

# пример range()
# for i in range(1, 8):
#    print(i) 
#1 
#2
#3
#4
#5
#6
#7
"""
for x in range(0, 2): 
    for y in range(0, 2):
         for w in range(0, 2):
            for z in range(0, 2):
                print(x,y,w,z)
0 0 0 0
0 0 0 1
0 0 1 0
0 0 1 1
0 1 0 0
0 1 0 1
0 1 1 0
0 1 1 1
1 0 0 0
1 0 0 1
1 0 1 0
1 0 1 1
1 1 0 0
1 1 0 1
1 1 1 0
1 1 1 1
"""

print('x y z w') # выводим переменные чтобы было понятно че к чему 
#В каждом цикле перебираем все возможные значения для конкретной переменной. Мы перебираем значения 0 и 1.
for x in range(0, 2): 
    for y in range(0, 2):
        for w in range(0, 2):
            for z in range(0, 2):

                if (not(w) or z) and ((not(y) or x) == (not(z) or y)): # получится один,значит if истинный 

                    print(x, y, z, w) # выводит то что подходит 

# x y z w
# 0 0 0 0
# 1 0 0 0
# 1 1 0 0
# 1 1 1 0
# 1 1 1 1
                  
#В получившийся табличке может быть больше строчек, чем в условии. 
# Так же при поиске переменных нельзя опираться на порядок, в котором идут нули и единицы в нашей табличке. 
# А можно опираться лишь на количество нулей и единиц в строчках или столбцах.    
              
#Можно вычеркнуть первую строчку и последнюю, потому что в таблице, которую дали в условии, 
#в каждой строчке есть хотя бы один ноль и хотя бы одна единица.  
# x y z w 
# 0 0 0 0 - хуита  
# 1 0 0 0
# 1 1 0 0
# 1 1 1 0
# 1 1 1 1 - хуита 
#ибо
# ? ? ? ? F
# 1     0 1
#   0 1   1
# 1 0 0 1 1
          
#Сразу видно, что первый столбец принадлежит переменной x, только там могут быть все единицы.P.S.смотри вертикально!
#Второй столбец принадлежит переменной w, только там могут быть все нули.    
    
#У нас остались две пустые клеточки в самой таблице. Нам нужно где-то поставить единицу, а где-то ноль, 
# потому что у нас остались столбцы с двумя единицами и одним нулём, а так же с двумя нулями и одной единицей. 
# Если мы в третий столбец поставим единицу, а в четвёртый ноль, то первая строчка и вторая будут совпадать.
#А в условии сказано, что строки не должны повторяться. Поэтому нужно ноль и единицу расставить наоборот.
#Получается, что в третий столбец идёт z, а в четвёртый y

#Ответ: xwzy