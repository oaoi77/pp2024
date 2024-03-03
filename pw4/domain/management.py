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
