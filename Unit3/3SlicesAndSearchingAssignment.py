# ========== 3.3.1 ==========
s1 = input("Please type in a string: ")
n1 = 1
while True:
    if n1 <= len(s1):
        print(s1[0:n1])
        n1 += 1
    else:
        break

# ========== 3.3.2 ==========
s1 = input("Please type in a string: ")
n1 = (len(s1))
while True:
    if n1 > 0:
        print(s1[(n1-1):len(s1)])
        n1 -= 1
    else:
        break

# ========== 3.3.3 ==========
s1 = input("Please type in a string: ")
if "a" in s1: 
    print("a found")
else:
    print("a not found")
if "e" in s1: 
    print("e found")
else:
    print("e not found")
if "o" in s1: 
    print("o found")
else:
    print("o not found")

# ========== 3.3.4 ==========
s1 = input("Please type in a word: ")
l1 = input("Please type in a character: ")
digit = s1.find(l1)
if l1 in s1:
    print(s1[digit: digit+3])

# ========== 3.3.5 ==========
newstring = input("Please type in a word: ")
l1 = input("Please type in a character: ")
digit = newstring.find(l1)
while l1 in newstring and len(newstring) > 2:  
    digit = newstring.find(l1)  
    print(newstring[digit: digit+3])
    newstring = newstring[(digit + 1):]

# ========== 3.3.6 ==========
s1 = input("Please type in a string: ")
s2 = s1
s3 = ""
substring = input("Please type in a substring: ")
l = substring[0] #find first letter
posSub = s1.find(l) #find index
newposSub = 0 #find new index
findsub = substring in s1 #true/false
truth = 0
while findsub and truth < 2:
    posSub = s1.find(l) #find index
    if truth == 1:
        s3 = s1
    s1 = s1[(posSub + 2):]
    findsub = substring in s1
    truth += 1
if truth <= 1:
    print("The substring does not occur twice in the string.")
elif truth >= 2:
    posSub = posSub + (len(s2) - len(s3))
    print("The second occurrence of the substring is at index", posSub, ".")