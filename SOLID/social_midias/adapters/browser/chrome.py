import webbrowser

from base.abstract_browser import AbstractBrowser

class Chrome(AbstractBrowser):
  
  def __init__(self, url, browser = webbrowser) -> None:
    self._url = url
    self._browser = browser
  
  def open(self):
    self._browser.get("google-chrome").open(self._url)
    
    