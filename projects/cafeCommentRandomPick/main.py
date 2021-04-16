import time
import math
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

#
# self.idList {USER_ID : index} 
#               string :  int
#
# self.commentList { USER_ID : { "nickName" : NICKNAME 
#                              , "comment"  : COMMENT
#                              , "time"     : TIME}}
#
# self.IsCommentCorresct { USER_ID : True/False }
#                                       
class Driver:
    def __init__(self):
        # download right chrome driver with pc's chrome version
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.url = self.getUrl()
        self.idList = {}
        self.commentList = {}
        self.IsCommentCorresct = {}
        self.idCount = 0
        self.pageNum = 1
        self.soup = None
        self.html = None

    def get(self, url=None):
        if url:
            self.driver.get(url)
        else:
            self.driver.get(self.url)
        time.sleep(random.randrange(1,3))

    #
    # Find latest article's url for choosing winner 
    #  Additional Implementation
    #  1. Read user's recent articles' title
    #  2. Parse with specific criterion
    #  3. Choose latest articles' article number
    #  Format : aritcleNum  articleTitle
    #
    def getUrl(self):
        return f"https://cafe.naver.com/ghdi58?iframe_url_utf8=%2FArticleRead.nhn%253Fclubid%3D14062859%2526page%3D1%2526boardtype%3DL%2526articleid%3D3988712%2526referrerAllArticles%3Dtrue"

    #
    # login with "user_id" and "password" to naver.com
    #  Implementation done
    #  Some improvement
    #  1. Some technique for loading page
    #  2. This function waits exact real time
    #    -> which can cause performance issue
    #
    def login(self, user_id, password):
        loginString = "document.getElementsByName(\'%s\')[0].value=\'%s\'"
        # wait until page is loaded
        self.get(NAVER_LOGIN_PAGE)
        self.driver.execute_script(loginString%("id", user_id))
        self.driver.execute_script(loginString%("pw", password))
        # To avoid chaptcha
        time.sleep(random.randrange(1,3))
        self.driver.find_element_by_class_name('btn_global').click()
        time.sleep(random.randrange(1,3))
    
    #
    # Update Driver.soup / Driver.html
    # after move into new page
    #
    def loadPage(self):
        self.driver.switch_to.frame("cafe_main")
        self.html = self.driver.page_source
        self.soup = BeautifulSoup(self.html, 'html.parser')

    #
    # Check page's length of comment page
    # More Implementation
    #  1. Check the driver is in right page
    #
    def inspectPage(self):
        commentNum = int(self.soup.find('strong', {'class':'num'}).string)
        self.pageNum = int(math.ceil(commentNum/100))

    #
    # Naive approach for reading comment from article
    # Make an dictionary {"userId" : True/False}
    #  Adiitional implementation
    #  1. Classify duplicate user
    #    -> maybe use state or string for this
    #

    def readComment(self):
        cssSelector = "#app > div > div > div.ArticleContentBox > " +\
                      "div.article_container > div.CommentBox > "   +\
                      "div.ArticlePaginate > button:nth-child(%d)"

        for i in range(1, self.pageNum + 1):
            self.driver.find_element_by_css_selector(cssSelector%(i+1)).click()
            time.sleep(1)
            self.html = self.driver.page_source
            self.soup = BeautifulSoup(self.html, "html.parser")
            for temp in self.soup.find('ul', {'class' : 'comment_list'}):
                ret = get_comment_item(temp)
                # if temp tag is comment
                # or user id is already in commentList
                if (ret is None) or ret[0] in list(self.idList.values()):
                    continue
                else:
                    self.idCount += 1
                    self.idList[self.idCount] = ret[0]
                    self.commentList[ret[0]] = ret[1][ret[0]]

        return
    
    #
    # Get comment of id = name
    #
    def getComment(self, name):
        return self.commentList[name]["comment"]
    

def get_comment_item(commentBlock):
    try:
        retId = commentBlock.find("a", {"class" : "comment_thumb"})["href"]
        retNickname = commentBlock.find("a", {"aria-expanded":"false"})
        retComment = commentBlock.find("span", {"class":"text_comment"})
        retTime = commentBlock.find("span", {"class":"comment_info_date"})

        Id = retId.split("&")[2].split("=")[1]
        comment = "".join(list(retComment.stripped_strings))
        return [Id, {Id : {"nickName": retNickname.string.strip(),
                           "comment" : comment,
                           "time"    : retTime.string}}]
    except TypeError:
        return None

# ===globalVariable===
# 0. Constant 
NAVER_LOGIN_PAGE = f"https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"
# ====================

def main():
    driver = Driver()
    driver.login("borengdev", "aszx1245")
    driver.get()
    driver.loadPage()
    driver.inspectPage()
    driver.readComment()

    for i in len(driver.idCount):
        print(driver.idList[i], driver.getComment(driver.idList[i]))

    import code
    code.interact(local=locals())
    return

if __name__ == "__main__":
    main()
