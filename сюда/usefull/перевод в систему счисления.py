"""
Значение арифметического выражения: 125 + 253 + 59 – записали в системе счисления с основанием 5. 
Сколько значащих нулей содержит эта запись?
"""
x=125 + (253) + (59)
k=0
while x>0:
    if x%5==0:
        k+=1
    x=x//5
print(k)