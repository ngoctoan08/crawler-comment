from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from bson import ObjectId
from models.news_comment import news_comment
from models.news_comment import sub_comment

class crawling_comment_vnexpress:
    def __init__(self, driver):
        self.driver = driver

    def checkStyleNone(self, selector):
        element = self.driver.find_element(By.ID, selector)
        style = element.get_attribute("style")
        if "none" in style:
            return True
        return False

    def getContent(self, elements):
        tags = elements.find_elements(By.CLASS_NAME, "full_content") if elements.find_elements(By.CLASS_NAME, "full_content") else elements.find_elements(By.CLASS_NAME, "content_more")
        # lấy ra nội dung của comment
        for j in tags:
            pHtml = j.get_attribute("innerHTML")
            # loại bỏ nội dung thẻ span 
            soup = BeautifulSoup(pHtml, "html.parser")
            for span in soup.find_all("span"):
                span.decompose()
            p_text_without_span = soup.get_text()
        return p_text_without_span

    def getReaction(self, element):
        reaction = element.find_element(By.CLASS_NAME, "reactions-total")
        total_reac = reaction.find_element(By.TAG_NAME, "a")
        return total_reac.text

    def crawlingComment(self):
        list_comment_element = self.driver.find_element(By.ID, "list_comment")
        if self.checkStyleNone("list_comment"):
            print("Không có comment nào!")
        else:
            i = 0
            comments = list_comment_element.find_elements(By.CLASS_NAME, "comment_item") #list <web-element>
            #lặp qua từng comments thực hiện các việc sau: 
            # lấy ra các comment chính - và comment phụ
            for comment in comments:
                i = i + 1
                # save to database
                #commentData = news_comment(_id = ObjectId(), content=self.getContent(comment), reaction=self.getReaction(comment))
                print(str(i) + self.getContent(comment) + self.getReaction(comment))
                #sub comment
                try:
                    showSubComment = comment.find_element(By.CLASS_NAME, 'view_all_reply')
                    showSubComment.click()
                    time.sleep(3)

                    subCommentElement = comment.find_element(By.CSS_SELECTOR, 'div.sub_comment')
                    subComments = subCommentElement.find_elements(By.CLASS_NAME, 'sub_comment_item')
                    for subComment in subComments:
                        #luu vao database
                        print('---' + self.getContent(subComment) + self.getReaction(subComment))

                        #commentData.subcomments.append(sub_comment(id=ObjectId(), content=self.getContent(subComment), reaction=self.getReaction(subComment)))

                except:
                    pass
                #commentData.save()
                #print(commentData.to_json())



