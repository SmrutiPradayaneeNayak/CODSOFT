r = int(input("Enter the first input: "))
s = int(input("Enter the second input: "))

operator = input("Enter the type of operation you want to perform (+, -, *, /, %): ")

result = 0
if operator == "+":
    result = r+s
elif operator == "-":
    result = r-s
elif operator == "*":
    result = r*s
elif operator == "/":
    result = r//s
elif operator == "%":
    result = r%s
else:
    print("Invalid Input")
print("Your answer is: ",result)