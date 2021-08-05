from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import authBlip
import Blip
auth = authBlip.authBlip()
blip = Blip.Blip()

driver = webdriver.Chrome()
urlBase = "https://contract.blip.ai/application"
emailsToAdd = ['usertoadd@gmail.com','usertoadd2@gmail.com','usertoadd3@gmail.com','usertoadd4@gmail.com','usertoadd5@gmail.com','usertoadd6@gmail.com','usertoadd7@gmail.com']

auth.google("emailtologin@gmail.com",driver,urlBase,60)
blip.addAllPermsToUsers(driver,urlBase,emailsToAdd)