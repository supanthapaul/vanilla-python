import random
import sys
import os

#Alt+R to run code

'''
Multiple lines comment
'''
print("Hello World")

# Printing without newline
print("I don't like ", end="")
print("Newlines")

#List
my_list = ['Juice', 'Tomatoes', 'Mangoes']
print("First Item: " + my_list[0]);
my_list[0] = "Green Juice"
print("New First Item: " + my_list[0])
# Adding new item in list in the end
my_list.append("Bananas")
print(my_list)

# dictionaries
# DICT[key] --> value
# {key1: value1, key2: value2, ...}
phone_book = {
    "Supantha": 7031842115,
    "Mom": 9434609916
    }
print(phone_book["Supantha"])

#dictionary with multiple values in a key
# we have to use a list here
detail_book = {
    "Supantha": [7031842115, "Supantha@supantha.com"],
    "Dad": [943442115, "dad@dad.com"]
    }
print(detail_book["Dad"][1])     #We use the index of the value we in the list


#Spliting Strings
#It returns a list of strings
string = "What-is-going-on"
print(string.split("-"))

#Another example of spliting
new_string = "XBOX 360 | 150 | New"
product, price, condition = new_string.split("|")
print(product)
print(price)
print(condition)

#Newline
print('\n')
print("It's a new line")