from math import sqrt


def calculate_square_root(number):
    return sqrt(number)


def append_item(item, l=None):
    if l is None:
        l = []
    l.append(item)
    return l


while True:
    try:
        your_number = float(input('Enter your number: '))
        print("Square root is:", calculate_square_root(your_number))
        break
    except Exception:
        pass
