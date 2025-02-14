class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

    def display_employee(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary}")

employee = Employee("Aldwin Vitualla", "Software Engineer", 60000)

employee.give_raise(5000)
employee.display_employee()
