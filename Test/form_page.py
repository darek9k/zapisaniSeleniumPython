import logging
import random

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Define the logger
logger = logging.getLogger(__name__)


class AcceptCookie:
    def __init__(self, driver):
        self.driver = driver

    def accept_cookies(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, '.modal-content').is_displayed()
            self.driver.find_element(By.CSS_SELECTOR, 'button[test-id="ok"]').click()
        except NoSuchElementException:
            pass


class FormPage:
    EMAIL_FIELD = '[test-id="email_main"]'
    PHONE_NUMBER_FIELD = '[test-id="phone_number"]'
    FIRST_NAME_FIELD = '[test-id="first_name"]'
    LAST_NAME_FIELD = '[test-id="last_name"]'
    BASIC_FIELD = '[test-id="{}"]'
    PRODUCT_FIELD = 'label[for="{}"]'
    REGISTRATION_BUTTON = 'button[test-id="registration-button"]'
    END_BUTTON = 'button[type="button"]'
    FAIL_TEXT = '/html/body/div[4]/div/div/div[2]/div[2]/div/div/ul/li'

    def __init__(self, driver):
        self.driver = driver

    def fill_email(self, email):
        logger.info(f'Filling email field with: {email}')
        self.driver.find_element(By.CSS_SELECTOR, self.EMAIL_FIELD).send_keys(email)

    def fill_phone_number(self, phone_number):
        logger.info(f'Filling phone number field with: {phone_number}')
        self.driver.find_element(By.CSS_SELECTOR, self.PHONE_NUMBER_FIELD).send_keys(phone_number)

    def fill_first_name(self, first_name):
        logger.info(f'Filling first name field with: {first_name}')
        self.driver.find_element(By.CSS_SELECTOR, self.FIRST_NAME_FIELD).send_keys(first_name)

    def fill_last_name(self, last_name):
        logger.info(f'Filling last name field with: {last_name}')
        self.driver.find_element(By.CSS_SELECTOR, self.LAST_NAME_FIELD).send_keys(last_name)

    def fill_basic_field(self, field_id, value):
        logger.info(f'Filling basic field {field_id} with: {value}')
        self.driver.find_element(By.CSS_SELECTOR, self.BASIC_FIELD.format(field_id)).send_keys(value)

    def select_product_field(self, field_id):
        logger.info(f'Selecting product field {field_id}')
        element = self.driver.find_element(By.CSS_SELECTOR, self.PRODUCT_FIELD.format(field_id))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)

    def click_registration_button(self):
        logger.info('Clicking registration button')
        element = self.driver.find_element(By.CSS_SELECTOR, self.REGISTRATION_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.modal-content'))
        )

    def click_end_button(self):
        logger.info('Clicking end button')
        self.driver.find_element(By.CSS_SELECTOR, self.END_BUTTON).click()

    def fill_form_with_test_data(self):
        logger.info('Filling form with data')
        self.fill_email('test@example.com')
        self.fill_phone_number('123456789')
        self.fill_first_name('John')
        self.fill_last_name('Doe')
        self.fill_basic_field('basic_field_ee0b49fb', '10')
        self.fill_basic_field('basic_field_855dd2b7', 'Lorem ipsum')
        self.select_radio_btn()

    def select_radio_btn(self):
        checkboxes = self.driver.find_elements(By.CSS_SELECTOR, 'div.form-check input[type="radio"]')
        random_index = random.randint(0, len(checkboxes) - 2)
        checkboxes[random_index].click()

    def check_fail_text(self):
        logger.info('Checking fail text')
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.FAIL_TEXT))
        )
        expected_text = "Rejestracja niemożliwa. Wybrany produkt nie jest dostępny."
        element = self.driver.find_element(By.XPATH, self.FAIL_TEXT)
        assert expected_text in element.text, f"Oczekiwany tekst '{expected_text}' nie został znaleziony w elemencie."

    def check_cash_method(self):
        logger.info('Checking cash method is available')
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="btn-cash"]'))
        )
        payment_method_element = self.driver.find_element(By.CSS_SELECTOR, 'label[for="btn-cash"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", payment_method_element)
        self.driver.execute_script("arguments[0].click();", payment_method_element)

    def check_final_count(self):
        logger.info('Checking final count')
        self.driver.get('http://testy-zadanie.zapisani.dev')
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '(//*[@id="alignment-decorator"]/div/div/div/div[5]/div)[3]'))
        )
        final_count_element = self.driver.find_element(By.XPATH,
                                                       '(//*[@id="alignment-decorator"]/div/div/div/div[5]/div)[3]')
        final_count_text = final_count_element.text
        final_count = int(final_count_text.split(':')[1].strip())
        return final_count

    def check_initial_count(self):
        logger.info('Checking initial count')
        initial_count_element = self.driver.find_element(By.XPATH, '(//div/div[@class="col"])[3]')
        initial_count_text = initial_count_element.text
        initial_count = int(initial_count_text.split(':')[1].strip())
        return initial_count

    def checking_success(self):
        logger.info('Checking success')
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_to_be("https://testy-zadanie.zapisani.dev/zakonczono/gotowka"))
        current_url = self.driver.current_url
        expected_url = "https://testy-zadanie.zapisani.dev/zakonczono/gotowka"
        assert expected_url == current_url
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.col-md-12'))
        )
        # Checking if the success message and end button are displayed
        success_message_element = self.driver.find_element(By.XPATH,
                                                           '//div[contains(text(), "Rejestracja przyjęta. '
                                                           'Dziękujemy!")]')
        success_message_text = success_message_element.text
        assert success_message_text == "Rejestracja przyjęta. Dziękujemy!"
