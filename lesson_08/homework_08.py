class Student:
    def __init__(self, first_name, last_name, age, avg_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.avg_grade = avg_grade

    def change_grade(self, new_grade):
        self.avg_grade = new_grade

    def show_info(self):
        print(f"Студент: {self.first_name} {self.last_name}, {self.age} років. Середній бал: {self.avg_grade}.")

student1 = Student("Веніамін", "Массур", 40, 5)
print("До змін")
student1.show_info()
student1.change_grade(7)
print("Після змін:")
student1.show_info()