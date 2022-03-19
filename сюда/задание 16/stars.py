#https://code-enjoy.ru/ege_po_informatike_2022_zadanie_16_rekursiya/
#ласт задание

#Ввдом global и замением принт* на s=s+1 после пишем s=0
def F(n):
    global s
    s=s+1
    if n>=1:
        s=s+1
        F(n-1)
        F(n-2)
        s=s+1

s=0
F(35)
print(s) #96631265