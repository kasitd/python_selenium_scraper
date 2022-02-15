from crawler.pracuj_crawler import Pracuj
from scraper.collect_data import DataCollection
from scraper.search_result import JobOffer
import asyncio
import aiohttp

# przejdź przez stronę
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
# zbierz wszystkie linki
    links = p.get_all_links()

# asynchronicznie przejdż przez linki zbierając dane
for link in links:

dd = DataCollection(LINK)
page_1 = dd.make_request()
soup_1 = dd.make_soup(page_1)
offer_1 = dd.get_offer(soup_1)

# asynchronicznie wyciągnij dane
j = JobOffer(offer_1)

# stwórz jeden zestaw danych w pamięci
job_title = j.get_job_title()
employer = j.get_employer_name()
city = j.get_city()
contract = j.get_contract_type()
position = j.get_position_name()
mode = j.get_job_mode()
recrutation = j.get_rerutation_type()
if j.no_technologies_provided() == True:
    required_technologies = ['No information provided']
    optional_technologies = ['No information provided']
else:
    required_technologies = j.get_required_technologies()
    optional_technologies = j.get_optionat_technologies()
responsibilities = j.get_responsibilities()
requirement = j.get_requirement()


# zapisz zestaw danych do pliku
file1 = open("raw_data.txt", 'w+')
file1.write({'job_title': job_title,
             'employer': employer,
             'city': city,
             'contract': contract,
             'position': position,
             'mode': mode,
             'recrutation': recrutation,
             'required_technologies': required_technologies,
             'optional_technologies': optional_technologies,
             'responsibilities': responsibilities,
             'requirement': requirement
})
file1.write('/n')
file1.close()

