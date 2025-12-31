import art

def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
def modulus(n1, n2):
    return n1 % n2

operations = {"+":add, "-":sub, "*":multiply, "/":divide}
def calculator():
    print(art.logo)
    print("Welcome to Calculator")
    condition = True
    num1 = float(input("Enter a number: "))
    while condition:
        for key in operations:
            print(key)
        operation_choice = input("Enter a choice:\n")
        num2 = float(input("Enter another number: "))
        answer = operations[operation_choice](num1, num2)
        print(answer)

        step = input("Do you want to continue?(y/n): ").lower()
        if step == "n":
            condition = False
            print("\n" * 20)
            calculator()

        else:
            num1 = answer

calculator()
