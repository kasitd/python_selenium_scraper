import requests
from bs4 import BeautifulSoup, SoupStrainer
import re
from crawler.pracuj_crawler import Pracuj
import asyncio


class DataCollection:
    def __init__(self):
        pass

    def make_request(self, link):
        return requests.get(link)

    def make_soup(self, page):
        return BeautifulSoup(page.content, 'html.parser')

    def get_offer(self, soup):
        return soup.find('div', {'class': 'OfferViewgl652f'})

    """def show_offer(self, offer):
        print(offer.prettify())"""





