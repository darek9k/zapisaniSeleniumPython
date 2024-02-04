import logging.handlers

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from form_page import FormPage, AcceptCookie

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)-15s %(message)s')

# Define the logger
logger = logging.getLogger(__name__)

# Set chrome options
chrome_options = Options()
# headless its Selenium drama!
# chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Instantiate the webdriver
driver = webdriver.Chrome(options=chrome_options)


# Test
def test_happy_path():
    driver.get('http://testy-zadanie.zapisani.dev')
    accept_cookie = AcceptCookie(driver)
    accept_cookie.accept_cookies()
    form_page = FormPage(driver)
    # Getting the initial count of available registrations
    initial_count = form_page.check_initial_count()
    form_page.fill_form_with_test_data()
    form_page.select_product_field('product_field_f5296ba2')
    form_page.click_registration_button()
    # Checking if the payment method option is available
    form_page.check_cash_method()
    # Clicking the registration button again
    form_page.click_registration_button()
    # Waiting for the page to load after selecting payment method
    form_page.checking_success()
    # Getting the final count of available registrations
    final_count = form_page.check_final_count()
    # Assertions
    assert initial_count - final_count == 1


test_happy_path()
driver.quit()
