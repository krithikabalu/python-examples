from collections import namedtuple

cars = ("Honda", "Maruthi Suzuki", "Ford", "Skoda", "Renault")
print("Original tuple - {}\n".format(cars))

tuple_length =len(cars)
print("Length of array - {}".format(tuple_length))

first_element = cars[0]
print("First element - {}".format(first_element))

last_element = cars[-1]
print("Last element - {}".format(last_element))

del cars

# cars[5] = "Toyota" will throw error since tuples are immutable

# Tuple can also be used as key in dictionary due to their hashable and immutable nature whereas Lists are not used as key in a dictionary because list can’t handle __hash__() and have mutable nature.

car = namedtuple('car', 'name model year')
honda_car = car("Honda", "City", "1981")

print("Named tuple - {}".format(honda_car))

print("Model of the car - {}".format(honda_car.model))

print("First element - {}".format(honda_car[0]))
