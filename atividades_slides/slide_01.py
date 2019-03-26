# coding: utf-8
import requests


def questao_03():
    print('\n----- Questão 03 -----\n')

    url = str(input('Insira a url:\n>>>  '))
    response = requests.get(url)


def questao_02():

    print('\n\n----- Questão 02 -----\n')

    # link da imagem:  https://studiosol-a.akamaihd.net/uploadfile/letras/fotos/b/7/0/8/b708789ed8080c2c84c2e2fef367b1d5.jpg

    url = str(input('Insira a url\n>>>  '))
    response = requests.get(url)

    with open("/Users/enriq/Downloads/imagem_baixada.jpg", "wb") as arquivo:
        arquivo.write(response.content)


def questao_01():

    print('\n----- Questão 01 -----\n')

    url = str(input('Insira a url\nEx: www.uol.com\n>>>  '))
    response = requests.get('http://%s'%(url))

    print('Status Code: ', response.status_code)
    print('Cabeçalhos: ', response.headers['content-type'])
    print('Tamanho da resposta: ', len(response.headers['content-length']))
    print('Corpo da resposta: \n', response.text)


def menu():

    print('\n----- Atividade do Slide 01 -----\n')
    print('1 - Questão 01\n2 - Questão 02\n3 - Questão 03')


def main():

    while True:
        
        menu()
        opcao = int(input('>>> '))

        if opcao == 1:
            questao_01()
        elif opcao == 2:
            questao_02()
        elif opcao == 3:
            print('fim')
        else:
            print('Finalizando...\n')
            quit()


if __name__ == "__main__":
    main()