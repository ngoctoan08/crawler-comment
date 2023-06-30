from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from crawling_comment_vnexpress import crawling_comment_vnexpress
from mongoengine import connect

#ket noi database
#connect(db='hoc_nodejs', host='localhost', port=27017)

#global driver

#driver.get("https://vnexpress.net/dai-tuong-to-lam-vu-dak-lak-cho-thay-khong-the-coi-thuong-an-ninh-co-so-4619672.html")
## To load entire webpage
#time.sleep(5)
#crawlingVnexpress = crawling_comment_vnexpress(driver)
#crawlingVnexpress.crawlingComment()
#time.sleep(2)
#driver.quit()
        

def crawlingCommentSkds(driver):
    url = "https://suckhoedoisong.vn/dieu-chinh-gia-nuoc-sach-o-ha-noi-phai-cung-ung-du-chat-luong-dung-quy-chuan-cua-bo-y-te-169230630093201445.htm"

def crawlingCommentThanhnien(driver):
    url = "https://thanhnien.vn/noi-lo-tri-tue-nhan-tao-tiep-quan-the-gioi-185230629122510256.htm"
    driver.get(url)
    time.sleep(5)

    listComment = driver.find_element(By.CLASS_NAME, 'list-comment')
    comments = listComment.find_elements(By.CLASS_NAME, 'item')
    for comment in comments:
        commentText = comment.find_element(By.CLASS_NAME, 'text-comment').text
        reaction = comment.find_element(By.CLASS_NAME, 'total-like').text
        print(commentText + '---' + reaction)
    time.sleep(2)
    driver.quit()

#crawlingCommentThanhnien(driver)

def crawlingCommentCand():
    driver = webdriver.Chrome()
    url = "https://cand.com.vn/Chong-dien-bien-hoa-binh/doi-tuong-nguyen-van-dai-trang-tron-xuyen-tac-vu-gay-roi-antt-o-dak-lak-i697108/"
    driver.get(url)
    time.sleep(10)
    boxComment = driver.find_element(By.CLASS_NAME, 'box-comment')
    #print(len(boxComment))

    #check show more comment
    #try:
    #showMore = boxComment.find_elements(By.CLASS_NAME, 'label')
    #print(len(showMore))
    #    showMore.click()
    #    time.sleep(3)
    #except :
    #    pass
    i = 1
    listComment = boxComment.find_element(By.TAG_NAME, 'ul')
    comments = listComment.find_elements(By.TAG_NAME, 'li')
    for comment in comments:
        commentText = comment.find_element(By.TAG_NAME, 'p').text
        #reaction = comment.find_element(By.CLASS_NAME, 'total-like').text
        print(str(i) + commentText)
        i = i + 1
    time.sleep(2)
    driver.quit()
crawlingCommentCand()
