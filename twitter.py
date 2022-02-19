import time
import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TwitterBot():
    def __init__(self,username,password,string):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.string = string

    def signIn(self):
        self.browser.get("https://twitter.com/i/flow/login")
        time.sleep(5)
        self.element = self.browser.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input')
        self.element.clear()
        self.element.send_keys(self.username)
        time.sleep(3)
        self.element.send_keys(Keys.RETURN)
        time.sleep(5)
        self.element_two = self.browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input')
        self.element_two.send_keys(self.password)
        time.sleep(3)
        self.element_two.send_keys(Keys.RETURN)
        time.sleep(8)

    def tweet(self):
        self.browser.get('https://twitter.com/compose/tweet')
        time.sleep(5)
        self.element_three = self.browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
        self.element_three.send_keys(self.string)
        time.sleep(3)
        self.element_three.send_keys(Keys.CONTROL,Keys.RETURN)
        time.sleep(8)
        self.browser.quit()

username = input("Username:\n")
password = getpass.getpass("Password:")
tweet = input("Tweet:\n")
t = TwitterBot(username,password,tweet)
t.signIn()
t.tweet()

