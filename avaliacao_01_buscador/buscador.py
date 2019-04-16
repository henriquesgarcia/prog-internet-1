#--------------------------------------
# Prova 01 - Programação para Internet
#
# Integrantes: 
#   Raisson Carvalho
#   Henrique Garcia
#--------------------------------------


import requests
from bs4 import BeautifulSoup
import re
import random
import requests_cache


def get_link(soup, url):
    
    internal_link = []

    for link in soup.findAll('a', href=re.compile('^(http|www)((?!' + url + ').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internal_link:
                internal_link.append(link.attrs['href'])

    link = internal_link[random.randint(0, len(internal_link) - 1)]

    return link


def search(url, deth, keyword):

    soup = make_soup(url)
    
    print('\n***** Buscador.py *****\n')
    print('URL: ' + url, '\n---------------------------------------')
    search_keyword(url, keyword)
    link = get_link(soup, url)

    links = get_all_links_to_search(url, deth)

    for link in links:
        print('---------------------------------------')
        print('Link: ' +link)
        search_keyword(link, keyword)
    
    requests_cache.core.remove_expired_responses()


def search_keyword(url, keyword):

    soup = make_soup(url)
    index = soup.text.find(keyword)

    print(soup.text[index - 30:index + 40], '\n')


def make_soup(url):

    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, 'html5lib')

    return soup


def get_all_links_to_search(url, deth):

    links = []
    soup = make_soup(url)
    link = get_link(soup, url)

    for i in range(deth):
        new_soup = make_soup(link)
        new_link = get_link(new_soup, link)
        links.append(new_link)

    return links


if __name__ == '__main__':
    requests_cache.install_cache(cache_name='buscador_cache', backend='sqlite', expire_after=15)
    # requests_cache.clear()
    search('https://pt.wikipedia.org', 3, 'goleador')

    # https://pt.wikipedia.org
    # https://store.steampowered.com/search/