def multiplication_tables(number, times):
	for time in range(1, times+1):
		print("{} * {} = {}".format(number, time, number*time))

print("\nUsing positional arguments")
multiplication_tables(7,10)
print("-"*90)

print("\nUsing named parameters")
multiplication_tables(times=10, number=7)
print("-"*90)

#using args
def multiplication_tables(*args):
	print(args)
	number = args[0]
	times = args[1]
	for time in range(1, times+1):
		print("{} * {} = {}".format(number, time, number*time))
print("\nUsing *args")
multiplication_tables(7,10)
print("-"*90)


#using kwargs
def multiplication_tables(**kwargs):
	print(kwargs)
	number = kwargs["number"]
	times = kwargs["times"]
	for time in range(1, times+1):
		print("{} * {} = {}".format(number, time, number*time))

print("\nUsing **kwargs")
multiplication_tables(number=7, times=10)
print("-"*90)