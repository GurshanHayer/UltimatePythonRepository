print("########## 1.4.1 ##########")
variable = input("Please type in a number: ")
print(variable, "times 5 is", 5 * int(variable))

print("########## 1.4.2 ##########")
name = input("What is your name? " )
yaer = input("Which year were you born? ")
print("Hi", name + ", you will be", 2024-int(yaer), "at the end of the year 2024")

print("########## 1.4.3 ##########")
days = input("How many days? ")
print("Seconds in that many days:", int(days)*24*60*60)

print("########## 1.4.4 ##########")
 # Fix the code
number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
number3 = int(input("Please type in the third number: "))
product = int(int(number1) * int(number2) * int(number3))
print("The product is", product)

print("########## 1.4.5 ##########")
number1 = input("Number 1: ")
number2 = input("Number 2: ")
print("The sum of the numbers:", int(number1) + int(number2))
print("The product of the numbers:", int(number1) * int(number2))

print("########## 1.4.6 ##########")
number1 = input("Number 1: ")
number2 = input("Number 2: ")
number3 = input("Number 3: ")
number4 = input("Number 4: ")
sum = (int(number1)+int(number2)+int(number3)+int(number4))
mean = ((int(number1)+int(number2)+int(number3)+int(number4))/4)
print("The sum of the number is", sum , "and the mean is",  mean)

print("########## 1.4.7 ##########")
times = float(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a trypical student lunch? "))
groceries = float(input("How much money do you spend on groceries in a week? "))

Daily =(((times*price)+groceries)/7)
Weekly =((times*price)+groceries)
print()
print("Average food expenditure:")
print("Daily: $" + str(Daily))
print("Weekly: $" + str(Weekly))

print("########## 1.4.8 ##########")
stu = float(input("How many student on the course? "))
size = float(input("Desired group size? "))

groups = (int(stu)%int(size))
if groups == 0:
    print("Number of groups formed:", int(stu/size))
else : print("Number of groups formed:", int(stu//size) + 1)
