# Create all list to contain object
Student = []
Id = []
Courses = []
Marks = []


class Student(object):
    def __init__(self, name, id, marks, courses):
        self.name = name
        self.id = id
        self.marks = marks
        self.courses = courses

    def getmarks(self):
        return self.marks

    def getid(self):
        return self.id

    def getcourses(self):
        return self.courses

    def __str__(self):
        return self.name + ' : ' + str(self.getid()) + ' :' + str(self.getmarks() + ':' + str(self.getcourses()))


def Markss(rec, name, id, marks, courses):
    rec.append(Student(name, id, marks, courses))
    return rec


# Main Code
Record = []
x = 'y'
while x == 'y':
    a = input('Enter the name of the student: ')
    b = input('Enter the student id: ')
    c = input('Enter the name of course:')
    d = input('Marks: ')
    Record = Markss(Record,a ,b ,c ,d )
    x = input('another student? y/n: ')

# Printing the list of student
n = 1
for el in Record:
    print(n, '. ', el)
    n = n + 1 
