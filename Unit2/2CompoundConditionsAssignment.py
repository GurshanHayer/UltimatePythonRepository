#print("########## 2.2.1 ##########")
age = int(input("What is your age? "))
if age > 0:
    if age < 7:
        print("I suspect you can't write quite yet...")
    else:
        print("Ok, you're", age, "years old")
else:
    print("That must be a mistake")

#print("########## 2.2.2 ##########")
name = input("Please type in your name: ")
if name == "Morty" or name == "Ferdie" or name == "Huey" or name == "Dewey" or name == "Louie":
    if name == "Morty" or name == "Ferdie":
        print("I think you might be one of Mickey Mouse's nephews.")
    else:
        print("I think you might be one of Donald Duck's nephews.")
else: 
    print("You're not a nephew of any character I know of.")    

#print("########## 2.2.3 ##########")
grade = int(input("Type in a percent: "))
if grade >= 0 and grade <= 100:
    if grade >= 90:
        print("Grade: A")
    elif grade >= 80:
        print("Grade: B")
    elif grade >= 70:
        print("Grade: C")
    elif grade >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
else:
    print("Grade: impossible!")

#print("########## 2.2.4 ##########")
n = int(input("Number: "))
if n % 3 == 0:
    print("Fizz", end="")
if n % 5 == 0:
    print("Buzz")

#print("########## 2.2.5 ##########")
year = int(input("Please type in a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("That year is a leap year.")
        else:
            print("That year is not a leap year.")
    else:
        print("That year is a leap year.")
else:
    print("That year is not a leap year.")
    
# print("########## 2.2.6 ##########")
fir = input("1st letter: ")
sec = input("2nd letter: ")
thi = input("3rd letter: ")
if fir > sec and fir < thi:
    print("The letter in the middle is", fir)
elif sec > fir and sec < thi:
    print("The letter in the middle is", sec)
else:
    print("The letter in the middle is", thi)