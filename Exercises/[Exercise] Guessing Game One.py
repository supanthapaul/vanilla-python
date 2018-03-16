import random
import math

random_number = random.randint(1,10)

print("==========Guessing Game==========")
user_number = int(input("Enter a number between 1 and 10"))

difference = user_number - random_number

difference = math.fabs(difference)      # Getting the absolute value of the difference

if difference == 0:
    print("You got it!")
elif difference <= 2:
    print("You were too close!")
elif difference >= 2 and difference<= 5 :
    print("You could do better")
else:
    print("you aren't even close")


