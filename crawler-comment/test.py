from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://vnexpress.net/bo-truong-xay-dung-bo-quy-dinh-thoi-han-so-huu-nha-chung-cu-4619193.html')

# click radio button
try:
    python_button = driver.find_element(By.CLASS_NAME, "view_all_reply") 
    python_button.click()
    time.sleep(3)
except :
    print("toandaika")

driver.quit()