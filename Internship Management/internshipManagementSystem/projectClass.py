class Project:
    def __init__(self, id, title, description):
        self.project_id = id
        self.title = title
        self.description = description
        self.assignedIntern = None # this woulbe the object of the intern class
        self.level = "started" # 4 levels: started, halfway, almost done, done

    def getIntern(self, intern):
        self.assignedIntern = intern
        intern.project = self.project_id

    def projectDetails(self):
        print(f"project id: {self.project_id}, title: {self.title}, description: {self.description}, assigned intern: {self.assignedIntern}")

    def updateProgress(self, level):
        self.level = level
