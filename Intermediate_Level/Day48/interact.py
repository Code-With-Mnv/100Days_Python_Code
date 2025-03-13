from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

# button = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")

# button.click()        (to click on a hyperlink/button on the site)

# to access a hyperlink on the website using it's face text

# link_to_content_portal = driver.find_element(By.LINK_TEXT, value="Content portals")

# link_to_content_portal.click()

# to type something and search in the search box present on the website
search_icon = driver.find_element(
    By.CSS_SELECTOR, value="#p-search a"
)  # TAPS ONTO THE SEARCH BOX

search_icon.send_keys(
    Keys.ENTER
)  # TYPES THE WORD "PYTHON" IN THE SEARCH BOXS and HITS "ENTER"

search_box = driver.find_element(By.CLASS_NAME, value="cdx-text-input__input")

search_box.send_keys("Python", Keys.ENTER)
