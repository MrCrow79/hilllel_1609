def get_5():
    print(str(5))
    return 5
new_fn = get_5

# print(id(get_5))
# print(id(new_fn))
# new_fn()

lst_of_str = ['asd', 'hjhjt', 'asdasdttttt', 'tt']

wrd = ''
max_t = 0

for k in lst_of_str:
    if k.count('t') > max_t:
        wrd = k
        max_t = k.count('t')

print(wrd)

def get_word_with_max_include_letter(letter):
    wrd = ''
    max_t = 0

    for k in lst_of_str:
        if k.count(letter) > max_t:
            wrd = k
            max_t = k.count(letter)

    return wrd

print(get_word_with_max_include_letter('t'))


def count_t(word):

    return word.count('t')


print(max(lst_of_str, key=count_t))
print(max(lst_of_str, key=lambda asd: asd.count('t')))
