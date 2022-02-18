"""
НАЧАЛО
  ПОКА нашлось (>1) ИЛИ нашлось (>2) ИЛИ нашлось (>3)
    ЕСЛИ нашлось (>1)
      ТО заменить (>1, 22>)
    КОНЕЦ ЕСЛИ
    ЕСЛИ нашлось (>2)
      ТО заменить (>2, 2>1)
    КОНЕЦ ЕСЛИ
    ЕСЛИ нашлось (>3)
      ТО заменить (>3, 1>2)
    КОНЕЦ ЕСЛИ
  КОНЕЦ ПОКА
КОНЕЦ

На вход приведённой ниже программе поступает строка, начинающаяся с символа «>», а затем содержащая 28 цифр 1, 18 цифр 2 и 35 цифр 3, 
расположенных в произвольном порядке. Определите сумму числовых значений цифр строки, получившейся в результате выполнения программы. 
Так, например, если результат работы программы представлял бы собой строку, состоящую из 50 цифр 4, то верным ответом было бы число 200.
"""
s = '>' + '1'*28 + '2'*18 + '3'*35

while ('>1' in s) or ('>2' in s) or ('>3' in s):
    if '>1' in s:
        s = s.replace('>1', '22>', 1)
    if '>2' in s:
        s = s.replace('>2', '2>1', 1)
    if '>3' in s:
        s = s.replace('>3', '1>2', 1)
#print(s) 2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222122212221222>
#находим сумму
sm=0
#print(s[43]) вывод 2
for i in range(0, len(s)): #Функция len() возвращает длину (количество элементов) в объекте. от нуля до 251
    if s[i]!='>': # если символ не > то 
        sm = sm + int(s[i]) #каждое число проганяется и складывается 
        
print(sm)#465