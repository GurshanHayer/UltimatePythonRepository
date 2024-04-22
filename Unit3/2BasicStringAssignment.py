# # ========== 3.2.1 ==========
# word = input("Please type in a string: ")
# amount = int(input("Please type in an amount: "))
# print((word*amount))

# # ========== 3.2.2 ==========
# s1 = input("Please type in string 1: ")
# s2 = input("Please type in string 2: ")
# if len(s1) > len(s2):
#     print(s1, "is longer")
# elif len(s2) > len(s1):
#     print(s2, "is longer")
# else:
#     print("The strings are equally long")

# # ========== 3.2.3 ==========
# word = input("Please type in a string: ")
# pos = len(word) - 1
# while pos >= 0:
#     print(word[pos])
#     pos -= 1

# # ========== 3.2.4 ==========
# word = input("Please type in a string: ")
# pos = len(word)- 1
# if len(word) >= 2:
#     if (word[pos - 1]) == (word[1]):
#         print("The second and second to last character are", word[1])
#     else:
#         print("The second and the second to last characters are different")

# # ========== 3.2.5 ==========
# width = int(input("Width: "))
# print("#"*width)

# # ========== 3.2.6 ==========
# width = int(input("Width: "))
# height = int(input("Height: "))
# while height > 0:
#     print("#"*width)
#     height -= 1

# # ========== 3.2.7 ==========
# while True:
#     s1 = input("Please type in a string: ")
#     if s1 != "":
#         print(s1)
#         print("-"*len(s1))
#     else:
#         break

# #========== 3.2.8 ==========
# s1 = input("Please type in a string: ")
# print(("*"*(20-len(s1))) + s1)

# # ========== 3.2.9 ==========
# word = input("Word: ")
# leng = int(len(word)/2)
# print("")
# print("*"*30)
# if len(word) % 2 == 0:
#     print("*"+(" "*(14-leng)) + word + (" "*(14-leng)) + "*")
# else:
#     print("*"+(" "*(14-leng)) + word + (" "*(13-leng)) + "*")
# print("*"*30)