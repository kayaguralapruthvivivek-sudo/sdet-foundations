def string_reverser(word):
    length_of_word = len(word)
    result = []
    
    for i in range(length_of_word - 1, -1, -1):
        result.append(word[i])
        
    return "".join(result)




reversed_string = string_reverser("hello")
print(reversed_string)