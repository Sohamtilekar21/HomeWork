def Is_pal(a):
    if len(a) ==1:
        return True
    else:
        if a[0]==a[-1]:
            return(Is_pal(a[1:-1]))
        else:
            return False
b=input("Enter word to be checked for palindrome ?")
if (Is_pal(b)==True):
    print(b,"is a palindrome")
else:
    print(b,"is not a palindrome")
