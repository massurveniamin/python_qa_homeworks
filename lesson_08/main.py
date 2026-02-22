import datetime

class DogSize:
    # height: float
    # lenght: float
    # weight: float
    pass

class Meal:
    pass

class Dog:
    # fields
    # name: str
    # breed: str
    # color: str
    # dog_size: DogSize
    # data_of_birth: datetime

    def __init__(self, **kwargs):
       self.name = kwargs.get('name')
       self.date_of_birth = datetime.datetime.now() - datetime.timedelta(days=kwargs.get('age', 0))
       self.breed = kwargs.get('breed', 'Dvorterier')
       self.color = kwargs.get('color', 'black')


       print(f'initialize new Dog with name {self.name}')
       pass
    # behavior
    # say()
    # eat(meal: Meal)
    # sleep()

dog1 = Dog('Patron', 18)
dog2 = Dog('Bobick', 22)