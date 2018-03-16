'''
Ask the user for a string and print out whether this string is a palindrome
or not. (A palindrome is a string that reads the same forwards and backwards.)
'''

user_string = str(input("Enter a string::"))

user_string = user_string.upper()

new_string = user_string[::-1]

if(user_string == new_string):
    print("The string is palindrome")
else:
    print("The string is not palindrome")