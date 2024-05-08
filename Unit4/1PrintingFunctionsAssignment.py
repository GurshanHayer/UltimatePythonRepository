# ========== 4.1.1 ==========
def line(length, text):
    if text != "":
        l = text[0]
        print(l*length)
    else:
        print("*"*length)

# line(7, "%")
# line(10, "LOL")
# line(3, "")

# ========== 4.1.2 ==========
def box_of_hashes(length):
    count = length
    while count > 0:
        line(10, "#")
        count -= 1

# box_of_hashes(5)
# print()
# box_of_hashes(2)

# ========== 4.1.3 ==========
def square_of_hashes(length):
    count = length
    while count > 0:
        line(length, "#")
        count -= 1

# square_of_hashes(5)
# print()
# square_of_hashes(3)

# ========== 4.1.4 ==========
def square(length, text):
    count = length
    while count > 0:
        line(length, text)
        count -= 1

# square(5, "*")
# print()
# square(3, "o")

# ========== 4.1.5 ==========
def triangle(length):
    count = 0
    while count <= length:
        line(count, "#")
        count += 1

# triangle(6)
# print()
# triangle(3)

# ========== 4.1.6 ==========
def shape(length1, text1, length2, text2):
    count1 = 0
    while count1 <= length1:
        line(count1, text1)
        count1 += 1
    count2 = length2
    while count2 > 0:
        line(length1, text2)
        count2 -= 1

# shape(5, "X", 3, "*")
# print()
# shape(2, "o", 4, "+")
# print()
# shape(3, ".", 0, ",")

# ========== 4.1.7 ==========

def spruce(number):
    print("a spruce!")
    count = -1
    spacing = (number)
    while count < (number*2) and (spacing > 0):
        spacing -= 1
        count += 2
        print((" " * spacing) + ("*" * count) + (" " * spacing))
    print((" " * (number - 1)) + ("*") + (" " * (number - 1)))

spruce(3)
print()
spruce(5)