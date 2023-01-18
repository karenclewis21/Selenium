from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import csv

#Set up CSV
file = open("Laptops.csv", "w")
writer = csv.writer(file)
writer.writerow(["name", "price", "specifications", "number of reviews"])

#Creat Chrome Service and Web Driver Instance
web_driver = Service(".\chromedriver.exe")
page_scraper = webdriver.Chrome(service= web_driver)

#Get Page
page_scraper.get("https://webscraper.io/test-sites/e-commerce/static/computers/laptops")


#Locate Name, Price, Specifications, and Number of reviews.
unique_id = 1
while True:
    cards = page_scraper.find_elements(By.CLASS_NAME, "caption")
    for card in cards:
        names = card.find_elements(By.CLASS_NAME,"title")
        prices= card.find_elements(By.CLASS_NAME,"pull-right price")
        specs= card.find_elements(By.CLASS_NAME,"description")
        num_of_reviews= card.find_elements(By.CLASS_NAME, "pull-right")

        #writer.writerow()
        unique_id += 1
        print(cards)

    try:
        element = page_scraper.find_element(By.PARTIAL_LINK_TEXT, "›") 
        element.click() 
    except NoSuchElementException:
        break
#Quit Browser
#file.close()
#web_page.quit()