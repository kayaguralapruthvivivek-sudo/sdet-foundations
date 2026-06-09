# numbers = [64, 34, 25, 12, 22]

# for j in range(len(numbers)):
               
#     for i in range(0, len(numbers) - 1):
#         temp = 0
#         #print(numbers[i])
#         if numbers[i] > numbers[i+1]:
#             temp = numbers[i]
#             numbers[i] = numbers[i+1]
#             numbers[i+1] = temp
#     print(numbers)



def bubblesort(numbers):
    for j in range(len(numbers)):
               
        for i in range(0, len(numbers) - 1 - j):
            temp = 0
            #print(numbers[i])
            if numbers[i] > numbers[i+1]:
                # temp = numbers[i]
                # numbers[i] = numbers[i+1]
                # numbers[i+1] = temp
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]  #simplified sort.
        #print(numbers)
    return numbers



result = bubblesort([64, 34, 25, 12, 22])
print(result)