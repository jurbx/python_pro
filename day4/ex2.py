class ProperFraction:
    """
    Class defines Proper fraction
    """
    def __init__(self, fraction: str):
        try:
            if not isinstance(fraction, str):
                raise TypeError(f'Invalid type, {type(fraction)}, {fraction} must be int')
            if len(fraction) != 3:
                raise ValueError("Enter str as expample: num1/num2 or num1 num2")
            if not fraction[0].isdigit():
                raise TypeError(f'Invalid type, {type(fraction[0])}, {fraction[0]} must be int')
            if not fraction[2].isdigit():
                raise TypeError(f'Invalid type, {type(fraction[2])}, {fraction[2]} must be int')
            if int(fraction[0]) < int(fraction[2]):
                raise ValueError(f"Enter proper fraction, you entered simple fraction: {fraction[0]} < {fraction[2]}, "
                                 f"must be: num > {fraction[2]}")
        except (ValueError, TypeError) as err:
            raise err

        self.highernum = int(fraction[0])
        self.lowernum = int(fraction[2])

    def get_value(self):
        return self.lowernum + self.lowernum * self.highernum

    def __gt__(self, other):
        if not isinstance(other, ProperFraction):
            return NotImplemented
        return self.get_value() > other.get_value()

    def __lt__(self, other):
        if not isinstance(other, ProperFraction):
            return NotImplemented
        return self.get_value() < other.get_value()

    def __eq__(self, other):
        if not isinstance(other, ProperFraction):
            return NotImplemented
        return self.get_value() == other.get_value()

    def __ge__(self, other):
        if not isinstance(other, ProperFraction):
            return NotImplemented
        return self.get_value() >= other.get_value()

    def __le__(self, other):
        if not isinstance(other, ProperFraction):
            return NotImplemented
        return self.get_value() <= other.get_value()

    def __neg__(self, other):
        if not isinstance(other, ProperFraction):
            return NotImplemented
        return self.get_value() != other.get_value()

    def __str__(self):
        return f'higher num: {self.highernum}, lower num: {self.lowernum}'


x = ProperFraction('9/8')
y = ProperFraction('9/7')
print(x != y)
