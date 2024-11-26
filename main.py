# calculator.py

def add(a,b):
    return a + b

def subtract(a,b):

    return a-b
 
def multiply(a,b):
    return a * b

def divide(a,b):
    
    if b== 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print("Simple calculator")
    print("Adição: ", add(2,3))
    print("Subtração:   ", subtract(5,2))
    print("Multiplicação: ", multiply(3,4))
    print("divisão: ", divide(10,2))
