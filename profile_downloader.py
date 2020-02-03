from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import urllib.request

class AMFBot():

    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('http://facebook.com')
        sleep(2)
        email_fld = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_fld.send_keys('your email here')
        pwd_fld = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pwd_fld.send_keys('your password here')
        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_b"]')        
        login_btn.click()

    def scroll_through(self):
        page = self.driver.find_element_by_tag_name('html')
        while True:
            page.send_keys(Keys.PAGE_DOWN)
            sleep(0.5)
            break

    def download_profile(self, url):
        try:
            self.driver.get(url)
            sleep(2)
            try:
                name = self.driver.find_elements_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[1]/div/div[3]/div/div[1]/div/div/h1/span[1]/a').text
                print(name)
                #about button
                btn = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[1]/div/div[3]/div/div[2]/div[3]/ul/li[2]/a')
                btn.click()
                #contact and info btn
                btn = bot.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/div[1]/div[2]/div/ul/li/div/div[1]/div/div/div/a[4]/span[1]')
                btn.click()
                #getting gender and other details
                dob = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/div[1]/div[2]/div/ul/li/div/div[2]/div/div/div[2]/div/ul/li[1]/div/div[2]/div/div/span').text
                gender = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/div[1]/div[2]/div/ul/li/div/div[2]/div/div/div[2]/div/ul/li[2]/div/div[2]/div/div/span').text
                print(dob, gender)
                #getting relationship status
                btn = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/div[1]/div[2]/div/ul/li/div/div[1]/div/div/div/a[5]/span[1]')
                btn.click()
                rl_status = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/div[1]/div[2]/div/ul/li/div/div[2]/div/div/div[1]/ul/li/div/div/div/div[2]/div').text
                print(rl_status)
                self.write_to_file(url, name, dob, gender, rl_status)
            except Exception:
                print('no data found')
            
        except Exception:
            print('No DATA')

    def write_to_file(self, url, name, dob, gender, rl_status):
        f = open('data.txt')
        f.write(url, name, dob, gender, rl_status)
        f.close()



if __name__ == '__main__':
    bot = AMFBot()
    bot.login()
    #bot.scroll_through()
    bot.download_profile('https://web.facebook.com/faizan.qadir.75')