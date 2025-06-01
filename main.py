from classes import Student, Class

students = [Student('Sally', 101,
                    {'quiz 1':87, 'test 1':90, 'quiz 2': 83},
                    86.67,
                    {'Fall 2024': [Class('Bio 101', 85, ''),
                                                Class('Engl 147', 92, ''),
                                                Class('Csc 101', 100, '')],
                                'Winter 2024': [Class('Calc 1', 75, ''),
                                                Class('Coms 101', 86, '')],
                                'Spring 2024': [Class('Stat 301', 94, ''),
                                                Class('Calc 2', 78, ''),
                                                Class('RPTA', 97, '')]}, 3.25),
            Student('Ben', 102,
                    {'quiz 1':67, 'test 1':73, 'quiz 2': 80},
                    73.33,
                    {'Fall 2024': [Class('Bio 101', 75, ''),
                                                Class('Calc 3', 68, ''),
                                                Class('Csc 101', 78, '')],
                                'Winter 2024': [Class('Calc 4', 73, ''),
                                                Class('Coms 101', 90, '')],
                                'Spring 2024': [Class('Stat 150', 70, ''),
                                                Class('Math 206', 81, ''),
                                                Class('BUS 101', 79, '')]}, 2.25),
            Student('Jake', 103,
                    {'quiz 1': 99, 'test 1': 92, 'quiz 2': 94},
                    95.0,
                    {'Fall 2024': [Class('Calc 1', 84, ''),
                                                Class('BUS 217', 98, ''),
                                                Class('Csc 202', 88, '')],
                                'Winter 2024': [Class('Calc 2', 89, ''),
                                                Class('Coms 101', 99, '')],
                                'Spring 2024': [Class('Stat 331', 92, ''),
                                                Class('Calc 3', 81, ''),
                                                Class('BUS 101', 98, '')]}, 3.5),

            Student('Emma', 104,
                    {'quiz 1': 89, 'test 1': 94, 'quiz 2': 86},
                    89.67,
                    {'Fall 2024': [Class('Calc 3', 82, ''),
                                                Class('BUS 101', 93, ''),
                                                Class('Csc 101', 98, '')],
                                'Winter 2024': [Class('Calc 4', 84, ''),
                                                Class('Stat 150', 94, '')],
                                'Spring 2024': [Class('Bio 303', 85, ''),
                                                Class('Calc 4', 83, ''),
                                                Class('Stat 217', 88, '')]}, 3.375),

            Student('Emma', 105,
                    {'quiz 1': 89, 'test 1': 94, 'quiz 2': 86},
                    89.67,
                    {'Fall 2024': [Class('Pre Calc', 92, ''),
                                                Class('BUS 101', 88, ''),
                                                Class('Csc 202', 85, '')],
                                'Winter 2024': [Class('Calc 1', 90, ''),
                                                Class('Stat 217', 87, '')],
                                'Spring 2024': [Class('Bio 101', 92, ''),
                                                Class('Calc 2', 89, ''),
                                                Class('Coms 101', 98, '')]}, 3.5),
            Student('Kacy', 104,
                    {'quiz 1': 90, 'test 1': 92, 'quiz 2': 89},
                    90.33,
                    {'Fall 2024': [Class('Calc 1', 87, ''),
                                                Class('BUS 301', 78, ''),
                                                Class('Bio 101', 92, '')],
                                'Winter 2024': [Class('Calc 2', 87, ''),
                                                Class('Stat 150', 97, '')],
                                'Spring 2024': [Class('Csc 202', 72, ''),
                                                Class('Calc 3', 89, ''),
                                                Class('Coms 101', 88, '')]}, 3.0)
            ]

def find_student(students: list[Student]) -> None:
    student = input("Student Name: ")
    student_names = []
    for stud in students:
        student_names.append(stud.name)
    if student not in student_names:
        print('Student not found, please try another name')

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

print(grade_test)

