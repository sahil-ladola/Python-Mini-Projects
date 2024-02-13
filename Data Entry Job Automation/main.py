import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(URL)

webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

links = soup.find_all("a", class_="property-card-link")
list_links = [link.get("href") for link in links]
print(list_links)

prices = soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")
list_price = [price.getText().replace("/mo", "").split("+")[0] for price in prices]
print(list_price)

addresses = soup.select(".StyledPropertyCardDataWrapper address")
list_address = [address.getText().strip().replace("|", "") for address in addresses]
print(list_address)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
for n in range(len(list_links)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdIswJTjfsxm_R5BHlFCsZT4GaZupSADYbGUKddrSElKozoGA/"
               "viewform?usp=sf_link")
    time.sleep(2)

    input_address = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/'
                                                           'div/div[1]/div/div[1]/input')
    input_price = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/'
                                                         'div/div[1]/div/div[1]/input')
    input_link = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/'
                                                        'div[1]/div/div[1]/input')

    input_address.send_keys(list_address[n])
    input_price.send_keys(list_price[n])
    input_link.send_keys(list_links[n])

    btn_submit = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    btn_submit.click()
driver.quit()
