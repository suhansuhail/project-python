# 1. addition
# 2.substraction
# 3.multiplication
# 4.division
# 5.sqaure
# 6.root
import math
print("select an operation to perform")
print("1.addition")
print("2.substraction")
print("3.multiplication")
print("4.division")
print("5.sqaure")
print("6.root")

operation = input()
if operation == "1":
    number1 = input("enter the first number: ")
    number2 = input("enter the second number: ")
    print("The value is"+str(int(number1)+int(number2)))
elif operation == "2":
    number1 = input("enter the first number: ")
    number2 = input("enter the second number: ")
    print("The value is "+str(int(number1)-int(number2)))
elif operation == "3":
    number1 = input("enter the first number: ")
    number2 = input("enter the second number: ")
    print("The value is"+str(int(number1)*int(number2)))
elif operation == "4":
    number1 = input("enter the first number: ")
    number2 = input("enter the second number: ")
    print("The value is"+str(int(number1)/int(number2)))
elif operation == "5":
    number1 = input("enter the first number: ")
    print("The square is"+str(int(number1)*int(number1)))
elif operation == "6":
     number1 = float(input("enter the first number: "))
     root = math.sqrt(number1)
     print("the root of the number is = "+str(int(root)))

else :
    print("invalid value")