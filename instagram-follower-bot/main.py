from selenium import webdriver
from selenium.webdriver.common.by import By
import time

PATH = DRIVER_PATH
PROFILE = webdriver.FirefoxProfile(profile_directory="/home/fnilvu/.mozilla/firefox/ehcf061z.selenium-testing/")
SIMILAR_ACCOUNT = "davidjmalan"
USERNAME = USERNAME
PASSWORD = PASSWORD

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=PATH, firefox_profile=PROFILE)
    def login(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        time.sleep(10)
        self.driver.find_element(by=By.NAME, value="username").send_keys(USERNAME)
        self.driver.find_element(by=By.NAME, value="password").send_keys(PASSWORD)
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button").click()
        time.sleep(10)
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/section/main/div/div/div/div/button").click()

    def find_followers(self):
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div/span').click()
        # self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
        time.sleep(10)
        
        self.followers = self.driver.find_elements(by=By.CLASS_NAME, value="sqdOP.L3NKy.y3zKF")
    def follow(self):
        time.sleep(10)
        try:
            for follower in self.followers:
                time.sleep(2)
                self.driver.execute_script("arguments[0].click();", follower)
                if self.followers.index(follower) % 7 == 0 and self.followers.index(follower) > 0:
                    scr1 = self.driver.find_element(by=By.XPATH, value='/html/body/div[6]/div/div/div/div[2]')
                    self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
        except ElementClickInterceptedException:
            self.driver.find_element(by=By.CLASS_NAME, value="aOOlW.HoLwm").click()

FollowBot = InstaFollower()
FollowBot.login()
FollowBot.find_followers()
FollowBot.follow()
