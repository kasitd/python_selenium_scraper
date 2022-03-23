import os
import time
from selenium import webdriver
from crawler.constants import BASE_URL
from selenium.common.exceptions import WebDriverException, NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options
from crawler.filter_selection import Filter

dir_path = os.path.dirname(__file__)
file_name = "/chromedriver.exe"
file_path = dir_path + file_name


class Pracuj:
    """Method responsible for initializing crawler class."""

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        driver_path = file_path
        os.environ["PATH"] += driver_path
        self.driver = webdriver.Chrome(service=Service(driver_path), options=options)
        self.driver.wait = WebDriverWait(self.driver, 10)


    def land_first_page(self):
        self.driver.get(BASE_URL)

    def is_alert_present(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR,
                     "#gp-cookie-agreements > div > div > div.g1kqzctt > div.bafq4sb > button")))
            print("detected allert")
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def accept_cookies(self):
        if self.is_alert_present():
            try:
                element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.CSS_SELECTOR,
                         "#gp-cookie-agreements > div > div > div.g1kqzctt > div.bafq4sb > button"))).click()
                print("cookies accepted")
            except (NoSuchElementException, TimeoutException):
                print("couldn't find element")
        else:
            pass

    def is_popup_present(self):
        time.sleep(5)
        try:
            print("popup present")
            return self.driver.find_element(By.TAG_NAME, 'picture')

        except (NoSuchElementException, TimeoutException):
            print("no popup")
            return False

    def accept_popup(self):
        elemenet = self.is_popup_present()
        if elemenet is not False:
            try:
                elem = self.driver.find_element(By.ID, 'pracuj_footer').find_elements(By.XPATH,".//*")[3].click()
                print("dismissed popuop")
            except (NoSuchElementException, TimeoutException):
                print("couldn't find element")
        pass

    def apply_filtrations(self, keyword):
        try:
            filteration = Filter(self.driver)
            filteration.enter_keyword(keyword)
            filteration.select_jobs_types()
            filteration.select_hybrid_jobs()
            filteration.select_remote_jobs()
            filteration.select_job_levels()
            filteration.select_junior_specialist_jobs()
            filteration.accept_selection()
        except WebDriverException:
            print("couldn't execute function")

    def collect_page_source(self):
        time.sleep(3)
        try:
            return self.driver.page_source
        except WebDriverException:
            print("couldn't execute function")
            self.close_browser()

    def triger_next_page_button(self):
        try:
            WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.CLASS_NAME, "pagination_trigger"))).click()
            print("next page")
        except (NoSuchElementException, TimeoutException):
            print("couldn't find element")

    def close_browser(self):
        self.driver.quit()



