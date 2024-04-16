# from math import sqrt
# # ========== 2.3.1 ==========
# while True: 
#     print("hi")
#     what = input("Shall we continue? ")
#     if what == "no":
#         print("okay then")
#         break

# # ========== 2.3.2 ==========
# while True:
#     n = int(input("Please type in a number: "))
#     if n > 0:
#         print(sqrt(n))
#     elif n < 0:
#         print("Invalid number")
#     else:
#         print("Exiting...")
#         break

# # ========== 2.3.3 ==========
# number = 5
# print("Countdown!")
# while True:
#   print(number)
#   number = number - 1
#   if number <= 0:
#     break
# print("Now!")

# #========== 2.3.4 ==========
# pas = input("Password: ")
# while True:
#     r = input("Repeat password: ")
#     if r == pas:
#         print("User account created!")
#         break
#     else:
#         print("They do not match!")

# # ========== 2.3.5 ==========
# pin = 4321
# attempts = 0
# while True:
#     p = int(input("Pin: "))
#     attempts = attempts + 1
#     if p == pin and attempts == 1:
#         print("Correct! It only took you a single attempt!")
#         break
#     elif p == pin:
#         print("Correct! It took you", attempts, "attempts")
#         break
#     else:
#         print("Wrong")

# # ========== 2.3.6 ==========
# year = int(input("Year: "))
# print("The next leap year after", year, "is", ((year - (year%4))+ 4))

# # ========== 2.3.7 ==========
# string = ""
# while True:
#     word = input("Please type in a word: ")
#     if word != "end":
#         string = str(str(string) + str(word) + " ")
#     else:
#         print(str(string))
#         break
# # ========== 2.3.8 ==========
# string = ""
# pword = ""
# word = ""
# while True:
#     pword = word
#     word = input("Please type in a word: ")
#     if word != "end" and word != pword:
#         string = str(str(string) + str(word) + " ")
#     else:
#         print(str(string))
#         break

# # ========== 2.3.9 ==========
n = ""
sum = 0
mean = 0
pos = 0
neg = 0
total = 0
print("Please type in integer number. Type in 0 to finish. ")
while True:
    n = int(input("Number: "))
    if n == 0:
        print("Numbers typed in:", total)
        print("Sum of number:", sum)
        print("Mean of numbers:", (sum/total))
        print("Positive number:", pos)
        print("Negative numbers:", neg)
        break
    else:
        total = total + 1
        sum = sum + n
        if n < 0:
            neg  = neg + 1
        else:
            pos = pos + 1
        
        
        


