import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.genie_page import GeniePage

@pytest.mark.web
@pytest.mark.positive
def test_new_chat(driver, base_url):
    page = GeniePage(driver)
    page.open(base_url)
    assert page.is_loaded()

    page.send_prompt("This is a test prompt.")
    page.wait_for_share_icon(timeout=40)
    time.sleep(2)


    new_page_locator = (By.XPATH, "//*[@id='chat-sidebar-new-chat-button']")
    driver.find_element(*new_page_locator).click()
    time.sleep(2)

    heading_locator = (By.XPATH, "//*[@id='chat-main-container']/div[2]/div[1]/div/h1")
    WebDriverWait(driver, timeout=15).until(
        EC.visibility_of_element_located(heading_locator)
    )