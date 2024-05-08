def greatest_number(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    elif n3 >= n1 and n3 >= n2:
        return n3

print(greatest_number(3, 4, 1)) # 4
print(greatest_number(99, -4, 7)) # 99
print(greatest_number(0, 0, 0)) # 0



def same_chars(stri, n1, n2):
    if n2 < (len(stri)-1) and n1 < (len(stri)-1):
        if str(stri)[n1] == str(stri)[n2]:
            return True
        else:
            return False
    else:
        return False
    
# same characters m and m
print(same_chars("programmer", 6, 7)) # True
# different characters p and r
print(same_chars("programmer", 0, 4)) # False
# the second index is not within the string
print(same_chars("programmer", 0, 12)) # False

x = 0

def first_word(string):
    space = " "
    if space in string:
        x = string.find(space)
        return string[0:x]

def second_word(string):
    space = " "
    count = 1
    while count == 1:
        x = string.find(space)
        string = string[x+1:]
        count -= 1
    x = string.find(space)
    return string[0:x]

def last_word(string):
    space = " "
    while space in string:
        x = string.find(space)
        string = string[x+1:]
    return string[0:]


sentence = "it was a dark and stormy python"    
print(first_word(sentence))
print(second_word(sentence))
print(last_word(sentence))