list1 = "aeioulnstr"
list2 = "dg"
list3 = "bcmp"
list4 = "fhvwy"
list5 = "k"
list8 = "jx"
list10 = "qz"

def scrabble_score(word):
    total = 0
    for letter in word:
        if letter in list1:
            total += 1
        elif letter in list2:
            total += 2
        elif letter in list3:
            total += 3
        elif letter in list4:
            total += 4
        elif letter in list5:
            total += 5
        elif letter in list8:
            total += 8
        elif letter in list10:
            total += 10
    return(total)

print(scrabble_score("hello")) # 8
print(scrabble_score("world")) # 9
print(scrabble_score("zebra")) # 16
print(scrabble_score("xylophone")) # 24