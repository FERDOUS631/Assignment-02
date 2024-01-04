#Write a program that determines if a year is a leap year or not.
year=int(input("enter the year"));

if(year%400==0 and year%100==0):
    print("this year is leap year");
elif(year%4==0 and year%100!=0):
    print("this year is leap year");
else:
    print("this year is not leap year");
