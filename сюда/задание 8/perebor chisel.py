#Сколько существует чисел, восьмеричная запись которых содержит 7 цифр, причём все цифры различны 
# и никакие две чётные и две нечётные цифры не стоят рядом.

# восьмиричная запись - 01234567 

#k=0 
#for x1 in '01234567':
 #   for x2 in '01234567':
#        print(x1 + x2) можно посмотреть 

k1=0 
k2=0
for x1 in '1234567': # в первом мы убираем ноль,так так ноль слева он  бесполезный 0123=123
    for x2 in '01234567':
        for x3 in '01234567':
            for x4 in '01234567':
                for x5 in '01234567':
                    for x6 in '01234567':
                        for x7 in '01234567':
                            s= x1 + x2 + x3 + x4 + x5 + x6 + x7
                            if s.count(x1) == 1 and s.count(x2) == 1 and s.count(x3) == 1 and s.count(x4) == 1 and s.count(x5) == 1 and s.count(x6) == 1 and s.count(x7) == 1: #причём все цифры различны 
                                if int(x1)%2 == 0 and int(x2)%2 == 1 and int(x3)%2 == 0 and int(x4)%2 == 1 and int(x5)%2 == 0 and int(x6)%2 == 1 and int(x7)%2 == 0: #должно быть или так 
                                   k1= k1 + 1
                                if int(x1)%2 == 1 and int(x2)%2 == 0 and int(x3)%2 == 1 and int(x4)%2 == 0 and int(x5)%2 == 1 and int(x6)%2 == 0 and int(x7)%2 == 1: #или так 
                                   k2= k2 + 1

print(k1)    
print(k2)
print(k1 + k2)  #Ответ: 1008
                           