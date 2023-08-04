from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

# Promised download by the Internet service provider
PROMISED_DOWN = 150
# Promised upload by the Internet service provider
PROMISED_UP = 20
TWITTER_EMAIL = "<your twitter email>"
TWITTER_PASSWORD = "<Your Twitter passoword>"
chrome_driver_path = "C:\Development\chromedriver.exe"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(10)
        go_button = self.driver.find_element(By.LINK_TEXT, "GO")
        go_button.click()
        time.sleep(50)
        download_speed = self.driver.find_element(By.XPATH,
                                                  '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        up_speed = self.driver.find_element(By.XPATH,
                                            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = download_speed
        self.up = up_speed
        pass

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(8)
        user_name = self.driver.find_element(By.XPATH,
                                             '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        user_name.send_keys(TWITTER_EMAIL)
        user_name.send_keys(Keys.ENTER)
        time.sleep(3)
        phone_no = self.driver.find_element(By.XPATH,
                                            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        phone_no.send_keys("@AnubhutiBhardw8")
        phone_no.send_keys(Keys.ENTER)
        time.sleep(3)
        password = self.driver.find_element(By.XPATH,
                                            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(10)
        tweet = self.driver.find_element(By.XPATH,
                                         'div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet_is = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet.send_keys(tweet_is)
        time.sleep(10)


TwitterBot = InternetSpeedTwitterBot()
TwitterBot.get_internet_speed()
TwitterBot.tweet_at_provider()
