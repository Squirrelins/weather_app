# Write a function to catch 0 divide error without using try...except

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError('Divide by zero')
    return a / b


def divisionby0(a, b):
    try:
        return divide(a, b)
    except ZeroDivisionError:
        return "Division by zero not possible unless you are a mathematician or a physicist that's studying black holes and solved the problem of singularity."

    