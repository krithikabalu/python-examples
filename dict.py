inventions_dict = {"Light bulb":"Edison", "Telescope":"Galileo", "Electricity": "Benjamin Franklin"}
print("Original dictionary - {}".format(inventions_dict))

print("Light bulb - invented by - {}".format(inventions_dict["Light bulb"]))

inventions = list(inventions_dict.keys())
print("Inventions - {}".format(inventions))

scientists = list(inventions_dict.values())
print("Inventors - {}".format(scientists))

for key,value in inventions_dict.items():
	print("{} invented {}".format(value, key))

removed_invention = inventions_dict.pop("Electricity")
print("Dictionary - {} after deletion of {}".format(inventions_dict, removed_invention))

inventions_dict.setdefault("Aeroplane", "Wright brothers")
inventions_dict.setdefault("Light bulb", "Unknown")
print("Updated dictionary - {}".format(inventions_dict))

inventions_dict.clear()
print("Empty dict - {}".format(inventions_dict))