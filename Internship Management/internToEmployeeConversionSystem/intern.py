class Intern:
    def __init__(self, intern_id, name, email, skills):
        self.intern_id = intern_id
        self.name = name
        self.email = email
        self.skills = skills
        self.performance_rating = None
        self.conversion_status = None

    def display_details(self):
        print("\n")
        print(f"Intern ID: {self.intern_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Skills: {self.skills}")
        print(f"Performance Rating: {self.performance_rating}")
        print(f"Conversion Status: {self.conversion_status or 'Not decided'}")

    def update_skills(self, new_skills):
        self.skills.extend(new_skills)

    def set_conversion_status(self, status):
        self.conversion_status = status

