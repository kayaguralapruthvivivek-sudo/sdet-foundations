def list_stats(numbers):
    count = 0
    length = len(numbers)
    for i in range(0, length):
        sum = numbers[i] + count
        count = sum
    average = count / length
    minimum = min(numbers)
    maximum = max(numbers)
    return count, average, minimum, maximum
    

    

result = list_stats([10, 20, 30, 40, 50])
print(result)

result2 = list_stats([5, 1, 8, 3])
print(result2)

result3 = list_stats([100, 200, 300])
print(result3)
