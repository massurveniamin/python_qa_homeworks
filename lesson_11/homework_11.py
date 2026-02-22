def sum_numbers_from_string(s):
    try:
        numbers = s.split(",")
        total = 0
        for num in numbers:
            total += int(num)
        return total
    except:
        return "Не можу це зробити!"


data = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

for item in data:
    result = sum_numbers_from_string(item)
    print(result)