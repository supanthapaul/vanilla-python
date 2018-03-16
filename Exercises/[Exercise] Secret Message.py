# This program will convert a given string to it's Unicode Value(Secret message)
# And return back to it's original string

# A - Z ===> 65 - 90
# a - z ===> 97 - 122

user_string = input('Enter a string in uppercase:: ')

secret_message = ''

# Cycle through each character and make a code out of that
# And add the code to the secret message string
for char in user_string:
    secret_message += str(ord(char) - 23)           # Subtracting 23 will make it available for uppercase and lowercase

print('Secret Message:: ' + secret_message)

original_message = ''

# Cycle through each character code 2 at a time by incrementing by 2 each time
for i in range(0, len(secret_message)-1, 2):
    # get the 1st and 2nd for the 2 digit number
    char_code = secret_message[i] + secret_message[i+1]
    # Convert the code in characters and add them to the original_message
    original_message += chr(int(char_code) + 23)        # Adding 23 will make it available for uppercase and lowercase

print('original Message:: ' + original_message)
