Student = []
StudentID = []

class Students:
    def __init__(self, id, name, dob):
        self.Studentid = id
        self.Studentname = name
        self.dob = dob
        Student.append(self)
        StudentID.append(self.Studentid)

    def get_id(self):
        return self.Studentid

    def get_name(self):
        return self.Studentname

    def get_dob(self):
        return self.dob