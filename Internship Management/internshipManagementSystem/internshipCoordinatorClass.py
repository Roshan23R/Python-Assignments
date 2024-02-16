from projectClass import Project
from internClass import Intern

import random

class InternshipCoordinator:
    project_id = 0
    intern_id = 0

    def __init__(self):
        self.projects = []
        self.interns = []

    def addProject(self, title, description):
        project1 = Project(InternshipCoordinator.project_id, title, description)
        self.projects.append(project1)
        InternshipCoordinator.project_id +=1 
    
    def addIntern(self, name, email, skills):
        intern1 = Intern(InternshipCoordinator.intern_id, name, email, skills)
        self.interns.append(intern1)
        InternshipCoordinator.intern_id +=1 

    def assignIntern(self):
        # print("assigning interns to projects")
        # if len(self.projects) > len(self.interns):
        #     print("need more interns as projects are more")

        # shuffled_interns = self.interns.copy()
        # random.shuffle(shuffled_interns)
        # shuffled_projects = self.projects.copy()
        # random.shuffle(shuffled_projects)
        # for intern, project in zip(shuffled_interns, shuffled_projects):
        #     project.getIntern(intern)

        pid = int(input("enter the project id to assign to an employee: "))
        iid = int(input("enter the intern id to assign to the project id mentioned above: "))

        temProject = None
        temIntern = None

        for project in self.projects:
            if project.project_id == pid:
                if project.assignedIntern != None:
                    print(f"project already assigned to intern with id {project.intern.intern_id}")
                    return
                else:
                    temProject = project
        
        for intern in self.interns:
            if intern.project != None:
                print("already assigned with project with id {intern.project}")
                return
            else:
                temIntern = intern

        temProject.getIntern(temIntern)
        
        
                    