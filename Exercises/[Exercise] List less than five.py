numbers = [1,3,7,4,87,43,2]

small_numbers = []

number_limit = int(input("Enter number limit:: "))

for number in numbers:
    if number < number_limit:
        small_numbers.append(number)

print(small_numbers)