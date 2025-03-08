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


empl_name_string = 'Ram-Das-100'
empl2_name_string = 'Hanuman-Das-500'
new_emp_1 = Employee.from_string(empl_name_string)
new_emp_1.apply_raise()
# before applying set_raise_method with classmethod
print(new_emp_1.fullname())
print(new_emp_1.pay)

print(f"new_emp_1 raise value before rasing it through class: {new_emp_1.raise_amt}\n\n")
print("Setting Raise Emt...")
new_emp_1.set_raise_amt(1.15) # earlier it was 1.04 but for further instances it will be same
print(f"new_emp_1 raise_amount value: {new_emp_1.raise_amt}")
print(f"Employee raise amount value: {Employee.raise_amt}")
new_emp_1.apply_raise()
# after applying set_raise_method:w
print(f"{new_emp_1.pay}\n\n")


print("Employee 2 details\n")
new_emp_2 = Employee.from_string(empl2_name_string)
print(new_emp_2.fullname())
new_emp_2.apply_raise()
print("500 * 1.15 = 575: our logic and classmethods are working.... \n ")
print(new_emp_2.pay) # since set_raise_amt = 1.15 this will be 115