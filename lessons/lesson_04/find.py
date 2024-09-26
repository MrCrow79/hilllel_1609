


#
# print(sent[8])
# print(sent.find('is'))
# print(sent.find('iss'))
#


# # погане рішення
# bool_is_deys_in = bool(sent.find('Denys'))
# print(bool_is_deys_in)
#
# bool_is_de1ys_in = bool(sent.find('Den1ys'))
# print(bool_is_de1ys_in)
#
# bool_is_My = bool(sent.find('M'))
# print(bool_is_My)

# is_denys_in_str = False
# if sent.find('Denys') >= 0:
#     is_denys_in_str = True
#     print('Denys in the sentence')



# # альтернативний варіант
#
# if 'Denys' in sent:
    # is_denys_in_str = True
#     print('Denys in the sentence')
#
# is_index = sent.find('is')
#
# result_sent = sent[:is_index]  # розділити до слова is
# print('Cut before is:   ', result_sent)
#
# result_sent = sent[is_index + 2:]  # +2 бо is це має довжину 2, поганий варіант
# print('Cut after is:   ', result_sent)


sent = 'My name is Denys. Really is Denys'
search_word = 'name'

# надрукувати все після слова search_word
search_word_index = sent.find(search_word)  # шукаю індекс початку цього слова(перша зустріч цього слова)
len_of_search_word = len(search_word)  # довжина слова після якого треба друкувати
final_index = search_word_index + len_of_search_word  # знаходжу індекс піля search_word
result_sent = sent[final_index:] # роблю слайс[search_word_index + len(search_word):]
print(result_sent)
