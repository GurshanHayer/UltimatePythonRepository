# ========== 3.1.1 ==========
number = 30
while number >= 2:
    print(number)
    number = number - 2

# ========== 3.1.2 ==========
print("Are you ready?")
number = int(input("Please type in a number: "))
while number != 0:
    print(number)
    number = number - 1
print("Go!")

# ========== 3.1.3 ==========
lim = int(input("Upper limit: "))
number = 1
while lim > number:
    print(number)
    number = number + 1

# ========== 3.1.4 ==========
lim = int(input("Upper limit: "))
number = 0
while lim > (2**number):
    print(2**number)
    number = number + 1

# ========== 3.1.5 ==========
lim = int(input("Upper limit: "))
base = int(input("Base: "))
number = 0
while lim >= (base**number):
    print(base**number)
    number = number + 1

# ========== 3.1.6 ==========
lim = int(input("Limit: "))
number = 1
total = 0
while True:
    if total < lim:
        total = total + number
        number = number + 1
    else:
        print(total)
        break

