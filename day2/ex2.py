from ex1 import Person

class Student(Person):

    def __init__(self, name, height, age, clas, group, surname):
        super().__init__(name,height,age,surname)
        self.clas = clas
        if isinstance(age, int) and isinstance(height, int):
            self.group = group
        else:
            TypeError(f'{type(height).__name__} object cannot be interpreted')

    def __str__(self):
        return f'{super().__str__()}; Class = {self.clas}, Group = {self.group}'


inst1 = Student('Dan', 190, 17, '8A', '2P-19', 'Rim')

print(inst1)