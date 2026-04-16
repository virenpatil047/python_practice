from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

print(logo)
n1 = float(input("What's the first number ? : "))
while True:
    for symbols in operations:
        print(symbols)
    opr = input("Pick an operation : ")
    n2 = float(input("What's the next number ? : "))
    res = operations[opr](n1, n2)
    print(f"{n1} {opr} {n2} = {res}")
    cont = input("Type 'y' to continue calculating with 2.0, or type 'n' to start a new calculation: ")
    if cont == "n":
        break
    n1 = res