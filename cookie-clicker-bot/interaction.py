from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

firefox_driver_path = WEBDRIVER_PATH
driver = webdriver.Firefox(executable_path=firefox_driver_path)
url = URL
driver.get(url)
first_name = driver.find_element(by=By.CLASS_NAME, value="form-control.top")
last_name = driver.find_element(by=By.CLASS_NAME, value="form-control.middle")
email_address = driver.find_element(
    by=By.CLASS_NAME, value="form-control.bottom")

first_name.send_keys(FIRST_NAME)
last_name.send_keys(LAST_NAME)
email_address.send_keys(EMAIL)
email_address.send_keys(Keys.ENTER)
# print(article_count.text.split(" ")[0])


# driver.quit()
