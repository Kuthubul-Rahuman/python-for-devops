
def task1():
    a = 5
    b = 7

    add = a+b
    sub = a-b
    quotient = a//b
    print(add)
    print(sub)
    print(quotient)
task1()

def task2():
    a = 45
    b = 30
    calc1 = a > b
    calc2 = a <= b
    calc3 = a >= b
    calc4 = a == b
    print(calc1, calc2, calc3, calc4)
task2()

def task3():
    x = True
    y = False
    x_and = x and y
    x_or = x or y
    x_not = not y 
    print(x_and, x_not, x_or)

task3()

def task4():
    total = 10
    total += 4
    total -= 6
    total *= 7
    total /= 8
    print(total)
task4()
