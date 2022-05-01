
for i in range(1,10):
    for j in range(1,10):
        if j<=i:
            if i%2==1:
                print(i,end=" ")
        else:
            print(" ",end=" ")
    print()
