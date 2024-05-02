# ========== 3.4.1 ==========
def seven_dwarves():
    print("Bashful")
    print("Doc")
    print("Dopey")
    print("Grumpy")
    print("Happy")
    print("Sleepy")
    print("Sneezy")

seven_dwarves()

# ========== 3.4.2 ==========
def first_character(x):
    print(x[0])
first_character('python')
first_character('yellow')
first_character('tomorrow')
first_character('heliotrope')
first_character('open')
first_character('night')

# ========== 3.4.3 ==========
def mean(n1, n2, n3):
    print((n1 + n2 + n3)/3)
mean(5, 3, 1)
mean(10, 1, 1)

# ========== 3.4.4 ==========
def print_many_times(text, times):
    while times > 0:
        times -= 1
        print(text)

print_many_times("All pythons, except one, grow up", 3)

# ========== 3.4.5 ==========
def hash_square(length):
    n1 = length
    while n1 > 0:
        n1 -= 1
        print("#"*length)

hash_square(3)
print()
hash_square(5)

# ========== 3.4.6 ==========
x = 0
y = 0
def chessboard(length):
    x = length
    count = 1
    while x > 0:
        if length % 2 == 0:
            count += 1
        y = length
        while y > 0:
            if count % 2 == 1:
                print("1", end="")
            if count % 2 == 0:
                print("0", end="")
            y -= 1
            count += 1
        print("")
        x -= 1
    
chessboard(3)
print()
chessboard(6)




