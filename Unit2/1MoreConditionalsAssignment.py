# print("########## 2.1.1 ##########")
word = input("Please type in a word: ")
if len(word) > 1:
    print("There are", int(len(word)), "letters in the word", word )
print("Thank You!")

# print("########## 2.1.2 ##########")
number = float(input("Please type in a number: "))
print("Integer part:", int(number))
print("Decimal part:", (number - int(number)))

print("########## 2.1.3 ##########")
age = int(input("How old are you? "))
if age >= 18:
    print("You may vote!")
else:
    print("You may not vote.")

#print("########## 2.1.4 ##########")
n1 = int(input("Please type in the first number: "))
n2 = int(input("Please type in the second number: "))
if n1 > n2:
    print("The greater number was:", n1)
elif n1 < n2:
    print("The greater number was:", n2)
else:
    print("The numbers are equal!")

#print("########## 2.1.5 ##########")
print("Person 1:")
name1 = input("Name: ")
age1 = int(input("Age: "))
print("Person 2:")
name2 = input("Name: ")
age2 = int(input("Age: "))
if age1 > age2:
    print("The elder is", name1 )
elif age2 > age1:
    print("The elder is", name2)
else:
    print(name1, "and", name2, "are the same age")

#print("########## 2.1.6 ##########")
word1 = input("Please type in the 1st word: ")
word2 = input("Please type in the 2nd word: ")
if word1 > word2:
    print(word1, "comes alphabetically last.")
elif word2 > word1:
    print(word2, "comes alphabetically last.")
else:
    print("You gave the same word twice.")
