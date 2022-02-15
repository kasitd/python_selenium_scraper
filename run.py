from crawler.pracuj_crawler import Pracuj
from scraper.collect_data import DataCollection
from scraper.search_result import JobOffer
import asyncio
import aiohttp
import itertools
import os
import json
import requests
from bs4 import BeautifulSoup
import aiofiles


# przejdź przez stronę
"""def get_all_links():
    with Pracuj() as p:
        p.land_first_page()
        p.accept_cookies()
        p.enter_keyword("python")
        p.select_jobs_types()
        p.select_hybrid_jobs()
        p.select_remote_jobs()
        p.select_job_levels()
        p.select_junior_specialist_jobs()
        p.accept_selection()
        list2d = p.get_all_links()
        flat_list = list(itertools.chain.from_iterable(list2d))
        temp = []

        # zbierz wszystkie linki
        for link in list2d:
            if type(link) == str:
                temp.append(link)
            if type(link) == list:
                for l in link:
                    temp.append(l)
        #all_links = '\n'.join(temp)
        return temp
print(get_all_links())"""

links = ['https://www.pracuj.pl/praca/junior-it-specialist-warszawa,oferta,1001529849?sort=0&s=187b3cc0', 'https://www.pracuj.pl/praca/intern-in-account-payable-team-vba-warszawa,oferta,1001544282?sort=0&s=187b3cc0']
link = 'https://www.pracuj.pl/praca/junior-it-specialist-warszawa,oferta,1001529849?sort=0&s=187b3cc0'

# stwórz jeden zestaw danych w pamięci


# asynchronicznie wyciągnij dane
async def get_site_content(link, session):
    async with session.get(link) as resp:
        text = await resp.read()

    soup = BeautifulSoup(text, 'html.parser')
    offer = JobOffer(DataCollection().get_offer(soup))

    offer_dict = await create_offer_dict(offer)
    return offer_dict


async def create_offer_dict(offer):
    offer_dict = {'job_title': offer.get_job_title(),
                  'employer': offer.get_employer_name(),
                  'city': offer.get_city(),
                  'contract': offer.get_contract_type(),
                  'position': offer.get_position_name(),
                  'mode': offer.get_job_mode(),
                  'recrutation': offer.get_rerutation_type(),
                  'required_technologies': offer.get_required_technologies(),
                  'optional_technologies': offer.get_optionat_technologies(),
                  'responsibilities': offer.get_responsibilities(),
                  'requirement': offer.get_requirement()
                  }
    return offer_dict


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
        async with aiofiles.open("raw_data.txt", 'w+') as new_file:
            await new_file.write(str(offer_data))

        return offer_data

    except Exception as err:
        print(f"An error ocurred: {err}")



def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_all_site_content(links))


if __name__ == '__main__':
    main()




"""
# zapisz zestaw danych do pliku
file1 = open("raw_data.txt", 'w+')
file1.write()
file1.write('/n')
file1.close()

"""