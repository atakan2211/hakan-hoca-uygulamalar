for i in range(1,1000):
    for a in range(2,i):
        if i%a ==0:
            break
        elif i%a !=0 and a==i-1:
            print(i)
