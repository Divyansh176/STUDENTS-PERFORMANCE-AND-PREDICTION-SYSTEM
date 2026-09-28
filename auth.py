COMMON_PASSWORD = "Student123"
def login(names):
    print("WELCOME TO STUDENT PORTAL ")
    enter_name = input("Enter your name")
    enter_password = input("Enter your password")
    if enter_password != COMMON_PASSWORD:
        print("\n LOGIN FAILED!")
        return -1
    student_index = -1
    for i in range (10):
        if names[i].lower()==enter_name.lower():
            student_index=i
            break
    if student_index==-1:
        print("\n LOGIN FAILED ! Student name not found ")
    else:
        print("\n LOGIN SUCCESSFUL ! Welcome " , names[student_index])
    return student_index
