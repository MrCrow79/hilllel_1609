my_name = 'DEnys Mer4ezhkiN'

print(my_name.upper())  # в верхній регістр кожне слово
print(my_name.lower())  # в нижній  регістр кожне слово
print(my_name.title())  # З великої кожне слово(розділення по будь-якому символу НЕ буква)
print(my_name.capitalize())  # першу дуве зробить великою, інші малі


my_name = 'Denys merezhkin ASD'
print(my_name.isupper())
print(my_name.islower())
print(my_name.istitle())

answer = 'asd USD'

if 'usd' in answer.lower():  # answer.lower() = переводить все в answer в нижній регістр
    print('True')