# list = ["mango", "apple", "pineapple", "watermelon"]
# for i in list:
#     if len(i) > 5:
#         print(i)
    

def fruits_with_morethan_5_characters(fruits):
    test = []
    for i in fruits:
        if len(i) > 5:
            test.append(i)
    return test    
        



result = fruits_with_morethan_5_characters(["mango", "apple", "pineapple", "watermelon"])
print(result)