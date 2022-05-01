a=[0,1,2,3,2,4,5,4,-1,-34,-2,-34,1,4,53,4,6]
cp=0
cn=0
for i in a:
    if i<0:
       cn+=1
    else:
        cp+=1
  
   
print(a)
print(" the total positive integers are ",cp)
print(" the total negative integers are ",cn)

