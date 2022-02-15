#Артур составляет 5-буквенные коды из букв Е, С, А, У, Л. 
#Каждую букву нужно использовать ровно один раз, при этом нельзя ставить рядом две гласные. 
#Сколько различных кодов может составить Артур?


k=0
bukvi = ['Е', 'С', 'А', 'У', 'Л']
for x1 in bukvi:
    for x2 in bukvi:
        for x3 in bukvi:
            for x4 in bukvi:
                for x5 in bukvi:
                    s=x1+x2+x3+x4+x5
                    if s.count('Е') == 1 and s.count('С') == 1 and s.count('А') == 1 and s.count('У') == 1 and s.count('Л') == 1: #одна буква
                        if s.count('ЕА') == 0 and s.count('АЕ') == 0 and s.count('ЕУ') == 0 and s.count('УЕ') == 0 and s.count('УА') == 0 and s.count('АУ') == 0: #пересечение гласных
                           k=k+1 
print(k) # 12
