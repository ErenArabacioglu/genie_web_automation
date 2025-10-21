import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GeniePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    chat_input = (By.XPATH, "//*[@id='chat-input-textarea']")
    send_button = (By.XPATH, "//*[@id='chat-input-send-button']")
    response_bubble = (By.XPATH, "//*[@role='article' or @role='listitem' or contains(@class,'message') or contains(@class,'chat') or contains(@data-testid,'message') or contains(@class,'assistant')]")
    body_selector = (By.TAG_NAME, "body")

    def open(self, base_url):
        self.driver.get(base_url)

    def is_loaded(self):
        self.wait.until(EC.visibility_of_element_located(self.chat_input))
        return True

    def send_prompt(self, text):
        time.sleep(1)
        box = self.wait.until(EC.element_to_be_clickable(self.chat_input))
        box.clear()
        time.sleep(2)
        box.send_keys(text)
        time.sleep(4)

        try:
            btn = self.driver.find_element(*self.send_button)
            btn.click()
        except Exception:
            from selenium.webdriver.common.keys import Keys
            box.send_keys(Keys.ENTER)

    def wait_for_share_icon(self, timeout=40):

        share_locator = (By.XPATH, "//*[@id='message-share-button']")
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(share_locator)
        )
