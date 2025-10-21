import time

import pytest
from src.pages.genie_page import GeniePage

@pytest.mark.web
@pytest.mark.smoke
def test_page_load(driver, base_url):
    page = GeniePage(driver)
    page.open(base_url)
    time.sleep(1)
    assert page.is_loaded()