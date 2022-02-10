from selenium import webdriver
url = 'http://www.sanasa.com.br/ura-quadrodeavisos/acessoqa.asp'
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('firefox')
driver = webdriver.Firefox(firefox_binary=binary, executable_path=r'/usr/local/bin/geckodriver')

driver.get(url)
emailElem = driver.find_element_by_name('codc')
emailElem.send_keys('178665')
buttonBuscar = driver.find_element_by_css_selector("input[type='submit']")
buttonBuscar.click()