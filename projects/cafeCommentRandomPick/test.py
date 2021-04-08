import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

class Driver:
    def __init__(self):
        # download right chrome driver with pc's chrome version
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.url = self.getUrl()
    
    def get(self, url=None):
        if url:
            self.driver.get(url)
        else:
            self.driver.get(self.url)
        print(url)

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


def main():
    driver = Driver()
    driver.get(f"https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")
    driver.login("borengdev", "aszx1245")
    time.sleep(2)
    driver.get(driver.url)
    import code
    code.interact(local=locals())
    return

if __name__ == "__main__":
    main()
