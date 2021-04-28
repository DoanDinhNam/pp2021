from Python.Lab3Nam import Credit

Course = []
CourseID = []



class Courses:
    def __init__(self, id, name, credits):
        self.Courseid = id
        self.Coursename = name
        self.credits = credits
        Course.append(self)
        CourseID.append(self.Courseid)
        Credit.append(self.credits)

    def get_id(self):
        return self.Courseid

    def get_name(self):
        return self.Coursename

    def get_credit(self):
        return self.credits