import pathlib
import os
import shutil

current_dir = pathlib.Path().absolute()  # шлях до папки в якій лежить поточний файл
base_dir = pathlib.Path(current_dir).parent.parent  # шлях до бахової директорії

# print(type(current_dir))
# print(current_dir)
# print(current_dir.name)
# print(current_dir.parent)
#
# parents = current_dir.parents
#
# for par in parents:
#     print(par.name)

# for path_ in current_dir.parent.parent.iterdir():
#     if path_.is_file():  # True or false
#         print(path_.name)
#
# print('-'*80)
#
# for path_ in current_dir.parent.parent.iterdir():
#     if path_.is_dir():  # True or false
#         print(path_.name)


# get data from lesson_04

lesson_folder_full_path = str(current_dir.parent)

full_path_to_lesson04_folder = os.path.join(lesson_folder_full_path, 'lesson_04')

for path_ in pathlib.Path(full_path_to_lesson04_folder).iterdir():
    if path_.is_file():  # True or false
        print(path_.name)

print('-'*80)

for path_ in pathlib.Path(full_path_to_lesson04_folder).iterdir():
    if path_.is_dir():  # True or false
        print(path_.name)


for path_ in pathlib.Path(full_path_to_lesson04_folder).parent.parent.iterdir():
    if path_.is_file() and path_.name == 'tst.py':
        print('found', path_)

print('-'*80)


file_to_find = 'exaMPLE.py'
for current_path, folders, files in os.walk(str(base_dir)):
    # print(current_path, folders, files)
    if file_to_find in files:
        # print(os.path.join(current_path, file_to_find))
        pass




test_folder_path =  pathlib.Path(os.path.join(str(base_dir), 'test_folder'))  # base_dir + test_folder
print(test_folder_path)
print('is exist = ', test_folder_path.exists())

test_folder_path.mkdir(exist_ok=True)  # створити теку, exist_ok=True - ігноруй помилку існування папки
print('is exist = ', test_folder_path.exists())

print('-'*80)
new_folders_with_three = pathlib.Path('/home/den/hillel/hilllel_1609/test_folder/first/second/last')

print('is exist = ', new_folders_with_three.exists())
new_folders_with_three.mkdir(parents=True, exist_ok=True)
print('is exist = ', new_folders_with_three.exists())

print('-'*80)
# new_folders_with_three.rmdir()  # видалити порожню папку
print('is exist = ', new_folders_with_three.exists())


with open(str(new_folders_with_three) + '/asd.txt', 'w') as f:  #  створити файл
    pass

os.remove(str(new_folders_with_three) + '/asd.txt') # видаляє файл
# shutil.rmtree(path=test_folder_path)  # видалити всі папки по сучасному шляху, аналог rm -rf
# print('is exist = ', new_folders_with_three.exists())


# os.system('ifconfig -a')