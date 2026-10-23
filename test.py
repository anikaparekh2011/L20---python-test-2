#Build a calculator that uses a separate function for each operation. 
# The user picks an operation and enters two numbers.#
#  Your program handles invalid input and division by zero without crashing.

# def and return     →  define 4 functions: add, subtract, multiply, divide
#2.  try/except         →  catch ZeroDivisionError and ValueError without crashing
#3.  float(input())     →  to read numbers from the user
#4.  return values      →  each function must return the correct result

try:
    def welcome():
        print("welcome to anika's calculator")
        print("to start you will have to input a number")
        
    welcome1 = welcome()
    print(welcome1)  

    def add(a,b):
        return(a+b)

    def sub(a,b):
        return(a-b)

    def div(a,b):
        return(a/b)

    def multiply(a,b):
        return(a*b)

    a = float(input("enter one number; "))
    b = float(input("enter another number: "))

    function = input("enter a function you want to do (add, sub, div or multiply): ")


    if function == "add":
        print(add(a,b))
    elif function == "sub":
        print(sub(a,b))
    elif function == "div":
        print(div(a,b))
    elif function == "multiply":
        print(multiply(a,b))
    else:
        print("wrong function")
except ValueError:
    print("there is a value error ")
except ZeroDivisionError:
    print("there is a zero division error, you cannot divide by zero")