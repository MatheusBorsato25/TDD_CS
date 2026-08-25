from selenium import webdriver
from selenium.webdriver.common.by import By

def test_calc():
    driver = setup()
    
    title = driver.title
    assert title == "Calculadora - TDD"
    
    driver.implicitly_wait(2.0)
    
    texto_operacao = driver.find_element(by=By.NAME, value="texto_operacao")
    submit_button = driver.find_element(by=By.NAME, value="button")
    resultado = driver.find_element(by=By.CLASS_NAME, value="resultado")
    
    cenarios: list[tuple[str, str]] = []
    total_testes: int = 0
    
    # Testes - Adição:
    for i in range(1, 16):
        for j in range(1, 16):
            cenarios.append((f"{i}+{j}", str(i + j)))
    
    # Testes - Subtração:
    for i in range(1, 16):
        for j in range(1, 16):
            cenarios.append((f"{i}-{j}", str(i - j)))

    # Testes - Multiplicação:
    for i in range(1, 16):
        for j in range(1, 16):
            cenarios.append((f"{i}*{j}", str(i * j)))
    
    # Testes - Divisão:
    for i in range(1, 16):
        for j in range(1, 16):
            cenarios.append((f"{i}/{j}", str(i / j)))
    
    cenarios.extend([
        ("2.5+2.5", "5"), ("10.5*2", "21"), 
        ("10/4", "2.5"), ("5.5-2.7", "2.8"),
        ("2+2+2", "Expressão inválida!"), ("2+a", "Expressão inválida!"),
        ("127892", "Expressão inválida!"), ("7,6*9", "Expressão inválida!"),
        ("2 + 8", "Expressão inválida!")
    ])
    
    total_testes = len(cenarios)
    
    for indice, (expressao, resultado_expressao) in enumerate(cenarios, 1):
        
        texto_operacao.clear()
        texto_operacao.send_keys(expressao)
        submit_button.click()
        
        valor = resultado.text
        assert str(valor) == str(resultado_expressao)
        print(f"Sucesso: [{indice}/{total_testes}] -> {expressao} = {valor}")
    
    teardown(driver)
    
    
def setup():
    driver = webdriver.Chrome()
    driver.get("https://matheusborsato25.github.io/TDD_CS/")
    return driver


def teardown(driver):
    driver.quit()
    

if __name__ == "__main__":
    test_calc()
    
    