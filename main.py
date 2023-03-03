from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep

login = 'alguembuscandoser'
senha = 'UnderWorld18122004'

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)
arq = open('inta.txt', 'r', encoding='utf-8')
arq2 = open('combinations.txt', 'r', encoding='utf-8')

navegador.get('https://www.instagram.com/')
sleep(2)
navegador.find_element('xpath', '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(login)
navegador.find_element('xpath', '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(senha)
sleep(1)
navegador.find_element('xpath', '//*[@id="loginForm"]/div/div[3]/button').click()
sleep(5)

for linha in arq:
    if linha.split(' ')[0].find('https://') == True:
        navegador.get(linha.split(' ')[0])
    else:
        navegador.get('https://' + linha.split(' ')[0])
    sleep(3)
    for l in arq2:
        try:
            print('testou' + ' ' + l)
            navegador.find_element('xpath', l).click()
        except:
            print()
    sleep(2)