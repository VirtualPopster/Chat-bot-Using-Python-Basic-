import datetime
now = datetime.datetime.now()
date = now.date()
hour = now.hour
if(hour<=12):
    print("Good morning Sir!")
if(hour>12):
    print("Good Afternoon Sir!")

print("\n\n")
def addition(a,b):
    return  a+b
def substraction(a,b):
    return a-b
def multiply(a,b):
    return  a*b
def divide(a,b):
    return a/b

greeting =["hi","hello","hey"]
while True:
    cmd = input("You >>")
    if cmd in greeting:
            print("Hey! nice to meet you")
    elif cmd.__eq__("add"):
        print("Yeah! i can assist you with that\n\n")
        a = int(input("You>> "))
        b = int(input("You>> "))
        print("\n here is your required answer! ", addition(a,b))
    elif cmd.__eq__("substract"):
        print("Yeah! i can assist you with that\n\n")
        a = int(input("You>> "))
        b = int(input("You>> "))
        print("\n here is your required answer! ", substraction(a,b))
    elif cmd.__eq__("multiply"):
        print("Yeah! i can assist you with that\n\n")
        a = int(input("You>> "))
        b = int(input("You>> "))
        print("\n here is your required answer! ", multiply(a, b))
    elif cmd.__eq__("divide"):
        print("Yeah! i can assist you with that\n\n")
        a = int(input("You>> "))
        b = int(input("You>> "))
        print("\n here is your required answer! ", divide(a, b))
    elif cmd.__eq__("!help"):
        print(" add --> Adds two 2 numbers ")
        print(" substract --> substracts two 2 numbers ")
        print(" multiply --> Multiplies two 2 numbers ")
        print(" divide --> divides two 2 numbers ")
        print(" date--> displays current date\n")
        print("  More features will be added soon !")
    elif (cmd.lower()).__eq__("date"):
        print(now.date())
