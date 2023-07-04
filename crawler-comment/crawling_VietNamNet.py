import time
from selenium.webdriver.common.by import By
from models.news_comment import news_comment
from bson import ObjectId

class crawling_comments_vietnamnet():
    def __init__(self, driver):
        self.driver = driver
    
 
    def convert_to_iframe_comment(self):
        '''Chuyển đổi sang iframe comments'''       
        iframe = self.driver.find_element(By.CSS_SELECTOR,"#comment > div > div > iframe")
        self.driver.switch_to.frame(iframe)
 
 
    def view_more_comment(self):
        '''Hiển thị comments bị ẩn'''
        try:
            view_more_button = self.driver.find_element(By.CSS_SELECTOR, '#root > div > div > button')
        except:
            pass
        else:
            if view_more_button:        
                view_more_button.click()
                time.sleep(3)
                return self.view_more_comment()
            
            
    def showSubComments(self):
        '''Hiển thị comments phụ'''
        try:
            show_sub_comments = self.driver.find_elements(By.CSS_SELECTOR,"li.pb-\[5px\]")
            for show_sub_comment in show_sub_comments:
                show_sub_comment.click()
                time.sleep(3)
        except:
            pass
        
        
    def getContent(self):
        """Lấy nội dung comment và lưu vào database"""
        
        #Lấy nội dung
        user_item = self.driver.find_elements(By.CLASS_NAME, 'user__item')
        for content in user_item:
            '''Lấy comments'''
            comment_text = content.find_element(By.TAG_NAME, "p").text
            
            '''Lấy reaction của comment'''
            try:
                user_react = content.find_element(By.CSS_SELECTOR,'span.group-hover\:text-\[\#666\]').text
            except:
                user_react = "0"
            
            #Lưu vào database
            # commentData = news_comment(_id = ObjectId(), content=comment_text)
            # commentData.save()
            print(comment_text + " " + user_react + " like" )

    
        

    def crawling_comment(self):
        '''Kết hợp chức năng của các hàm'''
        self.convert_to_iframe_comment()
        self.view_more_comment()
        self.showSubComments()
        self.getContent()
        
    
        
   
        
        
        
    
        
    