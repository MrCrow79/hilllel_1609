#  множина хешованих(незмінних) унікальних значень

my_set = {1,2,3,3}

print(my_set)


# incorrect_my_set = {1, 2, 3, 3, [1,2]}

# add

my_set.add(5)
my_set.add(3)

print(my_set)

my_set.add('Den')
my_set.add(False)
my_set.add(None)

print(my_set)


# update
new_set = {1,5,6,7}
my_set.update(new_set)

print(my_set)
# pop

removed_el = my_set.pop()
print(removed_el)
print(my_set)

# remove
my_set.remove(5)
my_set.remove(None)
print(my_set)