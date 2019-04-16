# coding: utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random


def getLinks(articleUrl):
    html = urlopen('https://pt.wikipedia.org' + articleUrl)
    soup = BeautifulSoup(html, 'html5lib')
    soup.prettify()

    return soup.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))


links = getLinks('/wiki/Raspagem_de_dados')

for link in range(10):
    newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)
    newHtml = urlopen('https://pt.wikipedia.org' + newArticle)
    newSoup = BeautifulSoup(newHtml, 'html5lib')
    keyword = newSoup.text.upper().find('DADOS')

    print(newSoup.text[keyword - 30:keyword + 40], '\n')

# def search(url, deth, keyword):
#     links = getLinks(url)
#     newLink = links[random.randint(0, len(links)-1)].attrs["href"]
#     print(newLink)
#     for links in range(deth):



# ------------------------------------------------------
# ACHO QUE TA BOM KKK:
#
#
# import requests
# from bs4 import BeautifulSoup
# import re
# import random
#
#
# def getLink(soup, url):
#     internalLink = []
#
#     for link in soup.findAll('a', href=re.compile('^(http|www)((?!' + url + ').)*$')):
#         if link.attrs['href'] is not None:
#             if link.attrs['href'] not in internalLink:
#                 internalLink.append(link.attrs['href'])
#
#     link = internalLink[random.randint(0, len(internalLink) - 1)]
#
#     return link
#
#
# # Terminando esse método
# def search(url, deth, keyword):
#     soup = make_soup(url)
#     print('URL: ' + url, '\n---------------------------------------')
#     search_keyword(url, keyword)
#     print('---------------------------------------')
#     link = getLink(soup, url)
#     print(link)
#
#     links = getAllLinksToSearch(url, deth)
#
#     for link in links:
#         print('Link: ' +link)
#         search_keyword(link, keyword)
#
# def search_keyword(url, keyword):
#     soup = make_soup(url)
#     index = soup.text.find(keyword)
#     print(soup.text[index - 10:index + 10], '\n')
#
#
# def make_soup(url):
#     response = requests.get(url, timeout=5)
#     soup = BeautifulSoup(response.text, 'html5lib')
#
#     return soup
#
#
# def getAllLinksToSearch(url, deth):
#     links = []
#     soup = make_soup(url)
#     link = getLink(soup, url)
#     for i in range(deth-1):
#         newSoup = make_soup(link)
#         newLink = getLink(newSoup, link)
#         links.append(newLink)
#
#     return links
#
#
# if __name__ == '__main__':
#     search('https://pt.wikipedia.org', 3, 'desempenho')