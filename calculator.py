x = float(input("x: "))
op = input("Operator: ")
y = float(input("y: "))

if op == "+":
    print(x + y)
elif op == "-":
    print(x - y)
elif op == "*":
    print(x * y)
elif op == "/":
    print(x / y)
else:
    print("Error")