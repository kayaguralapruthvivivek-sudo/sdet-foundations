with open("employees.csv", "r") as file:
    next(file)
    employees_list = []
    
    for i in file:
        employee = {}
        #print(i.strip().split(","))
        formatted_file = i.strip().split(",")
        employee["Name"] = formatted_file[0]
        employee["Age"] = int(formatted_file[1])
        employee["Salary"] = int(formatted_file[2])
        employees_list.append(employee)
    print(employees_list)
        #print(f"Name: {formatted_file[0]} | Age: {formatted_file[1]} | Salary: {formatted_file[2]}")
        
    
    

    