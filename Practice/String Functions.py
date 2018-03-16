
string = '       this is a important string        '

# Get rid of whitespace from left
string = string.lstrip()

# Get rid of whitespace from right
string = string.rstrip()

# get rid of whitespace from both sides
string = string.strip()

# Capitalize the correct letters in sentence
print(string.capitalize())

# Make whole string uppercase
print(string.upper())

# Make whole string lowercase
print(string.lower())

a_list = ['Bunch', 'of', 'random', 'words']
# Join the list items with a space
print(' '.join(a_list))

# Making the sentence a list of words
a_list_2 = string.split()
for i in a_list_2:
    print(i)
