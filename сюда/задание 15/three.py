"""
Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m». 
Для какого наибольшего натурального числа А формула тождественно истинна 
(то есть принимает значение 1 при любом натуральном значении переменной x)?

¬ДЕЛ(x, А) → (ДЕЛ(x, 6) → ¬ДЕЛ(x, 9))
"""
#не пугаемся и вместо ДЕЛ вернем функцию 
def D(n, m):
    if n%m==0:
        return True
    else:
        return False

     

for A in range(1, 1000):
    k=0
    for x in range(1, 1001):
        if D(x, A) or (not(D(x, 6)) or not(D(x, 9))):
            k=k+1
    if k==1000:
        print(A) #наибольшее число 18