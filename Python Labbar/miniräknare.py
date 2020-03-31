
def add(x, y):
   return x + y


def subtract(x, y):
   return x - y


def multiply(x, y):
   return x * y


def divide(x, y):
   return x / y


print("Select operation.")
print("1.Addera")
print("2.Subtrahera")
print("3.Multiplicera")
print("4.Dividera")


choice = input("Välj mellan (1/2/3/4): ")

num1 = float(input("Välj tal nummer 1: "))
num2 = float(input("Välj tal nummer 2: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")