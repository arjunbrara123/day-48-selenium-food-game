from selenium import webdriver

chrome_driver_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org/")

events = {}

for event_no in range(5):
    event_date = driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{event_no+1}]/time').text
    event_name = driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{event_no+1}]/a').text
    events[event_no] = {
        "time": event_date,
        "name": event_name
    }

print(events)

driver.quit()

