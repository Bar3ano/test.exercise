import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://github.com/")
time.sleep(2)

sign_in_button = driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/div[2]')
sign_in_button.click()

username = driver.find_element_by_id('login_field')
username.send_keys('')

password = driver.find_element_by_id('password')
password.send_keys('')

sign_in = driver.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]')
sign_in.click()

time.sleep(2)
driver.quit()
