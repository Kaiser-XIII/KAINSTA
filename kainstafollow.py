from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


username = input("İnstagram kullanıcı adınız:")
password = input("İnstagram şifreniz:")
userfollow = input("Takip edilecek kullanıcı adı:")



class Instagram:
    
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    driver_path = webdriver.Chrome(options=chrome_options)   
    
    
    
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.browser = Instagram.driver_path


    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        self.browser.maximize_window()
        time.sleep(3)            
        usernameInput = self.browser.find_element(By.NAME,"username")
        passwordInput = self.browser.find_element(By.NAME,"password")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        passwordInput.send_keys(Keys.ENTER)

        time.sleep(3)
        if self.browser.find_element(By.CLASS_NAME,"_ac8f"):
            self.browser.find_element(By.CLASS_NAME,"_ac8f").click()
            time.sleep(3)
        
        if self.browser.find_element(By.CLASS_NAME,'_a9-z'):
            self.browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
        
        time.sleep(3)  
    
    
    def followUser(self,username):
        self.browser.get(f"https://www.instagram.com/{username}/")
        time.sleep(5)

        followButton = self.browser.find_element(By.TAG_NAME,"button")

        if followButton.text == "Takip Et":
            followButton.click()
            time.sleep(2)
        else:
            print(f"{username} sayfasını zaten takip ediyorsunuz.")

        
    def __del___(self):
        time.sleep(5)
        # self.browser.close()


app = Instagram(username,password)

app.signIn()
app.followUser(userfollow)
