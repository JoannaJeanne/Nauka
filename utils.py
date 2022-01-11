#opcja z def
#przeniesiona tu do oddzielnego module:
def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum