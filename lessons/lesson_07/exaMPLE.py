def say_hello_for_all_people(*people, greeting_start, **kwargs):


    names = remove_retired_persons(list(people))
    names = [change_name_to_correct(name) for name in names]

    if kwargs.get('separator'):
        separator = kwargs['separator']
    print(greeting_start, *names, sep=separator)

    if kwargs.get('emails'):
        send_email(kwargs.get('emails'))


def change_name_to_correct(name: str):
    return name.title()


def remove_retired_persons(people: list):

    for k in ['Den', 'Alex']:
        if k in people:
            people.remove(k)
    return people

def send_email(emails):
    print(f'sending emails to {emails}')


say_hello_for_all_people(*['Ivan', 'Kostia', 'Den'],
                         greeting_start='Hey guys: ', separator=' Mr/Ms ', emails=['asd@asd.com', 'google@google.com'])
