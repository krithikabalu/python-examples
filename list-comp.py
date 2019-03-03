numbers = [1948, 957, 423, 65, 350]

even_numbers = [x for x in numbers if x % 2==0]

print("Even numbers {}".format(even_numbers))

multiplied_by_10 = [x * 10 for x in numbers]

print("Multiplied by 10 {}".format(multiplied_by_10))
