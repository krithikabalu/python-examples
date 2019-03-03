mobiles = ["Samsung", "Redmi", "Vivo", "Apple"]

print("Original list - {}\n".format(mobiles))

list_length =len(mobiles)
print("Length of array - {}".format(list_length))

first_element = mobiles[0]
print("First element - {}".format(first_element))

last_element = mobiles[-1]
print("Last element - {}".format(last_element))

first_two_elements = mobiles[:2]
print("First two elements - {}".format(first_two_elements))

last_two_elements = mobiles[2:] 
print("Last two elements - {}".format(last_two_elements))

middle_elements = mobiles[1:3]
print("Middle elements - {}".format(middle_elements))

sorted_elements = sorted(mobiles) #similarly max, min, sum can be applied on list of numbers
print("Sorted elements - {}".format(sorted_elements))

reverse_sorted_elements = sorted(mobiles, reverse = True)
print("Reverse sorted elements - {}".format(reverse_sorted_elements))

mobiles.append("Honor")
print("Updated list (by append) - {}".format(mobiles))

mobiles.extend(["Lenovo", "Asus"])
print("Updated list (by extend) - {}".format(mobiles))

popped_mobile = mobiles.pop(3)
print("Updated list (by pop with index) - {} after popping {}".format(mobiles, popped_mobile))

# Output: 'm'
popped_mobile = mobiles.pop()
print("Updated list (by pop without index) - {} after popping {}".format(mobiles, popped_mobile))

del mobiles[-1]
print("List after deleting - {}".format(mobiles))

is_element_present = "Redmi" in mobiles
print("Is Redmi present? - {}".format(is_element_present))

sequence = list(range(10))
print("Sequence range {}".format(sequence))

statement = ','.join(mobiles)
print("Mobiles available are " + statement)

mobiles.clear()
print("Empty list - {}".format(mobiles))