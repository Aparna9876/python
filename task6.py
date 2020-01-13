a=input("enter the side:")
b=input("enter the side:")
c=input("enter the side:")
if a==b and b==c:
    print("equilateral triangle")
elif a==b or b==c or c==a:
    print("isoceles triangle")
else:
    print("scalene triangle")
