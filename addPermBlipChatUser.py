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
emailToAdd ='usertoadd@gmail.com'

auth.google("usertologin@gmail.com",driver,urlBase,60)
blip.addAllPermsToUser(driver,urlBase,emailToAdd)