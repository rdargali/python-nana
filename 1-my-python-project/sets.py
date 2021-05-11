# sets have no defined order, no indexes, non mutable
my_set = {"January", "February", "March"}

# loop through elements in set
# for element in my_set:
#     print(element)

my_set.add("April")  # add elements
print(my_set)

# removed first occurence of value if there are duplicates
my_set.remove("January")
print(my_set)
