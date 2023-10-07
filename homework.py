# # Write an program that asks for user input for a student's name, the courses they are taking, and their quiz scores. Store this information in a dictionary. Print the student's average quiz score and all of their information neatly.

# students = {'name': 'Daniel', 'courses': ['Python', 'SQL', 'Math'], 'grade': ['100', '100', '90']} # create dictionary

# print(students) # print dictionary
# print(students['name']) # print name
# print(students.get('name')) # print name

# print(len(students)) # print length of dictionary
# print(students.keys()) # print keys of dictionary
# print(students.values()) # print values of dictionary
# print(students.items()) # print items of dictionary
# for key in students: # print keys of dictionary
#     print(key)

# Ask for the user to input a student's name, the courses they are taking, and their quiz scores. Store this information in the dictionary. Print the student's average quiz score and all of their information neatly.

students = {} # create empty dictionary
students['name'] = input("What is the student's name? ") # ask for student's name
students['courses'] = input("What is the name of the first course the student is taking? ") # ask for student's course

students['quiz_scores'] = [] # create empty list for quiz scores

for i in range(3): # loop through quiz scores
    score = int(input(f"What is the student's score {i+1}? ")) # ask for quiz score
    if score > 100 or score < 0: # Make sure score is between 0 and 100 or error
        print("Please enter a valid quiz score.") # print message
    else:
        students['quiz_scores'].append(score) # append score to list

average_score = sum(students['quiz_scores']) / len(students['quiz_scores']) # calculate average score by getting the sum of the scores then getting the length of the list and dividing by it to get the average.

print(f"The student's average quiz score is {average_score}") # print average score

print(f"Do you want to enter another student? ") # ask if user wants to enter another student if yes then loop through again if no then print dictionary
if input() == 'yes' or input() == 'Yes' or 'y' == 'Y':
    students['name'] = input("What is the student's name? ")
    students['courses'] = input("What is the name of the first course the student is taking? ")

    students['quiz_scores'] = []
    for i in range(3):
        score = int(input(f"What is the student's score {i+1}? "))
        if score > 100 or score < 0:
            print("Please enter a valid quiz score.")
        else:
            students['quiz_scores'].append(score)

    average_score = sum(students['quiz_scores']) / len(students['quiz_scores'])
    print(f"The student's average quiz score is {average_score}")
    print(students)
else:
    print("Thank-you! Program ending.")
    