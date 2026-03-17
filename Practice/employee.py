class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department
    
    def calculate_salary(self, salary, hours_worked):
        if hours_worked <= 50:
            pass
        else:
            overtime = hours_worked - 50
            overtime_amount = (overtime * (salary/50))
            self.emp_salary = overtime_amount + salary
    
    def assign_department(self, department):
        self.emp_department = department
    
    def print_employee_details(self):
        print(f"Name: {self.emp_name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Salary: {self.emp_salary}")
        print(f"Employee Department: {self.emp_department}")
        
