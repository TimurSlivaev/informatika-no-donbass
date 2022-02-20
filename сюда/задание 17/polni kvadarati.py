"""
В файле содержится последовательность целых чисел. 
Элементы последовательности могут принимать целые значения от -10000 до 10000 включительно. 
Определите и запишите в ответе сначала количество пар элементов последовательности, в которых хотя бы одно число является полным квадратом 
некоторого натурального числа, затем максимальную из сумм элементов таких пар. 
В данной задаче под парой подразумевается два подряд идущих элемента последовательности. 
Например для последовательности из пяти элементов: 9; 15; 23; -3; 4 - ответ 2 24
"""

f = open('задание 17\polni kvadarati.txt')

count = 0
sm= -20000

n1=int(f.readline())  

#хотя бы одно число является полным квадратом некоторого натурального числа.Это блять как?
#корень из 37 = 6 с копеками - это хуйня
#корень из 36 = 6 - это заебись

for s in f.readlines():
    n2=int(s)
    if (n1>0 and (int(n1**0.5)**2) == n1) or (n2>0 and  (int(n2**0.5)**2) == n2): # 0.5 а не 0,5. int() еще округляет резы в меньшую сторону 
       count=count + 1
       sm=max(n1+n2,sm)
    n1=n2
print(count) #60
print(sm) #18555

 