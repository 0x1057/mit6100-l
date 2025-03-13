#Finger exercise: Replace the comment in the following code with a while loop.
numXs = int(input('How many times should I print the letter X? '))
toPrint = ''
#concatenate X to toPrint numXs times
i = 0
while i < numXs:
    toPrint += 'x'
    i += 1
print(toPrint)