# coding: utf-8
import requests

print('----- Questão 01 -----\n')

url = str(input('Insira a url\nEx: www.uol.com\n>>>  '))
response = requests.get('http://%s'%(url))

print('Status Code: ', response.status_code)
print('Cabeçalhos: ', response.headers['content-type'])
print('Tamanho da resposta: ', response.headers['content-length'])
print('Corpo da resposta: \n', response.text)

#---------------------------------------------------------

print('----- Questão 02 -----\n')

