try:
    with open("employees.csv", "r") as file:
        next(file)
        for i in file:
            fortmatted_file = i.strip().split(",")
            name = fortmatted_file[0]
            age = int(fortmatted_file[1])
            salary = int(fortmatted_file[2])
            print(f"{name},{age},{salary}")

except FileNotFoundError:
    print("Error: employees.csv not found. Please check the file location.")
except ValueError:
    print("Invalid data in file")
    
