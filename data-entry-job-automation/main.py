from bs4 import BeautifulSoup
import requests
import lxml
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0",
    "Accept-Language": "en-US,en;q=0.5"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "lxml")

articles = soup.find_all(
    name="a", class_="list-card-link list-card-link-top-margin list-card-img")
prices = soup.find_all(name="div", class_="list-card-price")
# print(articles)
article_links = []
article_address = []
article_prices = []

for article in articles:
    link = article.get("href")
    article_links.append(link)

    address = article.find(name="img").get("alt")
    article_address.append(address)

for price_object in prices:
    price = price_object.getText()
    article_prices.append(price)

PATH = DRIVER_PATH
PROFILE = webdriver.FirefoxProfile(profile_directory=PROFILE_PATH)

driver = webdriver.Firefox(executable_path=PATH, firefox_profile=PROFILE)

for item in article_address:
    driver.get(GOOGLE_DOC_LINK)
    text_input = driver.find_elements(by=By.CLASS_NAME, value="whsOnd.zHQkBf")
    time.sleep(5)
    text_input[0].send_keys(item)
    text_input[1].send_keys(article_prices[article_address.index(item)])
    text_input[2].send_keys(article_links[article_address.index(item)])
    text_input[2].send_keys(article_links[article_address.index(item)])
    driver.find_element(
        by=By.XPATH, value="/html/body/div/div[3]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span").click()
