import os
from urllib.request import urlopen
from bs4 import BeautifulSoup

class RequisicaoGet(object):

    def __init__(self):
        self.site = 'http://google.com'

    def SetSite(self, site):
        self.site = site

    def GetSite(self):
        return self.site

    def MostraTemplateHtml(self):
        pagina = urlopen('http://' + self.site)
        bs4 = BeautifulSoup(pagina, 'lxml')
        result = print(bs4)
        return result

    def GerarHMTL(self):
        html = urlopen('http://' + self.site).read()
        mkdir = os.makedirs('arquivo/', exist_ok=True)
        arquivo_html = open('arquivo/gerandoHTML.html', 'wb')
        arquivo_html.write(html)
        arquivo_html.close()
        result = print("Arquivo HTML gerados")
        return result
    

#class Main(RequisicaoGet):

    #obj = RequisicaoGet()
    #obj.SetSite(input('Esqueva um site: '))
    #obj.MostraTemplateHtml()
    #obj.GerarHMTL()

class Bs():
    def __init__(self):
        self.site = "https://google.com"

    def SetUrl(self, site):
        self.site = site

    def GetHtml(self):
        html = urlopen(self.site)
        bs4 = BeautifulSoup(html, "html5lib")

        return bs4

class Main(Bs):
    var = Bs()
    var.SetUrl("https://youtube.com")
    print(var.GetHtml().head)




