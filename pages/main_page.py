from selenium.webdriver.common.by import By

from pages.base_page import Page



class MainPage(Page):
    def open_main(self):
        self.driver.get('https://www.target.com/')
