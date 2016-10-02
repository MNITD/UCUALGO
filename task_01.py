def sort(input):
    i = 0
    while i < len(input):
        temp = input[i]
        j = i
        if temp % 2 == 0:
            if j > 0 and input[j - 1] % 2 != 0:
                i -= 1
            while j > 0 and (input[j - 1] > temp or input[j - 1] % 2 != 0):
                input[j] = input[j - 1]
                j -= 1
        else:
            if j > 0 and (j < len(input)-1) and (input[j + 1] > temp or input[j + 1] % 2 == 0):
                i -= 2
            while j < len(input) - 1 and (input[j + 1] > temp or input[j + 1] % 2 == 0):
                input[j] = input[j + 1]
                j += 1

        input[j] = temp
        i += 1

    return input

print(sort([]))
print(sort([1,1,1,1]))
print(sort([1, 2, 3, 4, 5, 6]))
print(sort([6, 5, 4, 3, 2, 1]))
print(sort([2, 4, 6, 5, 3, 1]))
print(sort([6, 4, 2, 1, 3, 5]))
print(sort([1, 3, 5, 7]))
print(sort([2, 4, 6, 8]))
print(sort([3, 8, 5, 1, 2, 9]))