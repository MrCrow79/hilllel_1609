# username, paassword test_user, test_pass

import requests

token = requests.post('http://127.0.0.1:8080/auth',
                     auth=requests.auth.HTTPBasicAuth(username='test_user', password='test_pass'))

# token = requests.post('http://127.0.0.1:8080/auth',
#                      headers={
#                         'Authorization': 'Basic dGVzdF91c2VyOnRlc3RfcGFzcw=='
#                      })

print(token.text)
token = token.json()['access_token']

get_all_cars = requests.get(url='http://127.0.0.1:8080/cars',
                            headers={'Authorization': f'Bearer {token}'})

print(get_all_cars.status_code)
print(get_all_cars.json())