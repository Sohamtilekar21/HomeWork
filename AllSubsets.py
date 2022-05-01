import itertools
from itertools import combinations,chain
a={1,2,3}
n=int(input())
print(list(map(set,itertools.combinations(a,n))))
"""b=len(a)
counter=0
while counter<b:
    a=sorted(a)
    a.pop()
    print(a)
    counter+=1"""

