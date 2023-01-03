state = True 

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b 

def umnoj(a, b):
    return a * b

def delen(a, b):
    return a / b


dict = {
    "+": plus,
    "-": minus,
    "*": umnoj,
    "/": delen
}

a = float(input("What the first number?: "))
while state:
    for key in dict:
        print(key)
    op = input("Pick an operation: ")
    b = float(input("What the second number?: "))
    answer = dict[op](a, b)
    print(f"{a} {op} {b} = {answer}")
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
        a = answer
    else:
        state = False 
