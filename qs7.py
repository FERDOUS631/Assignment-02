#Write a program that finds the maximum of three numbers.
a=int(input("enter number a"))
b=int(input("enter number b"))
c=int(input("enter number c"))

if (a > b and a > c):
    print("a is lagest number");
elif(b > a and b > c):
     print("b is lagest number");
elif(a==b and b==c):
     print("enter number is eqal");
else:
     print("c is lagest number");
