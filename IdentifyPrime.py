a=[2,3,4,43,6,9,56,5,35,17,4,54,19,31,23]
b=[]

for i in a:
    i=int(i)
    counter=2
    while counter<i:
        
        if i%counter==0:
            break
        else:
            counter+=1
    if i==counter:
        b.append(i)
print(a)
print(b)
        
