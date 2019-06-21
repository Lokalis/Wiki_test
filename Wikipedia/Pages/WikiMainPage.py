
import time



class WikiMainHelper():

    links={"home":"https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0"}

    xpath={"search":"//input[@id='searchInput']",
           "table":"//h1[@id='firstHeading']",
           "logo_wiki":"//a[@class='mw-wiki-logo']",
           "upper_buttons":"//div[@id='p-namespaces']",
           "search_all":"//div[@class='suggestions']/a[1]",
           }

    css={

        }

    def __init__(self, app):
        """Init driver"""
        self.app = app
        self.driver = self.app.driver

    def find_xpath(self, selector):
        """Find and return element"""
        element = self.driver.find_element_by_xpath(self.xpath[selector])
        return element

    def find_all_xpath(self,selector):
        """Find and return list elements"""
        element=self.driver.find_elements_by_xpath(selector)
        return element

    def click_element(self, element):
        """Find element on page and click"""
        self.driver.find_element_by_xpath(self.xpath[element]).click()
        return

    def type_words(self,element,words):
        """Enter words on form in page"""
        self.driver.find_element_by_xpath(self.xpath[element]).send_keys(words)

    def expectation_words(self, element,words):
        """Finding words on page"""
        client=self.driver.find_elements_by_xpath(self.xpath[element])
        for text in client:
            if words in text.text:
                return True
        for text in client: # If words not finding - print all, that have selector
            try:
                print(" "+text.text,end=" ")
            except:
                print("That are not text")
        return False

    def submitt(self,element):
        """Submit element"""
        element.submit()

    def search(self,find_words):
        """Global search on Wiki"""
        element=self.driver.find_element_by_xpath(self.xpath["search"])
        element.send_keys(find_words)
        element.submit()

    def go_to(self,link):
        self.driver.get(self.links[link])

    def home(self):
        """Redirect on home page"""
        self.driver.get(self.links["home"])


class SuperWiki(WikiMainHelper):

    def __init__(self, app):
        """Init driver"""
        self.app = app
        self.driver = self.app.driver

    def search_all_results(self,find_words):
        self.type_words("search",find_words)
        self.click_element("search_all")
