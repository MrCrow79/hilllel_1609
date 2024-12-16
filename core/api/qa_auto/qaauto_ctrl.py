from core.api.qa_auto.schema_check import CurrentSchema
from core.api.rest_base import RestBase
from settings import settings



class QAAutoCtrl(RestBase):

    def __init__(self, url=settings.QAAUTO_BASE_API_URL):
        self.url = url
        self.cookies = None

    def login(self, json=None, status_code=200):
        """
        send request to get  /auth/signin
        """
        url = f'{self.url}/auth/signin'

        response = self._execute_request(method='post', url=url, json=json, status_code=status_code)
        self.cookies = dict(response.cookies)
        return response

    def get_current(self, status_code=200, use_cookies=True, check_schema=True):
        """
        send request to get  /users/current
        """

        url = f'{self.url}/users/current'

        cookies = self.cookies if use_cookies else None

        response = self._execute_request(method='get', url=url, status_code=status_code, cookies=cookies)
        if check_schema:
            CurrentSchema().load(response.json())
        return response


