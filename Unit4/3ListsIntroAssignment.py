# # ========== 4.3.1 ==========
# new_list = [1, 2, 3, 4, 5]
# n = input
# while True:
#     n = int(input("Index: "))
#     if n == -1:
#         break
#     value = int(input("New value: "))
#     new_list.pop(n)
#     new_list.insert(n, value)
#     print(new_list)

# # ========== 4.3.2 ==========
# itemsn = int(input("How many items: "))
# count = 0
# sndlist = []
# while itemsn > count:
#     count += 1
#     string = str("Item")
#     print("Item", count, end="")
#     n = int(input(": "))
#     sndlist.append(n)
# print(sndlist)

# # ========== 4.3.3 ==========
# trdlist = []
# count = 0
# while True:
#     print("The list is now", trdlist)
#     operat = input("a(d)d, (r)emove or e(x)it: ")
#     if operat == "d":
#         count += 1
#         trdlist.append(count)
#     elif operat == "r":
#         trdlist.remove(count)
#         count -= 1
#     elif operat == "x":
#         print("Bye!")
#         break

# # ========== 4.3.4 ==========
# llist = []
# count = 0
# while True:
#     word = input("Word: ")
#     if word in llist:
#         print("You typed in", count, "different words")
#         break
#     else:
#         llist.append(word)
#         count += 1