
# We could use a random number here
# But I didn't
number_to_guess = 5

while True:
    try:
        guessed_number = int(input('Guess a number between 1 and 10 :: '))
        if guessed_number == number_to_guess:
            break
        else:
            print('Try Again mate!')
    except ValueError:
        print('You did not enter a number')

print('You guessed it! The number is {}'.format(number_to_guess))
