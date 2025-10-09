from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER_EXEC = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'

def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)
        
    chrome_service = Service(executable_path=str(CHROMEDRIVER_EXEC))
    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options,
    )

    return browser

if __name__ == '__main__':
    TIME_TO_WAIT = 10
    # Example
    # options = '--headless', '--disable-gpu',
    options = ()
    browser = make_chrome_browser(*options)

    # Como antes
    browser.get('https://www.google.com/')
    
    # Espera para encontrar o botão Aceitar tudo
    try:
        accept_button = WebDriverWait(browser, TIME_TO_WAIT).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//button[.//div[text()="Aceitar tudo"]]')
            )
        )
        sleep(5) 
        accept_button.click()
    except Exception as e:
        print('Erro ao encontrar o botão Aceitar tudo', e)
       
    # Espera para encontrar input
    try:
        search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
            EC.presence_of_element_located(
                (By.NAME, 'q')
            )
        )

        search_input.send_keys('Hello World')
        sleep(7)  
        search_input.send_keys(Keys.ENTER)  

        results = browser.find_element(By.ID, 'search')
        links = results.find_element(By.TAG_NAME, 'a')
        links[0].click()

    except Exception as e:
        print('Erro ao encontrar o input de busca', e)

    # Sleep - apenas para visualização
    sleep(TIME_TO_WAIT)    
