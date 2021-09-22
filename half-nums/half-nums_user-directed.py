maxval = 0
minval = 0

num = 0
tries = 0

print("Reversed Number Guess project")
print("Project made by Segilmez06")
print("")
print("App will give you random numbers and you need to say if the number which was given is higher, lower or equals to the number you guessed.")
print("")

maxval = int(input("Enter the maximum value:"))

minval = int(input("Enter the minimum value:"))
if minval > maxval - 2:
    print("Invaild value.")
    quit()

gmax = maxval
gmin = minval

while True:
    
    num = int(gmax - gmin)
    num = int(num / 2)
    num = int(num + gmin)

    tries = tries + 1
    print("Try:", tries, "Number:", num)

    op = input("Enter the operator:")

    if op == "<":
        gmin = num
    
    elif op == ">":
        gmax = num

    elif op == "=":
        break

    else:
        print("Wrong operator.")

print("")
print("Yay! Found the number in", tries, "tries.", )