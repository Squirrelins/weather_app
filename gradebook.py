# Gradebook using dictionaries

print("Welcome to the school of hard knocks!")
print("This is the gradebook program.")

# Creat an empty dictionary.

students = {}

# Assign a student id starting from 100000. Student ID's will be the primary key for students and incremental based on how many students are in the dictionary. We'll go with a big number to make identifying students easier.

students['student_id'] = 100000 + len(students) + 1

# Ask for the student's first and last name

students['first_name'] = input("Enter the student's first name: ")
students['last_name'] = input("Enter the student's last name: ")

# Ask for the name of three courses and 3 grades for each course. I'm going to use a for loop  to do this 3 timnes per student.

courses = []
grades = []

for i in range(3):
    courses.append(input("Enter the name of a course: "))
    grades.append(input("Enter the grade for the course: "))
    print()

# Add the courses and grades to the dictionary

students['courses'] = courses
students['grades'] = grades

