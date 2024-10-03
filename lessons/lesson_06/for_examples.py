
# список прав
response = [
    {'id': 1, 'name': 'read_only', 'descriptions': 'For all users'},
    {'id': 2, 'name': 'RW', 'descriptions': 'For writing and reading'},
    {'id': 3, 'name': 'delete', 'descriptions': 'For deleting'},
    {'id': 3, 'name': 'delete', 'descriptions': 'For deleting'},
    {'id': 4, 'name': 'all', 'descriptions': 'For Admins'},
    {'id': None, 'name': 'broken', 'descriptions': None},
]

for perm in response:
    if perm.get('id', None) is None:  #
        print(f'ALARM, there is no id\n{perm}')

# ---------------------------------------------------------------------------
unique_ids = []

for perm in response:
    print(f'current id is {perm.get("id")}')
    if perm.get('id') in unique_ids:
        print(f'Ids are not unique, id={perm.get("id")}')
        break
    else:
        unique_ids.append(perm.get('id'))

# ---------------------------------------------------------------------------
response_ids = [k.get('id') for k in response]

if len(response_ids) != len(set(response_ids)):
    print(f'Ids are not unique')


# None, False, True для порівнянн використовувати is

# read_all_p = response[0]
# print(read_all_p['id'])  # get from dict by key
# # print(read_all_p['id1'])  # get error KeyError
# print(read_all_p.get('id1'))  # None by defaultD
# print(read_all_p.get('id1', 'asdasd'))  # return asdasd