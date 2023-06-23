from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from bson import ObjectId
from models.news_comment import news_comment
from models.news_comment import sub_comment

class crawling_comment_dantri:
    def __init__(self, driver):
        self.driver = driver


    def crawlingComment(self):
        container = self.driver.find_element(By.CLASS_NAME, "comment-container")
        list_comment_element = container.find_element(By.CLASS_NAME, "comment-list")
        #check empty
        isEmpty = list_comment_element.find_elements(By.CLASS_NAME, "comment-empty")
        if len(isEmpty) > 0:
            print("Khong co coment nao")
        else:
            #show more comment
            try:
                btnMore = container.find_element(By.CLASS_NAME, "comment-more")
                btnMore.click()
                time.sleep(2)
            except :
                pass
            i = 0
            comments = list_comment_element.find_elements(By.CLASS_NAME, "comment-item") #list <web-element>
            #lặp qua từng comments thực hiện các việc sau: 
            # lấy ra các comment chính - và comment phụ
            for comment in comments:
                i = i + 1
                commentText = comment.find_element(By.CLASS_NAME, "comment-text").text
                elementReaction = comment.find_element(By.CLASS_NAME, "like")
                reaction = elementReaction.find_element(By.TAG_NAME, "b")
                # save to database
                #commentData = news_comment(_id = ObjectId(), content=commentText, reaction=reaction)
                print(str(i) + commentText + '---' + reaction.text)
                #sub comment
                #try:
                #    showSubComment = comment.find_element(By.CLASS_NAME, 'view_all_reply')
                #    showSubComment.click()
                #    time.sleep(3)

                #    subCommentElement = comment.find_element(By.CSS_SELECTOR, 'div.sub_comment')
                #    subComments = subCommentElement.find_elements(By.CLASS_NAME, 'sub_comment_item')
                #    for subComment in subComments:
                #        #luu vao database
                #        commentData.subcomments.append(sub_comment(id=ObjectId(), content=self.getContent(subComment), reaction=self.getReaction(subComment)))

                #except:
                #    pass
                #commentData.save()
                #print(commentData.to_json())


global driver
driver = webdriver.Chrome()
driver.get("https://dantri.com.vn/kinh-doanh/pho-thong-doc-se-khong-ha-chuan-tin-dung-20230621114057709.htm")
# To load entire webpage
time.sleep(5)
crawlingDantri = crawling_comment_dantri(driver)
crawlingDantri.crawlingComment()
time.sleep(2)
driver.quit()

