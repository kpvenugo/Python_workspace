class Employee:
    employee_count = 0

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        Employee.employee_count += 1

    def display_employee(self):
        print(self.firstname + " " + self.lastname)


emp1 = Employee("kp", "venugopalan")
emp2 = Employee("jk", "venugopalan")
emp1.display_employee()
emp2.display_employee()
print(Employee.employee_count)
print(emp1.employee_count)
