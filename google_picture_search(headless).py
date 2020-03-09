# Import Modules

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time     
from os import path, mkdir

art = """
  _________                .___ _____  .__     __                    
 /   _____/__.__. ____   __| _//  _  \ |  |__ |  | _______    _____  
 \_____  <   |  |/ __ \ / __ |/  /_\  \|  |  \|  |/ /\__  \  /     \ 
 /        \___  \  ___// /_/ /    |    \   Y  \    <  / __ \|  Y Y  \\
/_______  / ____|\___  >____ \____|__  /___|  /__|_ \(____  /__|_|  /
        \/\/         \/     \/       \/     \/     \/     \/      \/ 
    \n"""

print(art)

url = 'https://www.google.com'  # URL
query = input('What do you want to search for?\n')  # Change query to anything
Screenshots = int(input('How many screenshots do you want?\n'))  # No of screenshots

opts = Options()
opts.add_argument("--headless")  # Headless

browser = webdriver.Chrome(options = opts)  # New Instance of chrome
browser.get(url)  # Go to our URL

text_field = browser.find_element_by_name('q')  # Find The search box
text_field.send_keys(query)  # Send our query
text_field.send_keys(Keys.RETURN)  # Hit enter

time.sleep(1)  # Wait 1 sec

images = browser.find_element_by_link_text('Images')  # Find the images link
images.click()  # Click on Images

time.sleep(2)  # Wait for images to load

counter = 1  # Starting value for the counter

while True:  # While loop to capture multiple screenshots
    body = browser.find_element_by_css_selector('body')  # Find body

    time.sleep(2)  # Wait to load page
    
    if not path.exists('screenshots'): # Check if there is a screenshot folder, If not make a new one
        print('screenshot folder not found,Making one...')
        mkdir('screenshots')
        
    fileName = query.replace(' ', '_') + str(counter) + '.png' # File name for the screnshot file
    browser.save_screenshot('./screenshots/' + fileName) # Save the screenshot to our screenshots folder
    print('Saved Screenshot: ' + fileName) # Print the file name
    
    body.send_keys(Keys.PAGE_DOWN)# IMPORTANT: Scroll down

    counter += 1 # Increase the counter to keep the loop going
    
    if (counter - 1) == Screenshots: # Check if we already got enough screenshots
        print('Saved all screenshots, Closing browser...')
        browser.close() # If yes, close the browser
        break

print('You can close this window now and check your screenshots folder')
