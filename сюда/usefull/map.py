#мап или как просумировать числа еще и в str

a='12344321'
b='12344321'
ki= list(map(int, b))
print(ki) 

kiki=sum(map(int, a))
print(kiki) #20

"""
Вместо использования цикла for функция map() дает возможность применить функцию к каждому элементу итерируемого объекта!

в данной хуйне мы кажое str число ебашим в int
Итерация - это общий термин, который описывает процедуру взятия элементов чего-то по очереди.
"""