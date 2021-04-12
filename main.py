from selenium import webdriver
from selenium.webdriver import FirefoxProfile
from time import sleep
from random import randrange
from creds import  user,password
import os

# Main part, find the play button, the duration and launch it. Sleep times can be changed.

def play_video(url) :
    try : 
        driver.get(url)
        sleep(10)
        btn_play_pause = driver.find_element_by_css_selector(".MuiButtonBase-root-77")
        btn_play_pause.click()
        print("Video started url={}".format(url))
        sleep(2)
        time = driver.find_element_by_css_selector("h3.MuiTypography-root:nth-child(6)").text
        min,second = time.split(":")
        min = int(min)
        second = int(second)
        print("Sleeping for {} minutes and {} seconds\n".format(min,second),flush=True)
        sleep(((min)*60)+second+10)
    except Exception  as e :
        print(e)
        pass



options = webdriver.FirefoxOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
profile = webdriver.FirefoxProfile()
profile.set_preference("media.volume_scale", "0.0")

# Firefox Path
options.binary_location = "C:/Program Files/Mozilla Firefox/firefox"

driver = webdriver.Firefox(
    executable_path='selenium/geckodriver.exe', service_log_path='selenium/geckodriver.log',firefox_profile=profile)

# Login Page
driver.get('https://user.7speaking.com/home')

sleep(1)

# Username
text_area = driver.find_element_by_name("username")
text_area.send_keys(user)

# Password
text_area = driver.find_element_by_name("password")

text_area.send_keys(password)

# Connection
submit_button = button = driver.find_element_by_class_name("MuiButton-label-28")
submit_button.click()


# There is a captcha, we have to do it manually.... Do it then press here enter to load your page
input("Press Enter when you are logged in....")

# Generate random links with random videos to play. You can change the randrange input
url_base = 'https://user.7speaking.com/document/'
urls = []
for i in range(0,500) : 
    urls.append(url_base + str(randrange(14000,17500)))

#  Play all the urls the while loop isn't necessary but if you want to have infinite hours on 7speaking...
while 1:
    for url in urls : 
        play_video(url)
   
