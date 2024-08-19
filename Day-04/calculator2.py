# Prefered code style
import sys
num1 = 10
num2 = 5

def addition(num1, num2):
    add = num1 + num2
    print("This comes from another file: " + str(add))
def subtraction(num1, num2):
    sub = num2 - num1
    return sub
def multip():
    m = num1 * num2
    print(m)

addition(24, 13)
print(subtraction(2, 5))
multip()

num1 = sys.argv[1]