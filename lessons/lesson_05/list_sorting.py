# списки

my_names = ['DDena', 'DVaenaa','Alex', 'Viktor', 'Xena']
my_ages = [1,2,3,1,2,3]

# sorted_names = sorted(my_names)  # by default  reverse=False
# sorted_ages = sorted(my_ages)  # by default  reverse=False
#
# sorted_names_reverse = sorted(my_names, reverse=True)
# sorted_ages_reverse = sorted(my_ages, reverse=True)
#
# # print(sorted_names)
# # print(my_names)
# # print(sorted_names_reverse)
# # print(sorted_ages)
# # print(sorted_ages_reverse)
#
#
# my_list_of_items = ['Den', 'Alex', 'Viktor',1,2,3]
# # print(sorted(my_list_of_items))  # error
#
# print(my_names)
# my_names.sort(reverse=True)
# print(my_names)
# my_names.sort(reverse=False)
# print(my_names)
#
# sorted_tuple = sorted((1,3,4,2))
# print(sorted_tuple)

# ---------------------------

sorted_names_by_default = sorted(my_names)
sorted_names_by_len = sorted(my_names, key=lambda x: len(x))

# lambda x: len(x) - анонімна функція, лямбда функція

# іншими словами
def my_fn(word):
    word_length = len(word)
    return word_length

sorted_names_by_len_custom = sorted(my_names, key=my_fn)
#  => sorted([len('DDena'), len('DVaenaa'), len('Alex'), len('Viktor'), len('Xena')])
#  => sorted([my_fn('DDena'), my_fn('DVaenaa'), my_fn('Alex'), my_fn('Viktor'), my_fn('Xena')])

print(sorted_names_by_default)
print(sorted_names_by_len_custom)
print(sorted_names_by_len)