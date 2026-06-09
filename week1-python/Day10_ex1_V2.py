# def word_frequency_counter(word):
#     formatted_word = word.lower().split()
#     word_count = {}
#     for i in formatted_word:
#         if i in word_count:
#             word_count[i] = word_count[i] + 1
        
#         else:
#             word_count[i] = 1
#     return word_count

# result = word_frequency_counter("ViveK")
# print(result)



def word_frequency_counter(word):
    formatted_word = word.lower().split()
    word_count = {}
    for i in formatted_word:
        word_count[i] = word_count.get(i,0)+1
    return word_count

result = word_frequency_counter("the cat sat on the mat the cat")
print(result)