from selenium import webdriver
from selenium.webdriver.common.by import By
import time

PATH = WEBDRIVER_PATH
# fp = webdriver.FirefoxProfile(profile_directory="/home/fnilvu/.mozilla/firefox/ehcf061z.selenium-testing")
driver = webdriver.Firefox(executable_path=PATH)
url = "https://tinder.com"
driver.get(url)

# try:
driver.find_element(
    by=By.XPATH, value="/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span").click()
time.sleep(5)
driver.find_element(
    by=By.XPATH, value="/html/body/div[2]/div/div/div[1]/div/div/div[3]/span/div[1]/div/button/span[2]").click()
time.sleep(5)
# print(driver.current_window_handle)
driver.switch_to.window(driver.window_handles[1])
driver.find_element(
    by=By.XPATH, value="""//*[@id="identifierId"]""").send_keys("mamatmks45@gmail.com")
driver.find_element(
    by=By.XPATH, value="/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button").click()
time.sleep(5)
driver.find_element(
    by=By.XPATH, value="""/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input""").send_keys("Nasywa180120")
driver.find_element(
    by=By.XPATH, value="/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button").click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[0])
driver.find_element(
    by=By.XPATH, value="/html/body/div[2]/div/div/div/div/div[3]/button[1]/span").click()
driver.find_element(
    by=By.XPATH, value="/html/body/div[2]/div/div/div/div/div[3]/button[2]/span").click()
driver.find_element(
    by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button").click()
time.sleep(10)
while True:
    driver.find_element(
        by=By.CSS_SELECTOR, value=".Bgc\(\$c-pink\)\:a > span:nth-child(1) > span:nth-child(1) > svg:nth-child(1)").click()
# finally:
#     driver.quit()
