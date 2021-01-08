from selenium import webdriver
from interruptingcow import timeout
from time import time

chrome_driver_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie = driver.find_element_by_id('bigCookie')

for i in range(20):
    t_end = time() + 5
    while time() < t_end:
        for j in range(100):
            cookie.click()
    for prod_no in range(18):
        prod = driver.find_element_by_xpath(f'//*[@id="product{17 - prod_no}"]')
        prod_text = prod.text
        if len(prod_text) != 0:
            prod_desc = prod_text.split('\n')
            if prod.text[:3] != "???":
                prod.click()

prods = driver.find_elements_by_class_name('product unlocked enabled')

breakpoint()
