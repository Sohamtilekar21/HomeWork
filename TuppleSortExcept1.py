a=(3,4,56,76,4,7,879,54,1,2,0)
a=list(a)
b=(a[0])
a.pop(0)
a.sort()
a.insert(0,b)
a=tuple(a)
print(a)

