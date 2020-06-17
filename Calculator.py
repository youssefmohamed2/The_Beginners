a = float(input("Enter A Number: "))
b = float(input("Enter An Operation: "))
c = float(input("Enter A Number: "))
if b == "+":
    print(a + c)
elif b == "-":
    print(a - c)
elif b == "*":
    print(a * c)
elif b == "/":
    print(a / c)
else:
    print("Invalid Operator")
