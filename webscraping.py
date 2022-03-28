'''

                        O QUE É WEB SCRAPING?

     Um web scraper é uma ferramenta de coleta de dados web, uma forma de mineração que permite
 a extração de dados de sites da web convertendo-os em informação estruturada para posterior
 análise.

    Bibliotecas:

- BeautifulSoup: é uma biblioteca de extração de dados de arquivos HTML e XML.

- Requests: permite que você envie solicitações HTTP em Python

'''

from bs4 import BeautifulSoup

import requests

site = requests.get('https://www.climatempo.com.br/').content
#objeto site recebendo todo o conteúdo da requisição http do site climatempo.com.br
soup = BeautifulSoup(site, 'html.parser')
#objeto soup baixando do site html
print(soup.prettify())
#transforma html em string e o print vai exibir o html

