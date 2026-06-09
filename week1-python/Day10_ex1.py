def word_frequency_counter(word):
    formatted_word = word.lower()
    #print(formatted_word)

    word_list = []
    word_count = {}
    for i in formatted_word:
        count = 0
        if i in word_list:
            word_count[i] = word_count[i] + 1
            word_list.append(i)

        else:
            word_list.append(i)
            count = count + 1
            word_count[i] = count
    return word_count




result = word_frequency_counter("ViVeK")
print(result)

