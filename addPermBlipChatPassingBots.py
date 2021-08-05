from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import authBlip
import Blip
auth = authBlip.authBlip()
blip = Blip.Blip()

emailToAdd = 'teste@gmail.com'

urlBase = 'https://portal.blip.ai/'


driver = webdriver.Chrome()
auth.google("juanudkp@gmail.com",driver,"https://portal.blip.ai/",40)

botsToAddPerm = ["testeud1234","testecontato6","prototipo4","prototype1","testebot429","smartbot6","thebot2","smart12"]
for bot in botsToAddPerm
    fullUrl = urlBase+'application/detail/'+bot+'/home'
    blip.addPermsBot(driver,fullUrl,emailToAdd)
    time.sleep(2)