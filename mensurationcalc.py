print("Area , Perimeter Caluculator")
a=int(input("Enter \n\t 1 for Rectangle\n\t 2 for circle\n\t 3 for Square\n\t 4 for Rhombus\n\t 5 for Trapezium\n\t"))
if (a==1):
      b=int(input("Enter Length: "))
      c=int(input("Enter Breadth:  "))
      print("Area of rectangle is  ",b*c)
      print("perimeter of rectangle is ", 2*b+2*c)
elif (a==2):
    b=int(input("Enter Radius: "))
    print("Area of circle is ",22/7*b*b)
    print("perimeter of circle is ",2*22/7*b)
elif (a==3):
    b=int(input("Enter Side: "))
    print("Area of Square is ",b*b)
    print("perimeter of square is ",4*b)
elif (a==4):
    b=int(input("Enter Diagonal 1: "))
    c=int(input("Enter Diagonal 2: "))
    d=int(input("Enter Side"))
    print("Area of rhombus is ",(b*c)/2)
    print("perimeter of rhombus is ",4*d)
elif (a==5):
     b=int(input("Enter Base 1: "))
     c=int(input("Enter Base 2: "))
     d=int(input("Enter Side 1: "))
     e=int(input("Enter Side 2: "))
     f=int(input("Enter Height: "))
     print("Area of Trapezium is ",((b+c)/2)*f)
     print("perimeter of Trapezium is ",b+c+d+e)
else:
    print("invalid input, Choose from the above numbers")
     
    
    
    
    
          
    
          
