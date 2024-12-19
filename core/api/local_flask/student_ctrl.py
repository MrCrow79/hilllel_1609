from core.api.rest_base import RestBase
from settings import settings


class LocalFlaskCtrl(RestBase):

    __headers = None

    def __init__(self, url=settings.flask_url):
        self.url = url
        self.auth()

    def auth(self, status_code=200):
        """
        send request to get  /users/
        """
        if __class__.__headers is not None:
            return

        url = f'{self.url}/auth/'
        name = settings.FLASK_USER_NAME
        password = settings.FLASK_USER_PASSWORD
        response = self._execute_request(method='post', url=url, json={'name': name, 'password': password},
                                     status_code=status_code).text

        __class__.__headers = {'token': response}


    def get_students(self, status_code=200):
        """
        send request to get  /students/
        """

        url = f'{self.url}/students/'

        return self._execute_request(method='get', url=url, status_code=status_code)


    def get_student(self, student_id: int, status_code=200):
        """
        send request to get  /students/{student_id}
        """

        url = f'{self.url}/students/{student_id}'

        return self._execute_request(method='get', url=url, status_code=status_code)


    def create_students(self, json_body: dict, status_code=201):
        """
        send request to get  /users/
        """

        url = f'{self.url}/students/'

        return self._execute_request(method='post', url=url, json=json_body, headers=self.__headers,
                                     status_code=status_code)
