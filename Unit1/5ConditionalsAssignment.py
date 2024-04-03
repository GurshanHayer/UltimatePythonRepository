
print("########## 1.5.1 ##########")
year = int(input("Please type in a number: "))
if year == 1984:
    print("Orwell")

print("########## 1.5.2 ##########")
number = int(input("Please type in a number: "))
if number < 0:
    number = number*(-1)
print("The absolute value of this number is:", number)
        
print("########## 1.5.3 ##########")
name = input("What is your name? ")
if name != str("Jerry"):
    portions = int(input("How many portions of soup? "))
    print("The total cost is", portions*5.90)
print("Next Please!")

print("########## 1.5.4 ##########")
number = int(input("Type in a number: "))
if number < 1000:
    print("This number is smaller than 1000")
    if number < 100:
        print("This number is smaller than 100")
        if number < 10:
            print("This number is smaller than 10")
print("Thank You!")

print("########## 1.5.5 ##########")
n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
operation = input("Operation: ")
if operation == "add" or operation == "+":
    print(n1, "+", n2, "=", n1+n2)
if operation == "multiply" or operation == "*":
    print(n1, "*", n2, "=", n1*n2)
if operation == "subtract" or operation == "-":
    print(n1, "-", n2, "=", n1-n2)
if operation == "divide" or operation == "/":
    print(str(n1) + "/" + str(n2), "=", n1/n2)

print("########## 1.5.6 ##########")
temp = int(input("Type in a temperature (F): "))
print(temp, "degrees Farhenheit equals", (temp-32)*(5/9), "degrees Celsius")
if ((temp-32)*(5/9)) < 0:
    print("Brr! It's cold in here!")

print("########## 1.5.7 ##########")
wage = float(input("Hourly wage: "))
hours = float(input("Hour worked: "))
day = input("Day of the week: ")
n = 1
if day == "Sunday":
    n = 2
print("Daily wages: $" + str(int(wage*hours*n)))

print("########## 1.5.8 ##########")
# Fix the program
points = int(input("How many points are on your card? "))
points2 = points
if points < 100:
    points2 *= 1.1
    print("Your bonus is 10 %")

if points >= 100:
    points2 *= 1.15
    print("Your bonus is 15 %")

print("You now have", points2, "points")

print("########## 1.5.9 ##########")
print("What is the weather forecast for tomorrow? ")
temp = int(input("Temperature: "))
rain = input("Will it rain (yes/no): ")
print("Wear jeans and a T-shirt")
if temp <= 20:
    print("I recommend a sweater as well")
if temp <= 10:
    print("Take a jacket with you")
if temp <= 5:
    print("Make it a warm coat, actually")
    print("I think gloves are in order")
if rain == "yes":
    print("Don't forget your umbrella!")