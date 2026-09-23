#This is the predefined password that works for all the students
COMMON_PASSWORD="Student123"
#Below here are the predefined data for 10 students
names=[
    "Riya",
    "Priya",
    "Ram",
    "Shayam",
    "Ritu",
    "Rahul",
    "Mohit",
    "Rohit",
    "Vikas",
    "Vikram"
]
attendance_list = [88,75,68,99,76,66,87,78,64,79]
marks_list = [72,45,67,79,88,95,36,68,88,82]
#Login System
print("WELCOME TO STUDENT PORTAL ")
#Student enters their name and the common password
enter_name = input("Enter your name")
enter_password = input("Enter your password")
#Checking if the password is correct
if enter_password!=COMMON_PASSWORD:
    print("\n LOGIN FAILED!")
else:
    student_index=-1
    for i in range (10):
        if names[i].lower()==enter_name.lower():
            student_index=i
            break

    if student_index==-1:
        print("\n LOGIN FAILED ! Student name not found ")
    else:
        print("\n LOGIN SUCCESSFUL ! Welcome " , names[student_index])
#Get Students current data
        student_name=names[student_index]
        student_attendance=attendance_list[student_index]
        student_marks =marks_list[student_index]
        print("Name :", student_name)
        print("Attendance :", student_attendance)
        print("Marks :", student_marks)
#Calculate class average
        total_students= len(names)
        total_marks=0
        for i in range (total_students):
            total_marks=total_marks+marks_list[i]
            class_avg_marks = total_marks/total_students
        print("Class Average Marks :", class_avg_marks)
#Calculate average attendance
        total_attendance=0
        for i in range (total_students):
            total_attendance=total_attendance+attendance_list[i]
            class_avg_attendance=total_attendance/total_students
        print("Class Average Attendance :", class_avg_attendance)
#Grade Predictor
#In Grade Predictor Calculation : 70% weight on marks + 30% weight on attendance
        predicted_score = ( student_marks * 0.7 ) + (student_attendance * 0.3)

        if predicted_score >= 90:
            predicted_grade = "A+"
        elif predicted_score >= 80:
            predicted_grade = "A"
        elif predicted_score >= 70:
            predicted_grade = "B"
        elif predicted_score >= 60:
            predicted_grade = "C"
        elif predicted_score >= 50:
            predicted_grade = "D"
        else:
            predicted_grade = "F"
        print("Grade :",predicted_grade)

# Attendance vs Performance correlation
        print("\n[ATTENDANCE vs PERFORMANCE ANALYSIS]")
        if student_attendance >=85 and student_marks >=75:
            print("-correlation : Strong positive relation !")
            print ("-Analysis : Your high attendance directly matches your high marks")
        elif student_attendance >=85 and student_marks < 75:
            print("-correlation : High attendance but low marks ")
            print("-Analysis : You attend classes regularly, but you need to improve exam technique")
        elif student_attendance < 75  and student_marks >= 75:
            print("-correlation : High marks but low attendance  ")
            print("-Analysis : You understand concepts well, but missing classes risks attendance penalties")
        else:
            print("-correlation : Low attendance and Low marks ")
            print("- Analysis : Missing classes is directly impacting your overall score ")
#Display academic report
        print ( "        ACADEMIC REPORT        ")
        print ("Student Name : ", student_name)
        print ("Attendance Percentage  : ", student_attendance , "%")
        print ("Current Marks : " ,student_marks , "/100" )
        print ("Predicted Final Score : " , round(predicted_score,2) , "/100")
        print ("Predicted Final Grade : " , predicted_grade)
        print ("Class Average Marks : " , round(class_avg_marks,2) , "/100")
        print ("Class Average Attendance : " , round(class_avg_attendance,2) , "%")
#Marks Advice vs Class Average
        if student_marks < class_avg_marks:
            print("Your score is below the class average . Focus on weak topics and revise daily ")
        elif student_marks == class_avg_marks:
            print("Your score is right at the class average . Work a bit harder to reach A grade")
        else:
            print("Great Work ! Your score is above the average")
#Attendance Advice
        print("\n PERSONALIZED ADVICE ")
        if student_attendance < 75:
            print("Attendance Warning : Below 75% . Try not to miss any upcoming class")
        else:
            print("Attendance : Great job keep your attendance High !")





