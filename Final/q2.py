amount = 50

while True:
    if amount > 0:
        print("Amount due:", amount)
        insert = int(input("Insert coin: "))
        if (insert == 25) or (insert == 10) or (insert == 5):
            amount = amount - insert
        else:
            print("Error - this coin type not accepted")
    else:
        print("Change owed:", (amount * -1))
        break