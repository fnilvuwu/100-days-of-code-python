from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
password = "your pass here"

firefox_driver_path = DRIVER_PATH
driver = webdriver.Firefox(executable_path=firefox_driver_path)
url = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
driver.get(url)


driver.find_element(by=By.CLASS_NAME, value="nav__button-secondary").click()
driver.find_element(by=By.ID, value="username").send_keys(EMAIL)
driver.find_element(by=By.ID, value="password").send_keys(password)
driver.find_element(by=By.CLASS_NAME, value="login__form_action_container").click()
# disabled ember-view job-card-container__link job-card-list__title


# WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "jobs-unified-top-card__content--two-pane")))
time.sleep(10)
job_list = driver.find_elements(by=By.CLASS_NAME, value="disabled.ember-view.job-card-container__link.job-card-list__title")
for item in job_list:
    item.click()
    time.sleep(2)
    driver.find_element(by=By.CLASS_NAME, value="jobs-save-button.artdeco-button.artdeco-button--3.artdeco-button--secondary").click()
    
    # driver.quit()