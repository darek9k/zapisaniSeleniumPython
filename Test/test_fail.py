import logging.handlers
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from form_page import FormPage, AcceptCookie

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)-15s %(message)s')

# Define the logger
logger = logging.getLogger(__name__)

# Set chrome options
options = webdriver.ChromeOptions()
# headless its Selenium drama!
# chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Instantiate the webdriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)


# Test
def test_fail():
    driver.get('http://testy-zadanie.zapisani.dev')
    accept_cookie = AcceptCookie(driver)
    accept_cookie.accept_cookies()

    form_page = FormPage(driver)
    form_page.fill_form_with_test_data()
    form_page.select_product_field('product_field_83cf9412')
    form_page.click_registration_button()
    form_page.check_fail_text()


test_fail()
driver.quit()
