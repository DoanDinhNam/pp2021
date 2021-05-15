import numpy as np
import curses
from domain.Student import *
from domain.Course import *
from domain.Mark import *

py = curses.initscr()
curses.start_color()


class outputs():
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