

def square_number(number):
    return number ** 2


# Function for testing square_number function
def test_square_number():
    assert square_number(2) == 4
    assert square_number(4) == 16
    assert square_number(8) == 64
    print("My CODE IS CORRECT!")


test_square_number()
