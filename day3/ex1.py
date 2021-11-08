class Price:
    def __init__(self, pricelist):
        self.pricelist = pricelist

    def checkprice(self):
        try:
            for item in self.pricelist:
                if not item.isalpha():
                    item = int(item)
                if not isinstance(item, (int,float)):
                    raise TypeError(f'{item} must be integer or float, your type is {type(item)}')
                if item <= 0:
                    raise ValueError('number must be > 0')
        except TypeError as err:
            return err
        else:
            return 'All right'


x = ' '
pricelist = []

while True:
    y = input('Enter price: ')
    if y == '' or y == 'q':
        break
    pricelist.append(y)

print(Price(pricelist).checkprice())