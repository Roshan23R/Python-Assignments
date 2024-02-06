students_dict = {}

def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    department = input("Enter student department: ")
    skills = input("Enter student skills (comma-separated): ").split(',')

    students_dict[student_id] = {'Name': name, 'Department': department, 'Skills': skills}
    print("Student added successfully.")

def display_students():
    if not students_dict:
        print("No students found.")
        return
    print("List of students:")
    for student_id, details in students_dict.items():
        print(f"ID {student_id}, Name: {details['Name']}, Department: {details['Department']}, Skills: {', '.join(details['Skills'])}")


def update_student_skills():
    student_id = input("Enter student ID to update skills: ")
    if student_id in students_dict:
        new_skills = input("Enter new skills (comma-seperated): ").split(',')
        students_dict[student_id]['Skills'] = new_skills
        print("Skills updated successfully.")
    else:
        print("Student not found.")

def remove_student():
    student_id = input("Enter student ID to remove: ")
    if student_id in students_dict:
        del students_dict[student_id]
        print("Student removed successfully.")
    else:
        print("Student not found.")

def search_by_department():
    department = input("Enter department to search: ")
    found_students = [student for student, details in students_dict.items() if details['Department'].lower() == department.lower()]

    if found_students:
        print("Students in the specified department:")
        for student_id in found_students:
            details = students_dict[student_id]
            print(f"ID: {student_id}, Name: {details['Name']}, Skills: {', '.join(details['Skills'])}")
    else:
        print(f"No students found in the {department} department.")

def generate_placement_reports():
    if not students_dict:
        print("No students found.")
        return
    
    print("Placement Reports:")
    for student_id, details in students_dict.items():
        skills = details['Skills']
        job_oppurtunities = ', '.join([f'{skill} positions' for skill in skills])
        print(f"\n{details['Name']} (ID: {student_id}):")
        print(f"   Department: {details['Department']}")
        print(f"   Eligible for: {job_oppurtunities}")

def main():
    print("\nStudent Placement System Menu:")
    print("1. Add Students")
    print("2. Display Students")
    print("3. Search for Students by Department")
    print("4. Update Student Skills")
    print("5. Remove Student")
    print("6. Generate Placement Reports")
    print("7. Exit System")

    while True:
       
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            search_by_department()
        elif choice == '4':
            update_student_skills()
        elif choice == '5':
            remove_student()
        elif choice == '6':
            generate_placement_reports()
        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

main()