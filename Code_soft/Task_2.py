#Different operation functions
def add(a,b):
    return a+b
def dif(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b == 0:
        print("Division cannot be perform!!")
    else:
        return a/b
def rem(a,b):
    return a%b
#main function
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
print("Enter the operation you want to perfrom from list:")
print("'+','-','*','/','%'")
oper = input()
match oper:
    case "+":
       print("Sum of ",num1,num2,"is",add(num1,num2))
    case "-":
       print("Difference of ",num1,num2,"is",dif(num1,num2))
    case "*":
        print("Product of ",num1,num2,"is",mul(num1,num2))
    case "/":
        print("Division of ",num1,num2,"is",div(num1,num2))
    case "%":
        print("Remainder of ",num1,num2,"is",rem(num1,num2))
    case _:
        print("Enter a vaild operator!")    
