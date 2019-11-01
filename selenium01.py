# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:21:45 2019

@author: kanwa
"""

# coding = utf-8
from time import sleep
from selenium import webdriver
selectMethod = eval(input('请输入序列号分别运行子程序'))
# 驱动文件路径
#driverfile_path = r'D:\coship\Test_Framework\drivers\chromedriver.exe'
# 启动浏览器 可以提供路径
#driver = webdriver.Chrome(executable_path=driverfile_path)
# 启动浏览器
def location(text):
    element = driver.find_element_by_link_text(text)
    element.click()


driver = webdriver.Chrome(r'D:\software\chrome_driver\chromedriver.exe')
# 打开百度首页
driver.get(r'https://www.baidu.com/')
# 浏览器窗口大小
driver.set_window_size(800,600)
# 浏览器窗口最大化
# driver.maximize_window()

if selectMethod == 1 :
   #1 id定位：find_element_by_id()
   element = driver.find_element_by_id('kw')
   element.send_keys('selenium')
elif selectMethod == 2:
    #2 name定位： find_element_by_name()  
    driver.find_element_by_name('wd').send_keys('python')
    driver.find
elif selectMethod == 3:
    #class定位：find_element_by_class_name()
    element = driver.find_element_by_class_name('s_ipt')
    element.send_keys('软件测试')
elif selectMethod == 4:
    #tag定位：find_element_by_tag_name()
    elements = driver.find_elements_by_tag_name('input')
    for element in elements:
        print(element)
        if element.get_attribute('class')=='s_ipt':
            element.send_keys('input')
elif selectMethod == 5:
    #link定位：find_element_by_link_text()
    location('新闻')
elif selectMethod == 6:
    #partial_link定位：find_element_by_partial_link_text()
    element = driver.find_element_by_partial_link_text('hao')
    if element.is_enabled:
        print(element.text)
        element.click()
elif selectMethod == 7:
    #1 name定位： find_element_by_name()
    #element = driver.find_element_by_xpath('//*[@id="u1"]/a[3]')    
    element = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/a[3]')
    if element.is_displayed():
        print("Good Job!")
        element.click()
        print("Title:"+ driver.title + "  URL:"+driver.current_url)
        driver.back()
        driver.forward()
        driver.refresh()
    else:
        print("Error happened!")
elif selectMethod == 8:
    #CSS定位：find_element_by_css_selector()
    #css可以通过元素的id、class、标签(tag)这三个常规属性直接定位
#    css用#号表示id属性,如：#kw
#    css用.表示class属性，如：.s_ipt
#    css直接用标签名称，无任何标示符，如：input
    driver.find_element_by_css_selector('#kw').send_keys('css')
# 等待10秒    
sleep(10)  
# 关闭浏览器退出 
driver.quit()
