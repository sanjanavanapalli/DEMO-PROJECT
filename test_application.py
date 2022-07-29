import unittest
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
import random
import string

from excel import set_data, set_emailid


class Users(unittest.TestCase):
    driver = None

    # def random_email(self):
    global email
    email = ''.join(random.choice(string.ascii_letters) for x in range(20)) + "@17gmail.com"

    # return email
    @pytest.mark.run(order=1)
    def test_create_account(self):
        print('pytest')
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[@class='login']").click()
        self.driver.find_element(By.ID, 'email_create').send_keys(email)
        print(email)

        self.driver.find_element(By.ID, 'SubmitCreate').click()
        # set_data(email)
        set_emailid(email)

        @pytest.mark.run(order=2)
        def test_personal_details(self):
            time.sleep(2)

        self.driver.find_element(By.XPATH, "//div[@class='radio-inline'][2]").click()
        time.sleep(2)
        self.driver.find_element(By.ID, 'customer_firstname').send_keys('sanjana')
        self.driver.find_element(By.ID, 'customer_lastname').send_keys('patnaik')
        self.driver.find_element(By.ID, 'passwd').send_keys('S@njana')
        select_date = Select(self.driver.find_element(By.ID, 'days'))
        select_date.select_by_index(4)
        select_month = Select(self.driver.find_element(By.ID, 'months'))
        select_month.select_by_index(7)
        select_year = Select(self.driver.find_element(By.ID, 'years'))
        select_year.select_by_index(20)
        self.driver.find_element(By.ID, 'company').send_keys('ABC company')
        self.driver.find_element(By.ID, 'address1').send_keys('XYZ street')
        self.driver.find_element(By.ID, 'city').send_keys('hyderabad')
        select_state = Select(self.driver.find_element(By.ID, 'id_state'))
        select_state.select_by_index(43)
        self.driver.find_element(By.ID, 'postcode').send_keys('52135')
        select_country = Select(self.driver.find_element(By.ID, 'id_country'))
        select_country.select_by_value('21')
        time.sleep(2)
        self.driver.find_element(By.ID, 'phone_mobile').send_keys(9321563452)
        self.driver.find_element(By.ID, 'submitAccount').click()

    @pytest.mark.run(order=2)
    def test_select_product(self):
        hover_element = self.driver.find_element(By.XPATH, "//a[text()='Women']")
        time.sleep(2)
        ActionChains(self.driver).move_to_element(hover_element).perform()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[text()='T-shirts']").click()
        time.sleep(2)

    #
    @pytest.mark.run(order=3)
    def test_add_to_cart(self):
        cart_hover_element = self.driver.find_element(By.XPATH, "//img[@title='Faded Short Sleeve T-shirts']")
        time.sleep(2)
        ActionChains(self.driver).move_to_element(cart_hover_element).perform()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[@title='Add to cart']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 '/html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[2]/div[4]/a/span').click()
        time.sleep(2)
        product_name = self.driver.find_element(By.XPATH,"//a[@title='Faded Short Sleeve T-shirts']").text
        print('product name is', product_name)

        total_price = self.driver.find_element(By.ID,'total_price').text
        print('Total Price ', total_price)
        @pytest.mark.run(order=4)
        def test_payment(self):
            time.sleep(2)

        self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[3]/div/p[2]/a[1]/span').click()
        time.sleep(3)
        self.driver.find_element(By.ID, 'email').send_keys(email)
        time.sleep(2)
        print('after login', email)
        self.driver.find_element(By.ID, 'passwd').send_keys('S@njana')
        time.sleep(2)
        self.driver.find_element(By.ID, 'SubmitLogin').click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[3]/div/form/p/button/span').click()
        time.sleep(2)

        self.driver.find_element(By.ID, 'cgv').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[3]/div/div/form/p/button/span').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[@title='Pay by bank wire']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[3]/div/form/p/button/span').click()
        time.sleep(2)
        print('Your order on My Store is complete.')
