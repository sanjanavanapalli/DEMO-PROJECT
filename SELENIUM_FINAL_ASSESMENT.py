from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
import random
import string

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chrome_service
from selenium.webdriver.common.by import By
from excel import set_data,set_emailid

# set_cartdata, set_details, set_data, set_cart_details, create_details

# step 1: Launching browser
c_service = chrome_service('Drivers\chromedriver.exe')
driver = webdriver.Chrome(service=c_service)
driver.get(" http://automationpractice.com/")
driver.maximize_window()

global email
email = ''.join(random.choice(string.ascii_letters) for x in range(10)) + "17@gmail.com"
# return email


time.sleep(2)
driver.find_element(By.XPATH, "//a[@class='login']").click()
driver.find_element(By.ID, 'email_create').send_keys(email)

driver.find_element(By.ID, 'SubmitCreate').click()

# personal_details
time.sleep(2)
driver.find_element(By.XPATH, "(//div[@class='radio-inline'])[2]").click()
time.sleep(2)
driver.find_element(By.ID, 'customer_firstname').send_keys('sanjana')
driver.find_element(By.ID, 'customer_lastname').send_keys('patnaik')
driver.find_element(By.ID, 'passwd').send_keys('S@njana')
select_date = Select(driver.find_element(By.ID, 'days'))
select_date.select_by_index(4)
select_month = Select(driver.find_element(By.ID, 'months'))
select_month.select_by_index(7)
select_year = Select(driver.find_element(By.ID, 'years'))
select_year.select_by_index(20)
driver.find_element(By.ID, 'company').send_keys('ABC company')
driver.find_element(By.ID, 'address1').send_keys('XYZ street')
driver.find_element(By.ID, 'city').send_keys('hyderabad')
select_state = Select(driver.find_element(By.ID, 'id_state'))
select_state.select_by_index(43)
driver.find_element(By.ID, 'postcode').send_keys('52135')
select_country = Select(driver.find_element(By.ID, 'id_country'))
select_country.select_by_value('21')
time.sleep(2)
driver.find_element(By.ID, 'phone_mobile').send_keys(9321563452)
driver.find_element(By.ID, 'submitAccount').click()

# select_product
hover_element = driver.find_element(By.XPATH, "//a[text()='Women']")
time.sleep(2)
ActionChains(driver).move_to_element(hover_element).perform()
time.sleep(2)
driver.find_element(By.XPATH, "//a[text()='T-shirts']").click()
time.sleep(2)

# test_add_to_cart
cart_hover_element = driver.find_element(By.XPATH, "//img[@title='Faded Short Sleeve T-shirts']")
time.sleep(2)
ActionChains(driver).move_to_element(cart_hover_element).perform()
time.sleep(2)
driver.find_element(By.XPATH, "//a[@title='Add to cart']").click()
time.sleep(2)
driver.find_element(By.XPATH,
                    '/html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[2]/div[4]/a/span').click()
time.sleep(2)

# test_payment
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[3]/div/p[2]/a[1]/span').click()
# driver.find_element(By.ID, 'email').send_keys('email')
# time.sleep(2)
# driver.find_element(By.ID, 'passwd').send_keys('S@njana')
# time.sleep(2)
# driver.find_element(By.ID, 'SubmitLogin').click()
time.sleep(2)

driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[3]/div/form/p/button/span').click()
time.sleep(2)

driver.find_element(By.ID, 'cgv').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[3]/div/div/form/p/button/span').click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[@title='Pay by bank wire']").click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[3]/div/form/p/button/span').click()
time.sleep(2)
print('Your order on My Store is complete.')
