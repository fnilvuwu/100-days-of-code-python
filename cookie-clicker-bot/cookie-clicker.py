from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import time

firefox_driver_path = WEBDRIVER_PATH
driver = webdriver.Firefox(executable_path=firefox_driver_path)
url = "https://orteil.dashnet.org/experiments/cookie/"
driver.get(url)
# current_money = 150
cookie = driver.find_element(by=By.ID, value="cookie")

timeout = time.time() + 5*60
current_highest = 0
last_bought_item = 0
while True:
    cookie.click()
    if datetime.datetime.now().second % 5 == 0:
        current_money = int(driver.find_element(by=By.ID, value="money").text)
        item_shop_prices_elements = driver.find_elements(
            by=By.CSS_SELECTOR, value="#rightPanel div div b")
        item_prices_list = []
        for price in item_shop_prices_elements[:len(item_shop_prices_elements) - 1]:
            item_prices_list.append(int(price.text.strip().split(
                "-")[1].replace(" ", "").replace(",", "")))

        for price in item_prices_list:

            if current_money/price > 1 and price > current_highest:
                current_highest = price

        if current_highest != 0 and current_highest != last_bought_item:
            last_bought_item = current_highest
            item_shop_prices_elements[item_prices_list.index(
                current_highest)].click()
    if time.time() > timeout:
        break

cps = driver.find_element(by=By.ID, value="cps").text
print(cps)
