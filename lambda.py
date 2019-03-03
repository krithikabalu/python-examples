numbers = [100, 957, 423, 65, 350]

# traditional way
def is_even(number):
	return number%2 == 0

def even_numbers(numbers):
	even_numbers = []
	for number in numbers:
		if is_even(number):
			even_numbers.append(number)
	return even_numbers

print("Even numbers using traditional method {}".format(even_numbers(numbers)))

#lambda way
even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print("Even numbers using lambda filter {}".format(even_numbers))

multiplied_by_10 = list(map(lambda x: x*10, numbers))
print("Multiplied by 10 {}".format(multiplied_by_10))

import functools;
sum_of_all = functools.reduce(lambda x,y : x+y, numbers)
print("Sum of all numbers {}".format(sum_of_all))

least_of_all = functools.reduce(lambda x,y : x if x<y else y, numbers)
print("Least number {}".format(least_of_all))

numbers = [1948, 957, 423, 65, 350]
print_all_numbers = lambda x: print("All numbers: %s" %(numbers))
print_all_numbers(numbers)
