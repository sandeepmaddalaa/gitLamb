from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path='C:\Driver\chromedriver.exe')


driver.get('https://www.lambdatest.com/selenium-playground')


driver.find_element(By.PARTIAL_LINK_TEXT, "Simple Form Demo").click()
driver.find_element(By.ID, "user-message").send_keys("Welcome to Lambdatest")
driver.find_element(By.ID, "showInput").click()
lamp=driver.find_element(By.ID, "message").text
assert lamp == 'Welcome to Lambdatest'

driver.close()
