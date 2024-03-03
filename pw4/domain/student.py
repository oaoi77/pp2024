import numpy as np

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