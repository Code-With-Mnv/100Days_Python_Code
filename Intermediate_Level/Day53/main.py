import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
access_the_site = requests.get(url=ZILLOW_URL)

web_soup = BeautifulSoup(access_the_site.text, "html.parser")

all_weblinks = [
    weblink["href"]
    for weblink in web_soup.find_all(
        name="a", class_="StyledPropertyCardDataArea-anchor", href=True
    )
]

all_prices = [
    rent.getText()
    for rent in web_soup.find_all(
        name="span", class_="PropertyCardWrapper__StyledPriceLine"
    )
]

all_addresses = [
    address.getText().strip() for address in web_soup.find_all(name="address")
]

properties = []

for _ in range(len(all_weblinks)):
    properties.append(
        {
            "price": all_prices[_],
            "address": all_addresses[_],
            "link": all_weblinks[_],
        }
    )


for propertyData in properties:
    driver = webdriver.Chrome()
    driver.get(url="https://forms.gle/sgmNLUzCnR7n5B5a8")

    time.sleep(2)

    rent_input = driver.find_element(
        by=By.XPATH,
        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input',
    )

    address_input = driver.find_element(
        by=By.XPATH,
        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea',
    )

    link_input = driver.find_element(
        by=By.XPATH,
        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input',
    )

    submit_button = driver.find_element(
        by=By.XPATH,
        value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span',
    )

    time.sleep(2)

    rent_input.send_keys(propertyData["price"])
    address_input.send_keys(propertyData["address"])
    link_input.send_keys(propertyData["link"])
    submit_button.click()
