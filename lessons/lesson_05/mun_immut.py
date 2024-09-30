name = 'Den'

print(id(name))

name = name + ' Mer'
print(id(name))


my_list_of_names = ['Den', 'Alex']  #  list
print(id(my_list_of_names))
print(my_list_of_names)

my_list_of_names.append('Viktor')  # add element
print(id(my_list_of_names))
print(my_list_of_names)