class User:

    def __init__(self, name, password, site_url, height=175):  # конструктор

        self.name = name
        self.password = password
        self.site_url = site_url
        self.finished_courses = []
        self.height = height

    # def __len__(self):  # при виклику len()
    #     return len(self.finished_courses)

    def __len__(self):  # при виклику len()
        return self.height


    def __eq__(self, other_obj):  # a == b

        if isinstance(other_obj, User):
            print(f'current user has height={self.height}, another user has height={other_obj.height}')
            return self.height == other_obj.height

        print('Can\'t compare 2 objects')
        return False

    def __str__(self):  # при виклику str()
        return f'User: {self.name}, url: {self.site_url}'

    def __repr__(self):  # representation,  # при виклику repr()
        return f'User(name=\'{self.name}\', password=\'{self.password}\', site_url=\'{self.site_url}\')'


    def __gt__(self, other_obj):  # a > b
        if isinstance(other_obj, User):
            return self.height > other_obj.height
        return False

    def __le__(self, other_obj):  # a <= b
        if isinstance(other_obj, User):
            return self.height <= other_obj.height
        return False


den = User('Den', 'Den', 'google.com')
ivan = User('Ivan', 'Den', 'google.com', height=180)

print(den > ivan)  # == not (ivan < den)
print(den < ivan)

print(den <= ivan)
print(ivan <= den)


print(den.__dict__)

den.finished_courses.append('math')
den.finished_courses.append('phil')

# print(den == ivan)
# print(den == den)
# print(den == 5)
#
# print(st.finished_courses)
# print(len(st))
# st.finished_courses.append('phil')
#
#
# print(st.finished_courses)
# print(len(st))