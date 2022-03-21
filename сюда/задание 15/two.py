for A in range(0, 2):
    k=0
    for x in range(1, 3):
        for y in range(1, 3):
            if (x >= A) or (y >= A) or (x * y <= 205):
                k=k+1
                print(k,A)
                
    if k==4:
        print('lol')