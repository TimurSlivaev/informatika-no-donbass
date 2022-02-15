#((x → y ) ∧ (y → w)) ∨ (z ≡ ( x ∨ y))

#? ? ? ? f
#1     1 0
#1       0
#  1   1 0

print("x y z w")
for x in range(0,2):
    for y in range(0,2):
        for w in range(0,2):
            for z in range(0,2):
               if not((( not(x) or y) and (not(y) or w)) or (z == (x or y))):  
                 print(x,y,z,w)
#x y z w
#0 1 0 0
#1 0 0 0
#1 0 0 1
#1 1 0 0

# z-3
# w-2
#! Посмотрим на строчку, где у w стоит единица. В этой же строчке и у x единица. Значит, x идёт в последний столбец, а y в первый столбец.
#Ответ ywzx