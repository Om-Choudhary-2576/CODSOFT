#Simple Calculator 

def calculator(a,b,op_choice):
    match op_choice:
        case '+':
            print(f"Result: {a} + {b}={a+b}")

        case '-':
            print(f"Result: {a} - {b}={a-b}")

        case '*':
            print(f"Result: {a} * {b}={a*b}")
        
        case '/':
            print(f"Result: {a} / {b}={a/b}")

        case '%':
            print(f"Result: {a} % {b}={a%b}")


num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))

op_choice=input("Enter Operator(+,-,*,/,%): ")

calculator(num1,num2,op_choice)
