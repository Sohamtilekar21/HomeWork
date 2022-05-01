a=[9,2,3,4,5,7,8,6,235,6,3,634,5,6,457]
b=0
c=10000
for i in a:
    if i>b:
        b=i
    if i<c:
        c=i

a.remove(b)
a.remove(c)

b=0
c=10000
for i in a:
    if i>b:
        b=i
    if i<c:
        c=i
print(b)
print(c)

