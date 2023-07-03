from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from crawling_comment_vnexpress import crawling_comment_vnexpress
from mongoengine import connect
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#ket noi database
#connect(db='hoc_nodejs', host='localhost', port=27017)

driver = webdriver.Chrome()

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


def crawlingCommentCand(driver):
    url = "https://cand.com.vn/Chong-dien-bien-hoa-binh/doi-tuong-nguyen-van-dai-trang-tron-xuyen-tac-vu-gay-roi-antt-o-dak-lak-i697108/"
    driver.get(url)
    driver.implicitly_wait(10) # seconds
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

    # Tìm các phần tử có class name là "uk-comment-list"
    ul_comments = driver.find_element(By.CLASS_NAME, 'uk-comment-list')
    liTags = ul_comments.find_elements(By.TAG_NAME, 'li')
    for liTag in liTags:
        commentText = liTag.find_element(By.TAG_NAME, 'p').text
        reaction = liTag.find_element(By.CLASS_NAME, 'btn-like').get_attribute('data-like')
        print(commentText + '---' + reaction)

def crawlingCommentHanoimoi(driver):
    url = "https://hanoimoi.vn/khai-mac-hoi-nghi-lan-thu-muoi-ba-ban-chap-hanh-dang-bo-thanh-pho-ha-noi-khoa-xvii-538828.html"
    driver.get(url)
    time.sleep(5)

    commentElement = driver.find_element(By.CLASS_NAME, 'c-comments')
    listComment = commentElement.find_element(By.CLASS_NAME, 'c-comment-list')
    if listComment.text == '':
        print("Khong co comment")
    else:
        listComment
    #comments = listComment.find_elements(By.CLASS_NAME, 'item')
    #for comment in comments:
    #    commentText = comment.find_element(By.CLASS_NAME, 'text-comment').text
    #    reaction = comment.find_element(By.CLASS_NAME, 'total-like').text
    #    print(commentText + '---' + reaction)
    #time.sleep(2)
    #driver.quit()

def crawlingCommentVtv(driver):
    url = "https://vtv.vn/xa-hoi/ca-voi-quy-hiem-xuat-hien-o-vung-bien-de-gi-binh-dinh-20230703030300518.htm"
    driver.get(url)
    time.sleep(5)

    commentElement = driver.find_element(By.CLASS_NAME, 'comment_list')
    if commentElement.text == '':
        print("Khong co comment")
    else:
        print("Co comment")
    #comments = listComment.find_elements(By.CLASS_NAME, 'item')
    #for comment in comments:
    #    commentText = comment.find_element(By.CLASS_NAME, 'text-comment').text
    #    reaction = comment.find_element(By.CLASS_NAME, 'total-like').text
    #    print(commentText + '---' + reaction)
    time.sleep(2)
    driver.quit()

def crawlingCommentDbns(driver):
    url = "https://daibieunhandan.vn/quoc-hoi-va-cu-tri/tao-dong-luc-khich-le-manh-me-can-bo-chien-si-cong-an-nhan-dan-i334662/"
    driver.get(url)
    time.sleep(5)

    commentElement = driver.find_element(By.CLASS_NAME, 'comment_list')
    if commentElement.text == '':
        print("Khong co comment")
    else:
        print("Co comment")
    #comments = listComment.find_elements(By.CLASS_NAME, 'item')
    #for comment in comments:
    #    commentText = comment.find_element(By.CLASS_NAME, 'text-comment').text
    #    reaction = comment.find_element(By.CLASS_NAME, 'total-like').text
    #    print(commentText + '---' + reaction)
    time.sleep(2)
    driver.quit()

def crawlingCommentQdns(driver):
    url = "https://www.qdnd.vn/quoc-phong-an-ninh/tin-tuc/dai-tuong-phan-van-giang-chu-tri-hoi-nghi-thuong-vu-quan-uy-trung-uong-732106"
    driver.get(url)
    time.sleep(5)

    commentElement = driver.find_element(By.CLASS_NAME, 'comment_list')
    if commentElement.text == '':
        print("Khong co comment")
    else:
        print("Co comment")
    #comments = listComment.find_elements(By.CLASS_NAME, 'item')
    #for comment in comments:
    #    commentText = comment.find_element(By.CLASS_NAME, 'text-comment').text
    #    reaction = comment.find_element(By.CLASS_NAME, 'total-like').text
    #    print(commentText + '---' + reaction)
    time.sleep(2)
    driver.quit()


#crawlingCommentHanoimoi(driver)
#crawlingCommentVtv(driver)
#crawlingCommentCand(driver)
#crawlingCommentThanhnien(driver)
def crawlingCommentBaotintuc(driver):
    url = "https://baotintuc.vn/thoi-su/thu-tuong-ly-cuong-chu-tri-le-don-thu-tuong-pham-minh-chinh-tham-chinh-thuc-trung-quoc-20230626103202912.htm"
    driver.get(url)
    driver.implicitly_wait(10) # seconds
    # nếu trang nào dùng iframe thì phải switch ra html để lấy các elements
    iframe = driver.find_element(By.ID, 'ifComment')
    driver.switch_to.frame(iframe)

    listCommentElement = driver.find_element(By.ID, 'listComment')
    listComment = listCommentElement.find_element(By.TAG_NAME, 'ul')
    if listComment.text == '':
        print("Khong co comment")
    else:
        print("co comment")

        #comments = listComment.find_elements(By.CLASS_NAME, 'item')
        #for comment in comments:
        #    commentText = comment.find_element(By.CLASS_NAME, 'text-comment').text
        #    reaction = comment.find_element(By.CLASS_NAME, 'total-like').text
        #    print(commentText + '---' + reaction)
    time.sleep(2)
    driver.quit()

def crawlingCommentCongthuong(driver):
    url = "https://congthuong.vn/bo-cong-thuong-ho-tro-dinh-hinh-thi-truong-cho-doanh-nghiep-260652.html"
    driver.get(url)
    driver.implicitly_wait(10) # seconds
    # nếu trang nào dùng iframe thì phải switch ra html để lấy các elements
    iframe = driver.find_element(By.ID, 'ifComment')
    driver.switch_to.frame(iframe)

    listCommentElement = driver.find_element(By.ID, 'listComment')
    listComment = listCommentElement.find_element(By.TAG_NAME, 'ul')
    if listComment.text == '':
        print("Khong co comment")
    else:
        print("co comment")

        #comments = listComment.find_elements(By.CLASS_NAME, 'item')
        #for comment in comments:
        #    commentText = comment.find_element(By.CLASS_NAME, 'text-comment').text
        #    reaction = comment.find_element(By.CLASS_NAME, 'total-like').text
        #    print(commentText + '---' + reaction)
    time.sleep(2)
    driver.quit()

def crawlingCommentBaophapluat(driver):
    url = "https://baophapluat.vn/lo-ngai-thieu-nuoc-phat-dien-neu-mua-khong-nhu-du-bao-post451525.html"
    driver.get(url)
    driver.implicitly_wait(10) # seconds

    listCommentElement = driver.find_element(By.CLASS_NAME, 'list-comment')
    if listCommentElement.text == '':
        print("Khong co comment")
    else:
        print("co comment")

        #comments = listComment.find_elements(By.CLASS_NAME, 'item')
        #for comment in comments:
        #    commentText = comment.find_element(By.CLASS_NAME, 'text-comment').text
        #    reaction = comment.find_element(By.CLASS_NAME, 'total-like').text
        #    print(commentText + '---' + reaction)
    time.sleep(2)
    driver.quit()
crawlingCommentBaophapluat(driver)