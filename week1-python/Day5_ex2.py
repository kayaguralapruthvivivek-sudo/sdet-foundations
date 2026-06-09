def vowel_counter(word):
    formatted_word = word.strip().lower()
    #print(formatted_word)
    result = []
    #print(result)
    for i in range (0, len(formatted_word)):
        if formatted_word[i] in ["a", "e", "i", "o", "u"]:
            result.append(formatted_word[i])
    return len(result)

number_of_vowels = vowel_counter("      H e T K  P  ")
print(number_of_vowels)



# def vowel_counter(word):
#     formatted_word = word.strip().lower()
#     count = 0
#     for i in range(len(formatted_word)):
#         if formatted_word[i] in ["a", "e", "i", "o", "u"]:
#             count += 1
#     return count