#  множина хешованих(незмінних) унікальних значень

# first_set = {1,2,3}
# second_set = {2,3,4}
#
# only_in_first_set = first_set.difference(second_set)  # що є тільки в first_set і нема в second_set
# only_in_second_set = second_set.difference(first_set)  # що є тільки в second_set і нема в second_set
#
# print(only_in_first_set)
#
# only_in_first_set_and_only_in_second = first_set.symmetric_difference(second_set)  # що є НЕ спільного в first_set і second_set
#
# print(only_in_first_set_and_only_in_second)
#
# # -----------
# in_2_and_in_second = first_set.intersection(second_set)  # що є спільного в first_set і second_set
#
# print(in_2_and_in_second)
# # ----
# third_set = {2,3}
# is_subset = third_set.issubset(first_set)  #  чи ж частиною(по наченнях) | чи {2,3} частина {1,2,3}
#
# print(is_subset)


# print({1,2,3} == {1,3,2})  # true

# в тестуванні
# case 1

actual_list_of_users = ['Den', 'Alex', 'Ivan']

expected_list_of_users = ['Den', 'Ivan', 'Alex']

print(actual_list_of_users == expected_list_of_users)
print(set(actual_list_of_users) == set(expected_list_of_users))

# case 2

list_of_ids_from_endpoint = [1001, 1002, 1001, 1003]

len_list = len(list_of_ids_from_endpoint)
len_set =  len(set(list_of_ids_from_endpoint))

print(len_list == len_set)

