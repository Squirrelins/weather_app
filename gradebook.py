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

# Ask for the name of three courses and 3 grades for each course. I'm going to use a for loop to do this 3 times per student.

courses = []
grades = []

for i in range(3):
    courses.append(input("Enter the name of a course: "))
    grades.append(input("Enter the grade for the course: "))
    print()

# Add the courses and grades to the dictionary

students['courses'] = courses
students['grades'] = grades

# Average the 3 grades for each course

average = 0 # Set the average to 0
for grade in grades: # Loop through the grades
    average += int(grade) # Add up all the grades
average /= 3 # Divide by 3 to get the average

# Add the average to the dictionary

students['average'] = average

# Print the student's information

print()
print("Student ID:", students['student_id'])
print("Name:", students['first_name'], students['last_name'])
print("Courses:", students['courses'])
print("Grades:", students['grades'])
print("Average:", students['average'])

# Ask if the user wants to add another student

add_another = input("Would you like to add another student? (y/n): ")

# If the user wants to add another student, repeat the process

while add_another == 'y':
    students = {}
    students['student_id'] = 100000 + len(students) + 1
    students['first_name'] = input("Enter the student's first name: ")
    students['last_name'] = input("Enter the student's last name: ")
    courses = []
    grades = []
    for i in range(3):
        courses.append(input("Enter the name of a course: "))
        grades.append(input("Enter the grade for the course: "))
        print()
    students['courses'] = courses
    students['grades'] = grades
    average = 0
    for grade in grades:
        average += int(grade)
    average /= 3
    students['average'] = average
    print()
    print("Student ID:", students['student_id'])
    print("Name:", students['first_name'], students['last_name'])
    print("Courses:", students['courses'])
    print("Grades:", students['grades'])
    print("Average:", students['average'])
    add_another = input("Would you like to add another student? (y/n): ")

# If the user doesn't want to add another student, exit the program
    
else:
    print("Goodbye!")
    exit()