from conversionManager import ConversionManager
from intern import Intern

class InternshipManagementSystem:

    def __init__(self):
        self.interns = []
        self.employees = []
        self.conversion_manager = ConversionManager()

    def add_intern(self):
        # name, email, skills, performance_rating):
        name = input("enter the name of the intern ")
        email = input("enter the email of the intern ")
        skills = input("enter the skills of the intern ")
        intern = Intern(len(self.interns)+1, name, email, skills)
        self.interns.append(intern)

    def simulate_conversion_process(self, performance_needed):
        for intern in self.interns:
            self.conversion_manager.evaluate_performance(intern, performance_needed)
            try:
                employee = self.conversion_manager.convert_to_employee(intern)
                self.employees.append(employee)
            except Exception as e:
                print(f"Conversion failed: {e} for {intern.name}")

    def display_interns(self):
        for intern in self.interns:
            intern.display_details()

    def display_employees(self):
        for employee in self.employees:
            employee.display_details()