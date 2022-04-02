from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Firefox()
browser.get('https://www.ubereats.com')
addresElem = browser.find_element(By.ID,'location-typeahead-home-input') #Locates the address box.
addresElem.send_keys("New york") #Writes down the address
time.sleep(5) #The program may stop at the next line. Probably the page can't react when the following instruction occurs immediately after.
addresElem.send_keys(Keys.ENTER) #Sends the address.

time.sleep(5)

Super = browser.find_element(By.XPATH, '//*[@id="main-content"]/div/div[1]/div[1]/nav/ul/li[3]/a')
time.sleep(5)
Super.click()
time.sleep(5)

#Gets to the Super section of uber eats. It's done with an xpath due to the dynamic elements of the page.

productSearch = browser.find_element(By. XPATH, '//*[@id="search-field"]') 
productSearch.click()
productSearch.send_keys('banana' + Keys.ENTER)

#Goes to the search bar and makes a search for the specified product.

time.sleep(5)
searchResults = browser.find_elements(By. CLASS_NAME, 'search-result-access') #List of all the stores that appear as search results.
storeCounter = 1 #Counter for the different number of stores.

for i in range(len(searchResults)):
    productsForStore = browser.find_element(By. XPATH, '//*[@id="app-container"]/main/div/div[%s]/button' % str(storeCounter))
    storeCounter += 1
    time.sleep(5)
    productsForStore.click()
    time.sleep(5)

    #A store's button is identified and clicked to get to the store's page.
    #The results of interest will appear in the first row of products.

    productsName = browser.find_elements(By. CLASS_NAME, 'name') 
    productsPrice = browser.find_elements(By. XPATH, '//*[@class="price" or @class="price discounted"]')
    productsPackage = browser.find_elements(By. CLASS_NAME, 'package')

    #Creates three distinct list for each of the given types of information about the product.
    #All lists should be of the same length.

    for name, price, package in zip(productsName, productsPrice, productsPackage): #zip makes a tuple that can loop
                                                                                   #through all names, prices and
                                                                                   #packages from the 3 products lists    
        print(name.text,price.text, package.text)
    browser.back()
    time.sleep(5)

    #Returns to the search results' page.
