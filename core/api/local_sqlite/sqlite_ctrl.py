from core.api.rest_base import RestBase


class SqLiteCtrl(RestBase):

    def __init__(self, url='http://127.0.0.1:8080/'):
        self.url = url

    def get_students(self, status_code=200):
        """
        send request to get  /students
        """

        url = f'{self.url}students/'

        return self._execute_request(method='get', url=url, status_code=status_code)

    def get_student(self, student_id, status_code=200):
        """
        send request to get  /students/{student_id}/
        """

        url = f'{self.url}students/{student_id}/'

        return self._execute_request(method='get', url=url, status_code=status_code)

    def crate_student(self, json=None, status_code=200):
        """
        send request to post  /students/
        """

        url = f'{self.url}students/'

        return self._execute_request(method='post', url=url, json=json, status_code=status_code)
