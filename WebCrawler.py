#! /usr/bin/env python3

import requests
from bs4 import BeautifulSoup as bs


def writeTitle(titulo, arquivo):
    with open(arquivo, "w") as file:
        file.write("___________________________________" + "\n")
        file.write(titulo.string.encode("UTF-8") + "\n")
        file.write("___________________________________" + "\n")


def writeNew(noticias, arquivo):
    with open(arquivo, "a") as file:
        for noticia in noticias:
            file.write("NOTICIA:" + "\n")
            file.write("===================================================================" + "\n")
            file.write(noticia.string.encode("UTF-8") + "\n")
            file.write("===================================================================" + "\n")

if __name__ == "__main__":

    arquivo = "noticias-bbc.txt"

    pagina = requests.get('https://www.bbc.com/portuguese')
    conteudo = bs(pagina.content, 'html.parser')
    noticias = conteudo.findAll('span', {'class': 'title-link__title-text'})
    titulo = conteudo.find('title')

    writeTitle(titulo, arquivo)
    writeNew(noticias, arquivo)

    print('\n')
    print('SITE:')
    print('___________________________________')
    print(titulo.string)
    print('___________________________________')
    print('\n')

    for noticia in noticias:
        print('NOTICIA:')
        print('===================================================================')
        print(noticia.string)
        print('===================================================================')
        print('\n')
