import this
import requests
from bs4 import BeautifulSoup as bs

pagina = requests.get('https://www.bbc.com/portuguese')
conteudo = bs(pagina.content, 'html.parser')
noticias = conteudo.findAll('span', {'class': 'title-link__title-text'})
titulo = conteudo.find('title')

print('\n')
print('___________________________________')
print(titulo.string)
print('___________________________________')
print('\n')

for noticia in noticias:
    print('===================================================================')
    print(noticia.string)
    print('===================================================================')
    print('\n')
