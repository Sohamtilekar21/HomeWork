print ("Anagram checker")
c=1
d=0
f=0
a=(input("Enter first string :"))
b=(input("Enter second string :"))
while c==1:
    for i in a:
        if i in b:
            d+=1
           
        else:
            
            break
    for j in b:
        if j in a:
            f+=1
            
        else:
            print("not an anagram")
            break
    if d==f and f!=0:
        print("its an anagram")
        break
    else :
        c+=1
   
    
