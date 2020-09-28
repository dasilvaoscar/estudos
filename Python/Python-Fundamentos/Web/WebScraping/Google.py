from selenium import webdriver
import os
os.environ["PATH"] += os.pathsep + r'I:\WebDriver'


class Google(object):
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://google.com.br'
        self.search_bar = 'gLFyf'
        self.bind_buttom = 'btnK'

    def navigate(self):
        self.driver.get(self.url)

    def search(self, word='None'):
        self.driver.find_element_by_class_name(self.search_bar).send_keys(word)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_name(self.bind_buttom).click()


class Main(Google):
        ff = webdriver.Firefox()
        g = Google(ff)
        g.navigate()
        g.search('Django 2.2.3')