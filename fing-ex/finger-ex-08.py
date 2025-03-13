# Write a function isIn that accepts two strings as arguments and
# returns True if either string occurs anywhere in the other, and False otherwise.
# Hint: you might want to use the built-in str operation in.
def is_in(str_one, str_two):
    if str_one in str_two or str_two in str_one:
        return True
    else:
        return False
    
def main():
    a = input("Type in a string: ")
    b = input("Type in another string: ")
    print(is_in(a, b))

main()