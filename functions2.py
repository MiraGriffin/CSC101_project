from classes import Student, Class
#List of all the students. The "assignment" characteristic is a dictionary.
students = [Student('Sally', 101,
                    {'quiz 1':87, 'test 1':90, 'quiz 2': 83},
                    86.67,
                    {'Fall 2024': [Class('Bio 101', 85, ),
                                                Class('Engl 147', 92, ),
                                                Class('Csc 101', 100, )],
                                'Winter 2024': [Class('Calc 1', 75, ),
                                                Class('Coms 101', 86, )],
                                'Spring 2024': [Class('Stat 301', 94, ),
                                                Class('Calc 2', 78, ),
                                                Class('RPTA', 97, )]}, 3.25),
            Student('Ben', 102,
                    {'quiz 1':67, 'test 1':73, 'quiz 2': 80},
                    73.33,
                    {'Fall 2024': [Class('Bio 101', 75, ),
                                                Class('Calc 3', 68, ),
                                                Class('Csc 101', 78, )],
                                'Winter 2024': [Class('Calc 4', 73, ),
                                                Class('Coms 101', 90, )],
                                'Spring 2024': [Class('Stat 150', 70, ),
                                                Class('Math 206', 81, ),
                                                Class('BUS 101', 79, )]}, 2.25),
            Student('Jake', 103,
                    {'quiz 1': 99, 'test 1': 92, 'quiz 2': 94},
                    95.0,
                    {'Fall 2024': [Class('Calc 1', 84, ),
                                                Class('BUS 217', 98, ),
                                                Class('Csc 202', 88, )],
                                'Winter 2024': [Class('Calc 2', 89, ),
                                                Class('Coms 101', 99, )],
                                'Spring 2024': [Class('Stat 331', 92, ),
                                                Class('Calc 3', 81, ),
                                                Class('BUS 101', 98, )]}, 3.5),

            Student('Emma', 104,
                    {'quiz 1': 89, 'test 1': 94, 'quiz 2': 86},
                    89.67,
                    {'Fall 2024': [Class('Calc 3', 82, ),
                                                Class('BUS 101', 93, ),
                                                Class('Csc 101', 98, )],
                                'Winter 2024': [Class('Calc 4', 84, ),
                                                Class('Stat 150', 94, )],
                                'Spring 2024': [Class('Bio 303', 85, ),
                                                Class('Calc 4', 83, ),
                                                Class('Stat 217', 88, )]}, 3.375),

            Student('Emma', 105,
                    {'quiz 1': 89, 'test 1': 94, 'quiz 2': 86},
                    89.67,
                    {'Fall 2024': [Class('Pre Calc', 92, ),
                                                Class('BUS 101', 88, ),
                                                Class('Csc 202', 85, )],
                                'Winter 2024': [Class('Calc 1', 90, ),
                                                Class('Stat 217', 87, )],
                                'Spring 2024': [Class('Bio 101', 92, ),
                                                Class('Calc 2', 89, ),
                                                Class('Coms 101', 98, )]}, 3.5),
            Student('Kacy', 104,
                    {'quiz 1': 90, 'test 1': 92, 'quiz 2': 89},
                    90.33,
                    {'Fall 2024': [Class('Calc 1', 87, ),
                                                Class('BUS 301', 78, ),
                                                Class('Bio 101', 92, )],
                                'Winter 2024': [Class('Calc 2', 87, ),
                                                Class('Stat 150', 97, )],
                                'Spring 2024': [Class('Csc 202', 72, ),
                                                Class('Calc 3', 89, ),
                                                Class('Coms 101', 88, )]}, 3.0)
            ]
#This function prompts the user to enter a name.
# The function will then find the students name in the list,
# if the students name is not in the list then it will tell the user.
#The input is a list of students.
#The return type is none. This is not super useful on its own but we will use this function
#later when it is apart of a larger function.
def find_student(students: list[Student]) -> None:
    student = input("Student Name: ")
    student_names = []
    for stud in students:
        student_names.append(stud.name)
    if student not in student_names:
        print('Student not found, please try another name')

