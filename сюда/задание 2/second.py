#(x ≡ ¬y) → ((x ∧ w) ≡ z)
# ? ? ? ? f
# 1 1     0
# 1 1   1 0
#   1 1   0
print('x y z w') # я не знаю почему,но нужно в таком расположении 
for x in range(0, 2): 
    for y in range(0, 2):
         for w in range(0, 2): #!
            for z in range(0, 2): #!
                if not( not((x == (not(y)))) or ((x and w) == z)): # так как там нуль,то if not 
                  print(x, y, z, w)
#x y z w
#0 1 1 0
#0 1 1 1
#1 0 1 0
#1 0 0 1 - хуита, ибо должно быть три еденици вертикаль 

# в этих штуках главное чета убрать,чтобы было три строчки
# z-2
# x-3 там нолик 
# y -1 там две едницы 

# ответ yzxw

