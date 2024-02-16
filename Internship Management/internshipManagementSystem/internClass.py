class Intern:
    def __init__(self, id, name, email, skills):
        self.intern_id = id
        self.name = name
        self.email = email
        self.skills = skills
        self.project = None

    def getDetails(self):
        print(f"employee id: {self.id}, Name. {self.name}, email: {self.email}, skills: {self.skills}")

    def updateSkills(self, skills):
        self.skills = skills