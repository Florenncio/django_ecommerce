import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def chrome_browser_instance(request):
    browser = webdriver.Chrome(ChromeDriverManager().install())
    yield browser
    browser.close()