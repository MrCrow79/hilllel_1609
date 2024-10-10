with open('main') as f:  # contex manager
    print(f.read())


try:
    f = open('main')
    print(f.read())

finally:
    f.close()

# __enter__
# __exit__

class DBConnect():

    def __init__(self, db_str):
        pass

    def __enter__(self):
        print('Enter method')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exit method')


with DBConnect('asd') as f:
    1/0

