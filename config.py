import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

load_dotenv()

WEBDRIVER_PATH = "chromedriver-win64/chromedriver.exe"
LINKEDIN_USER = os.getenv("USER")
LINKEDIN_PASS = os.getenv("PASSWORD")

def setup_webdriver():
    """
    Configura e retorna uma instância do WebDriver do Chrome.
    """
    chrome_options = Options()
    chrome_options.add_argument("--disable-webrtc")  
    chrome_options.add_argument("--start-maximized")
    service = Service(WEBDRIVER_PATH)
    return webdriver.Chrome(service=service, options=chrome_options)
