from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from tqdm import tqdm
import random
from EmailSender import *


class InstagramBot:
    # Creates object and starts the browser
    def __init__(self, username, password):
        print("Hi, i'm your personal bot")
        print("Im using account: @" + username)

        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()
        self.followers = None
        self.following = None
        sleep(1)

    # Logs in instagram.com
    def login(self):
        # Open web page
        driver = self.driver
        driver.get("https://www.instagram.com/")
        sleep(4)

        '''# Click login button
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        sleep(3)'''

        # Enter data
        print("Trying to log in as: " + self.username)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        if len(self.password) > 1:
            passworword_elem.send_keys(self.password)
            passworword_elem.send_keys(Keys.RETURN)
            sleep(8)
        else:
            sleep(20)

        # Disable pop ups
        for i in range(3):
            try:
                self.navigateToProfile()
                break
            except Exception:
                pass
            try:
                not_download = driver.find_element_by_xpath("//a[@class='_3m3RQ _7XMpj']")
                not_download.click()
                sleep(4)
                self.navigateToProfile()
                break
            except Exception:
                pass
            try:
                not_now_button = driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']")
                not_now_button.click()
                sleep(4)
                self.navigateToProfile()
                break
            except Exception:
                pass
        self.goToMain()

    # sets it selfs parameters
    def setFollowers(self):
        driver = self.driver
        self.goToProfile()
        following, followers = self.getFollowLists(self.username)
        self.following = following
        self.followers = followers

    # Goes to the main page of insta
    def goToMain(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        sleep(2)

    # Goes to the profile by clicking in the profile button
    def navigateToProfile(self):
        driver = self.driver
        profile_link = driver.find_element_by_xpath('//a[@class="gmFkV"]')
        profile_link.click()
        sleep(2)

    # Goes to the user profile page
    def goToProfile(self):
        self.lookForAccount(self.username)

    # searches for the given account
    def searchForAccount(self, account):
        driver = self.driver
        seach_box = driver.find_element_by_xpath("//input[@placeholder='Search']")
        seach_box.clear()
        seach_box.send_keys(account)
        sleep(2)
        seach_box.send_keys(Keys.ARROW_DOWN)
        sleep(0.5)
        for i in range(6):
            seach_box.send_keys(Keys.ARROW_UP)
            sleep(0.2)
        sleep(1)
        seach_box.send_keys(Keys.RETURN)
        sleep(3)

    def lookForAccount(self, account):
        driver = self.driver
        driver.get("https://www.instagram.com/"+account+"/")
        sleep(2)

    # searches the given hastag
    def searchHastag(self, htg):
        self.searchForAccount(htg)

    # NOT TESTED !!!!!
    def followInScreen(self):
        driver = self.driver
        posts = self.getPostList(200)
        for post in posts:
            driver.get(post)
            sleep(15)
            try:
                follow_button = driver.find_element_by_xpath("//button[@class='oW_lN sqdOP yWX7d    y3zKF     ']")
                follow_button.click()
                like_button = driver.find_element_by_xpath("//button[@class='dCJp8 afkep']")
                like_button.click()
                sleep(15)
            except Exception:
                print("exception")

    # Returns the number of followers and follows of the current profile
    def getFollowersNum(self):
        driver = self.driver
        spans = driver.find_elements_by_xpath("//span[@class='g47SY ']")
        values = [self.get_text(s) for s in spans]
        return int(values[1]), int(values[2])

    # Returns the number of posts of the given account
    def getPostNum(self, account):
        driver = self.driver
        self.lookForAccount(account)
        spans = driver.find_elements_by_xpath("//span[@class='g47SY ']")
        values = [self.get_text(s) for s in spans]
        return int(values[0])

    # Returns the HTML text inside an element
    def get_text(self, el):
        return self.driver.execute_script("""
        var parent = arguments[0];
        var child = parent.firstChild;
        var ret = "";
        while(child) {
            if (child.nodeType === Node.TEXT_NODE)
                ret += child.textContent;
            child = child.nextSibling;
        }
        return ret;
        """, el)

    # Returns the following and the follower lists of a given account
    def getFollowLists(self, account):
        driver = self.driver
        n_followers, n_following = self.getFollowersNum()

        # Get following:
        following_button = driver.find_element_by_xpath("//a[@href='/" + account + "/following/']")
        following_button.click()
        sleep(2)
        for i in range(int(n_following / 8)):                   
            last_follow = driver.find_elements_by_xpath("//a[@class='FPmhX notranslate  _0imsa ']")[-1]
            driver.execute_script("arguments[0].scrollIntoView(true);", last_follow)
            sleep(1)
        following_a = driver.find_elements_by_xpath("//a[@class='FPmhX notranslate  _0imsa ']")
        following = [f.get_property("title") for f in following_a]
        self.goToProfile()
        if account != self.username:
            self.lookForAccount(account)
        #close_button = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button/svg")
        #close_button.click()
        sleep(1)

        # Get followers
        following_button = driver.find_element_by_xpath("//a[@href='/" + account + "/followers/']")
        following_button.click()
        sleep(2)

        for i in range(int(n_followers / 8)):
            last_follow = driver.find_elements_by_xpath("//a[@class='FPmhX notranslate  _0imsa ']")[-1]
            driver.execute_script("arguments[0].scrollIntoView(true);", last_follow)
            sleep(1)

        following_a = driver.find_elements_by_xpath("//a[@class='FPmhX notranslate  _0imsa ']")
        followers = [f.get_property("title") for f in following_a]
        #close_button = driver.find_element_by_xpath("//span[@class='glyphsSpriteX__outline__24__grey_9 u-__7' and"
        #                                           " @aria-label='Cerrar']")
        #close_button.click()
        self.goToProfile()
        self.lookForAccount(account)
        sleep(1)

        return following, followers

    # NOT TESTED !!!
    def getPostList(self, n_posts=144):
        driver = self.driver
        for i in range(int(n_posts / 12)):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(3)
        posts_a = driver.find_elements_by_xpath("//div[@class='v1Nh3 kIKUG  _bz0w']/a")
        return [elem.get_attribute('href') for elem in posts_a if '.com/p/' in elem.get_attribute('href')]

    # NOT TESTED !!!
    def getCommenters(self, comment=[]):
        driver = self.driver
        commenters = driver.find_elements_by_xpath('//a[@class="FPmhX notranslate TlrDj"]')
        comments = driver.find_elements_by_xpath('//div[@class="C4VMK"]/span')
        comments = [self.get_text(comments[i]) for i in range(len(commenters)) if commenters[i].get_attribute("title") != self.username]
        commenters = [c.get_attribute("title") for c in commenters if c.get_attribute("title") != self.username]
        if comment != []:
            commenters = [commenters[i] for i in range(len(comments)) if comments[i] in comment]
            comments = [c for c in comments if c in comment]
        return commenters, comments

    # Check who isn't following back an account, if account == None => checks it for itself
    def checkFollowersOf(self, account):
        driver = self.driver
        if account:
            self.lookForAccount(account)
        else:
            self.goToProfile()
            account = self.username

        following, followers = self.getFollowLists(account)

        print("People that don't follow " + account + " back: ")
        for f in following:
            if not f in followers:
                print(f)

        self.goToMain()

    # Likes all post from a given account, use dislike to dislike them
    def likeAll(self, account, dislike=False):
        driver = self.driver
        print("Liking all photos from: " + account)
        self.lookForAccount(account)

        n_posts = self.getPostNum(account)
        posts_href = self.getPostList(n_posts)

        self.likeList(posts_href, dislike)

    # Likes all posts in the list use dislike to dislike them
    def likeList(self, list, pause=2, dislike=False):
        for post in tqdm(list, desc="(Dis)Likes"):
            self.like(post, dislike)
            sleep(pause)
           
    # likes the given post, use dislike option to dislike
    def like(self, post, dislike=False):
        driver = self.driver
        if dislike:  # Dislike xPath
            #xPath = '//button[@class="wpO6b "]'
            xPath = '//*[//*[name()="svg"] and @class="_8-yf5 " and @aria-label="Unlike" and @height="24" and @width="24"]' #  and @height="24" and width="24"
        else:  # Like xPath
            xPath = '//*[//*[name()="svg"] and @class="_8-yf5 " and @aria-label="Like" and @height="24" and @width="24"]' #  and @height="24" and width="24"
       
        driver.get(post)
        sleep(3)
        try:
            like_button = lambda: driver.find_element_by_xpath(xPath).click()
            like_button()
        except Exception as e:
            if dislike:
                print("Didn't dislike ;(\n" + str(e))
            else:
                print("Didn't like ;(\n" + str(e))
            sleep(2)
    
    # Un follows account
    def unfollow(self, account):
        driver = self.driver
        self.lookForAccount(account)
        try:
            unfollow_button = driver.find_element_by_xpath('//button[@class="_5f5mN    -fzfL     _6VtSN     yZn4P   "]')
            unfollow_button.click()
            sleep(1)
            unfollow_button = driver.find_element_by_xpath('//button[@class="aOOlW -Cab_   "]')
            unfollow_button.click()
            sleep(1)
        except Exception as e:
            print("Couldn't unfollow " + account + "\n" +  str(e))

    # Follows given account
    def follow(self, account):
        driver = self.driver
        self.lookForAccount(account)        
        try:
            follow_button = driver.find_element_by_xpath('//button[@class="_5f5mN       jIbKX  _6VtSN     yZn4P   "]')
            follow_button.click()
            sleep(2)
            self.goToMain()
        except Exception as e:
            print("Couldn't follow      " + str(e))

    # Accepts all follow requests filtering by a usernames list if given
    def acceptFollows(self, filter=None):
        driver = self.driver
        activity_button = driver.find_element_by_xpath("//a[@class='_0ZPOP kIKUG  ']")
        activity_button.click()
        sleep(2)
        try:
            accept_button = driver.find_element_by_xpath("//span[@class='BcJ68']")
            accept_button.click()
            sleep(2)
            follow_list = driver.find_elements_by_xpath("//a[@class='FPmhX notranslate  yrJyr']")
            follow_list = [f.get_attribute("title") for f in follow_list]
            button_list = driver.find_elements_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']")
            button_list = [b for b in button_list if self.get_text(b) == 'Confirm']
            if filter != None:
                button_list = [button_list[i] for i in range(len(filter)) if follow_list[i] in filter]
            for b in button_list:
                b.click()

        except Exception as e:
            print("Didn't accept" + str(e))
        self.lookForAccount(self.username)
        self.goToMain()

    # Unstable
    def randomTag(self, photo, num):
        driver = self.driver
        driver.get(photo)
        sleep(3)


        comment_txtBox = driver.find_element_by_xpath('//textarea[@class="Ypffh"]')
        #driver.execute_script("arguments[0].textContent = 'Hola carcola';", comment_txtBox)
        sleep(4)
        try:
            comment_txtBox.send_keys(Keys.ENTER)
        except Exception:
            comment_txtBox.send_keys(Keys.ENTER)
        #comment_txtBox.send_keys("caracola")
        '''
        # comment_txtBox.send_keys()

        for n in range(num):
            comment = "@" + random.choice("bcdfghjklmnpqrstvwxyz") + random.choice("aeiouy")
            #comment_txtBox.send_keys(comment)
            comment_txtBox.send_keys("hola")
            sleep(2)
            for _ in range(2):
                comment_txtBox.send_keys(Keys.ENTER)
                sleep(0.5)

        comment_txtBox.send_keys(Keys.ENTER)
        sleep(0.5)'''

    # Open chat window from main menu
    def chatMenu(self):
        driver = self.driver
        chat_btn = driver.find_element_by_xpath('//a[@class="xWeGp"]')
        chat_btn.click()
        sleep(1)
    
    # Return the account with unread chats
    def getNewChats(self):
        driver = self.driver
        chats = driver.find_elements_by_xpath('//div[@class="_7UhW9   xLCgt       qyrsm KV-D4             fDxYl     "]')
        return [self.get_text(c) for c in chats]

    # Open the chat to talk to a given account
    def openChat(self, account):
        driver = self.driver
        chats = driver.find_elements_by_xpath('//div[@class="_7UhW9   xLCgt       qyrsm KV-D4             fDxYl     "]')
        matching = [c for c in chats if self.get_text(c) == account][-1]
        matching.click()
        sleep(1)

    # Send msg in the chat currently open
    def sendMsg(self, msg="Hi"):
        driver = self.driver
        txtarea = driver.find_element_by_xpath('//textarea[@placeholder="Message..."]')
        txtarea.click()
        sleep(0.2)
        txtarea.send_keys(msg)
        txtarea.send_keys(Keys.RETURN)

    # Closes browser
    def closeBrowser(self):
        self.driver.close()

