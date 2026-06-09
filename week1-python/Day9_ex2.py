with  open("employees.csv", "r") as file:
    next(file)
    for i in file:
        try:
            formatted_file = i.strip().split(",")
            salary = int(formatted_file[2])
        except ValueError:
            print(f"Skipping invalid row: {i.strip()}")
            continue

        
            