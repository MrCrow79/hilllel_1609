#  пара ключ = значення
# ключі унікальні і хешабельні(типи незмінні)

my_dict = {'name': 'Denys', 'age': 33, 'has_a_job': True}


# set value
my_dict['new_key'] = 'new_value'

# print(my_dict)
new_dict_for_update = {'one': 1, 'two': 2, 'None_value': None}
my_dict.update(new_dict_for_update)

# print(my_dict)


my_dict['new_dict_as_a_value'] = new_dict_for_update
print(my_dict)

# get value
# print(my_dict['name'])
# print(my_dict['new_dict_as_a_value'])
# print(my_dict['new_dict_as_a_value']['one'])

# get without error
print(my_dict.get('name1'))  # return None by default
print(my_dict.get('new_dict_as_a_value').get('None_value'))  # return None бо  'None_value': None(строка 11)


print(my_dict.get('name1', 'Default Alex name'))  # return Default Alex name
print(my_dict.get('name', 'Default Alex name'))  # return Denys


my_string = 'My name is denys'

symbols = dict()

for let in my_string:
    if symbols.get(let) is None:
        symbols[let] = 0
    symbols[let] += 1  # symbols[let] = symbols[let] + 1

print(symbols)


name, age = 'Den', 33

print(name)
print(age)

age, name = name, age  # поміняти місцями

print(name)
print(age)

# print(my_dict['name1'])  error
