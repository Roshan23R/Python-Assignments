from internshipCoordinatorClass import InternshipCoordinator


class Internship:
    
    def __init__(self):
        self.coordinator = InternshipCoordinator()
    
    def onboarding(self):
        name = input("enter the name of the intern ")
        email = input("enter the email of the intern ")
        skills = input("enter the skills of the intern ")
        self.coordinator.addIntern(name, email, skills)
        print("added info of the intern successfully")

    def addProject(self):
        title = input("enter the title of the project ")
        description = input("enter the description of the project ")
        self.coordinator.addProject(title, description)
        print("added info of the project successfully")

    def assignIntern(self):
        self.coordinator.assignIntern()
        print("Assigned interns to projects successfully.")

    
    def trackProjects(self):
        for project in self.coordinator.projects:
            # project object
            print(f"project id: {project.project_id} is {project.level}")

    def overallInfo(self):
        for project in self.coordinator.projects:
            print(f"project id: {project.project_id} title: {project.title},  description: {project.description} is assigned to intern with id:{project.assignedIntern.intern_id} and by name: {project.assignedIntern.name} is {project.level}")

    def internInfo(self, id):
        flag = False
        for intern in self.coordinator.interns:
            if intern.intern_id == id:
                print(f"intern id: {intern.intern_id}, name: {intern.name}, email: {intern.email}, skills: {intern.skills}, project id: {intern.project}")
                flag = True

        if not flag:
            print("no intern with this id")


    def projectInfo(self, id):
        flag = False
        for project in self.coordinator.projects:
            if project.project_id == id:
                print(f"project id: {project.project_id}, title: {project.title}, description: {project.description}, assigned intern: {project.assignedIntern.name}")
                flag = True

        if not flag:
            print("no project with this id")

    def updateProjectStatus(self, pid, iid):
        for project in self.coordinator.projects:
            if project.project_id == pid:
                if project.assignedIntern.intern_id != iid:
                    print("you are not allowed to change as you are not assigned to this project")
                else:
                    project.level = input("enter the current status of the project ")
                    print("updated project current status")