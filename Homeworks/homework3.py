# Course Grade Application

# Create 5 students. Ask these students from the user.
# I created a dictionary with 5 students and every student has a list as their value to store the grades.

studentDict = {"firstStudent": {"midterm": 0, "project": 0, "final": 0, "passingGrade": 0},
               "secondStudent": {"midterm": 0, "project": 0, "final": 0, "passingGrade": 0},
               "thirdStudent": {"midterm": 0, "project": 0, "final": 0, "passingGrade": 0},
               "fourthStudent": {"midterm": 0, "project": 0, "final": 0, "passingGrade": 0},
               "fifthStudent": {"midterm": 0, "project": 0, "final": 0, "passingGrade": 0}}

for students, exams in studentDict.items():
    for grades in exams:
        if grades == "passingGrade":
            continue
        exams[grades] = float(
            input(students + " please enter your " + grades + " score: "))

# Each of these students should have a midterm grade, project grade and final grade
# Each student will have a course passing grade.
# passingGrade = midterm * 0.3 + project * 0.3 + final * 0.4 passing should be determined like this.

# Create a dictionary to keep these students' information.
# Calculate the students' grades and transfer them to the list with the help of indexing.

gradeList = []

for students, exams in studentDict.items():
    exams["passingGrade"] = "{:.2f}".format(
        (exams["midterm"] * 0.3) + (exams["project"] * 0.3) + (exams["final"] * 0.4))

    gradeList.append(exams["passingGrade"])

# Finally, set the student with the highest grade to be in the first index
# and student with the lowest grade to be in the last index of the list.

gradeList = sorted(gradeList, key=float, reverse=True)
