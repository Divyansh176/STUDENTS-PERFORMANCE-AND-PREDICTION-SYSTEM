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

def get_student_data(student_index):
    student_name=names[student_index]
    student_attendance=attendance_list[student_index]
    student_marks=marks_list[student_index]

    return student_name,student_attendance,student_marks

def calculate_class_averages():
    total_students=len(names)
    total_marks=sum(marks_list)
    class_avg_marks=total_marks/total_students
    total_attendance=sum(attendance_list)
    class_avg_attendance=total_attendance/total_students
    return class_avg_attendance,class_avg_marks