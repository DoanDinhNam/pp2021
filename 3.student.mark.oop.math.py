# Create all list to contain object
import math
import numpy as np

# Student management
Student = []
StudentID = []
Course = []
CourseID = []
Mark = []
Credit = []
gpa_s = []

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


class Marks:
    def __init__(self, a, b, mark, Gpa=1):
        self._a = a
        self._b = b
        self._mark = mark
        Mark.append(self)

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def get_mark(self):
        return self.mark

    def set_GPa(self, Gpa=10):
        self.Gpa = Gpa


# Function input of number of student
def numberofstudent():
    student_class = int(input("Enter the number of student:"))
    if (student_class <= 0):
        print("Doesn't exits")
        return 'False'
    else:
        return student_class

def add_student_infor():
    print(" Student Infor ")

    id = input("Enter the ID:")
    name = input("Enter the student name:")
    dob = input("Enter the dob student:")
    st_infor = {
        'id': id,
        'name': name,
        'dob': dob
    }
    StudentID.append(id)
    Student.append(st_infor)


# Function to input number of course
def number_course():
    print(" Number of Course ")
    number_course = int(input("Enter the number of course :"))
    if (number_course <= 0):
        print("Doesn't exits")
        return 0
    else:
        return number_course


# Function to add course
def add_course():
    name = input("Enter the name course:")
    id = input("Enten the ID course: ")
    cd = input("Enter the credits are:")
    course_f = {
        'cd': cd,
        'name': name,
        'id': id
    }
    Course.append(course_f)
    CourseID.append(id)


# Mark function
def mark_mana():
    g = 1
    tu = len(Student)
    while g <= tu:
        g += 1
        a = input("Enter the ID Student: ")
        if a in StudentID:
            for i in range(0, len(Course)):
                b = input("Enter the ID Course: ")
                if b in CourseID:
                    mark = math.floor(float(input("Enter mark of Student: ")))
                    kk = {
                        'a': a,
                        'b': b,
                        'mark': mark

                    }
                else:
                    print("False ID Student")
                    break
                Mark.append(kk)

        else:
            print("False ID course")
            break


def aver_gpa(self):
    print(" Aver Gpa ")
    value = np.array([self.mark])
    cre = np.array([self.credit])
    ol = input("Enter the ID student:")
    if ol in self.id:
        for i in range(len(Mark)):
            gpa = value[i] / cre[i]
            return gpa
    print(gpa)


def calculate_mark(self):
    print("=====GPA FIND ======")
    id_a = input("Enter the ID:")
    if id_a in self.id:
        marks = input("Enter the mark:")
    Mark.append(marks)

    cre_value = [Credit]
    mark_val = [Mark]
    name_again = input(" Enter the name of student: ")
    gpa = mark_val / cre_value
    return gpa

# Function to show all of student in class
def show_student():
    print(" List of student ")
    for i in range(0, len(Student)):
        print(f"ID:{Student[i]['id']} name:{Student[i]['name']} DoB:{Student[i]['dob']}")

def show_course():
    print(" List course ")
    for i in range(0, len(Course)):
        print(f"ID:{Course[i]['id']}  Name :{Course[i]['name']} Credits:{Course[i]['cd']}")

def show_mark():
    print(" List mark ")
    for i in range(0, len(Mark)):
        print(f"ID-course: {Mark[i]['b']} ID-Student: {Mark[i]['a']}  mark:{Mark[i]['mark']}")


# Function to show the GPA of Student
def GPA_decending():
    arr = np.array([gpa_s])
    arr[::-1].sort()
    print("=====LIST====")
    print("The list is %s:\n" % (arr))

# Main function
s = int(numberofstudent())
l = 1
while l <= s:
    l += 1
    add_student_infor()
show_student()
c = int(number_course())
p = 1
while p <= c:
    p += 1
    add_course()
show_course()
mark_mana()

print("  Choose  ")
print("1.YES")
print("2.NO")
for i in range(0, len(Course)):
    ol = int(input(" Enter your choose: "))
    if ol == 1:
        print(" Mark of the student ")
        show_mark()
        break 
    else:
        break
l = aver_gpa()
l.getaver_gpa()
calculate_mark()
