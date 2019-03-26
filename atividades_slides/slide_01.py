# coding: utf-8
import requests

url = str(input('Insira a url\nEx: www.uol.com.br\n>>>  '))
response = requests.get('http://%s'%(url))

print(response.status_code)