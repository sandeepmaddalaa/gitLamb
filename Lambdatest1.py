from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\Driver\chromedriver.exe')

driver.get('https://www.lambdatest.com/selenium-playground')


driver.find_element(By.PARTIAL_LINK_TEXT, "Drag & Drop Sliders").click()
ele = driver.find_element(By.XPATH, '//*[@id="slider3"]/div')
ActionChains(driver).drag_and_drop_by_offset(ele, 80, 0).perform()

ele1 = driver.find_element(By.ID, "rangeSuccess").text

print(ele1)

driver.close()
