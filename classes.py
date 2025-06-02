class Student:
    def __init__(self, name:str, id:int, assignments:dict,
                 overall:float, quarter_grades:dict, gpa:float):
        self.name = name
        self.id = id
        self.assignments = assignments
        self.overall = overall
        self.quarter_grades = quarter_grades
        self.gpa = gpa
    def __repr__(self):
        return ("Name: {}, Student ID: {}, Grades by Assignment: {}, Overall Grade: {}, Grades by Quarter: {}, GPA: {}"
                .format(self.name,self.id,self.assignments,self.overall,self.quarter,self.gpa))
    def __str__(self):
        return(("Name: {}, Student ID: {}, Grades by Assignment: {}, Overall Grade: {}, Grades by Quarter: {}, GPA: {}"
                .format(self.name,self.id,self.assignments,self.overall,self.quarter,self.gpa)))
    def __eq__(self, other):
        return (self is other or
                type(other) == Student and
                self.name == other.name and
                self.id == other.id and
                self.assignments == other.assignments and
                self.overall == other.overall and
                self.quarter == other.quarter and
                self.gpa == other.gpa)

class Class:
    def __init__(self, name:str, grade:int, quarter_taken:str):
        self.name = name
        self.grade = grade
        self.quarter_taken = quarter_taken
    def __repr__(self):
        return "Class: {}, Grade: {}, Quarter Taken: {}".format(self.name,self.grade,self.quarter_taken)
    def __str__(self):
        return "Class: {}, Grade: {}, Quarter Taken: {}".format(self.name, self.grade, self.quarter_taken)
    def __eq__(self, other):
        return  (self is other or type(other)==Class and
                 self.name == other.name and
                 self.grade == other.grade and
                 self.quarter_taken == other.quarter_taken)

class TestGrade:
    def __innit__(self, name:str, grade:int):
        self.name = name
        self.grade = grade
    def __repr__(self):
        return "Test: {}, Grade: {}", format(self.name, self.grade)
    def __str__(self):
        return "Test: {}, Grade: {}", format(self.name, self.grade)
    def __eq__(self, other):
        return  (self is other or type(other)==Class and
                 self.name == other.name and
                 self.grade == other.grade)