class Employee:
    def __init__(self, employee_id, name, email, skills):
        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.skills = skills
        self.designation = 'Intern'

    def display_details(self):
        print("\n")
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Skills: {self.skills}")
        print(f"Designation: {self.designation}")

    def update_skills(self, new_skills):
        self.skills.extend(new_skills)

    def set_designation(self, new_designation):
        self.designation = new_designation