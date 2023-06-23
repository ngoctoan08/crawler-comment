from selenium import webdriver
import time
from crawling_comment_vnexpress import crawling_comment_vnexpress
from mongoengine import connect

#ket noi database
connect(db='hoc_nodejs', host='localhost', port=27017)

global driver
driver = webdriver.Chrome()
driver.get("https://vnexpress.net/dai-tuong-to-lam-vu-dak-lak-cho-thay-khong-the-coi-thuong-an-ninh-co-so-4619672.html")
# To load entire webpage
time.sleep(5)
crawlingVnexpress = crawling_comment_vnexpress(driver)
crawlingVnexpress.crawlingComment()
time.sleep(2)
driver.quit()
        
