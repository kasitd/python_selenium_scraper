from crawler.pracuj_crawler import Pracuj
from scraper.collect_data import DataCollection
from scraper.search_result import JobOffer
import asyncio
import aiohttp
import itertools
import os
import json
import requests
from bs4 import BeautifulSoup, SoupStrainer
import aiofiles
import time
import csv
from datetime import date
from selenium.webdriver.support import expected_conditions as EC



async def get_site_content(link, session):
    async with session.get(link) as resp:
        page_html = await resp.read()

    strainer = DataCollection().strain_soup()
    soup = DataCollection().make_soup(page_html)
    site_content_list = await create_offer_list(soup)
    return site_content_list


async def create_offer_list(soup):
    offer = JobOffer(soup)
    offer_list = [offer.get_job_title(),
                  offer.get_employer_name(),
                  offer.get_city(),
                  offer.get_contract_type(),
                  offer.get_position_name(),
                  offer.get_job_mode(),
                  offer.get_rerutation_type(),
                  offer.get_required_technologies(),
                  offer.get_optionat_technologies(),
                  offer.get_responsibilities(),
                  offer.get_requirement()
                  ]
    return offer_list


# asynchronicznie przejdż przez linki zbierając dane
async def get_all_site_content(links):
    actions = []
    offer_data = []

    try:
        async with aiohttp.ClientSession() as session:
            for link in links:
                actions.append(asyncio.ensure_future(get_site_content(link, session)))
            offer_res = await asyncio.gather(*actions)

            for data in offer_res:
                offer_data.append(data)

        return offer_data

    except Exception as err:
        print(f"An error ocurred: {err}")


def write_into_csv_file(offer_list):
    file_name = f'raw_data{date.today().strftime("%d_%m_%Y")}.csv'
    try:
        with open(file_name, mode='w+', newline='', encoding='utf8') as raw_csv_file:
            filds = ['Job_title',
                     'Employer',
                     'City',
                     'Contract',
                     'Position',
                     'Mode',
                     'Recrutation',
                     'Required_technologies',
                     'Optional_technologies',
                     'Responsibilities',
                     'Requirement']
            file_writer = csv.writer(raw_csv_file)
            file_writer.writerow(filds)
            file_writer.writerows(offer_list)

    except FileNotFoundError:
        print("Output file not present", 'raw_data.csv')
        print("Current dir: ", os.getcwd())
        raise FileNotFoundError

def main():
    p = Pracuj()
    p.land_first_page()
    p.accept_cookies()
    p.accept_popup()

    p.apply_filtrations('python')
    data = p.collect_page_source()
    d = DataCollection(data)
    pages = d.get_number_of_pages()
    links = d.get_single_links_from_page()
    links.extend(d.get_nested_links_from_page())
    for n in range(int(pages)-1):
        p.triger_next_page_button()
        links.extend(d.get_single_links_from_page())
        links.extend(d.get_nested_links_from_page())

    loop = asyncio.get_event_loop()
    data_list = loop.run_until_complete(get_all_site_content(links))
    #write_into_csv_file(data_list)
    print(data_list)



if __name__ == '__main__':
    main()

