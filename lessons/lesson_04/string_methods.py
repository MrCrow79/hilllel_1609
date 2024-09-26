# my_name = 'Denys'

# print(my_name[2])  # get by index
#
# # slices
# print(my_name[:4])
# print(my_name[1:])
# print(my_name[1:4])
# print(my_name[::2])
# print(my_name[1::2])

my_name = 'Denys'
print(my_name)
print(id(my_name))
print('----------')
# my_name = 'Denys M'
# print(my_name)
# print(id(my_name))

my_name = my_name + ' M'  # concatenation
print(my_name)
print(id(my_name))
print('----------')

my_name =  f"{my_name} 23"
print(my_name)
print(id(my_name))
print('----------')

my_name = my_name*5
print(my_name)
print(id(my_name))

# my_new_name = 'SuperD'
# my_name = my_new_name
#
# print(id(my_name))
# print(id(my_new_name))
#
# my_new_name = 'New new name'
#
# print(my_name)
# print(my_new_name)
