

# If statements
study_hours = 41

if study_hours >= 40:
    print("You read a lot mate")

number_1 = int(input("Enter number 1"))
number_2 = int(input("Enter number 2"))


def sum_two(number_1, number_2):
  sumnumbers = number_1+number_2
  return sumnumbers


# assert is used for testing code
# If it doesn't show any error it means your code is correct
# ASSERT DOES NOT DO ANYTHING IN GENERAL
assert sum_two(number_1, number_2) == number_1 + number_2

print(sum_two(number_1, number_2))

# While Loops
count = 100
while count >= 0:
    print(str(count))
    count -= 1
print("Blast Off!")
