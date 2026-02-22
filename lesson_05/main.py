#tuple ()
first_number = 1
second_number = 2
numbers_tuple = (first_number, second_number, 3, 7, 1, -7, -33)
print(numbers_tuple)
print(numbers_tuple[3])
print(numbers_tuple[::2])

#list []
numbers_list = [first_number, second_number, 3, 7, 1, -7, -33]
inner_list = [100, 101, 102]
print(numbers_list)
numbers_list.append(77)
print(numbers_list)
numbers_list.insert(1, 33)
print(numbers_list)
numbers_list.pop(-2)
print(numbers_list)
numbers_list.remove(1)
print(numbers_list)
numbers_list.extend(inner_list)
print(numbers_list)
print(*numbers_list)

numbers_list.sort()
print(type(numbers_list))
sorted_numbers_list = sorted(numbers_list)
print(type(sorted_numbers_list))

# set
numbers_set = {-1, 2, 3, -10, 33}
print(numbers_set)
numbers_set.add(1)
numbers_set.add(3)
print(numbers_set)
numbers_set.pop()
print(numbers_set)
numbers_set.remove(1)
print(numbers_set)

# dict {}
numbers_dict = {'key': 'value'}
numbers_dict = {'first_number': 1, 'second_number': 2, 'third_number': 3}
print(numbers_dict)
print(numbers_dict.get('first_number'))

item = {"color": "red", "price": 100, "additionals_properties": {'producer': 'Samsung', 'id': 'iddid}'}, 'seller': {'name': 'mike'}}
print(item)