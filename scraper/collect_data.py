import requests
from bs4 import BeautifulSoup, SoupStrainer
import re
from crawler.pracuj_crawler import Pracuj
import asyncio


class DataCollection:
    def __init__(self):
        pass

    def strain_soup(self):
        return SoupStrainer('div', attrs={'data-test': 'section-offerView'})

    def make_soup(self, response):
        strainer = self.strain_soup()
        return BeautifulSoup(response, 'html.parser', parse_only=strainer)
    """def show_offer(self, offer):
        print(offer.prettify())"""





