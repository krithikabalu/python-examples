subjects = set()
subjects = {"biology", "english", "computer", "physics", "chemistry", "hindi"}

print("Original set - {}\n".format(subjects)) # unordered

subjects.add("maths")
print("Set after addition - {}".format(subjects))

subjects.remove("biology") # discard can also be used
print("Set after deletion - {}".format(subjects))

extra_subjects = {"history", "geography"}
subjects.update(extra_subjects)
print("Updated set - {}".format(subjects))

# subjects.pop() # pops arbitrary element

# print("Set after pop - {}".format(subjects))

subjects.add("computer") # set cannot contain duplicates
print("Set after addition of element which is already present- {}".format(subjects))

languages = {"english", "hindi", "tamil"}
language_subjects = languages.intersection(subjects)
print("Language subjects - {}".format(language_subjects))
print("Language subjects is a subset of subjects? {}".format(language_subjects.issubset(subjects))) # similarly issuperset and isdisjoint can be used

elective_subjects = {"home science", "biology"}
all_subjects = subjects.union(elective_subjects)
print("All subjects - {}".format(all_subjects))

non_subject_languages = languages.difference(subjects) 
print("Non subject languages - {}".format(non_subject_languages))

non_subject_languages_and_non_language_subjects = languages.symmetric_difference(subjects)
print("Non subject languages and non language subjects - {}".format(non_subject_languages_and_non_language_subjects))

subjects.clear()
print("Empty set - {}".format(subjects))