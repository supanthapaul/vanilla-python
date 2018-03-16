
# Acronyms ---> Random Access Memory = RAM

string = input('Enter a string:: ')

# Make the string to uppercase
string = string.upper()

# Convert the string to a list
list_of_words = string.split(" ")

# Print the first letter of each word
# and eliminate newline
for word in list_of_words:
    print(word[0], end='')

print()     # printing a new line for the acronym
