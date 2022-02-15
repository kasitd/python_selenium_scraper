import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from crawler.constants import BASE_URL

class Pracuj(webdriver.Chrome):
    def __init__(self, driver_path = r"\chromedriver", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Pracuj, self).__init__()
        self.implicitly_wait(30)
        self.maximize_window()

# można usunąć po zakończeniu devel.

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(BASE_URL)

    def is_alert_present(self):
        try:
            element = WebDriverWait(self, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR,
                     "#gp-cookie-agreements > div > div > div.g1kqzctt > div.bafq4sb > button")))
            return element
        except NoSuchElementException:
            return False

    def accept_cookies(self):
        if self.is_alert_present():
            self.is_alert_present().click()
        else:
            pass

    def enter_keyword(self, keyword):
        time.sleep(4)
        search_bar = self.find_element(By.CSS_SELECTOR, 'input.autocomplete-item__field')
        search_bar.clear()
        search_bar.send_keys(keyword)
        search_bar.send_keys(Keys.RETURN)


    def select_jobs_types(self):
        work_form = self.find_element(By.XPATH, '//*[contains(text(), "Tryb pracy")]')
        work_form.click()
        time.sleep(4)

# popracować nad bardziej stabilnym wyborem
    def select_hybrid_jobs(self):
        hybrid = WebDriverWait(self, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search-filters"]/div[1]/div/ul/li[5]/div/div[2]/ul/li[2]')))
        hybrid.click()

    def select_remote_jobs(self):
        remote = WebDriverWait(self, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search-filters"]/div[1]/div/ul/li[5]/div/div[2]/ul/li[3]')))
        remote.click()

    # zmienione na 'stażysta' ze względu na testy
    def select_job_levels(self):
        word_levels = self.find_element(By.XPATH, '//*[@id="search-filters"]/div[1]/div/ul/li[2]')
        word_levels.click()

    def select_junior_specialist_jobs(self):
        junior_jobs = self.find_element(By.XPATH, '//*[contains(text(), "Młodszy specjalista (Junior)")]')
        junior_jobs.click()

    def accept_selection(self):
        accept = self.find_element(By.XPATH, '//*[@id="search-filters"]/div[1]/div/ul/li[2]/div/div[3]/div/div/button')
        accept.click()

    # znaleźć sposób na paginację
    def get_links(self):
        link_list = []
        links = self.find_elements(By.CSS_SELECTOR, 'a.offer-details__title-link')
        for link in links:
            link_list.append(link.get_attribute('href'))
        return link_list

    def get_number_of_pages(self):
        element = self.find_element(By.XPATH, '//*[@id="pagination-under-results"]/div/ul')
        number = int(max(element.text))
        return number

    def land_next_pagination_page(self):
        element = self.find_element(By.CSS_SELECTOR, 'a.pagination_trigger')
        element.click()

    def get_all_links(self):
        link_list = self.get_links()
        number = self.get_number_of_pages()
        for n in range(number-1):
            self.land_next_pagination_page()
            link_list.append(self.get_links())
        return link_list