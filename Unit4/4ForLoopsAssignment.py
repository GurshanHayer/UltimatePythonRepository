# ========== 4.4.1 ==========
word = "Python"
for letter in word:
    print(letter)
    print("*")

# ========== 4.4.2 ==========
Nu = int(input("Please type in a poistive integer: "))
for number in range((-1*Nu), (Nu + 1)):
    if number != 0:
        print(number)

# ========== 4.4.3 ==========
def list_of_stars(newlist):
    index = 0
    while index < len(newlist):
        print("*"*(newlist[index]))
        index += 1

list_of_stars([3, 7, 1, 1, 2])

# ========== 4.4.4 ==========
def palindromes(word):
    failed = False
    check = True
    for number in range(0, len(word)):
        index = number
        lindex = len(word) - (1 + number)
        if word[index] != word[lindex]:
            failed = True
    if failed:
        return False
    else:
        return True
    
print(palindromes("python")) # False
print(palindromes("java")) # False
print(palindromes("neveroddoreven")) # True
print(palindromes("racecar")) # True

# ========== 4.4.5 ==========
def sum_of_positives(list):
    index = 0
    total = 0
    while index < len(list):
        if list[index] > 0:
            total += list[index]
        index += 1
    return total

my_list = [1, -2, 3, -4, 5]
result = sum_of_positives(my_list)
print("The result is", result)   

# ========== 4.4.6 ==========
def even_numbers(list):
    index = 0
    total = []
    while index < len(list):
        if list[index] % 2 == 0:
            total.append(list[index])
        index += 1
    return total

my_list = [1, 2, 3, 4, 5]
new_list = even_numbers(my_list)
print("original", my_list)
print("new", new_list)

# ========== 4.4.7 ==========
def list_sum(list1, list2):
    newlist =[]
    index = 0
    while index < len(list1):
        newlist.append(list1[index] + list2[index])
        index +=1
    return newlist

a = [1, 2, 3]
b = [7, 8, 9]
print(list_sum(a, b)) # [8, 10, 12]

# ========== 4.4.8 ==========
def length_of_longest(list):
    total = 0
    for word in list:
        if len(word) > total:
            total = len(word)
    return total

my_list = ["first", "second", "fourth", "eleventh"]

result = length_of_longest(my_list)
print(result)
my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

result = length_of_longest(my_list)
print(result)

# ========== 4.4.9 ==========
def shortest(list):
    total = list[0]
    for word in list:
        if len(word) < len(total):
            total = word
    return total
my_list = ["first", "second", "fourth", "eleventh"]

result = shortest(my_list)
print(result)
my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

result = shortest(my_list)
print(result)
