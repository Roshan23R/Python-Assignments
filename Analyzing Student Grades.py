from functools import reduce

def enter_student_grades():
    global studentGrades
    gradesStr = input("Enter grades for each student (comma-separated): ")
    studentGrades = list(map(int, gradesStr.split(',')))
    print("Student grades entered successfully!")

# Function to display student grades
def display_student_grades():
    print("Student Grades:\n", studentGrades)

calculate = lambda grade: 4.0 if grade >= 90 else (3.0 if grade >= 80 else (2.0 if grade >= 70 else (1.0 if grade >= 60 else 0.0)))

def calculate_grade_points():
    global gradePoints
    gradePoints = list(map(calculate, studentGrades))
    print("\nGrade Points Calculated:\n", gradePoints)

def filter_students_needing_assistance():
    global threshold
    threshold = float(input("Enter the threshold grade for students needing assistance: "))
    students_needing_assistance = list(filter(lambda grade: grade < threshold, gradePoints))      
    print("Students Needing Assistance:\n", students_needing_assistance)

def calculate_average_grade():
    average_grade = reduce(lambda x, y: x + y, studentGrades) / len(studentGrades)
    print("Average Grade:", average_grade)

def analysis_system():
    '''Welcome to the Student Grade Analysis System!
    1. Enter Student Grades
    2. Display Student Grades
    3. Calculate Grade Points
    4. Filter Students Needing Assistance
    5. Calculate Average Grade
    6. Exit
    '''

    print(analysis_system.__doc__)
    global studentGrades
    studentGrades = []
    while True:
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            enter_student_grades()
        elif choice == '2':
            display_student_grades()
        elif choice == '3':
            calculate_grade_points()
        elif choice == '4':
            filter_students_needing_assistance()
        elif choice == '5':
            calculate_average_grade()
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    analysis_system()
