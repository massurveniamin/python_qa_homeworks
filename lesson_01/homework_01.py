# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")
print()

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")
print()

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)
print()

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4
print(f"Бананів {banana} штук")
print()

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(f"Периметр фігури - {perimetery}")
print()


"""

"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apple = 4
pear = apple + 5
plum = apple - 2
total_trees = apple + pear + plum
print(f"Всього {total_trees} дерев")
print()

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
temp = 0
temp_before = temp + 5
temp_after = temp_before - 10
temp_night = temp_after + 4
print(f"Температура надвечір {temp_night} градусів")

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
total_boys = 24
total_girls = total_boys // 2
boys_today = total_boys - 1
girls_today = total_girls - 2
all_children_today = boys_today + girls_today
print(f"Сьогодні у театральному гуртку {all_children_today} дітей")

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
f_book = 8
s_book = f_book + 2
t_book = (f_book + s_book) // 2
total_price = f_book + s_book + t_book
print(f"Загальна вартість книг - {total_price} грн")