import math
import domain
import pickle 
import os
import zipfile
#write to file - 'w' mode
#append - 'a' mode

file_student = "student.pickle"
file_course = "course.pickle"
file_mark = "mark.pickle"
file_zip = "student.dat"
file_extract = "ex"

def compress_file():
    with zipfile.ZipFile(file_zip, 'w') as zfile:
        zfile.write(file_student)
        zfile.write(file_course)
        zfile.write(file_mark)
    #can use os.remove() to remove single file 
    #if not remove, the data in zipfile will be appended after entering


def inputStudentInfo():
    idStudent = input("Enter Student's ID: ")
    nameStudent = input("Enter Student's name: ")
    dobStudent = input("Enter DoB of Student: ")
    student = {'id': idStudent, 'name': nameStudent, 'dob': dobStudent}
    #save object obj into already-opened-for-binary-write file f
    #pickle.dump(obj, f)
    with open(file_student, 'ab') as f:
        pickle.dump(student, f)
    return domain.student.Student(idStudent, nameStudent, dobStudent)

def inputCourseInfo():
    idCourse = input("Enter the Course's ID: ")
    nameCourse = input("Enter the Course's name: ")
    credit = int(input("Enter the number of credits of course: "))
    course = {'id': idCourse, 'name': nameCourse, 'credit': credit}
    with open(file_course, 'ab') as f:
        pickle.dump(course, f)
    return domain.course.Course(idCourse, nameCourse, credit)

def inputMark(student_id, course_id):
    mark = float(input("Enter the mark for this Course: "))
    mark_file = {'idS': student_id, 'idC': course_id, 'mark': mark}
    with open(file_mark, 'ab') as f:
        pickle.dump(mark_file, f)
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

def decompress_zip():
    if os.path.exists(file_zip):
        if not os.path.exists(file_extract):
            os.makedirs(file_extract)
        with zipfile.ZipFile(file_zip, 'r') as z:
            z.extractall(file_extract)
    else:
        print("Does NOT exist")


def load_data():
    # Load data from the files
    if os.path.exists(file_extract):
        # List files in the extract folder
        extracted_files = os.listdir(file_extract)
        for extracted_file in extracted_files:
            # Construct the full path to the extracted file
            file_path = os.path.join(file_extract, extracted_file)
            # Check if the extracted item is a regular file
            if os.path.isfile(file_path):
                # Open and read the file
                with open(file_path, 'rb') as f:
                    while True:
                        try:
                            data = pickle.load(f)
                            print("Data loaded from", extracted_file, ": ")
                            print(data)
                        except EOFError:
                            break
    else:
        print("Extracted folder does not exist.")