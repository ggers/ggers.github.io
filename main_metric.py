from urllib.parse import urlencode
import requests

APP_ID = '9d5ed9221c594cc38ca235e447cb3243'
URL = 'https://oauth.yandex.ru/authorize'

My_URL = 'https://ggers.github.io./'

auth_data = {
    'response_type': 'token',
    'client_id': APP_ID
}

#print("?".join((URL, urlencode(auth_data))))
TOKEN = 'AQAAAAAAhvkvAAUiTkBg8fOqj0Mltwx_r3nlI4k'

class YaApiUser():

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Authorization': 'OAuth {}'.format(TOKEN)
        }

    @property
    def counters(self):
        response = requests.get('https://api-metrika.yandex.ru/management/v1/counters', headers=self.get_headers())
        return [c['id'] for c in response.json()['counters']]

    def get_counter_info(self, counterId):
        response = requests.get('https://api-metrika.yandex.ru/management/v1/counter/{}'.format(counterId), headers=self.get_headers())
        return response.json()

    def get_accounts(self):
        response = requests.get('https://api-metrika.yandex.ru/management/v1/counters', headers=self.get_headers())
        return response.json()['accounts']

user1 = YaApiUser(TOKEN)
print(user1.counters)

counter_list = user1.counters
for i in counter_list :
    print(user1.get_counter_info(i))