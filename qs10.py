#Write a program that calculates the grade based on a given percentage.
print("Enter Marks Obtained in 5 Subjects: ")
total1 = int(input("enter the number1"))
total2 = int(input("enter the number2"))
total3 = int(input("enter the number3"))
total4 = int(input("enter the number4"))
total5 = int(input("enter the number5"))
 
tot = total1 + total2 + total3 + total4 + total4
avg = tot / 5
 
if avg >= 91 and avg <= 100:
    print("Your Grade is A1")
elif avg >= 81 and avg < 91:
    print("Your Grade is A2")
elif avg >= 71 and avg < 81:
    print("Your Grade is B1")
elif avg >= 61 and avg < 71:
    print("Your Grade is B2")
elif avg >= 51 and avg < 61:
    print("Your Grade is C1")
elif avg >= 41 and avg < 51:
    print("Your Grade is C2")
elif avg >= 33 and avg < 41:
    print("Your Grade is D")
else:
    print("you are failed!")