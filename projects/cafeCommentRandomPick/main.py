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

#############################
# First test of the program #
#############################
# 1. If there are no comment in article,
#    Program can't read any further comment
# 
# 2. When there're less than 100 comments,
#    it can't press button in self.readComment()
#
# 3. False negative -> easy to add to True list
#
# 4. # of emoji -> should be 1
#
# 5. Comment count should be dynamic
#
# 6. when testing comment page,
#    MAX_COUNT should be dynamic -> min(comment.count % 100, 10)
#
# 7. Consider duplicate user -> forbid duplicate
#
# 8. get winner's cafe page



# ===globalVariable===
# 0. Constant 
NAVER_LOGIN_PAGE = f"https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"
NAVER_USER_PAGE = f"https://cafe.naver.com/CafeMemberNetworkView.nhn?m=view&clubid=14062859&memberid=syeon7706#"
DEV_ID = "borengdev"
DEV_PASSWORD = "aszx1245"

TIME_INTERVAL = 20
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
        self.commentNum = 0
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

    def getCafeMain(self):
        self.driver.get(self.url)
        
        try:
            self.wait = WebDriverWait(self.driver, 3)
            self.wait.until(
             EC.presence_of_element_located((By.NAME, 'cafe_main'))
                    )
        except TimeoutException:
            print("Timeout happened no page load")
        self.driver.switch_to.frame("cafe_main")
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

        #return f"https://cafe.naver.com/ghdi58/%s"%self.articleNumber
        return f"https://cafe.naver.com/ghdi58/3932356"
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
        self.commentNum = int(self.soup.find('strong', {'class':'num'}).string)
        self.pageNum = int(math.ceil(self.commentNum/100))

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
        self.tempList = [["temp"]*5]
        self.inspectPage()
        for i in range(1, self.pageNum + 1):
            testBool = True #
            if self.pageNum != 1:
                self.wait = WebDriverWait(self.driver, 3)
                try:
                    self.wait.until(EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, cssSelectorButton%(i+1)))
                    ).click() 
                except TimeoutException:
                    print("Time out exception at readComment")

            # Check if UL is properly loaded
            while True:
                self.html = self.driver.page_source
                self.soup = BeautifulSoup(self.html, "html.parser")
                # User should be new to list
                if self.testUl(i):
                    break

            for temp in self.soup.find('ul', {'class' : 'comment_list'}):
                ret = get_comment_item(temp)
                ######FOR_DEBUGGGING#####
                if testBool:
                    testBool = False
                    if ret is not None:
                        print(ret[0])
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

    #Start at here
    def testUl(self, pageIndex):
        counterFalse = 0
        counterTrue = 0
        count = 0
        tempList = []
        MAX_MATCH = 0


        if self.commentNum % 100 == 0:
            MAX_MATCH = len(self.tempList[pageIndex - 1])
        else:
            MAX_MATCH = min(self.commentNum % 100, 
                len(self.tempList[pageIndex-1]))

        if self.soup.find('ul', {'class' : 'comment_list'}) is None:
            return False
        for temp in self.soup.find('ul', {'class' : 'comment_list'}):
            ret = get_comment_item(temp)

            if (ret is None):
                continue
            
            
            tempList.append(ret[0])
            
            
            print(self.tempList)
            print(count, MAX_MATCH)
            if ret[0] == self.tempList[pageIndex - 1][count]:
                counterFalse += 1
            else:
                counterTrue += 1
            count += 1

            if count == MAX_MATCH:
                if counterFalse < counterTrue:
                    self.tempList.append(tempList)
                    return True
                else:
                    return False

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

    def dumComment(self, arg):
        f = open("dump%d.txt"%arg, "w")
        
        string = "id:%s$nickName:%s$comment:%s$time:%s"
        for i in range(1, self.idCount + 1):
            _id = self.idList[i]
            nickName = self.commentList[_id]['nickName']
            comment = self.commentList[_id]['comment']
            time = self.commentList[_id]['time']
            f.write(string%(_id, nickName, comment, time) + '\n')

        f.close()

        


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
    
    while True:
        start = timeit.default_timer()
        driver.getCafeMain()
        driver.readComment()

        if counter % TIME_INTERVAL is 0:
            driver.dumComment(int(counter/TIME_INTERVAL))
        print('[%d]Time: '%counter, timeit.default_timer() - start)
        print('\n\n\n\n\n')
            
        counter += 1
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
