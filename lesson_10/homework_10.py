class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size


tl = TeamLead("Veniamin", 1500, "IT", "Python", 24)

print("Name:", tl.name)
print("Salary:", tl.salary)
print("Department:", tl.department)
print("Language:", tl.programming_language)
print("Team size:", tl.team_size)

#________________________________________________________________________________________________________

from abc import ABC, abstractmethod
import math


class Figure(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Figure):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def perimeter(self):
        return self.__a + self.__b + self.__c

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c))


figures = [
    Rectangle(5, 3),
    Circle(4),
    Triangle(3, 4, 5)
]

for fig in figures:
    print(type(fig).__name__)
    print("Area:", fig.area())
    print("Perimeter:", fig.perimeter())
    print()