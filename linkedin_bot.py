import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LinkedInBot:
    def __init__(self, driver):
        """
        Inicializa o bot com uma instância do navegador.
        """
        self.driver = driver

    def login(self, username, password):
        """
        Realiza o login no LinkedIn usando as credenciais fornecidas.
        """
        try:
            self.driver.get("https://www.linkedin.com/login")
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )

            self.driver.find_element(By.ID, "username").send_keys(username)
            self.driver.find_element(By.ID, "password").send_keys(password)

            self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("feed")
            )
            print("Login realizado com sucesso.")

            search_url = "https://www.linkedin.com/search/results/people/?keywords=machine%20learning&origin=GLOBAL_SEARCH_HEADER&sid=%3A(j"
            self.driver.get(search_url)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//button[contains(@aria-label, "Convidar") or .//span[text()="Conectar"]]'))
            )
            print(f"Navegado para a URL: {search_url}")
        except Exception as e:
            print(f"Erro ao fazer login: {e}")

    def send_connection_requests(self):
        """
        Envia solicitações de conexão para usuários encontrados na página atual.
        """
        page = 1
        while True:
            try:
                print(f"Iniciando processamento da página {page}...")
                connect_buttons = self.driver.find_elements(By.XPATH, '//button[contains(@aria-label, "Convidar") or .//span[text()="Conectar"]]')
                
                if not connect_buttons:
                    print("Nenhum botão 'Conectar' encontrado nesta página. Finalizando...")
                    break

                for idx, button in enumerate(connect_buttons):
                    try:
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
                        ActionChains(self.driver).move_to_element(button).perform()
                        time.sleep(1)
                        button.click()
                        time.sleep(2)
                        try:
                            send_button = WebDriverWait(self.driver, 3).until(
                                EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Enviar sem nota"]'))
                            )
                            send_button.click()
                            print(f"Solicitação enviada (com modal) - Usuário {idx + 1} na página {page}.")
                        except Exception:
                            print(f"Solicitação enviada (sem modal) - Usuário {idx + 1} na página {page}.")
                        
                        time.sleep(1)  

                    except Exception as err:
                        print(f"Erro ao processar o usuário {idx + 1} na página {page}: {err}")

                try:
                    page += 1
                    next_page_button = WebDriverWait(self.driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, f'//button[@aria-label="Página {page}"]'))
                    )
                    next_page_button.click()
                    time.sleep(5)
                except Exception:
                    print(f"Fim das páginas alcançado na página {page - 1}.")
                    break
            except Exception as err:
                print(f"Erro inesperado na página {page}: {err}")
                break
