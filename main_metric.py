from urllib.parse import urlencode
#import requests

APP_ID = '02c3896d5dbf45d0a7b4270349918882'
URL = 'https://oauth.yandex.ru/authorise'

auth_data = {
    'response_type': 'token',
    'client_id': APP_ID
}

print("?".join((URL, urlencode(auth_data))))