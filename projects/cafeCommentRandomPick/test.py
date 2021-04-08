import time
import math
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

class Driver:
    def __init__(self):
        # download right chrome driver with pc's chrome version
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.url = self.getUrl()
        self.commentList = {}
    
    def get(self, url=None):
        if url:
            self.driver.get(url)
        else:
            self.driver.get(self.url)

    def getUrl(self):
        return f"https://cafe.naver.com/ghdi58?iframe_url_utf8=%2FArticleRead.nhn%253Fclubid%3D14062859%2526page%3D1%2526boardtype%3DL%2526articleid%3D3988712%2526referrerAllArticles%3Dtrue"

    def login(self, user_id, password):
        import random
        # wait until page is loaded
        loginString = "document.getElementsByName(\'%s\')[0].value=\'%s\'"
        time.sleep(random.randrange(1,3))
        self.driver.execute_script(loginString%("id", user_id))
        self.driver.execute_script(loginString%("pw", password))
        time.sleep(random.randrange(1,3))
        self.driver.find_element_by_class_name('btn_global').click()

    def readComment(self):
        return

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



def main():
    f = open("output.txt", "w")
    driver = Driver()
    driver.get(f"https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")
    driver.login("borengdev", "aszx1245")
    time.sleep(2)
    driver.get()
    time.sleep(2)
    driver.driver.switch_to.frame('cafe_main')
    html = driver.driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    commentNum = int(soup.find("strong", {"class":"num"}).string)
    pageNum = int(math.ceil(commentNum/100))
    for i in range(1, pageNum + 1):
        driver.driver.find_element_by_css_selector(
                "#app > div > div > div.ArticleContentBox > " + 
                "div.article_container > div.CommentBox > "   + 
                "div.ArticlePaginate > button:nth-child(%d)"%(i+1)).click()
        time.sleep(1)
        html = driver.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        for temp in soup.find('ul', {'class':'comment_list'}):
            ret = get_comment_item(temp)
            if ret:
                print(ret[1])
                f.write(ret[0] + " : " + ret[1][ret[0]]['comment'] + "\n")

    f.close()
    import code
    code.interact(local=locals())
    return

if __name__ == "__main__":
    main()
