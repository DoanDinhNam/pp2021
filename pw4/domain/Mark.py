Mark = []
Mark_marks = []



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