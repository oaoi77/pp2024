import math
import domain

def inputStudentInfo():
    idStudent = input("Enter Student's ID: ")
    nameStudent = input("Enter Student's name: ")
    dobStudent = input("Enter DoB of Student: ")
    return domain.student.Student(idStudent, nameStudent, dobStudent)

def inputCourseInfo():
    idCourse = input("Enter the Course's ID: ")
    nameCourse = input("Enter the Course's name: ")
    credit = int(input("Enter the number of credits of course: "))
    return domain.course.Course(idCourse, nameCourse, credit)

def inputMark():
    mark = float(input("Enter the mark for this Course: "))
    return math.floor(mark*10)/10

def inputChoice():
    choice = int(input("Enter your choice: "))
    return choice

def inputNumSt():
    numSt = int(input("Enter number of student: "))
    return numSt

def inputNumCourse():
    numC = int(input("Enter number of course for: "))
    return numC


