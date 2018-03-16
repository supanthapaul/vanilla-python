# This program forces the user to enter a number

# The user may write letter and other stuff
# In that case we keep asking for a integer
# Until the user enters an integer

while True:

    try:
        number = int(input('Enter a integer number:: '))
        break
    except ValueError:                          # ValueError: if the user inputs a value which is not int in this case
        print("You didn't enter a number")
    except:                                     # An unknown error might occur which we don't know about
        print('An unknown error occurred')

# It is always good to check for a exception which we are aware of
# Using just 'except' is not recommended

print('Thank you for entering a number: {}'.format(number))     # Replacing the {} with number

