import numpy as np
import math

class Course:
    def __init__(self, idCourse, nameCourse, credit):
        self._idCourse = idCourse
        self._nameCourse = nameCourse
        self._credit = credit

    def get_credit(self):
        return self._credit

    def get_idC (self):
        return self._idCourse
        
    def get_nameC (self):
        return self._nameCourse

class Student:
    def __init__(self, idStudent, nameStudent, dobStudent):
        self._idStudent = idStudent
        self._nameStudent = nameStudent
        self._dob = dobStudent
        self._courses = [] #empty list to store courses

    def get_nameS(self):
        return self._nameStudent
    
    def get_idS (self):
        return self._idStudent

    def get_dob(self):
        return self._dob
    
    def add_course(self, course, mark):
        #appends a dict to this courses list, where each dict contains 
        #information about a course and the corresponding mark
        self._courses.append({"Course":course, "Mark": mark}) #add dict to to the end of the list

    def gpa(self):
        marks = np.array([course["Mark"] for course in self._courses])
        credits = np.array([course["Course"].get_credit() for course in self._courses])
        
        total_mark = np.sum(marks * credits)
        total_credit = np.sum(credits)

        average_gpa = np.round(total_mark / total_credit, 1)
        return average_gpa


    def showFull(self):
        print("\n{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "Student ID", "Name", "Date of Birth", "Course ID", "Course Name", "Mark"))
        for data in self._courses:
            course = data["Course"]
            mark = data["Mark"]
            print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
                self.get_idS(), self.get_nameS(), self.get_dob(), course.get_idC(), course.get_nameC(), mark))
        print()


class MarkManagement:
    def __init__(self):
        self._StudentList = [] #empty list to store instances of the Student class

    def add_student(self, student): 
        #appends an instance of the Student class to the list 
        self._StudentList.append(student)

    def showList(self):
        for student in self._StudentList:
            student.showFull()
    
    def showStudentInfo(self):
        print("{:<15} {:<15} {:<15}".format("Student ID", "Student name", "Date of Birth"))
        for student in self._StudentList:
            print("{:<15} {:<15} {:<15}".format(student.get_idS(), student.get_nameS(), student.get_dob()))

    def showCourseInfo(self):
        print("{:<15} {:<15} {:<15}".format("Course ID", "Course name", "Credits"))
        for student in self._StudentList:
            for data in student._courses:
                course = data["Course"]
                print("{:<15} {:<15} {:<15}".format(course.get_idC(), course.get_nameC(), course.get_credit()))

    def showFollowChoose(self):
        idStudent = input("Enter Student ID: ")
        found = False
        for student in self._StudentList:
            if student.get_idS()== idStudent:
                idCourse = input("Enter Course ID: ")
                for data in student._courses:
                    course = data["Course"]
                    mark = data["Mark"]
                    if course.get_idC() == idCourse:
                        found = True
                        print("\nMark for {} in {}: {}".format(student.get_nameS(), course.get_nameC(), mark))
        if not found:
            print("Student or Course not found.")

    def showGpa(self):
        sorted_students = sorted(self._StudentList, key=lambda x: x.gpa(), reverse=True)
        print("{:<15} {:<15} {:<15}".format("Student ID", "Student name", "GPA"))
        for s in sorted_students:
            print("{:<15} {:<15} {:<15}".format(s.get_idS(), s.get_nameS(), s.gpa()))


def inputStudentInfo():
    idStudent = input("Enter Student's ID: ")
    nameStudent = input("Enter Student's name: ")
    dobStudent = input("Enter DoB of Student: ")
    return Student(idStudent, nameStudent, dobStudent)

def inputCourseInfo():
    idCourse = input("Enter the Course's ID: ")
    nameCourse = input("Enter the Course's name: ")
    credit = int(input("Enter the number of credits of course: "))
    return Course(idCourse, nameCourse, credit)

def inputMark():
    mark = float(input("Enter the mark for this Course: "))
    return math.floor(mark*10)/10

def main():
    Management_System = MarkManagement()

    numOfStudent = int(input("Number of the student: "))

    for _ in range(numOfStudent):
        studentInfo = inputStudentInfo()
        numOfCourse = int(input("Enter number of course for {}: ".format(studentInfo.get_nameS())))

        #Student object is created and add to StudentList list
        student = Student(studentInfo.get_idS(), studentInfo.get_nameS(), studentInfo.get_dob())

        for _ in range(numOfCourse):
            courseInfo = inputCourseInfo()
            mark = inputMark()

            #Course object is created 
            course = Course(courseInfo.get_idC(), courseInfo.get_nameC(), courseInfo.get_credit())
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
        choice = int(input("Enter your choice: "))
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




    
