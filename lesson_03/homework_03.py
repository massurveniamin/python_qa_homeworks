alice_in_wonderland = '''"Would you tell me, please, which way I ought to go from here?"
"That depends a good deal on where you want to get to," said the Cat.
"I don't much care where ——" said Alice.
"Then it doesn't matter which way you go," said the Cat.
"—— so long as I get somewhere," Alice added as an explanation.
"Oh, you're sure to do that," said the Cat,
"if you only walk long enough."'''
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
symbol_count = alice_in_wonderland.count("'")
print(alice_in_wonderland)
print(f"\nВсього символов - {symbol_count}")


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04

"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea = 436402
azov_sea = 37800
total_sea = black_sea + azov_sea
print(f"\nЗагальна площа Чорного та Азовського морів = {total_sea} км2")
# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
one_month = 1179
total_month = 18
total_sum = one_month * total_month
print(f"\nЗагальна вартість комп'ютера = {total_sum} грн.")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a1 = 8019
a2 = 8
a3 = a1 % a2

b1 = 9907
b2 = 9
b3 = b1 % b2

c1 = 2789
c2 = 5
c3 = c1 % c2

d1 = 7248
d2 = 6
d3 = d1 % d2

e1 = 7128
e2 = 5
e3 = e1 % e2

f1 = 19224
f2 = 9
f3 = f1 % f2

print(f"\nОстача від {a1} : {a2} = {a3}")
print(f"Остача від {b1} : {b2} = {b3}")
print(f"Остача від {c1} : {c2} = {c3}")
print(f"Остача від {d1} : {d2} = {d3}")
print(f"Остача від {e1} : {e2} = {e3}")
print(f"Остача від {f1} : {f2} = {f3}")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
big_pizza_price = 274
big_pizza_quantity = 4
middle_pizza_price = 218
middle_pizza_quantity = 2
juice_price = 35
juice_quantity = 4
cake_price = 350
cace_quantity = 1
water_price = 21
water_quantity = 3
total_money = (big_pizza_price*big_pizza_quantity)+(middle_pizza_price*middle_pizza_quantity)+(juice_price*juice_quantity)+(cake_price*cace_quantity)+(water_price*water_quantity)
print(f"\nВсього для замовлення потрібно {total_money} грн.")


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
total_photo = 232
photo_in_list = 8
total_lists = total_photo // photo_in_list
print(f"\nЩо б вклеїти всі фото потрібно {total_lists} сторінок")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600
per_100 = 9
segment = 100
bak = 48

total_oil = (distance//segment)*per_100
stops_need = total_oil//bak

print(f"\nвсього потрібно палива: {total_oil} л., \nВсього зупинок на заправку потрібно: {stops_need}")