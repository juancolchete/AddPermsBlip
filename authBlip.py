from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
class authBlip:
    def google(self,emailToLogin,driver,loginUrl,timeToWait):
        driver.get(loginUrl)
        element = driver.find_element_by_id("blip-login-with-google")
        element.click()
        element = driver.find_element_by_id("identifierId")
        element.send_keys(emailToLogin, Keys.RETURN)
        time.sleep(timeToWait)