# Bad format
import calculator2 as imported_cal
num1 = 10
num2 = 5

addition = num1 + num2
print("Value of addition is: " + str(addition))


sub = num1 - num2
print("This number equals: " + str(sub))

mult = num1 * num2
print(mult)

# You are calling a function from another file
imported_cal.addition()