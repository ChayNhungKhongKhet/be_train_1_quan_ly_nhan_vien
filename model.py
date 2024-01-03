class Employee:


    def __init__(self,id,first_name,
                 last_name,email,phone,
                 gender,age,job_title,
                 years_of_experience,
                 salary,department):
        
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.gender = gender
        self.age = age
        self.job_title = job_title
        self.years_of_experience = years_of_experience
        self.salary = salary
        self.department = department

    def __init__(self,dict_employee):
        '''
        Take employee dictionary type and pass to constructor corresponding

        Parameters:
            self: this instance
            dict_employee: dictionary employee

        Returns:
            None
        '''
        self.id = dict_employee['id']
        self.first_name = dict_employee['first_name']
        self.last_name = dict_employee['last_name']
        self.email = dict_employee['email']
        self.phone = dict_employee['phone']
        self.gender = dict_employee['gender']
        self.age = dict_employee['age']
        self.job_title = dict_employee['job_title']
        self.years_of_experience = dict_employee['years_of_experience']
        self.salary = dict_employee['salary']
        self.department = dict_employee['department']
    
    def __str__(self):
        return f"Employee ID: {self.id}\n" \
               f"Name: {self.first_name} {self.last_name}\n" \
               f"Email: {self.email}\n" \
               f"Phone: {self.phone}\n" \
               f"Gender: {self.gender}\n" \
               f"Age: {self.age}\n" \
               f"Job Title: {self.job_title}\n" \
               f"Years of Experience: {self.years_of_experience}\n" \
               f"Salary: {self.salary}\n" \
               f"Department: {self.department}"
    
    def get_all_values(self):
        '''
        Get all the values of the instance employee object

        Parameters:
            self: instance employee object

        Returns:
            dict: name and value pairs of all this instance employee
        '''
        return vars(self)