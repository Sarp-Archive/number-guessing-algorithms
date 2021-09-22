maxval = 0
minval = 0
val = 0

num = 0
tries = 0

maxval = int(input("Enter the maximum value:"))

minval = int(input("Enter the minimum value:"))
if minval > maxval - 2:
    print("Invaild value.")
    quit()

val = int(input("Enter the number you choose:"))
if (val < minval) | (val > maxval):
    print("Invaild value.")
    quit()

gmax = maxval
gmin = minval

while True:
    
    tries = tries + 1
    num = int(gmax - gmin)
    num = int(num / 2)
    num = int(num + gmin)

    print("Try:", tries, "Value:", val, "Number:", num)

    if num < val:
        gmin = num
    
    elif num > val:
        gmax = num

    elif num == val:
        break

print("")
print("Yay! Found the number in", tries, "tries.", )