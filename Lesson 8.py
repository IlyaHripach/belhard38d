#1
class Car:
    def __init__(self, color:str, count_passenger_seats: int is_baby_seats):
    self.color = color
    self.count_passenger_seats = count_passenger_seats
    self.is_baby_seat = is_baby_seat
    self.is_busy = False




#2
class Taxi:
        def __init__(self,cars: list[Car]):
            self.cars = cars
        def find_car(self, count_passenger: int, is_baby: bool):
            cars = filter(lambda x: not x.is_busy, self.cars)
            if is_baby:
                cars = filter(lambda  x: x.is_baby, cars)
            for car in cars:
                if car.count_passenger_seats >= count_passenger:
                    car.is_busy = True
                    return car


#4
class Category:
    categories: list[dict] = []
    @classmethod
    def add(cls, name: str) -> int:
        for category in cls.categories:
            if category.get('name') == name.title():
                raise ValueError('category is not unique')
        cls.categories.append(
            {
                'name': name.title(),
                'is_published': False
            }
        )
        return len(cls.categories) - 1
    @classmethod
    def get(cls, index: int) -> dict:
        return cls.categories[index]
    @classmethod
    def delete(cls, index: int) -> None:
        try:
            del cls.categories[index]
        except IndexError:
            pass
    @classmethod
    def update(cls, index: int, name: str):
        try:
            obj = cls.get(index)
        except IndexError:
            return cls.add(name)
        else:
            for category in cls.categories:
                if category.get('name') == name.title


