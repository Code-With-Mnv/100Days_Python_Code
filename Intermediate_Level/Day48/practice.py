from selenium import webdriver

# from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.in")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text

# to access a particular HTML tag by CLASS (can also be accessed by NAME/ID/CSS SELECTOR attribute)
# IF NOTHING WORKS OUT OF CLASS/ID/NAME/CSS SELECTOR... (some tags may not have any such attributes)... then we can use... XPATH... it always works. XPATH can be copied by right clicking the element in the inspect tab.
# once a tag/element is accessed using "By" and "values", we can tap into any of it's related info... like it's id, class, name, text, size(in case of buttons/images), placeholder (in case of input text boxes)

# driver.close() to close a single tab
# driver.quit() to close whole browser
