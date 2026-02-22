# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 10:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_numbers(first_number, second_number):
    return first_number + second_number
print(sum_numbers(5, 10))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def avg(numbers):
    return sum(numbers) / len(numbers)
print(f"{avg([10, 10, 10, 50])}")

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def str_text(text):
    return (text[::-1])
print(f"{str_text('My name is Veniamin')}")

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def search_long_word(words):
    long_word = ""
    for i in words:
        if len(i) > len(long_word):
            long_word = i
    return long_word
print(f"{search_long_word('Lord of the rings'.split())}")

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""