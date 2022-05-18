def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

add(3,4,5,6)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan",model="GT_45")
print(my_car.model)
