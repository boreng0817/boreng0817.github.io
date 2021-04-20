import time
import math
import random
import emojis
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

# ===globalVariable===
# 0. Constant 
NAVER_LOGIN_PAGE = f"https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"
NAVER_USER_PAGE = f"https://cafe.naver.com/CafeMemberNetworkView.nhn?m=view&clubid=14062859&memberid=syeon7706#"
DEV_ID = "borengdev"
DEV_PASSWORD = "aszx1245"
# ====================


#
# self.idList {USER_ID : index} 
#               string :  int
#
# self.commentList { USER_ID : { "nickName" : NICKNAME 
#                              , "comment"  : COMMENT
#                              , "time"     : TIME}}
#
# self.IsCommentCorrect { USER_ID : True/False }
#                                       
class Driver:
    def __init__(self):
        # download right chrome driver with pc's chrome version
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.articleNumber = "4039248"
        self.idList = {}
        self.commentList = {}
        self.IsCommentCorrect = {}
        self.idCount = 0
        self.pageNum = 1
        self.soup = None
        self.html = None
        self.wait = None

        self.login()
        self.url = self.getUrl()

    def get(self, url=None):
        if url:
            self.driver.get(url)
        else:
            self.driver.get(self.url)
        try:
            self.wait = WebDriverWait(self.driver, 3)
            self.wait.until(
             EC.presence_of_element_located((By.NAME, 'cafe_main'))
                    )
        except TimeoutException:
            print("Timeout happened no page load")

    #
    # Find latest article's url for choosing winner 
    #  Additional Implementation
    #  1. Read user's recent articles' title
    #  2. Parse with specific criterion
    #  3. Choose latest articles' article number
    #  Format : aritcleNum  articleTitle
    #
    def getUrl(self):
        self.get(NAVER_USER_PAGE) 
        self.driver.switch_to.frame("cafe_main")
        self.driver.switch_to.frame("innerNetwork")
        # Implement finding appropriate article number
        self.html = self.driver.page_source
        self.soup = BeautifulSoup(self.html, 'html.parser')
        
        # Update self.articleNumber
        # ====
        #
        # traverse through all buttons
        #
        # +===
        for temp in self.soup.find_all("td", {"class" : "td_article"}):
            self.articleNumber = get_article_number(temp)
            if self.articleNumber:
                break

        return f"https://cafe.naver.com/ghdi58/%s"%self.articleNumber
    #
    # login with "user_id" and "password" to naver.com
    #  Implementation done
    #  Some improvement
    #  1. Some technique for loading page
    #  2. This function waits exact real time
    #    -> which can cause performance issue
    #
    def login(self, user_id = DEV_ID, password = DEV_PASSWORD):
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
        cssSelector = "#app > div > div > div.ArticleContentBox > " +\
                      "div.article_header > div.ArticleTool > " +\
                      "a.button_comment > strong"
        self.driver.switch_to.frame("cafe_main")
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 
            cssSelector)))
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
    #  Adiitional implementation
    #  1. Classify duplicate user
    #    -> maybe use state or string for this
    #

    def readComment(self):
        cssSelectorButton = "#app > div > div > div.ArticleContentBox > " +\
                            "div.article_container > div.CommentBox > "   +\
                            "div.ArticlePaginate > button:nth-child(%d)"
        cssSelectorUl = "#app > div > div > div.ArticleContentBox > " +\
                        "div.article_container > div.CommentBox > ul"
        self.tempList = []
        for i in range(1, self.pageNum + 1):
            testBool = True #
            #self.driver.find_element_by_css_selector(cssSelector%(i+1)).click()
            self.wait = WebDriverWait(self.driver, 3)
            try:
                self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, cssSelectorButton%(i+1)))
                ).click() 
            except TimeoutException:
                print("Time out exception")

            # Check if UL is properly loaded
            while True:
                self.html = self.driver.page_source
                self.soup = BeautifulSoup(self.html, "html.parser")
                # User should be new to list
                if self.testUl():
                    break

            for temp in self.soup.find('ul', {'class' : 'comment_list'}):
                ret = get_comment_item(temp)
                ######FOR_DEBUGGGING#####
                if testBool:
                    testBool = False
                    print(ret)
                #########################
                # if temp tag is comment
                # or user id is already in commentList
                if (ret is None) or ret[0] in list(self.idList.values()):
                    continue
                else:
                    self.idCount += 1
                    self.idList[self.idCount] = ret[0]
                    self.commentList[ret[0]] = ret[1][ret[0]]

        return

    def testUl(self):
        counterFalse = 0
        counterTrue = 0
        MAX_MATCH = 10
        for temp in self.soup.find('ul', {'class' : 'comment_list'}):
            ret = get_comment_item(temp)

            if (ret is None):
                continue
            
            if ret[0] in self.tempList:
                counterFalse += 1
                continue
            else:
                counterTrue += 1
                self.tempList.append(ret[0])

            if counterFalse == MAX_MATCH:
                return False
            if counterTrue == MAX_MATCH:
                return True

    #
    # Get comment of id = name
    #
    def getComment(self, name):
        return self.commentList[name]["comment"]
    
    #
    # Build IsCommentCorrect
    # Make an dictionary {"userId" : True/False}
    #
    def testComment(self):
        # Check commentList is filled
        for i in range(1, self.idCount + 1):
            idIter = self.idList[i]
            # Emoji should be in the last of comment
            containedEmojis = emojis.get(self.getComment(idIter)[-1])
            if len(containedEmojis) != 0:
                self.IsCommentCorrect[idIter] = True
            else:
                self.IsCommentCorrect[idIter] = False


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

#
# swapNumber -> for option
#
# ====
#
# Check if option is in valid range
#
# ====
#
def get_article_number(articleBlock, option = None):

    def swapNumber(string):
        numberBold = "𝟏 𝟐 𝟑 𝟒 𝟓 𝟔 𝟕 𝟖 𝟗 𝟎".split()
        number = "1 2 3 4 5 6 7 8 9 0".split()

        for i in range(10):
            string.replace(numberBold[i], number[i])

        return string

    mileGift = "날이 좋아서 마일 나눔"

    text = articleBlock.find("a").text.strip()
    number = articleBlock.find("div", {"class":"inner_number"}).string
    
    if option:
        if mileGift in text:
            if option is int(swapNumber(text.split()[-1])):
                return number
    else:
        if mileGift in text:
            return number

    return None

def main():
    import timeit
    counter = 0
    driver = Driver()
    driver.get()
    driver.loadPage()
    #import code
    #code.interact(local=locals())
    driver.inspectPage()
    
    while True:
        start = timeit.default_timer()
        driver.readComment()
        counter += 1

        if counter % 100 is 0:
            # save comment
            continue
        print('Time: ', timeit.default_timer() - start)
            
    driver.testComment()
    
    f1 = open("outTrue.txt", "w")
    f2 = open("outFalse.txt", "w")
    for i in range(1, driver.idCount+1):
        _id = driver.idList[i]
        (f1 if driver.IsCommentCorrect[_id] else f2).\
                write("%s : %s\n"%(_id, driver.getComment(_id)))
    f1.close()
    f2.close()


    return

if __name__ == "__main__":
    main()
