from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
class Blip:
    def clickOnTeam(self,driver):
        print("Tentativa de CLICK ---------------")
        teamicon = driver.find_element_by_xpath("//i[@class='icon-team-1']")
        teamicon.click()
    def clickOnTeamRetry(self,driver,timer):
        try:
            time.sleep(timer)
            self.clickOnTeam(driver)
            return
        except:
            self.clickOnTeamRetry(driver,timer+timer)

    def addAllPermsToUsers(self,driver,url,emailsToAdd):
        elements = driver.find_elements_by_xpath("//div[@class='card-content tc']")
        size = len(elements)
        counter=0
        while(counter<size):
            time.sleep(4)
            elements = driver.find_elements_by_xpath("//div[@class='card-content tc']")
            elements[counter].click()
            counter= counter + 1
            for emailToAdd in emailsToAdd:
                time.sleep(4)
                self.clickOnTeam(driver)
                time.sleep(4)
                addmember = driver.find_element_by_xpath("//button[@class='bp-btn bp-btn--true']")
                addmember.click()
                email = driver.find_element_by_xpath("//input[@type='email']")
                email.send_keys(emailToAdd)
                time.sleep(4)
                perms = driver.find_element_by_xpath("//span[@class='rz-pointer rz-pointer-min']")
                perms.send_keys(Keys.ARROW_RIGHT)
                perms.send_keys(Keys.ARROW_RIGHT)
                perms.send_keys(Keys.ARROW_RIGHT)
                saveButton = driver.find_element_by_xpath("//button[@class='bp-btn bp-btn--bot bp-btn--small']")
                saveButton.click()
            time.sleep(4)
            driver.get(url)
            time.sleep(4)
    def addAllPermsToUser(self,driver,url,emailToAdd):
        elements = driver.find_elements_by_xpath("//div[@class='card-content tc']")
        size = len(elements)
        counter=0
        while(counter<size):
            time.sleep(4)
            elements = driver.find_elements_by_xpath("//div[@class='card-content tc']")
            elements[counter].click()
            counter= counter + 1
            time.sleep(4)
            self.clickOnTeam(driver)
            addmember = driver.find_element_by_xpath("//button[@class='bp-btn bp-btn--true']")
            addmember.click()
            email = driver.find_element_by_xpath("//input[@type='email']")
            email.send_keys(emailToAdd)
            time.sleep(4)
            perms = driver.find_element_by_xpath("//span[@class='rz-pointer rz-pointer-min']")
            perms.send_keys(Keys.ARROW_RIGHT)
            perms.send_keys(Keys.ARROW_RIGHT)
            perms.send_keys(Keys.ARROW_RIGHT)
            saveButton = driver.find_element_by_xpath("//button[@class='bp-btn bp-btn--bot bp-btn--small']")
            saveButton.click()
            time.sleep(4)
            driver.get(url)
    def addPermsBot(self,driver,url,emailtoadd):
        driver.get(url)
        time.sleep(4)
        self.clickOnTeam(driver)
        addmember = driver.find_element_by_xpath("//button[@class='bp-btn bp-btn--true']")
        addmember.click()
        email = driver.find_element_by_xpath("//input[@type='email']")
        email.send_keys(emailtoadd)
        time.sleep(4)
        perms = driver.find_element_by_xpath("//span[@class='rz-pointer rz-pointer-min']")
        perms.send_keys(Keys.ARROW_RIGHT)
        perms.send_keys(Keys.ARROW_RIGHT)
        perms.send_keys(Keys.ARROW_RIGHT)
        saveButton = driver.find_element_by_xpath("//button[@class='bp-btn bp-btn--bot bp-btn--small']")
        saveButton.click()
        time.sleep(4)
    def addPermsBotUsers(self,driver,url,emailsToAdd):
        driver.get(url)
        for emailToAdd in emailsToAdd:
            self.clickOnTeamRetry(driver,4)
            addmember = driver.find_element_by_xpath("//button[@class='bp-btn bp-btn--true']")
            addmember.click()
            email = driver.find_element_by_xpath("//input[@type='email']")
            email.send_keys(emailToAdd)
            time.sleep(4)
            perms = driver.find_element_by_xpath("//span[@class='rz-pointer rz-pointer-min']")
            perms.send_keys(Keys.ARROW_RIGHT)
            perms.send_keys(Keys.ARROW_RIGHT)
            perms.send_keys(Keys.ARROW_RIGHT)
            saveButton = driver.find_element_by_xpath("//button[@class='bp-btn bp-btn--bot bp-btn--small']")
            saveButton.click()
            time.sleep(4)
