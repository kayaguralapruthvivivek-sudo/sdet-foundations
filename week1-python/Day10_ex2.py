
def merged_dictionary(dict1, dict2):
    merged_dict = {}
    for i in dict1:
        #print(i)
        merged_dict[i] = dict1[i]

    for j in dict2:
        merged_dict[j] = dict2[j]

    #print(merged_dict)
    return merged_dict

    



dict1 ={"name": "Vivek", "age": 26, "city": "Hyderabad"}
dict2 = {"age": 28, "salary": 45000, "country": "India"}
result = merged_dictionary(dict1, dict2)
print(result)