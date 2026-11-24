a = float(input("enter the first number:"))
b = float(input("enter the second number:"))
c = float(input("enter the third number:"))
if a>=b and a>=c:
    print("a is largest")
elif b>=a and b>=c:
    print("b is largest")
else:
    print("c is largest")