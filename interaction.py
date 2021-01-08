from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chrome_driver_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")
fName = driver.find_element_by_name("fName")
fName.send_keys("Arjun")
lName = driver.find_element_by_name("lName")
lName.send_keys("Brara")
email = driver.find_element_by_name("email")
email.send_keys("arjunbrara@hotmail.co.uk")
email.send_keys(Keys.ENTER)


