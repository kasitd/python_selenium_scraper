from selenium.webdriver.remote.webdriver import WebDriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class Filter:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def enter_keyword(self, keyword):
        time.sleep(4)
        try:
            search_bar = self.driver.find_element(By.CSS_SELECTOR, 'input.autocomplete-item__field')
            search_bar.clear()
            search_bar.send_keys(keyword)
            search_bar.send_keys(Keys.RETURN)
            print("entered keyword")
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def select_jobs_types(self):
        try:
            work_form = self.driver.find_element(By.XPATH, '//*[contains(text(), "Tryb pracy")]')
            work_form.click()
            time.sleep(4)
            print("selected job types")
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def select_hybrid_jobs(self):
        try:
            hybrid = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[contains(text(), "Praca hybrydowa")]')))
            hybrid.click()
            print("selected hybrid jobs")
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def select_remote_jobs(self):
        try:
            remote = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[contains(text(), "Praca zdalna")]')))
            remote.click()
            print("selected remote jobs")
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def select_job_levels(self):
        try:
            word_levels = self.driver.find_element(By.XPATH, '//*[contains(text(), "Poziom stanowiska")]')
            word_levels.click()
            print("selected job levels")
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def select_junior_specialist_jobs(self):
        try:
            junior_jobs = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, '//*[contains(text(), "Młodszy specjalista (Junior)")]')))
            junior_jobs.click()
            print("selected junior specialist jobs")
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def accept_selection(self):
        try:
            accept = self.driver.find_element(By.XPATH, '//*[@id="search-filters"]/div[1]/div/ul/li[2]/div/div[3]/div/div/button')
            accept.click()
            print("accepted selection")
            return True
        except (NoSuchElementException, TimeoutException):
            return False