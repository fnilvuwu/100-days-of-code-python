from selenium import webdriver
from selenium.webdriver.common.by import By
import time

PATH = DRIVER_PATH
PROFILE = webdriver.FirefoxProfile(
    profile_directory="/home/fnilvu/.mozilla/firefox/ehcf061z.selenium-testing")
password = "password here"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Firefox(
            executable_path=PATH, firefox_profile=PROFILE)
        self.PROMISED_DOWN = 30
        self.PROMISED_UP = 2

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.find_element(by=By.CLASS_NAME, value="start-text").click()
        time.sleep(180)
        self.DOWN = self.driver.find_element(
            by=By.CLASS_NAME, value="result-data-large.number.result-data-value.download-speed").text
        self.UP = self.driver.find_element(
            by=By.CLASS_NAME, value="result-data-large.number.result-data-value.upload-speed").text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        time.sleep(10)
        self.driver.find_element(
            by=By.XPATH, value='/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a').click()
        time.sleep(5)
        self.driver.find_element(
            by=By.XPATH, value="/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input").send_keys("mamatmks45@gmail.com")
        self.driver.find_element(
            by=By.XPATH, value="/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div").click()
        time.sleep(5)
        self.driver.find_element(
            by=By.XPATH, value="/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input").send_keys("fnilvu")
        self.driver.find_element(
            by=By.XPATH, value="/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div").click()
        time.sleep(5)
        self.driver.find_element(
            by=By.XPATH, value="/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input").send_keys(password)
        self.driver.find_element(
            by=By.XPATH, value="/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div").click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div").send_keys(
            f"Hey Internet Provider, why is my internet speed {self.DOWN}down/{self.UP}up when i pay for {self.PROMISED_DOWN}down/{self.PROMISED_UP}up?")
        self.driver.find_element(
            by=By.XPATH, value="/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span").click()


TwitterBot = InternetSpeedTwitterBot()
TwitterBot.get_internet_speed()
TwitterBot.tweet_at_provider()
