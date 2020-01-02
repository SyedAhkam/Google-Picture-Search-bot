from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = 'https://www.google.com'
query = input('What do you want to search for?\n') ## Change query to anything

browser = webdriver.Chrome()
browser.get(url)

text_field = browser.find_element_by_name('q')
text_field.send_keys(query)
text_field.send_keys(Keys.RETURN)

time.sleep(1)

images = browser.find_element_by_link_text('Images')
images.click()
time.sleep(2)

counter = 1
while True:
    body = browser.find_element_by_tag_name('body')
    body.send_keys(Keys.DOWN)
    time.sleep(2)
    browser.save_screenshot("screenshot" + str(counter) + ".png")
    counter = counter + 1
