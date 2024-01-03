class ManagementEmployee():


    def __init__(self):
        self.employees = []
    
    def add_employees(self,employees):
        if len(employees) == 1:
            self.employees.append(employees)
        else:
            self.employees.extend(employees)

    def count_gender_of_employees(self):
        male_employee = len([x for x in self.employees if x.gender == 'male'])
        females_employee = len([x for x in self.employees if x.gender == 'female'])
        return male_employee, females_employee
    
    def cal_highest_salary_employees(self):
        highest_salary_employees = [x for x in self.employees 
                                    if x.salary 
                                    == max([y.salary for y in self.employees])]
        return highest_salary_employees
    
    def cal_lowest_salary_employees(self):
        lowest_salary_employees = [x for x in self.employees if x.salary
                                   == min([y.salary for y in self.employees])]
        return lowest_salary_employees
    
    def cal_highest_years_of_experience_emps(self):
        highest_years_of_experience_emps = [x for x in self.employees 
                                            if x.years_of_experience 
                                            == max([x.years_of_experience for x in self.employees])]
        return highest_years_of_experience_emps
    
    def cal_oldest_youngest_employees(self):
        oldest_employees = [x for x in self.employees if x.age 
                            == max([y.age for y in self.employees])]
        youngest_employees = [x for x in self.employees if x.age 
                              == min([y.age for y in self.employees])]
        return oldest_employees, youngest_employees
    
    def sum_of_salaries(self):
        sum_of_salaries = sum([x.salary for x in self.employees])
        return sum_of_salaries