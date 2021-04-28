import math
import curses
import numpy as np
from domain.Student import *
from domain.Course import *
from domain.Mark import *

py = curses.initscr()
curses.start_color()

class inputs():
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
