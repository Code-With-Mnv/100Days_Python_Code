from selenium import webdriver
from selenium.webdriver.common.by import By

date_list = []
event_list = []

driver = webdriver.Chrome()
driver.get("https://www.python.org/")

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

# for i in range(0,len(event_times)):

# tags = driver.find_elements(
#     By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul'
# )
#
#
# dates_events = tags[0].text.split("\n")
#
#
# for i in range(0, len(dates_events)):
#     if i in [0, 2, 4, 6, 8]:
#         date_list.append(dates_events[i])
#     else:
#         event_list.append(dates_events[i])
#
# event_dict = {}
#
# for i in range(0, 5):
#     event_dict[i] = {"date": date_list[i], "event": event_list[i]}
#
# print(event_dict)
