def who_do_you_know():
    people = input("Enter the list of people you know\n")
    list_of_people = people.split(",")
    normalised_people = []
    for person in list_of_people:
    	normalised_people.append(person.strip().lower())
    return normalised_people

def ask_user():
    person = input("Enter the name of the person\n")
    if person.strip().lower() in list_of_people:                   # conditional operators are and, not, or 
        print("You know this person {}".format(person))
    else:                                                          # use elif in case of one more conditional branch
    	print("You do not know this person {}".format(person))

list_of_people = who_do_you_know()
ask_user()
