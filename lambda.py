import functools;

numbers = [1948, 957, 423, 65, 350]
print_all_numbers = lambda x: print("All numbers: %s" %(numbers))
print_all_numbers(numbers)

even_numbers = list(filter(lambda x: x%2==0, numbers))
print("Even numbers {}".format(even_numbers))

multiplied_by_10 = list(map(lambda x: x*10, numbers))
print("Multiplied by 10 {}".format(multiplied_by_10))

sum_of_all = functools.reduce(lambda x,y : x+y, numbers)
print("Sum of all numbers {}".format(sum_of_all))

least_of_all = functools.reduce(lambda x,y : x if x<y else y, numbers)
print("Least number {}".format(least_of_all))
