import time

from scraper.collect_data import DataCollection
from crawler.pracuj_crawler import Pracuj


def get_site_content(link):
    p = Pracuj(link)
    time.sleep(5)
    p.land_first_page()
    time.sleep(5)
    p.accept_cookies()
    page_html = p.collect_page_source()
    p.close_browser()

    site_content_list = DataCollection(page_html).collect_job_details()
    return site_content_list

# asynchronicznie przejdż przez linki zbierając dane
def get_all_site_content(links):
    actions = []
    offer_data = []

    for link in links:
        offers = DataCollection(get_site_content(link))
        print(offers)
        data = offers.collect_job_details()
        print(data)
        for data in offers:
                offer_data.append(data)
        return offer_data



