#Write a program that calculates the factorial of a number.

n = int(input("Enter any number: "))

f = 1
for i in range(n,0,-1):
   f*=i;
print(f)


