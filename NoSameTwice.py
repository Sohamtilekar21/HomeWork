
b=[1,2,2,1,5,1]
for i in b:
    for j in b:
        if j== i:
            b.remove(i)
           
print(b)
