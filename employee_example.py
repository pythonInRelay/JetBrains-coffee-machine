# Employee Class


class Employee:

    # This is called a class variable (it is the same for every instance of Employee)
    raise_amount = 1.04
    num_of_employees = 0

    # Defining how to create each instance of the "Employee()" class
    def __init__(self, first_name, last_name, pay):
        self.first = first_name
        self.last = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@company.com'

        # We don't want this different for any one specific instance, so we aren't using 'self' here
        Employee.num_of_employees += 1

        # Methods

        # To easily get the full name of an employee we make a method within the class
    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # Class methods use the @decorator
    # Use them when we want to modify the class variable (so it is true for each instanciation)
    @classmethod
    def set_raise_amt(cls, amount):  # use cls instead of self
        cls.raise_amount = amount

    # This is a 'constructor' i.e. it creates an instance of Employee() using any emp_str argument passed to it
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # Static methods do not take self, or cls. Only the arguments being passed to them
    # They are similar to a regular function but still have a relationship with the class
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# When we instanciate an object of Employee
# Self is passed automatically, we only need to provide first, last and pay.
emp_1 = Employee('Frodo', 'Baggins', '50000')
emp_2 = Employee('Sam', 'Gamwise', '40000')

# Employee strings to be used for our constructor above (remove the hyphen and make an employee)
emp_str_1 = 'Bilbo-Baggins-45000'
emp_str_2 = 'Aragon-Hunter-85000'
emp_str_3 = 'Legolass-Elf-75000'

# Create 1 more employee using the above example and print their fullname
emp_3 = Employee.from_string(emp_str_1)
print(emp_3.fullname())

# When using a method in eg. a print statement. We need to call the method so fullname()
print(emp_1.fullname())
print(emp_2.fullname())

# Can also call the class directly with an argument but it's longer
print(Employee.fullname(emp_1))

# We could print one of thee class' attributes in all lowercase by adding .lower() at the end
print(emp_1.email.lower())

# How to change the class variable directly (for all instances) using the @classmethod decorator
# cls is passed automatically so we only pass the second argument which is 'amount'
Employee.set_raise_amt(1.05)

# How to access the class variable amount directly
print(emp_1.pay)
print(emp_1.raise_amount)

# Show number of employees go up by 2 because we instanciated 2 above (as emp_1 and emp_2)
print(Employee.num_of_employees)

# Test the @Staticmethod above
import datetime
my_date = datetime.date(2020, 3, 9)  # MUST BE FORMAT: Year, month, day
print(Employee.is_workday(my_date))
