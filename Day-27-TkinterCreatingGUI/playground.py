def add(*args):
    total = 0
    for n in args:
        total += n
    return total


print(add(15, 5, 9, 37))


def calculate(**kwargs):
    print(kwargs)


calculate(add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.colour = kw.get('colour')
        self.seats = kw.get('seats')


my_car = Car(make='Nissan')
print(my_car.model)
