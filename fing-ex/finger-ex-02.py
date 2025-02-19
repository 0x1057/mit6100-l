# Finger exercise: Write a program that examines three variables—
# x, y, and z—and prints the largest odd number among them. If none
# of them are odd, it should print the smallest value of the three

x = 2
y = 3
z = 6

if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
    if x <= y and x <= z:
        print(x)
    elif y <= x and y <= z:
        print(y)
    else:
        print(z)
elif x % 2 != 0 and y % 2 != 0 and z % 2 != 0:
    if x >= y and x >= z:
        print(x)
    elif y >= x and y >= z:
        print(y)
    else:
        print(z)
elif x % 2 != 0 and y % 2 != 0 and z % 2 == 0:
    if x >= y:
        print(x)
    else:
        print(y)
elif x % 2 != 0 and y % 2 == 0 and z % 2 != 0:
    if x >= z:
        print(x)
    else:
        print(z)
elif x % 2 == 0 and y % 2 != 0 and z % 2 != 0:
    if y >= z:
        print(y)
    else:
        print(z)
elif x % 2 != 0 and y % 2 == 0 and z % 2 == 0:
    print(x)
elif x % 2 == 0 and y % 2 != 0 and z % 2 == 0:
    print(y)
elif x % 2 != 0 and y % 2 == 0 and z % 2 != 0:
    print(z)


