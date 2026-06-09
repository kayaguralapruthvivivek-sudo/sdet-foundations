# with open("employees.csv", "r") as file:
#     next(file)
#     total_salary = 0
#     count = 0
   
#     for i in file:
        
#         formatted_file = i.strip().split(",")
#         #print(formatted_file)
#         salary = int(formatted_file[2])
#         total_salary = salary + total_salary
#         count = count+1
#         average_salary = total_salary/count
#     if salary > average_salary:
#         with open("above_average.csv", "w") as file:
#             file.write("name,age,salary\n")
#             file.write(i)
                

    #print(average_salary)


with open("employees.csv", "r") as file:
    next(file)
    employees = []
    for i in file:
        employee = {}
        formatted_file = i.strip().split(",")
        employee["name"] = formatted_file[0]
        employee["age"] = formatted_file[1]
        employee["salary"] = formatted_file[2]
        
        employees.append(employee)
    print(employees)
    salary = 0
    for i in employees:
        #print(i["salary"])
        salary = salary + int(i["salary"])
    print(salary)
    average_salary = salary/len(employees)
    print(average_salary)
    

with open("above_average.csv", "w") as file:
    file.write("name,age,salary\n")
    for j in employees:
        if int(j["salary"]) > average_salary:
            file.write(f'{j["name"]},{j["age"]},{j["salary"]}\n')

    #print(employees[0]["salary"])
    #average_salary = sum(int(employees[2]["salary"])) /len(employees)
    #print(average_salary)

