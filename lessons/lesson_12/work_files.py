file_path = 'file_for_read_write.txt'
file_path_append = 'file_for_append.txt'

# r - читання
# w - режим запису/перестворення файлу(кожний раз файл буде перезаписуватись)
# a - append, додавання в файл/створення файлу

# r+ - read + write, файл повинен існувати
# w+ - read + write, файл можу бути створений
# a+ - read + append, файл може бути створений

with open(file_path, mode='w') as f:
    f.write('line1')
    f.write('\tline2\n')
    f.write(r'line3\n')  # raw строка
    f.write(' line4\\n')  # екранування
    f.write(' line5')

    f.write('\ncurrent file is ')
    f.write(str(file_path))

    f.write("""\n\nfirst row 
    second
    
last
    """)
    f.write('!!!\n')

    f.writelines(['writelines1,', 'writelines2, ', 'writelines3\n'])
    f.writelines((str(k) for k in range(57)))  # generator


with open(file_path_append, mode='a') as f:
    f.write('line1')
    f.write('\tline2\n')
    f.write(r'line3\n')  # raw строка
    f.write(' line4\\n')  # екранування
    f.write(' line5')

# do stuff


with open(file_path, mode='r') as f:  # the same as with open(file_path) as f:
    data = f.read()  # поверне стрінгу

    data2 = f.read()  # поверне порожню строку



with open(file_path, mode='r') as f:  # the same as with open(file_path) as f:
    data = f.readlines()  # поверне список строк

for line in data:
    if 'line' in line:
        print(line)

with open(file_path, mode='r') as f:  # the same as with open(file_path) as f:

    counter = 0
    line = f.readline()

    while line != '':
        if 'line' in line:
            print('-'*80)
            print(counter)
            print(line)
        counter += 1
        line = f.readline()



