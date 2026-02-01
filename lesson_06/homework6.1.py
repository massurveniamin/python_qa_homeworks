#Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False. Строку отримати за допомогою функції input()

str = input('Input sometging\n')
str_set = set(str)
count = len(str_set)
result = count > 10
print(f'В строці більше 10 унікальних символів? - {result}')
