class GeneralInfo:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    def get_id(self):
        return self._id
    
    def get_name(self):
        return self._name
    
    def print(self):
        print("\n{:<15} {:<15}".format("ID", "Name"))
        print("\n{:<15} {:<15}".format(self.get_id, self.get_name))

class Course(GeneralInfo):
    def __init__(self, idCourse, nameCourse):
        super().__init__(idCourse, nameCourse)

class Student(GeneralInfo):
    def __init__(self, idStudent, nameStudent, dobStudent):
        super().__init__(idStudent, nameStudent)
        self._dob = dobStudent
        self._courses = [] #empty list to store courses
    
    def get_dob(self):
        return self._dob
    
    def add_course(self, course, mark):
        #appends a dict to this courses list, where each dict contains 
        #information about a course and the corresponding mark
        self._courses.append({"Course":course, "Mark": mark}) #add dict to to the end of the list

    def print(self): #overriding
        print("\n{:<15} {:<15} {:<15}".format("Student ID", "Name", "Date of Birth"))
        print("{:<15} {:<15} {:<15}".format(self.get_id(), self.get_name(), self.get_dob()))
        print()

    def showFull(self):
        print("\n{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "Student ID", "Name", "Date of Birth", "Course ID", "Course Name", "Mark"))
        for data in self._courses:
            course = data["Course"]
            mark = data["Mark"]
            print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
                self.get_id(), self.get_name(), self.get_dob(), course.get_id(), course.get_name(), mark))
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
        for student in self._StudentList:
            student.print()

    def showCourseInfo(self):
        print("\n{:<15} {:<15}".format("Course ID", "Course name"))
        for student in self._StudentList:
            for data in student._courses:
                course = data["Course"]
                print("{:<15} {:<15}".format(course.get_id(), course.get_name()))
            print()

    def showFollowChoose(self):
        idStudent = input("Enter Student ID: ")
        idCourse = input("Enter Course ID: ")

        found = False
        for student in self._StudentList:
            if student.get_id()== idStudent:
                for data in student._courses:
                    course = data["Course"]
                    mark = data["Mark"]
                    if course.get_id() == idCourse:
                        found = True
                        print("\nMark for {} in {}: {}".format(student.get_name(), course.get_name(), mark))
        if not found:
            print("Student or Course not found.")

def inputStudentInfo():
    idStudent = input("Enter Student's ID: ")
    nameStudent = input("Enter Student's name: ")
    dobStudent = input("Enter DoB of Student: ")
    return Student(idStudent, nameStudent, dobStudent)

def inputCourseInfo():
    idCourse = input("Enter the Course's ID: ")
    nameCourse = input("Enter the Course's name: ")
    return Course(idCourse, nameCourse)

def inputMark():
    mark = float(input("Enter the mark for this Course: "))
    return mark

def main():
    Management_System = MarkManagement()

    numOfStudent = int(input("Number of the student: "))

    for _ in range(numOfStudent):
        studentInfo = inputStudentInfo()
        numOfCourse = int(input("Enter number of course for {}: ".format(studentInfo.get_name())))

        #Student object is created and add to StudentList list
        student = Student(studentInfo.get_id(), studentInfo.get_name(), studentInfo.get_dob())

        for _ in range(numOfCourse):
            courseInfo = inputCourseInfo()
            mark = inputMark()

            #Course object is created 
            course = Course(courseInfo.get_id(), courseInfo.get_name())
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
        elif choice == 0:
            break
        else:
            print("Invalid")

if __name__ == "__main__":
    main()




    
