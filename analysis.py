
#Download selenium library
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
driver  = None
waiting = 2

def wait(web_opening_time=3):
    time.sleep(web_opening_time)

## load web driver for selenium : chrome
def web_driver_load():
    global driver
    driver = webdriver.Firefox()

## quit web driver for selenium
def web_driver_quit():
    driver.quit()

## actual login in hockey app site
def website_login():
    driver.get('https://alchemy-language-demo.mybluemix.net/');
    wait(2)

def sendMessage(msg):
    web_obj = driver.find_element_by_css_selector('#panel1 > textarea')
    web_obj.clear()
    web_obj.send_keys(msg)
    snd = driver.find_element_by_css_selector('#submitbutton')
    snd.click()
    time.sleep(2)
    snd2 = driver.find_element_by_css_selector('#t3')
    snd2.click()


def extract():
	x  = '.keywords-table'
	vb =  driver.find_element_by_css_selector(x)
	vt = vb.text
	return vt


#this is where we have to bring in the article 
msg = "AlchemyAPI is trained on billions of webpages and can detect and extract information such as concepts, entities, sentiment, and keywords. Alternatively, you can train a custom model to identify specific entities and typed relations that are unique to your domain or industry, for example law or finance."
web_driver_load()
website_login()
sendMessage(msg)

time.sleep(1)
line=(extract())

# writing on to the 

file= open("result.csv","w")
file.write(line)
file.close()