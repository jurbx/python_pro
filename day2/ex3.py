from ex2 import Student

class Group:
    def __init__(self, students):
        self.students = students

    def find_by_surname(self, surname):
        res = []
        for stun in self.students:
            if stun == surname:
                res.append(stun)
        return res or None

    def del_bysurname(self, surname):
        for stud in self.students:
            if stud == surname:
                self.students.remove()
                return 'Fine'
        else:
            return None
