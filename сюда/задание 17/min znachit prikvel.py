f=open('задание 17\min zhach prikvel.txt')

count=0
sm=20000

n1=int(f.readline())
print(n1)
print(f.readline())
for s in f.readlines():
    n2=int(s)

    if n1%7==0 and n2%7==0:
        count=count+1
        sm=min(n1+n2, sm)
    
    n1=n2
print(n2)

print(count)
print(sm)