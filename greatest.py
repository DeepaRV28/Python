a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
d=int(input("Enter fourth number:"))
if (a>b and a>c and a>d):
    print("a is greater",a)
    if(a%2==0):
        print("a is even number",a)
    else:
        print("a is not even number",a)
    if(a>50):
        print("a value is greater than 50")
    else:
        print("a value is lesser than 50")

elif (b>a and b>c and b>d):
    print("b is greater",b)

elif (c>b and c>a and c>d):
    print("c is greater",a)

elif (d>a and d>b and d>a):
    print("a is greater",a)

else:
    print("All are equal")
