class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
 
 
class Student(Person): 
    def __init__(self, name, age, student_id):
        # Call the constructor of the base class
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("Student ID: " + self.student_id)
    
class Employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary

    def display_info(self):
        print("Employee ID: " + self.emp_id)
        print("Salary: " + str(self.salary))

class StudentEmployee(Student, Employee):
    def __init__(self, name, age, student_id, emp_id, salary):
        Student.__init__(self, name, age, student_id)
        Employee.__init__(self, emp_id, salary)

    def display_info(self):
        Student.display_info(self)
        Employee.display_info(self)

if __name__ == "__main__":
    test = StudentEmployee("Bob", 20, "123456", "7891011", 100000)
    test.display_info()