# state_city = {"NC": "Raleigh", "VA": "Richmond", "CA": "Sacramento", "TX": "Austin", "NY": "Albany"}

# # Add NY to the dictionary
# state_city["NY"] = "New York City"

# print(state_city)

# student = {"name": "Daniel", "courses": ["Python", "SQL", "Web Development"]}
# print(student)

students = {}
students["name"] = input("What is the students name? ")
students["courses"] = input("What is the name of the first course the student is taking? ")

students["quiz_scores"] = []
for i in range(3):
    score = int(input(f"What is the student's score {i+1}? "))
    if score > 100 or score < 0:
        print("Please enter a valid quiz score.")
    else:
        students["quiz_scores"].append(score)

average_score = sum(students["quiz_scores"]) / len(students["quiz_scores"])
print(f"The student's average quiz score is {average_score:.2f}")
print(students)
