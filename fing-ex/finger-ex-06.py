# Let s be a string that contains a sequence of decimal numbers
# separated by commas, e.g., s = '1.23,2.4,3.123'. Write a program that prints the
# sum of the numbers in s.

dec_num = input("Input a number over 999 separated properly by commas, e.g. 1,999,834: ")

int_list = dec_num.split(",")
total = 0


for i in range(len(int_list)):
    total += int(int_list[i])

print(total)

