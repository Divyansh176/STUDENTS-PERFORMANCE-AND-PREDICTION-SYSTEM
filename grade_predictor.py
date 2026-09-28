def predict_grade(student_marks,student_attendance):
    predicted_score = (student_marks * 0.7) + (student_attendance * 0.3)
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
    return predicted_score,predicted_grade