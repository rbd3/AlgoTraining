def Sum(array):
    total = 0
    n = len(array)

    for x in array:
        total += x

    return total

print(Sum([2,4,3]))