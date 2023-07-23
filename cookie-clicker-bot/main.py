from selenium import webdriver
from selenium.webdriver.common.by import By

firefox_driver_path = DRIVER_PATH
driver = webdriver.Firefox(executable_path=firefox_driver_path)
url = "https://www.python.org/"
# url = "https://www.amazon.com/Instant-Pot-Plus-Programmable-Sterilizer/dp/B075CWJ3T8/ref=pd_di_sccai_cn_sccl_2/142-0349101-7757720?pd_rd_w=0YUiP&pf_rd_p=1ed8df3a-0df8-4988-98b9-252e4c99c568&pf_rd_r=RW13CQG6Z460Y80RRQ3C&pd_rd_r=4f67b2b3-b136-48a9-83ac-f5fc14da309b&pd_rd_wg=1b7AP&pd_rd_i=B075CWJ3T8&psc=1"
driver.get(url)
date = driver.find_elements(by=By.CLASS_NAME, value="menu time")

events_list_element = []
events = driver.find_elements(
    by=By.XPATH, value="/html/body/div/div[3]/div/section/div[3]/div[2]/div/ul/li")

event_list = []
date_list = []

for item in date[5:]:
    date_list.append(item.get_attribute("textContent"))

for i in range(1, len(events) + 1):
    events_list_element.append(driver.find_element(
        by=By.XPATH, value=f"/html/body/div/div[3]/div/section/div[3]/div[2]/div/ul/li[{i}]/a"))

for item in events_list_element:
    event_list.append(item.get_attribute("textContent"))

event_dict = {}
for item in event_list:
    event_item = {
        "time": date_list[event_list.index(item)],
        "name": item
    }
    event_dict[event_list.index(item)] = event_item

print(event_dict)


driver.quit()
