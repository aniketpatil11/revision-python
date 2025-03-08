# Python Object oriented programming 

class Employee:
    num_of_employee = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay): 
        # Self is the current instance of object we are referring 
        # Its passed by default 

        self.first = first
        self.last = last
        self.pay = pay 
        self.email = first + "." + last + "@company.com"

        Employee.num_of_employee += 1

    def fullname(self): 
        return f"{self.first} {self.last}"
    
    def apply_raise(self): 
        return int(self.pay * self.raise_amount) # type: ignore
# If not for  
# emp_1.first = "Ram"
# emp_2.first = "Hanuman"
emp_1 = Employee('Ram', 'Das', 42400)
emp_2 = Employee('Hanuman', 'Das', 5000000000000000000)

print(emp_1.email)
print(emp_2.email)
print(emp_2.fullname())

print(emp_1.apply_raise())
print(Employee.num_of_employee)
print(emp_1.fullname()) # since self, the instance is passed by default we don't pass any arguments to the fullname method
print(Employee.fullname(emp_1)) # Here we pass emp_1 object

