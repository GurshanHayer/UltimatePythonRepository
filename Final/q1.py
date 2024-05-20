name1 = input("Please enter your first name: ")
name2 = input("Please enter your last name: ")
cGPA = float(input("Please enter your GPA: "))
days = 1
money = "$0."

if name2[0] <= "K":
    days = 0

if cGPA >= 3.86:
    money = "$16000."
elif cGPA >= 3.7:
    money = "$12000."
elif cGPA >= 3.5:
    money = "$8000."
elif cGPA >= 3.25:
    money = "$4000."

if days == 1:
    print("Hello, " + name1 + ". You should report to school on Tuesday and Friday. You are eligible for a scholarship of " + money)
else:
     print("Hello, " + name1 + ". You should report to school on Monday and Thursday. You are eligible for a scholarship of " + money)