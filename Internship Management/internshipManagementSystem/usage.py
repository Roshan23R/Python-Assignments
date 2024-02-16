from internshipClass import Internship

internship = Internship()

print("1. Add intern")
print("2. Add project")
print("3. Assign interns")
print("4. get intern info")
print("5. get project info")
print("6. Track projects")
print("7. Overall info")
print("8: update project status: started, completed, mid-way")
print("9. Exit")

while True:

    num = int(input("Enter your choice "))

    if num == 1:
        internship.onboarding()

    elif num == 2:
        internship.addProject()

    elif num == 3:
        internship.assignIntern()
    
    elif num == 4:
        id = int(input("enter the intern id to get info "))
        internship.internInfo(id)

    elif num == 5:
        id = int(input("enter the project id to get info "))
        internship.projectInfo(id)
        
    elif num == 6:
        internship.trackProjects()
        
    elif num == 7:
        internship.overallInfo()

    elif num == 8:
        pid = int(input("enter the project id to update info "))
        iid = int(input("enter your id "))
        internship.updateProjectStatus(pid, iid)

    else:
        print("exited the program")
        break
