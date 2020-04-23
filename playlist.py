# chrome driver exe should be in the same directory

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def process():
     
    driver.get("https://www.youtube.com/playlist?list=PLjzTNlf-E32OXtDrsWsuD6NyEZydWJDJH")
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input").send_keys('\t'*(18+(3*i))+'\n')
    time.sleep(1)
    url=driver.current_url
    driver.get("https://ytmp3.cc/en13/")
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/form/input[1]").send_keys(url+'\n')
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/a[1]").click()
    time.sleep(1)

n=int(input("No. of songs: "))
i=0
while i<n:
    if(i==0):
        driver=webdriver.Chrome()
    process()
    i+=1
driver.get("https://google.com") 
terminate=input()
