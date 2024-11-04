class User:

    def __init__(self, name, password, site_url):  # конструктор

        self.name = name
        self.password = password
        self.site_url = site_url


    def login(self):
        print(f'User {self.name} was logged in {self.site_url}')


    def logout(self):
        print(f'User {self.name} was logged out {self.site_url}')


dev_user = User('dev_user', 'dev_password', 'http://dev-something.org')  # створення інстанса

print(dev_user.name)  # атрибут, властивість

dev_user.login()  # метод
dev_user.logout()  # метод






stage_user = User('stage_user', 'stage_password', 'http://stage-something.org')
prod_user = User('prod_user', 'prod_password', 'http://prod-something.org')