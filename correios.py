"""colocar o bairro como argumento ou escrever em notepad e copiar para área de
transferência """
from selenium import webdriver
import sys,pyperclip
if len(sys.argv) > 1:
    bairro = ' '.join(sys.argv[1:]) 
else:
    bairro = pyperclip.paste()
# versao nova para uso do selenium
url='http://www.buscacep.correios.com.br/sistemas/buscacep/buscaLogBairro.cfm'
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# from selenium.webdriver.support.ui import Select
binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary, executable_path=r'C:\\gecko\geckodriver.exe')
# driver.get('https://siga.cps.sp.gov.br/aluno/login.aspx')
# driver.get('http://www.buscacep.correios.com.br/sistemas/buscacep/buscaLogBairro.cfm')
driver.get(url)
# driver.get('https://gmail.com')
ufElemento = driver.find_element_by_xpath("//select[@name='UF']/option[text()='SP']").click()


emailElem = driver.find_element_by_name('Localidade')
emailElem.send_keys('Campinas')
cidadeElem = driver.find_element_by_name("Bairro")
cidadeElem.send_keys(bairro)
buttonBuscar = driver.find_element_by_css_selector("input[type='submit']")
buttonBuscar.click()