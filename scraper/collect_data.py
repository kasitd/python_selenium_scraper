from bs4 import BeautifulSoup, SoupStrainer
from crawler.pracuj_crawler import Pracuj


class DataCollection:
    def __init__(self, response):
        self.soup =  BeautifulSoup(response, 'html.parser')


    def get_number_of_pages(self):
        return self.soup.find('span', {'class': 'pagination_label--max'}).get_text()[2:]

    def get_single_links_from_page(self):
        return [a['href'] for a in self.soup.find_all('a', {'class': 'offer-details__title-link'}, href=True)]

    def get_nested_links_from_page(self):
        return [a['href'] for a in self.soup.find_all('a', {'class': 'offer-regions__label'}, href=True)]







