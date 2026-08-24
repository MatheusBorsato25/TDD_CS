from selenium import webdriver
from selenium.webdriver.common.by import By

def test_calc():
    driver = setup()
    
    title = driver.title
    assert title == "Calculadora - TDD"
    
    driver.implicitly_wait(0.5)
    
    texto_operacao = driver.find_element(by=By.NAME, value="texto_operacao")
    submit_button = driver.find_element(by=By.NAME, value="button")
    
    texto_operacao.send_keys("2*2")
    submit_button.click()
    
    resultado = driver.find_element(by=By.CLASS_NAME, value="resultado")
    value = resultado.text
    assert value == "4"
    
    texto_operacao.send_keys("2+2")
    submit_button.click()
    
    resultado = driver.find_element(by=By.CLASS_NAME, value="resultado")
    value = resultado.text
    assert value == "4"
    
    teardown(driver)
    
def setup():
    driver = webdriver.Chrome()
    driver.get("https://matheusborsato25.github.io/TDD_CS/")
    return driver

def teardown(driver):
    driver.quit()
    
    