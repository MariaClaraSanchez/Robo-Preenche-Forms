from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import time


class Site:
    def __init__(self) -> None:
        """Instancia a classe com as configurações iniciais
        Args: 
            caminho_driver (str): caminho do executavel do chromedriver 
        """
        self.chromediver = chromedriver_autoinstaller.install()  
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--lang=pt-BR')
        self.chrome_options.add_argument('disable-infobars')
        self.chrome_options.add_argument('--log-level=3')

        

    def acessar_forms(self, pessoas:dict) -> None:
        """Acessa o site do forms
        """
        for dados in pessoas:
            
            time.sleep(2)
            driver = webdriver.Chrome(self.chromediver,options=self.chrome_options)
            driver.get('https://pt.surveymonkey.com/r/Y9Y6FFR')
            
            #Dados pois o nome é a chave de identificação de cada pessoa dentro do dicionário
            driver.find_element(By.ID,'683928983').send_keys(dados) #Nome
            driver.find_element(By.ID,'683932318').send_keys(pessoas[dados]['email']) #Email
            driver.find_element(By.ID,'683930688').send_keys(pessoas[dados]['telefone']) #Telefone
            driver.find_element(By.ID,'683932969').send_keys(pessoas[dados]['sobre']) #Sobre
            
            if(pessoas[dados]['sexo'] == 'Masculino'):
                driver.find_element(By.ID,'683931881_4497366118_label' ).click()
            else:
                driver.find_element(By.ID,'683931881_4497366119_label').click()
            
            driver.find_element(By.XPATH,'.//button[contains(text(), "Enviar Dados")]').click()
            
            
        