class Employee: 
    num_of_employee = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay): 
        self.first = first
        self.last = last 
        self.pay = int(pay)
        self.email = f"{first}.{last}@company.com"
        Employee.num_of_employee += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = self.pay * self.raise_amt


# Developer: Inheriting from Employee class
class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # some people above line = Employee.__init__()
        self.prog_lang = prog_lang


dev_1 = Developer('Ram', 'Das', 50000, 'Python')
print(dev_1.fullname())
print(dev_1.email)