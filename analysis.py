def attendance_performance_analysis(student_attendance,student_marks):
    print("\n[ATTENDANCE vs PERFORMANCE ANALYSIS]")
    if student_attendance >= 85 and student_marks >= 75:
        print("-correlation : Strong positive relation !")
        print("-Analysis : Your high attendance directly matches your high marks")
    elif student_attendance >= 85 and student_marks < 75:
        print("-correlation : High attendance but low marks ")
        print("-Analysis : You attend classes regularly, but you need to improve exam technique")
    elif student_attendance < 75 and student_marks >= 75:
        print("-correlation : High marks but low attendance  ")
        print("-Analysis : You understand concepts well, but missing classes risks attendance penalties")
    else:
        print("-correlation : Low attendance and Low marks ")
        print("- Analysis : Missing classes is directly impacting your overall score ")