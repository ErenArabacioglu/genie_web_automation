import time
import pytest
from src.pages.genie_page import GeniePage

@pytest.mark.web
def test_chat_flow(driver, base_url):
    page = GeniePage(driver)
    page.open(base_url)
    assert page.is_loaded()
    time.sleep(1)
    page.send_prompt("This is a test prompt.")
    page.wait_for_share_icon(timeout=40)
    time.sleep(2)
