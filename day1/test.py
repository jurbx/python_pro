class Student:
    """
    Class about student
    """

    count = 0
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.__age = age
        Student.count += 1

st_1 = Student('Ivan', 'Rimskiy', 40)
#print(st_1.__dict__)
#print(Student.__name__)
#print(Student.__doc__)
#print(Student.__module__)
#print(Student.__bases__)
#print(id(st_1))

print(st_1._Student__age)