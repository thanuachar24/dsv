from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

# Get the first page.
url = 'https://www.gosc.pl/doc/791526.Zaloz-zbroje'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
page_link_el = soup.select('.pgr_nrs a')

# Do more with the first page.

# Make links for and process the following pages.
for link_el in page_link_el:
    link = urljoin(url, link_el.get('href'))
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'lxml')
    print(response.url)
    # Do more with each page.