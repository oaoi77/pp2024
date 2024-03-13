import domain
import input

def main():
    Management_System = domain.management.MarkManagement()

    numOfStudent = input.inputNumSt()

    for _ in range(numOfStudent):
        studentInfo = input.inputStudentInfo()
        numOfCourse = input.inputNumCourse()

        #Student object is created and add to StudentList list
        student = domain.student.Student(studentInfo.get_idS(), studentInfo.get_nameS(), studentInfo.get_dob())

        for _ in range(numOfCourse):
            courseInfo = input.inputCourseInfo()
            mark = input.inputMark()

            #Course object is created 
            course = domain.course.Course(courseInfo.get_idC(), courseInfo.get_nameC(), courseInfo.get_credit())
            #adding the course to course list created in Student class
            student.add_course(course, mark)

        #adding the student to the StudentList list 
        Management_System.add_student(student)
    while True:
        print("---------------------------------------------------------")
        print("1. Show the Student List information")
        print("2. Show the Course List")
        print("3. Show Student with mark of choosen Course")
        print("4. Show full")
        print("5. GPA")
        print("0. Exit")
        print("---------------------------------------------------------")
        choice = input.inputChoice()
        if choice == 1:
            Management_System.showStudentInfo()
        elif choice == 2:
            Management_System.showCourseInfo()
        elif choice == 3:
            Management_System.showFollowChoose()
        elif choice ==4:
            Management_System.showList()
        elif choice ==5:
            Management_System.showGpa()
        elif choice == 0:
            break
        else:
            print("Invalid")

if __name__ == "__main__":
    main()