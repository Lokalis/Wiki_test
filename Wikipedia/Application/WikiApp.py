from selenium import webdriver
from Pages.WikiMainPage import WikiMainHelper
from Pages.WikiMainPage import SuperWiki
class App:

    def __init__(self):
        self.driver = webdriver.Chrome("C://browdriver/chromedriver.exe")
        self.wiki = WikiMainHelper(self)
        self.superwiki=SuperWiki(self)
        self.driver.implicitly_wait(1)

    def open_main_page(self):
         self.driver.get("https://ru.wikipedia.org/wiki")

    def destroy(self):
        self.driver.quit()
