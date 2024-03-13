import math
import domain

#write to file - 'w' mode
#append - 'a' mode

def inputStudentInfo():
    idStudent = input("Enter Student's ID: ")
    nameStudent = input("Enter Student's name: ")
    dobStudent = input("Enter DoB of Student: ")
    student = f"{idStudent}, {nameStudent}, {dobStudent}\n"
    with open('student.txt', 'a') as f:
        f.write(student)
    return domain.student.Student(idStudent, nameStudent, dobStudent)


def inputCourseInfo():
    idCourse = input("Enter the Course's ID: ")
    nameCourse = input("Enter the Course's name: ")
    credit = int(input("Enter the number of credits of course: "))
    course = f"{idCourse}, {nameCourse}, {credit}\n"
    with open('course.txt', 'a') as f:
        f.write(course)
    return domain.course.Course(idCourse, nameCourse, credit)

def inputMark():
    mark = float(input("Enter the mark for this Course: "))
    mark_file = f"{mark}\n"
    with open('mark.txt', 'a') as f:
        f.write(mark_file)
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


