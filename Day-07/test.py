import sys

type = sys.argv[1]

if type == "t2.micro":
    print("You will be charged $2 per day")
elif type == "t2.medium":
    print("You will be charged $4 per day")
elif type == "t2.xlarge":
    print("You will be charged $8 per day")
else:
    print("Please provide a valid instance type")
# to run this, use python3 test.py t2.micro