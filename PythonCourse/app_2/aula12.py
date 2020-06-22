import requests

response = requests.get('https://viacep.com.br/ws/{}/json/'.format('13800061'))
print(response.text)