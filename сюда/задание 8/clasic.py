# цикла for напоминате range()
# str-слова int-числа

#languages = ["C", "C++", "Perl", "Python"]
# for x in languages:
#     print(x)
#C
#C++
#Perl
#Python

#for x1 in 'АБВГ': #x1 это ожна ячейка в которой ф,б,в,г
  #  s=x1
   # print(s)
#А
#Б
#В
#Г

#for a1 in 'АБВГ': # 
#    for a2 in 'АБВГ': # оно добавляет больше значений и приклеивает буквы 
#        f=a1 + a2 
#        print(f)
#АА
#АБ
#АВ
#АГ
#БА
#ББ
#БВ
#БГ
#ВА
#ВБ
#ВВ
#ВГ
#ГА
#ГБ
#ГВ
#ГГ

#Женя составляет 5-буквенные слова, в которых встречаются только буквы А, Б, В, Г, причём буква А появляется ровно 1 раз.
#Каждая из других допустимых букв может встречаться в слове любое количество раз или не встречаться совсем. 
#Словом считается любая допустимая последовательность букв, не обязательно осмысленная. Сколько существует таких слов, 
#которые может написать Женя?

k=0
for x1 in 'АБВГ':
    for x2 in 'АБВГ':
        for x3 in 'АБВГ':
            for x4 in 'АБВГ':
                for x5 in 'АБВГ':
                    s=x1+x2+x3+x4+x5
                    if s.count('А')==1: # x = 'количество вхождений подстроки `sub` в диапазоне индексов' >>> x.count('о', 10, 30) выведет 3 ,10-30 это промежуток поиска
                        k=k+1
print(k)   #Ответ: 405      
#spisok = [10, 40, 20, 30]  
#>>> i = 0
#>>> for element in spisok:
#...     spisok[i] = element + 2
#...     i += 1
#...
#>>> spisok
#[12, 42, 22, 32]      
       
#https://younglinux.info/python/for