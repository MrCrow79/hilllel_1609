# кортеж

my_names = ('Den', 'Alex', 'Viktor')

print(my_names)
print(my_names[0])
print('-'*80)

for name in my_names:
    print(name)
print('-'*80)
print(my_names[1:])
# ------------------------------

my_names = ('Den', 'Alex', 'Viktor')
my_name, alex_name, friend_name = ('Den', 'Alex', 'Viktor')
print(alex_name)
print('-'*80)
print(my_names)
print(*my_names) # ==> print('Den', 'Alex', 'Viktor')
print('Den', 'Alex', 'Viktor')
print('-'*80)
# ------------------------------
my_name, *not_my_names, ivan_name, last_name = ('Den', 'Alex', 'Viktor', 'Ivan', 'Serge')
print(my_name)
print(not_my_names)
print(*not_my_names)
print(ivan_name)
print(last_name)
# ------------------------------
# приведення до tuple
some_text = 'bla-bla'

tuple_text = tuple(some_text)  # ('b', 'l', 'a', '-', 'b', 'l', 'a')
print(tuple_text)

my_list = [1,2,3]
new_tuple_from_list = tuple(my_list)
print(new_tuple_from_list)

# ------------------------------

my_list = [1,2]

my_tuple_with_evr = (1, my_list, 'asd', None, (1,2))  # це tuple

print(my_tuple_with_evr)
my_list.append([None, True])
print(my_tuple_with_evr)

empty_tuple = ()
print(type(empty_tuple))

tuple_with_1_el = (42, )
not_tuple_with_1_el = (42)
print(type(tuple_with_1_el))
print(type(not_tuple_with_1_el))
