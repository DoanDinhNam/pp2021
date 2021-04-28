import curses
from output import outputs
from input import inputs
from domain.Student import *
from domain.Course import *
from domain.Mark import *


py = curses.initscr()
curses.start_color()

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
