from django.core.management.base import BaseCommand
import os
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd



class Command(BaseCommand):
    help = "collect jobs"

    def handle(self, *args, **options):

        listaHyperlink = []
        listaMercadoria = []
        ce = self

        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities['acceptSslCerts'] = True
        capabilities['acceptInsecureCerts'] = True

        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        chrome_options.add_argument('--window-size=1280,1696')
        chrome_options.add_argument('--start-maximized')

        driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver'), options=chrome_options,
                                  desired_capabilities=capabilities)

        driver.get("https://www4c.receita.fazenda.gov.br/g33159/jsp/logon.jsp?ind=11")
        driver.find_element(By.XPATH, '//*[@id="cpfsenha"]/table[1]/tbody/tr[2]/td/table/tbody/tr[4]/td[1]/table/tbody/tr[4]/td[2]/div/a').click()
        driver.get("https://www4c.receita.fazenda.gov.br/carga-web/ConsultarDadosBasicosCEMercanteMenu.do")
        consult = driver.find_element(By.XPATH, '//*[@id="principal"]/div/div[1]/div/form/fieldset/p/input')
        consult.send_keys(ce)
        consult.send_keys(Keys.ENTER)

        listaCNT = []
        listaISO = []
        listaTIPO = []
        listaTARA = []
        listaPB = []
        listaM3 = []
        listaIMO = []
        listaCIMO = []

        #bl = driver.find_element(By.XPATH, '//*[@id="quadro"]/div[1]/div/dl[6]/dd[1]').text
        divGeral = driver.find_element(By.XPATH, '//*[@id="quadro"]/div[1]/div')
        titulos = divGeral.find_elements(By.TAG_NAME, 'dt')
        conteudo = divGeral.find_elements(By.TAG_NAME, 'dd')

        listaTitulos=[]
        listaConteudo=[]

        for item in titulos:
            listaTitulos += {item.text}

        for i in conteudo:
            listaConteudo += {i.text}

        ListasUnidas = zip(listaTitulos, listaConteudo)
        DicionarioCapaCE = dict(ListasUnidas)
        #print(DicionarioCapaCE['Tipo de Conhecimento :'])

        table_cnt = driver.find_element(By.XPATH, '//*[@id="lista-itens-carga"]/form/center/table/tbody')
        rows = table_cnt.find_elements(By.TAG_NAME, "tr")

        for row in rows:
            div = row.find_element_by_tag_name("a")
            hyperlink = div.get_attribute('href')
            listaHyperlink.append(hyperlink)

        for link in listaHyperlink:
            driver.get(link)
            cnt = driver.find_element(By.XPATH, '//*[@id="quadro"]/div[1]/div/dl[1]/dd[1]').text
            listaCNT.append(cnt)
            cntISO = driver.find_element(By.XPATH, '//*[@id="quadro"]/div[1]/div/dl[1]/dd[2]').text
            listaISO.append(cntISO)
            cntTipo = driver.find_element(By.XPATH, '//*[@id="quadro"]/div[1]/div/dl[1]/dd[3]').text
            listaTIPO.append(cntTipo)
            cntTara = driver.find_element(By.XPATH, '//*[@id="quadro"]/div[1]/div/dl[1]/dd[4]').text
            listaTARA.append(cntTara)
            cntPB = driver.find_element(By.XPATH, '//*[@id="quadro"]/div[1]/div/dl[1]/dd[5]').text
            listaPB.append(cntPB)
            m3 = driver.find_element(By.XPATH, '//*[@id="quadro"]/div[1]/div/dl[1]/dd[6]').text
            listaM3.append(m3)
            codIMO = driver.find_element(By.XPATH, '//*[@id="quadro"]/div[1]/div/dl[1]/dd[8]').text
            listaIMO.append(codIMO)
            clasIMO = driver.find_element(By.XPATH, '//*[@id="quadro"]/div[1]/div/dl[1]/dd[9]').text
            listaCIMO.append(clasIMO)

        #lista = [bl, repcnpj, reprazao, emissao, situacao, modalidade, pOrigem, psProcede, UFdestino]
        listaMercadoria = [listaCNT, listaISO, listaTIPO, listaTARA, listaPB, listaM3, listaIMO, listaCIMO]
        print(listaMercadoria)
        driver.quit
        driver.close

        return DicionarioCapaCE, listaMercadoria



#ce = '172005123371986'
#ce = '182005050108960'
#ce = '172005133732108'
#Command.handle(ce)