from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support. ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import csv

#Set up CSV
file = open("Laptops.csv", "w")
writer = csv.writer(file)
writer.writerow(["name", "price", "specifications", "number of reviews"])

#Create Chrome Service and Web Driver Instance
web_driver = Service(".\chromedriver.exe")
page_scraper = webdriver.Chrome(service= web_driver)

#Get Page
load_page = WebDriverWait(web_driver, 10)
page_scraper.get("https://webscraper.io/test-sites/e-commerce/static/computers/laptops")

#Close Popups
page_scraper.find_element(By.CLASS_NAME, "acceptCookies").click()
#element_to_watch = page_scraper.find_element(By.CLASS_NAME, "col-md-9")

#Locate Name, Price, Specifications, and Number of reviews.
unique_id = 1
while True:
    cards = page_scraper.find_elements(By.CLASS_NAME, "caption")
    for card in cards:
       name = card.find_element(By.CLASS_NAME,"title"),
       # price= card.find_element(By.CLASS_NAME, "pull-right.price"),
       # specifications= card.find_element(By.CLASS_NAME,"description"),
       # num_of_reviews= card.find_element(By.CLASS_NAME, "pull-right"),

     #   writer.writerow([unique_id, name, price, specifications, num_of_reviews])
       # unique_id += 1
    print(name.text)
    try:
      element = page_scraper.find_element(By.PARTIAL_LINK_TEXT, "›").click() 
        
    except NoSuchElementException:
      break
#Quit Browser
#file.close()
#web_page.quit()