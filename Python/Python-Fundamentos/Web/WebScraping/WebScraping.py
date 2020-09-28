from selenium import webdriver  # pip install selenium
import os

os.environ["PATH"] += os.pathsep + r'I:\WebDriver'  # Mostra o local onde foi descompactador o geckodriver
browser = webdriver.Firefox()

browser.get('http://twitter.com')