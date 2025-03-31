student_marks = {
    "Ram": 85,
    "Rohit": 78,
    "Mohit": 92,
    "Raju": 74,
    "Khan": 88
}
student_name = input("Enter the student's name: ")
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print(f"Student '{student_name}' not found in the records.")
