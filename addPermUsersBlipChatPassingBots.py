from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import authBlip
import Blip
auth = authBlip.authBlip()
blip = Blip.Blip()

emailsToAdd = ['usertoadd@gmail.com','usertoadd2@gmail.com','usertoadd3@gmail.com','usertoadd4@gmail.com','usertoadd5@gmail.com','usertoadd6@gmail.com','usertoadd7@gmail.com']


urlBase = 'https://portal.blip.ai/'


driver = webdriver.Chrome()
auth.google("juan.colchete@fluna.io",driver,"https://portal.blip.ai/",40)

botsToAddPerm = ["testeud1234","testecontato6","prototipo4","prototype1","testebot429","smartbot6","thebot2","smart12"]
for bot in botsToAddPerm:
    fullUrl = urlBase+'application/detail/'+bot+'/home'
    blip.addPermsBotUsers(driver,fullUrl,emailsToAdd)
    driver.get(fullUrl)
    time.sleep(2)