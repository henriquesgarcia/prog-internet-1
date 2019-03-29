# coding: utf-8
import requests
import re


def questao_03():

    print('\n----- Questão 03 -----\n')

    url = str(input('Insira a url:\n>>>  '))
    response = requests.get(url)

    link_href = re.compile(r'href="(.*?)"')
    list_links = []
    
    for linha in response.text:
        list_links += link_href.findall(linha)
    
    return list_links


def questao_02(url):

    # link da imagem:  https://studiosol-a.akamaihd.net/uploadfile/letras/fotos/b/7/0/8/b708789ed8080c2c84c2e2fef367b1d5.jpg

    response = requests.get(url)

    if response.status_code == 200:

        with open("/Users/enriq/Downloads/imagem_baixada.jpg", "wb") as arquivo:
            arquivo.write(response.content)
        
        print('Download concluído...')


def questao_01(url):

    response = requests.get('http://%s'%(url))

    print('Status Code: ', response.status_code)
    print('Cabeçalhos: ', response.headers)
    print('Tamanho da resposta: ', len(response.headers))
    print('Corpo da resposta: \n', response.text)


def menu():

    print('\n----- Atividade do Slide 01 -----\n')
    print('1 - Questão 01 (status, headers, length and body)\n')
    print('2 - Questão 02 (baixar imagem)\n')
    print('3 - Questão 03 (encontrar links)\n')
    print('\n0 - Sair')


def main():

    while True:
        
        menu()
        opcao = int(input('>>> '))

        if opcao == 1:

            print('\n----- Questão 01 -----\n')
            url_input = str(input('Insira a url\nEx: www.uol.com\n>>>  '))
            questao_01(url_input)

        elif opcao == 2:

            print('\n\n----- Questão 02 -----\n')
            url_input = str(input('Insira a url\n>>>  '))
            questao_02(url_input)

        elif opcao == 3:

            print('\n\n----- Questão 03 -----\n')
            url_input = str(input('Insira a url\n>>>  '))
            questao_03(url_input)
            print('Links encontrados: \n ',questao_03())
            
        elif opcao == 0:
            print('Finalizando...\n')
        
            
            quit()


if __name__ == "__main__":
    main()