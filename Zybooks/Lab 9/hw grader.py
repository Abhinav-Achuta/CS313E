HOMEWORK_MAX = 800.0
QUIZZES_MAX = 400.0
MIDTERM_MAX = 150.0
FINAL_MAX = 200.0

# Type your code here.
def grade_output(status, grades): #Check if is student
    if is_student(status):
        grades_list = list(grades.split())
        return (print_grades(grades_list, status)) #Returns grades list after calculating
    else:
        return "Error: student status must be UG, G or DL"

def is_student(status):
    return status in ["UG", "G", "DL"]
    
def print_grades(grades, status):
    homework_maxes = [HOMEWORK_MAX, QUIZZES_MAX, MIDTERM_MAX, FINAL_MAX]
    grade_types = ["Homework", "Quizzes", "Midterm", "Final Exam"]
    raw_grades = []
    homework_text = []

    if len(grades) != len(homework_maxes):
        return ["Error: Insufficient grades provided"]

    for i in range(len(grades)):
        grade = float(grades[i])

        max = homework_maxes[i]
        current_grade = (grade / max) * 100
        
        if current_grade > 100:
            current_grade = 100.0
        raw_grades.append(current_grade)
        homework_text.append(f"{grade_types[i]}: {current_grade:2.1f}%")

    final_grades = grades_per_status(status, raw_grades) #Calculate final grade based on status and rawgrades

    homework_text.append(final_grades["grade_text"][0])
    homework_text.append(final_grades["letter_average"][0])
    return "\n".join(homework_text)

def grades_per_status(status, grades):
    weights = {
        "UG": (.2, .2, .3, .3),
        "G" : (.15, .05, .35, .45),
        "DL": (.05, .05, .4, .5),
    }

    grades_key = {
        "number_value": [],
        "grade_text": [],
        "letter_average": [],
    }

    if status in weights:
        weighted_grades = [grades[i]*weights[status][i] for i in range(len(grades))]
        grade_total = sum(weighted_grades)

        grades_key["number_value"].append(grade_total)
        grades_key["grade_text"].append(f"{status} average: {grade_total:.1f}%")

        if grades_key["number_value"][0] < 60.0:
            grades_key["letter_average"].append("Course grade: F")
        elif 60.0 <= grades_key["number_value"][0] < 70.0:
            grades_key["letter_average"].append("Course grade: D")
        elif 70.0 <= grades_key["number_value"][0] < 80.0:
            grades_key["letter_average"].append("Course grade: C")
        elif 80.0 <= grades_key["number_value"][0] < 90.0:
            grades_key["letter_average"].append("Course grade: B")
        elif 90.0 <= grades_key["number_value"][0]:
            grades_key["letter_average"].append("Course grade: A")

        return grades_key

def main():
    student_status = input("") #Student status
    student_grades = input("") #Grades

    grades = grade_output(student_status, student_grades)

    print(grades)
    
if __name__ == "__main__":
    main()