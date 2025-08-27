from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

s = Service("C:/Users/preet/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = s)
url = 'https://us.smartprix.com/mobiles'
driver.get(url)
time.sleep(1)

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

excl_out_stock = driver.find_element(by = By.XPATH, value = '//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/span')
excl_out_stock.click()
time.sleep(1.5)

excl_upcm = driver.find_element(by = By.XPATH, value = '//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/span')
excl_upcm.click()
time.sleep(1.5)

# load_more part -
# driver.find_element(by = By.XPATH, value = '//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
# time.sleep(2)

old_height = driver.execute_script('return document.body.scrollHeight')
cnt = 1

while True:
    driver.find_element(by = By.XPATH, value = '//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    time.sleep(0.75)
    new_height = driver.execute_script('return document.body.scrollHeight')
    print('old h = ',old_height)
    print('new h = ',new_height)
    cnt+=1
    if cnt == 9: break
    old_height = new_height

    # actually this condition is correct - # if old_height == new_height: break
    # but i had to used the cnt = 9 condition because of a problem in the webpage as web developer have not made any result after
    # there are no more objects to be loaded hence, file was not getting created due to that issue
    # so i made cnt variable ,found the number of times load_more is happening and then added the break condition accordingly 
    # so as to make sure no content is lost
    
