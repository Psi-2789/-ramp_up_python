import random

def employee_details(num_employees):
    cities = ["Kormangala", "HSR Layout", "Ballary", "Mumbai", "Chennai", "Nellore", "Gurgon", "Hyderabad"]
    for _ in range(num_employees):
        emp_id = random.randint(1,9999)
        emp_location = random.choice(cities)
        emply_salary = random.randint(20000,150000)
        yield f"emp_id:{emp_id},emp_location:{emp_location},emp_salary:{emply_salary}"

def main():
    try:
        number_of_employees = int(input("enter the number of details"))
        employee_generator = employee_details(number_of_employees)
        print("employee details")
        for _ in range(number_of_employees):
            emp_details = next(employee_generator)
            print(emp_details)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
