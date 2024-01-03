import json 
from prettytable import PrettyTable

from management_employee import ManagementEmployee
from model import Employee


manage = ManagementEmployee()

with open('./employees.json','r') as file:  
    data = json.load(file)

def dump_data():
    '''
    Extracts employee data from the global variable 'data',
    creates Employee objects for each entry, and adds them to
    the employee management system using the 'manage' object.

    Parameters:
        None

    Returns:
        None
    '''
    employees = []
    for emp in data:
        employee = Employee(emp)
        employees.append(employee)
    manage.add_employees(employees=employees)


def print_menu():
    print("""
            0. Exit
            1. Total employee
            2. Number of employee gender
            3. Highest of salary employees
            4. Lowest of salary employees
            5. Highest of experience employees
            6. Oldest and youngest employees
            7. Sum of salary employees
          """)

def serve(option):
    '''
    Get option and return a Pretty table object corresponding

    Parameters:
        option: int

    Returns:
        PrettyTable object or None
    '''
    table = PrettyTable()
    match option:
        case 1:
            employee_total = len(manage.employees)
            table.add_column("employee_total", [employee_total])
            return table
        case 2:
            male_employee, female_employee = manage.count_gender_of_employees()
            table.add_column("male_employee", [male_employee])
            table.add_column("female_employee", [female_employee])
            return table
        case 3:
            highest_salary_employees = manage.cal_highest_salary_employees()
            table.field_names = ['id', 'first_name', 'last_name', 'email', 
                                 'phone', 'gender', 'age', 'job_title', 
                                 'years_of_experience', 'salary', 'department']
            #get all values from employee and convert to list
            table.add_rows([[*x.get_all_values().values()] 
                            for x in highest_salary_employees])    
            return table
        case 4:
            lowest_salary_employees = manage.cal_lowest_salary_employees()
            table.field_names = ['id', 'first_name', 'last_name', 'email', 
                                 'phone', 'gender', 'age', 'job_title', 
                                 'years_of_experience', 'salary', 'department']
            table.add_rows([[*x.get_all_values().values()] 
                            for x in lowest_salary_employees])
            return table
        case 5:
            highest_years_of_experience_emps = manage.cal_highest_years_of_experience_emps()
            table.field_names = ['id', 'first_name', 'last_name', 'email', 
                                 'phone', 'gender', 'age', 'job_title', 
                                 'years_of_experience', 'salary', 'department']
            table.add_rows([[*x.get_all_values().values()] 
                            for x in highest_years_of_experience_emps])
            return table
        case 6:
            oldest_employees, youngest_employees = manage.cal_oldest_youngest_employees()
            table.field_names = ['id', 'first_name', 'last_name', 'email', 
                                 'phone', 'gender', 'age', 'job_title', 
                                 'years_of_experience', 'salary', 'department']
            table.add_rows([[*x.get_all_values().values()] 
                            for x in oldest_employees[:-2]])
            table.add_row([*oldest_employees[-1].get_all_values().values()],
                          divider=True)
            table.add_rows([[*x.get_all_values().values()] 
                            for x in youngest_employees])   
            return table
        case 7:
            sum_of_salaries = manage.sum_of_salaries()
            table.add_column('sum_of_salaries', [sum_of_salaries])
            return table
        case _:
            return None
        
if __name__ == "__main__":
    dump_data()
    print_menu()
    while True:
        try:
            print("Press enter to show menu \nOr")
            user_input = input('Enter your choice... ')
            option = -1
            if user_input == '':
                print_menu()
                pass
            else:
                option = int(user_input)
                if option == 0:
                    break
                result = serve(option=option)
                if result != None:
                    result.align="c"
                    print(result)
                else:
                    print(f"Your option not match menu {option}")
        except ValueError as e:
            print(f'{e}, please enter an integer number!!!')
        