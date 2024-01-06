def input_s_in4():
    s_id = input("Enter Student ID: ")
    s_name = input("Enter name of the student: ")
    dob = input("Enter the date of birth of student: ")
    return {"s_id": s_id, "s_name": s_name, "dob": dob}

def input_c_in4():
    c_id = input("Enter Course ID: ")
    c_name = input("Enter the Course name: ")
    return {"c_id": c_id, "c_name": c_name}

def input_mark(s_name, c_name):
    marks = float(input("{}'s {} mark: ".format(s_name, c_name)))
    return marks

def print_full_info(students_data):
    print("\n{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("Student ID", "Name", "Date of Birth", "Course ID", "Course Name", "Mark"))
    for student_data in students_data:
        for course_data in student_data["c_data"]:
            print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
                student_data["s_info"]["s_id"],
                student_data["s_info"]["s_name"],
                student_data["s_info"]["dob"],
                course_data["c_info"]["c_id"],
                course_data["c_info"]["c_name"],
                course_data["mark"]
            ))
        print()  # Print a new line after each block

def print_student_info(students_data):
    print("\n{:<15} {:<15} {:<15}".format("Student ID", "Name", "Date of Birth"))
    for student_data in students_data:
        print("{:<15} {:<15} {:<15}".format(
            student_data["s_info"]["s_id"],
            student_data["s_info"]["s_name"],
            student_data["s_info"]["dob"]
        ))
        print()  # Print a new line after each block

def print_course_info(students_data):
    print("\n{:<15} {:<15}".format("Course ID", "Course Name"))
    for student_data in students_data:
        for course_data in student_data["c_data"]:
            print("{:<15} {:<15}".format(
                course_data["c_info"]["c_id"],
                course_data["c_info"]["c_name"]
            ))
            print()  # Print a new line after each block

def print_student_course_marks(students_data):
    student_id = input("Enter Student ID: ")
    course_id = input("Enter Course ID: ")

    found = False
    for student_data in students_data:
        if student_data["s_info"]["s_id"] == student_id:
            for course_data in student_data["c_data"]:
                if course_data["c_info"]["c_id"] == course_id:
                    found = True
                    print("\nMark for {} in {}: {}".format(student_data["s_info"]["s_name"], course_data["c_info"]["c_name"], course_data["mark"]))

    if not found:
        print("Student or Course not found.")

def main():
    num_students = int(input("Number of students: "))
    students_data = []

    for _ in range(num_students):
        s_info = input_s_in4()
        num_courses = int(input("Enter the number of courses for {}: ".format(s_info["s_name"])))
        c_data = []

        for _ in range(num_courses):
            c_info = input_c_in4()
            mark = input_mark(s_info["s_name"], c_info["c_name"])

            course_data = {"c_info": c_info, "mark": mark}
            c_data.append(course_data)

        student_data = {"s_info": s_info, "c_data": c_data}
        students_data.append(student_data)

    while True:
        print("\nMenu:")
        print("1. Print full (student, course, marks)")
        print("2. Print list student info only")
        print("3. Print course info only")
        print("4. Print student and course marks")
        print("0. Exit")

        choice = input("Enter your choice (0-4): ")

        if choice == "1":
            print_full_info(students_data)
        elif choice == "2":
            print_student_info(students_data)
        elif choice == "3":
            print_course_info(students_data)
        elif choice == "4":
            print_student_course_marks(students_data)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
