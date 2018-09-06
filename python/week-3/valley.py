def valley(numbers):
    size = len(numbers)
    if (size <= 2):
        return False

    valley_pivot = 0

    # First half
    for current in range(size - 1):
        next = current + 1
        if(numbers[current] <= numbers[next]):
            if(current == size - 1):
                return False
            valley_pivot = current
            break

    if(valley_pivot == 0):
        return False

    # Second half
    for current in range(valley_pivot, size - 1):
        next = current + 1
        if(numbers[current] >= numbers[next]):
            return False

    return True


# 3 2 1 1 2 3
# 3 > 2
print(valley([3, 2, 1, 2, 3]))
#  True

print(valley([3, 2, 1]))
#  False

print(valley([3, 3, 2, 1, 2]))
#  False

print(valley([17, 1, 2, 3, 4, 5]))
# True

print(valley([5, 4, 3, 2, 1, 2]))
# True

# 5 - 0 to 4
# 4 - 0 to 3
