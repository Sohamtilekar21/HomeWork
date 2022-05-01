print("Volume Caluculator")
a=int(input("Enter \n\t 1 for Cuboid\n\t 2 for Cube\n\t 3 for Sphere\n\t 4 for Hemishpere\n\t 5 for Cone\n\t"))
if (a==1):  
      b=int(input("Enter Length  : "))
      c=int(input("Enter Breadth : "))
      d=int(input("Enter Height  : "))
      print("Cuboid Volume Formula : L * B * H")
      print("Volume of Cuboid is  ",b*c*d)
elif (a==2): 
    b=int(input("Enter Side: "))
    print("Cube Volume Formula : L^3")
    print("Volume of Cube is ",b*b*b)
elif (a==3):
    b=int(input("Enter Radius: "))
    print("Sphere Volume Formula : 4/3 * π * r^3")
    print("Volume of Sphere is ",4/3*22/7*b*b*b)
elif (a==4):
     b=int(input("Enter Radius: "))
     print("Hemisphere Volume Formula : 2/3 * π * r^3")
     print("Volume of HemiSphere is ",2/3*22/7*b*b*b)
elif (a==5):
     b=int(input("Enter Radius: "))
     f=int(input("Enter Height: "))
     print("Cone Volume Formula : 1/3 * π * r^2 * h")
     print("Volume of Cone is ",1/3*22/7*f*b*b)
     
else:
    print("invalid input, Choose from the above numbers")
     
    
    
    
    
          
    
          
