a=int(input())
b=1
c=1
d=0
while c<a+1:
    for i in range(1, c+1):
        b=b*i
        print(b)
        c+=1
    d=d+b
   
    
print(d)
    
