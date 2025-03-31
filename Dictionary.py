# Step 1: Create a dictionary with student names and marks
student_marks = {
    "Ram": 85,
    "Rohit": 78,
    "Mohit": 92,
    "Raju": 74,
    "Khan": 88
}

# Step 2: Ask the user to input a student's name
student_name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve and display marks or show an appropriate message
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print(f"Student '{student_name}' not found in the records.")
