import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.coolgenerator.com/random-text-generator")
time.sleep(2)

sign_in_button = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/div[1]/div/div[2]/form/div[4]/div/button')
sign_in_button.click()

text_area = driver.find_element_dy_xpath('//*[@id="main"]/div/div[2]/div[1]/div[2]/ul/li/textarea')
text_area.click()

driver.execute_script("")

time.sleep(2)
driver.quit()

# попробовать
# text_area.sendKeys(Keys.CONTROL + "a");
# text_area.sendKeys(Keys.DELETE);
