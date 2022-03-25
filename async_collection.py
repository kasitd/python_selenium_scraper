import asyncio
import aiohttp
import itertools
import os
import json
import requests
from bs4 import BeautifulSoup
import aiofiles
import time
import csv
from datetime import date
from selenium.webdriver.support import expected_conditions as EC
from scraper.collect_data import DataCollection
from scraper.search_result import JobOffer



async def get_site_content(link, session):
    async with session.get(link) as resp:
        page_html = await resp.read()

    site_content_list = await DataCollection(page_html).collect_job_details()
    return site_content_list



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
            print(offer_list)
            #file_writer.writerows(offer_list)

    except FileNotFoundError:
        print("Output file not present", 'raw_data.csv')
        print("Current dir: ", os.getcwd())
        raise FileNotFoundError