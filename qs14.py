14.#Write a program that checks if a given number is prime or not.

number=int(input("enter number is : "))

f=False;

if number==1:
    print(number,"is not prime number");
elif(number>1):
    for i in range(2,number):
        if(number%1==0):
            f=True
            break       
if f:
    print("is  not prime");
else:
    print("is prime")
