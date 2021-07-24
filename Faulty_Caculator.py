# Faulty Caculator

print("Please enter first number")
num1 = int(input())
print("Please enter second number")
num2 = int(input())
print("Please provide the sign of operation you want to perform:+,-,/,*")
op = input()
if (num1 == 56 and num2 == 9 and op == "+"):
    print("Your answer is", "77")
elif op == "+":
    print(num1 + num2)
elif (num1 == 45 and num2 == 3 and op == "*"):
    print("Your answer is", "555")
elif op == "*":
    print(num1 * num2)
elif (num1 == 56 and num2 == 6 and op == "/"):
    print("Your answer is", "4")
elif op == "/":
    print(num1 / num2)
elif op == "-":
    if num1 > num2:
        print(num1 - num2)
    elif num1 == num2:
        print(num1 - num2)
    else:
        print(num2 - num1)
else:
    print("Please enter correct operation")
