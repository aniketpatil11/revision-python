class Employee: 
    num_of_employee = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay): 
        self.first = first
        self.last = last 
        self.pay = int(pay)
        Employee.num_of_employee += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = self.pay * self.raise_amt

    @classmethod
    # exampel of classmethods

    def set_raise_amt(cls, amount): 
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, empl_string): # like self for instance, cls is passed by default
        first, last, pay = empl_string.split('-') # split string at -
        return cls(first, last, pay) # that is saying Employee(first, last, pay)


    @staticmethod
    def is_workday(day): 
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
import datetime
my_date = datetime.date(2025, 3, 8)

print(Employee.is_workday(my_date))