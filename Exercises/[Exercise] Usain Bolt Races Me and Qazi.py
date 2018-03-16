def choice_to_number(choice):
    return {'Usain': 1, 'Me': 2, 'Qazi': 3}.get(choice)


def number_to_choice(num):
    return {1: 'Usain', 2: 'Me', 3: 'Qazi'}.get(num)


print(number_to_choice(1))     # Should return Usain
print(choice_to_number('Me'))  # Should return 2

