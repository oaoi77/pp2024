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
