import requests
from bs4 import BeautifulSoup as BS
import re
from crawler.pracuj_crawler import Pracuj

LINK = ['https://www.pracuj.pl/praca/tester-oprogramowania-sopot,oferta,1001544351?sort=3&s=187b3cc0',
'https://www.pracuj.pl/praca/data-engineer-krakow,oferta,1001490347?sort=4&s=187b3cc0']


class DataCollection:
    def __init__(self, link):
        self.link = link

    def make_request(self):
        return requests.get(self.link)

    def make_soup(self, page):
        return BS(page.content, 'html.parser')

    def get_offer(self, soup):
        return soup.find('div', {'class': 'OfferViewgl652f'})

    """def show_offer(self, offer):
        print(offer.prettify())"""





