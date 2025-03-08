# Class and special, dudner methods

class Employee: 
    raise_amt = 1.04

    def __init__(self, first, last, pay): 
        self.first = first
        self.last = last
        self.email = f"{first}+{last}+@company.com"
        self.pay = pay

    def fullname(self):
        return f"{self.first} {self.last}"
    
    def __repr__(self): 
        return f"Employee: {self.first}, {self.last}, {self.pay}"
    
    def __str__(self): 
        return f"{self.fullname()} {self.email}"
    
    def __add__(self, other): 
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())
    

emp_1 = Employee('Ram','Das', 500)
emp_2 = Employee('Shambhu', 'Raje', 10)

print(emp_1 + emp_2)
print(len(emp_1))