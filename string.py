example = "Python is classic"

lower_example = example.lower()
print("Lower case example - {}".format(lower_example))

upper_example = example.upper()
print("Upper case example - {}".format(upper_example))

length = len(example)
print("String length - {}".format(length))

words = example.split(" ")
print("Words in the example - {}".format(words))

first_part = example[:7]
print("First part - {}".format(first_part))

last_part = example[10:]
print("Last part - {}".format(last_part))

middle_part = example[7:10]
print("Middle part - {}".format(middle_part))

example2 = " and simple"
print("concatenated string - {}".format(example + example2))

