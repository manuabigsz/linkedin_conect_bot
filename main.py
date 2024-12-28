from config import setup_webdriver, LINKEDIN_USER, LINKEDIN_PASS
from linkedin_bot import LinkedInBot

def main():
    driver = setup_webdriver()
    bot = LinkedInBot(driver)

    try:
        bot.login(LINKEDIN_USER, LINKEDIN_PASS)
        bot.send_connection_requests()
    finally:
        driver.quit()
        print("Bot finalizado.")

if __name__ == "__main__":
    main()