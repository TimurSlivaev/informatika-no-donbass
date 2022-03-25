"""
67)(Е. Джобс) Алгоритм вычисления функции F(n), где n – натуральное число, задан следующими соотношениями:
F(n) = n + 1 при n < 3,
F(n) = n + 2*F(n + 2), когда n ≥ 3 и четно,
F(n) = F(n – 2) + n – 2, когда n ≥ 3 и нечетно.
Сколько существует чисел n, для которых значение F(n) ОПРЕДЕЛЕННО! и будет трехзначным?
"""
def F( n ):
  if n < 3:
    return n + 1
  elif n % 2 == 0:
    return n + 2*F(n + 2)
  else:
    return F(n-2) + n - 2
#Что значит определено?!
#Это значит что если мы не ебанем try и except то - RecursionError: maximum recursion depth exceeded in comparison
#если код выдает оишбку в try код идет в except а там ниче нет
count=0
for n in range(1,1000):
    try:
        if 100 <= F(n) <= 999:
            count=count+1
    except:
        pass
print(count) #22

