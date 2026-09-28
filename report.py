def generate_report(
        student_name,
        student_attendance,
        student_marks,
        predicted_score,
        predicted_grade,
        class_avg_marks,
        class_avg_attendance
):
    print("        ACADEMIC REPORT        ")
    print("Student Name : ", student_name)
    print("Attendance Percentage  : ", student_attendance, "%")
    print("Current Marks : ", student_marks, "/100")
    print("Predicted Final Score : ", round(predicted_score, 2), "/100")
    print("Predicted Final Grade : ", predicted_grade)
    print("Class Average Marks : ", round(class_avg_marks, 2), "/100")
    print("Class Average Attendance : ", round(class_avg_attendance, 2), "%")


    if student_marks < class_avg_marks:
        print("Your score is below the class average . Focus on weak topics and revise daily ")
    elif student_marks == class_avg_marks:
        print("Your score is right at the class average . Work a bit harder to reach A grade")
    else:
        print("Great Work ! Your score is above the average")

    print("\n PERSONALIZED ADVICE ")

    if student_attendance < 75:
        print("Attendance Warning : Below 75% . Try not to miss any upcoming class")
    else:
        print("Attendance : Great job keep your attendance High !")