#x=int(input("entert the first number1:")
#y=int(input("entert the first number2:")
#if x>y:
    #print(f"{x} is largest")
    #else:
    #print(f"{y}is largest")
'''
x=int(input("enter the first number1:"))

if x % 2 == 0:
  print("even")    
else:
  print("odd")    
'''

#wap to find the largest b/w 3 number
'''x=int(input("enter the first no1:"))
y=int(input("enter the second no2:"))
z=int(input("emter the third no3:"))
if x>y and x>z:
  print(f"{x} is largest")
elif y>z:
  print(f"{y} is largest")  
else:
  print(f"{z} is largest")'''

#wap to take three sides as input and if they form a traingle ,
#check whether the traingle is equiteral/isoceles/scalene
#equilateral - all sides = , isoceles - any two sides = , scalene means
#all different
a=int(input("enter the first side:"))
b=int(input("enter the first side:"))
c=int(input("enter the third side:"))  

if a+b>c and b+c>a and c+a>b:
  if a==b and b==c:
    print("Equiteral Traingle")
  elif a==b or b==c or c==a:
    print("Isoceles Traingle")
  else:
    print("Scalene Traingle")
else:
  print("Invalid sides")

