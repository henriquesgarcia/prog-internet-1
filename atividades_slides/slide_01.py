# coding: utf-8
import requests

print('----- Questão 01 -----\n')

url = str(input('Insira a url\nEx: www.uol.com\n>>>  '))
response = requests.get('http://%s'%(url))

print('Status Code: ', response.status_code)
print('Cabeçalhos: ', response.headers['content-type'])
print('Tamanho da resposta: ', response.headers['content-length'])
#print('Corpo da resposta: \n', response.text)

#---------------------------------------------------------

print('\n\n----- Questão 02 -----\n')

# link da imagem:  https://studiosol-a.akamaihd.net/uploadfile/letras/fotos/b/7/0/8/b708789ed8080c2c84c2e2fef367b1d5.jpg
url = str(input('Insira a url\n>>>  '))
response = requests.get(url)

with open("imagem_baixada.jpg", "wb") as code:
    code.write(response.content)
