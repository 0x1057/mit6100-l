#Finger exercise: Write a program that asks the user to input 10 integers, and then
#prints the largest odd number that was entered. If no odd number was entered, it
#should print a message to that effect.
import sys


int_list = []
i = 0
maxi = float('-inf') # set maxi to smallest int value possible
checker = 0 # used to see if odd value was even entered

# while loop to get user input and fill our list
while len(int_list) < 10:
    list_element = int(input(f"Enter 10 ints starting now ({i+1}): "))
    if list_element % 2 != 0: # checking if value entered is odd, if so update checker
        checker = 1
    int_list.append(list_element)
    i += 1

if checker == 0:
    print("No odd vals entered")
else:
    # reset i so we can use it again
    i = 0

    while i < len(int_list):
        if (int_list[i] % 2 != 0) and (int_list[i] > maxi):
            maxi = int(int_list[i])
        i += 1
    print(maxi)

