def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input("whats the first number?"))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("which operation symbol u want to proceed with?")
        num2 = float(input("whats the next number?"))
        calculation = operations[operation_symbol]
        answer = calculation(num1, num2)

        print(f"{answer}")

        if input(f"type 'y' to continue calculating with {answer}, or type 'n' to start with new calculation:") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
