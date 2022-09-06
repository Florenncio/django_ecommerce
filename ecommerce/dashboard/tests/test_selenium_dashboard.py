import pytest
from django.contrib.auth.models import User
from selenium.webdriver.common.by import By


@pytest.mark.selenium
def test_dashboard_admin_login(live_server, db_fixture_setup, chrome_browser_instance):

    i = User.objects.get(id=1)
    print(i.password)

    browser = chrome_browser_instance

    browser.get(("%s%s" % (live_server.url, "/admin/login/")))

    user_name = browser.find_element(By.NAME, "username")
    user_password = browser.find_element(By.NAME, "password")
    submit = browser.find_element(By.XPATH, '//input[@value="Log in"]')

    user_name.send_keys("admin")
    user_password.send_keys("password")
    submit.click()

    assert "Site administration" in browser.page_source
