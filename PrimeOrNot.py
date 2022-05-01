a=int(input("enter number to check wheter prime or not : " ))
counter=2
while counter<a:
    if a%counter==0:
        print("NOT A PRIME")
        break
    else:
        counter+=1
        
if a==counter:
    print("Its a Prime")
        
