def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero error"
    
def percentage(part, whole):
    if whole != 0:
        return (part / whole) * 100
    else:
        return "Division by zero error"