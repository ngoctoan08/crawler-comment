from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url = "https://cand.com.vn/Chong-dien-bien-hoa-binh/doi-tuong-nguyen-van-dai-trang-tron-xuyen-tac-vu-gay-roi-antt-o-dak-lak-i697108/"
driver.get(url)
driver.implicitly_wait(10) # seconds
    
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)

# Tìm các phần tử có class name là "uk-comment-list"
ul_comments = driver.find_element(By.CLASS_NAME, 'uk-comment-list')
liTags = ul_comments.find_elements(By.TAG_NAME, 'li')
print(len(liTags))
for liTag in liTags:
    commentText = liTag.find_element(By.TAG_NAME, 'p').text
    reaction = liTag.find_element(By.CLASS_NAME, 'btn-like').get_attribute('data-like')
    print(commentText + '---' + reaction)