import random
from employee import Employee

class ConversionManager:

    def evaluate_performance(self, intern, performance_needed):
        rating = round(random.uniform(3.5, 4.5), 2)
        intern.performance_rating = rating
        if intern.performance_rating > performance_needed:
            intern.set_conversion_status('Approved')
        else:
            intern.set_conversion_status('Rejected')

    def convert_to_employee(self, intern):
        if intern.conversion_status == 'Approved':
            employee = Employee(intern.intern_id, intern.name, intern.email, intern.skills)
            employee.set_designation('Full-Time Employee')
            return employee
        else:
            raise Exception("Conversion not approved")

