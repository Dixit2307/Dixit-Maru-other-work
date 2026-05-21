#  chack leap year maltipale condition

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Assignment Operator

# Incriment and decriment number

num1=int(input("Enter a number for incriment and dicrement"))
num2=int(input("Enter how many number you have to incriment and dicrement "))

ans1=num1+num2
ans2=num1-num2

print("increment",ans1)
print("Dicrement",ans2)

# Salary increment calculation

salary=int(input("Enter your current salary"))
increment=int(input("Enter your increment"))

Ans=salary+increment

print("your salary after increment is ", Ans)

# discount calculation  using assignment operators

num1=int(input("Enter Prodect Prise"))
num2=int(input("% of Discount"))

DIscount=(num1 - (num1*num2/100))

print("your Product price after Discounit is",(num1 - (num1*num2/100))








