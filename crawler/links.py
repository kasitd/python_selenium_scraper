import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class Links:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def get_links(self):
        link_list = []
        try:
            links = self.driver.find_elements(By.CSS_SELECTOR, 'a.offer-details__title-link')
            for link in links:
                link_list.append(link.get_attribute('href'))
        except (NoSuchElementException, TimeoutException):
            print("collected links")
            return link_list

    def get_number_of_pages(self):
        time.sleep(5)
        try:
            element = self.driver.find_element(By.ID,
                     'pagination-under-results').find_elements(By.TAG_NAME, 'li')
            return max([e.text for e in element if e!=''])

        except (NoSuchElementException, TimeoutException):
            return False

    def land_next_pagination_page(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 'a.pagination_trigger')))
            element.click()
            print("clickes pagination")
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def get_all_links(self):
        link_list = self.get_links()
        number = self.get_number_of_pages()
        for n in range(number-1):
            self.land_next_pagination_page()
            link_list.append(self.get_links())
        print("got all links")
        return link_list