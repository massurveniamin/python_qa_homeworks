from unittest import result


def func_name(arg1, arg2):
	#local variable
	#logic
	#return
	pass


def own_sum(first_number, second_number):
	#local_variable
	#result = 0

	#logic
	result = first_number + second_number

	#return
	return result


sum_of_two_numbers = own_sum(1, 10)
print(sum_of_two_numbers)

sum_of_two_numbers = own_sum(20, 45)
print(sum_of_two_numbers)

sum_of_func_name = func_name(1, 2)
print(sum_of_func_name)

print(type(own_sum))

print(own_sum('Hello,', ' world'))

reslt = own_sum(second_number=10, first_number=20)
print(reslt)
