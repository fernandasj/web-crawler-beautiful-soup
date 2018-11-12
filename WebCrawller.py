import this
import requests
from bs4 import BeautifulSoup as bs

pagina = requests.get('https://www.bbc.com/portuguese')
conteudo = bs(pagina.content, 'html.parser')
noticias = conteudo.findAll('span', {'class': 'title-link__title-text'})

for noticia in noticias:
    print('===================================================================')
    print(noticia.string)
    print('===================================================================')
    print('\n')
