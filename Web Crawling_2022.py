#-*- coding: utf-8 -*-
import selenium
from selenium import webdriver
# from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
import time
import csv

options = webdriver.ChromeOptions() 
options.add_argument("disable-gpu") # #그래픽 성능 낮춰서 크롤링 성능 쪼금 높이기 
driver = webdriver.Chrome('C:\Python\chromedriver.exe',chrome_options=options)
driver.maximize_window()
driver.get("https://www.youtube.com/watch?v=vlTgPkijThA")
time.sleep(1)

f = open(r'C:\Python\New_Covid.csv','wt', encoding='UTF8') 
wr = csv.writer(f) 

body = driver.find_element_by_tag_name('body')   
for i in range(0,100):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
# textlist = [] 
for x in range(1,600): 
    t = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[%d]/ytd-comment-renderer/div[3]/div[2]/ytd-expander/div/yt-formatted-string[2]'%x) 
    t2 = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[%d]/ytd-comment-renderer/div[3]/div[2]/div[1]/div[2]/yt-formatted-string/a'%x)
    text = t.text
    text2 = t2.text 
    wr.writerow([x, text, text2]) 
    time.sleep(0.5)
    
# Test
    