dict1 = {"name": "Vivek", "age": 26, "city": "Hyderabad"}
dict2 = {"age": 28, "salary": 45000, "country": "India"}
merged_dict ={**dict1, **dict2}
print(merged_dict)