#This function is still in progress. We have not finsihed it.
#This function will grade a students test by opening the txt file and reading it.
#The function then will compare the answers to the key and grade the test.
#The function takes no arguments (we will use input and find student) and returns a list of students.
def grade_test() -> list[str]:
    answers = []
    try:
        with open("sally_test.txt", 'r') as test:
            for line in test:
                line = line.strip()
                if line.startswith("Question"):
                    chars = line.split()
                answers.append(chars[-1])
    except FileNotFoundError as e:
        print(e)
    return answers

def grade_test_2():
    name = input("Enter student name:")
    student_file = "{}_test.txt".format(name)
    key = "test_key.txt"
    try:
        with open(key,'r') as x:
            key_lines = x.readlines()
        key_answers = []
        for line in key_lines:
            if "Question" in line and "Answer:" in line:
                parts = line.strip().split("Answer:")
                if len(parts)==2:
                    key_answers.append(parts[1].strip())
        with open(student_file, 'r') as x:
            student_lines = x.readlines()
        student_answers = []
        for line in student_lines:
            if "Question" in line and "Answer:" in line:
                parts = line.strip().split("Answer:")
                if len(parts) == 2:
                    student_answers.append(parts[1].strip())
        correct_count = 0
        total_questions = len(key_answers)
        for x in range(min(len(key_answers),len(student_answers))):
            if student_answers[x] == key_answers[x]:
                correct_count +=1
        score = (correct_count/total_questions)*100
        print("{}'s score:{}%".format(name,round(score,2)))
    except FileNotFoundError as e:
        print(e)


#This function calculates the overall GPA of a student that is given by the user once prompted.
#The function takes the 0-100 grade and turns it into a 4.0 grading scale
#the input is a list of students and the output is None.
def overall_gpa_calc(students: list[Student]) -> None:
    name = input("Enter student name: ")
    for student in students:
        if student.name.lower() == name.lower():
            total_points = 0
            total_classes = 0
            for quarter in student.quarter_grades.values():
                for course in quarter:
                    grade = course.grade
                    if grade >= 90:
                        points = 4.0
                    elif grade >= 80:
                        points = 3.0
                    elif grade >= 70:
                        points = 2.0
                    elif grade >= 60:
                        points = 1.0
                    else:
                        points = 0.0
                    total_points += points
                    total_classes += 1
            if total_classes == 0:
                print("No classes found for GPA calculation.")
                return
            gpa = total_points / total_classes
            student.gpa = round(gpa, 2)
            print(f"{student.name}'s GPA: {student.gpa}")
            return

    print("Student not found.")

#This function is similar to the one above, however it calculate the GPA by quarter.
#The user will be prompted to input a students name and a quarter
#The function will then find the student and their grades for the specified quarter and calculate the GPA
#The input is a list of students and the output is None.
def quarter_gpa_calc(students: list[Student]) -> None:
    name = input("Enter student name: ")
    quarter = input("Enter quarter (Example:Fall 2024): ")
    for student in students:
        if student.name.lower() == name.lower():
            if quarter not in student.quarter_grades:
                print(f"{quarter} not found for {student.name}.")
                return
            courses = student.quarter_grades[quarter]
            if not courses:
                print(f"No courses in {quarter} for {student.name}.")
                return
            total_points = 0
            total_classes = 0
            for course in courses:
                grade = course.grade
                if grade >= 90:
                    points = 4.0
                elif grade >= 80:
                    points = 3.0
                elif grade >= 70:
                    points = 2.0
                elif grade >= 60:
                    points = 1.0
                else:
                    points = 0.0
                total_points += points
                total_classes += 1
            gpa = total_points / total_classes
            print(f"{student.name}'s GPA for {quarter}: {round(gpa, 2)}")
            return
    print("Student not found.")

def letter_grades(grade:float)->str:
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'
def get_letter_grades(student: Student) -> dict:
    grades = {}
    for quarter, class_list in student.quarter_grades.items():
        grades[quarter] = {}
        for cls in class_list:
            grades[quarter][cls.name] = letter_grades(cls.grade)
    return grades
print(get_letter_grades(students[0]))







