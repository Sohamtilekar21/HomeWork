a=[1,2,3,4,5,6,7,2,4,6,7,3,5,6,7,4,5,0,7]
#for i in a :
    #if i%2==1:
       # a.remove(i)
       # i+=1
       # a.append(i)
for i in range (len(a)):
    if a[i]%2==1:
        a[i]+=1




 
print (a)        
