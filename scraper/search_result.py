import requests
from bs4 import BeautifulSoup as BS
import re


class JobOffer():
    def __init__(self, offer):
        self.offer = offer

    def get_job_title(self):
        return self.offer.find('h1', {'data-scroll-id': 'job-title'}).get_text()

    def get_employer_name(self):
        employer_name = self.offer.find('h2', {'data-scroll-id': 'employer-name'}).get_text()
        text_firma = 'O firmie'
        text_company = 'About the company'
        if text_firma in employer_name:
            pattern = re.compile(text_firma)
        else:
            pattern = re.compile(text_company)
        return pattern.split(employer_name)[0]

    def get_city(self):
        city = self.offer.find('div', {'data-test': 'text-benefit'}).get_text()
        return city.split(', ')[0]

    def get_contract_type(self):
        try:
            contract = self.offer.find(
                'div', {'data-test': 'sections-benefit-contracts-text'}).get_text()
            return contract.split(', ')
        except:
            None

    def get_position_name(self):
        position = self.offer.find('div',
                                   {'data-test':
                                        'sections-benefit-employment-type-name-text'}).get_text()

        return position.split(', ')

    def get_job_mode(self):
        try:
            mode = self.offer.find('div',
                                   {'data-test': 'sections-benefit-work-modes-text'}).get_text()
            return mode.split(', ')
        except:
            None

    def get_rerutation_type(self):
        try:
            recrutation = self.offer.find('div', {'data-test' : 'sections-benefit-remote-recruitment-text'}).get_text()
            return recrutation.split(', ')
        except:
            None
    def get_technolofgies(self):
        try:
            technologies = self.offer.find('div', {'data-scroll-id': 'technologies-1'})
        except:
            None


# może dobrze byłoby wydzielić oddzielną klasę

    def no_technologies_provided(self):
        technologies = self.get_technolofgies()
        if  technologies == None:
            return True
        else:
            return False


    def get_required_technologies(self):
        if self.no_technologies_provided():
            try:
                req = self.offer.find('div', {'data-test': 'section-technologies-expected'})
                return [elem.get_text() for elem in req.find_all('p')]
            except:
                None

    def get_optionat_technologies(self):
        if self.no_technologies_provided():
            try:
                req = self.offer.find('div', {'data-test': 'section-technologies-optional'})
                return [elem.get_text() for elem in req.find_all('p')]
            except:
                None

    def get_responsibilities(self):
        try:
            resp = self.offer.find('div', {'data-scroll-id': 'responsibilities-1'})
            return [elem.get_text() for elem in resp.find_all('p')]
        except:
            None

    def get_requirement(self):
        try:
            req = self.offer.find('div', {'data-scroll-id': 'requirements-1'})
            return [elem.get_text() for elem in req.find_all('p')]
        except:
            None
