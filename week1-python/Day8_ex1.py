# employee1 = {"name" : "Pruthvi", "age" : 21, "salary" : 40000}
# employee2 = {"name" : "Vivek", "age" : 23, "salary" : 45000}
# employee3 = {"name" : "Kayagurala", "age" : 26, "salary" : 48000}
# print(employee1["name"])
# print(employee2["salary"])
# print(employee3["age"])
# print(type(employee1))

employees = [
    {"name" : "Pruthvi", "age" : 21, "salary" : 40000},
    {"name" : "Vivek", "age" : 23, "salary" : 45000},
    {"name" : "Kayagurala", "age" : 26, "salary" : 48000}
]

#print(employees[0]["name"])

# for i in range(0, len(employees)):
#     employee_name = employees[i]["name"]
#     employee_salary = employees[i]["salary"]
#     print(f"{employee_name} earns {employee_salary}")

for i in employees:
    print(f"{i['name']} earns {i['salary']}")