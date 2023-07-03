from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from bson import ObjectId
from models.news_comment import news_comment
from models.news_comment import sub_comment

class crawling_comment_tuoitre:
    def __init__(self, driver):
        self.driver = driverf


    def crawlingComment(self):
        listComment = self.driver.find_element(By.ID, "listComment")
        ul = listComment.find_element(By.TAG_NAME, "ul")
        comments = ul.find_elements(By.CLASS_NAME, "item-comment")

        if len(comments) <= 0:
            print("Khong co coment nao")
        else:
            i = 0
            #lặp qua từng comments thực hiện các việc sau: 
            # lấy ra các comment chính - và comment phụ
            for comment in comments:
                i = i + 1
                commentText = comment.find_element(By.CLASS_NAME, "contentcomment").text
                elementReaction = comment.find_element(By.CLASS_NAME, "totalreact")
                reaction = elementReaction.find_element(By.TAG_NAME, "span").text
                # save to database
                #commentData = news_comment(_id = ObjectId(), content=commentText, reaction=reaction)
                #print(str(i) + commentText + '---' + reaction)
                #sub comment
                
                try:
                    showSubComment = comment.find_element(By.CLASS_NAME, 'viewreply')
                    isSubcomment = showSubComment.get_attribute('data-visible')

                    if isSubcomment == "1":
                        print(isSubcomment)

                        showSubComment.click()
                        time.sleep(15)
                    
                        subCommentElement = comment.find_element(By.CLASS_NAME, 'comment-rep-top')
                        subComments = subCommentElement.find_elements(By.CLASS_NAME, 'item-comment')
                        print('---' + len(subComments))
                        for subComment in subComments:
                            subCommentText = subComment.find_element(By.CLASS_NAME, "contentcomment").text
                            subElementReaction = subComment.find_element(By.CLASS_NAME, "totalreact")
                            subReaction = subElementReaction.find_element(By.TAG_NAME, "span").text
                            print('----' + subCommentText + '---' + subReaction)
                            #luu vao database
                            #commentData.subcomments.append(sub_comment(id=ObjectId(), content=self.getContent(subComment), reaction=self.getReaction(subComment)))

                except:
                    pass
                #commentData.save()
                #print(commentData.to_json())


global driver
driver = webdriver.Chrome()
driver.get("https://tuoitre.vn/quoc-lo-o-tp-hcm-un-u-toi-7km-xe-co-bo-tung-chut-20230629200625329.htm")
# To load entire webpage
time.sleep(10)
crawlingTuoitre = crawling_comment_tuoitre(driver)
crawlingTuoitre.crawlingComment()
time.sleep(2)
driver.quit()


