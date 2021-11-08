class Buyer:
    def __init__(self, name, surname, thirdname, mobile_phone):
        if not isinstance(name, str):
            raise ValueError(f'{type(name).__name__} incorrect type')

        if not isinstance(surname, str):
            raise ValueError(f'{type(name).__name__} incorrect type')
        self.name = name
        self.surname = surname
        self.third_name = thirdname
        self.phone = mobile_phone

    def get_name(self):
        return {'Name': self.name, 'Surname': self.surname, 'Thirdname': self.third_name, 'Phone': self.phone}

    def __str__(self):
        return f'Name: {self.name}, Surname: {self.surname}, Third_name: {self.third_name}, phone: {self.phone}'