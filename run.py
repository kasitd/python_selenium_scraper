from crawler.pracuj_crawler import Pracuj
from scraper.collect_data import DataCollection
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from async_collection import get_site_content, get_all_site_content
from create_csv import write_into_csv_file
import asyncio
from slow_collection import get_all_site_content
import traceback
import logging

def main():
    try:
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
        if data_list == None:
            print("Couldn't collect data.")
            print("You might have been blocked by the site")
            try:
                get_all_site_content(links)
                write_into_csv_file(data_list)
            except:
                TypeError
                print("Couldn't collect data.")
    except Exception as e:
        logging.error(traceback.format_exc())
    p.close_browser()
    print("closed browser")
    print("finished")




if __name__ == '__main__':
    main()

