def calculate_salary(employee_data):
    for name, data in employee_data.items():
        salary = (data['salary'] / 30) * data['days_worked']
        bonus = (data['salary'] / 30) * data['days_worked'] * 0.1
        print(f"{name}: Salary - {salary}, Bonus - {bonus}")

def calculate_bonuses(employee_data):
    bonuses = {}
    for name, data in employee_data.items():
        bonus = (data['salary'] / 30) * data['days_worked'] * 0.1
        bonuses[name] = bonus
    return bonuses

def input_employee_data():
    employees = {}
    while True:
        name = input("Enter employee name (or 'exit' to finish): ")
        if name.lower() == 'exit':
            break
        salary = float(input("Enter employee salary: "))
        days_worked = int(input("Enter number of days worked: "))
        employees[name] = {'salary': salary, 'days_worked': days_worked}
    return employees

def recursive_display(employees, index=0):
    if index < len(employees):
        print(list(employees.keys())[index])
        recursive_display(employees, index + 1)

def recursive_search(employees, name, index=0):
    if index < len(employees):
        current_name = list(employees.keys())[index]
        if current_name.lower() == name.lower():
            return current_name
        else:
            return recursive_search(employees, name, index + 1)

if __name__ == "__main__":
    employees = input_employee_data()
    calculate_salary(employees)
    
    name_to_search = input("Enter the name to search: ")
    result = recursive_search(employees, name_to_search)
    if result:
        print(f"Employee {result} found!")
    else:
        print(f"Employee {name_to_search} not found.")

    recursive_display(employees)
