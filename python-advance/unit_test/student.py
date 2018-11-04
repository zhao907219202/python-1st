"""
exercise:
    another test unit example
"""


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score < 0 or self.score > 100:
            raise ValueError("student score must be >=0 and <=100")

        if 60 <= self.score < 80:
            return 'B'

        if self.score >= 80:
            return 'A'
        return 'C'
