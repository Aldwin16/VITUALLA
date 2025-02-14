class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        # Print a short introduction
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am studying {self.course}.")

student1 = Student("Aldwin", 20, "Information Technology")
student2 = Student("Jarold", 21, "Tourism Management")
student3 = Student("Joshua", 21, "Criminology")

print("Student 1 Introduction:")
student1.introduce()
print("\nStudent 2 Introduction:")
student2.introduce()
print("\nStudent 3 Introduction:")
student3.introduce()
