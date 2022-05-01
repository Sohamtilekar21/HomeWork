
c=["apple","guitar","hello","banana","cat","kiwi","dog","welcome"]
while " " in c :
    print("Enter one word at a time")
    global a
    a=list(input())
    c=c+a

b=sorted(c)
print(b)
