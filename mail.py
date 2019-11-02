from selenium import webdriver
from time import sleep
import html2text
import pandas as pd
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
def login_mail(driver,username,passwd,verify_password=None):
    driver = webdriver.Chrome(r'.\chromedriver.exe')
    driver.get("https://mail.qq.com")
    driver.switch_to.frame('login_frame')
    switch = driver.find_element_by_id("switcher_plogin")
    if (switch != None):
        switch.click()
    driver.find_element_by_id("u").send_keys("1490780232")
    driver.find_element_by_id("p").send_keys("Lla34038885051202")
    driver.find_element_by_id("login_button").click()
    driver.switch_to.default_content()
    # driver.find_element_by_id("pp").click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "pp"))
    )

    element.send_keys("a34038885051202")
    element = driver.find_element_by_id("btlogin")
    element.click()
    sleep(3)
    return driver
def send_mail(driver,mail_name,subject,content,attach=None):
    # 写信
    driver.find_element_by_id("composebtn").click()
    driver.switch_to.frame("mainFrame")
    sleep(1)
    # 收件人
    driver.find_element_by_id("toAreaCtrl").find_element_by_tag_name("input").send_keys("2573304635@qq.com")
    # 邮件主题
    driver.find_element_by_id("subject").send_keys("这是一封测试邮件")
    # 添加附件
    driver.find_element_by_id("composecontainer").find_element_by_tag_name("input").send_keys(
        "C:\\Users\\Administrator\\Desktop\\1904.01975.pdf")
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
    # 邮件正文
    driver.find_element_by_tag_name('body').send_keys("感谢大哥，今天测试完成")
    sleep(10)
    driver.switch_to.parent_frame()
    # 发送
    element = driver.find_element_by_id("toolbar")
    element.find_element_by_link_text("发送").click()
    return driver
    sleep(1000)
#接受所有邮件到excel中
def get_mail(driver):
    mail_info = pd.DataFrame(columns=["邮件主题", "发件人", "时间", "邮件内容", "是否有附件"])
    driver.find_element_by_id("folder_1").click()
    # driver.switch_to_default_content()
    # print(driver.find_element_by_tag_name("body").text)
    # driver.switch_to.frame("")
    driver.switch_to.frame('mainFrame')
    sleep(2)
    is_last_page=False
    while(not is_last_page):
        mails = driver.find_elements_by_css_selector('table.i td.l')
        mail_num = len(mails)
        print(mail_num)
        windows = []
        for i in range(mail_num):
            print("================>", i)
            mail = driver.find_elements_by_css_selector('table.i td.l')[i]
            ActionChains(driver).context_click(mail).perform()
            driver.find_elements_by_css_selector(".menu_item")[1].click()
            # driver.switch_to.frame("mainFrame")
            sleep(2)
            driver.switch_to.window(driver.window_handles[1])
            driver.switch_to.frame("mainFrame")
            # print(driver.find_element_by_tag_name("body").text)
            dic={}
            # print("邮件主题=====>", driver.find_element_by_id("subject").text)
            # print("发件人=======>",
            #       driver.find_element_by_xpath("//*[@id=\"mainmail\"]/div[2]/table[2]/tbody/tr/td[1]/span[2]").text)
            # print("邮件时间=====>",
            #       driver.find_element_by_xpath("//*[@id=\"mainmail\"]/div[2]/table[3]/tbody/tr[1]/td[1]/b").text)
            # print("邮件内容=====>", )
            dic["邮件主题"]=driver.find_element_by_id("subject").text
            dic["发件人"]= driver.find_element_by_xpath("//*[@id=\"mainmail\"]/div[2]/table[2]/tbody/tr/td[1]/span[2]").text
            dic["时间"]=driver.find_element_by_xpath("//*[@id=\"mainmail\"]/div[2]/table[3]/tbody/tr[1]/td[1]/b").text
            dic["邮件内容"]=driver.find_element_by_id("contentDiv").text
            mail_info=mail_info.append(dic,ignore_index=True)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            driver.switch_to.frame('mainFrame')
            print(mail_info)
            sleep(2)
        mail_info.to_excel("./mail.xlsx", sheet_name='Sheet1', index=False)
        element=driver.find_element_by_id("nextmail")
        if(element!=None):
            is_last_page=True
            element.click()
            sleep(2)
    print("===========>OK")


if __name__ == '__main__':
    driver=webdriver.Chrome(r'.\chromedriver.exe')
    driver.get("https://mail.qq.com")
    driver.switch_to.frame('login_frame')
    switch=driver.find_element_by_id("switcher_plogin")
    if(switch!=None):
        switch.click()
    driver.find_element_by_id("u").send_keys("1490780232")
    driver.find_element_by_id("p").send_keys("Lla34038885051202")
    driver.find_element_by_id("login_button").click()
    driver.switch_to.default_content()
    # driver.find_element_by_id("pp").click()
    element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID,"pp"))
    )

    element.send_keys("a34038885051202")
    element=driver.find_element_by_id("btlogin")
    element.click()
    sleep(3)

    get_mail(driver)


print(html2text.html2text(driver.find_element_by_tag_name("body").text))

#写信
driver.find_element_by_id("composebtn").click()
driver.switch_to.frame("mainFrame")
sleep(1)
#收件人
driver.find_element_by_id("toAreaCtrl").find_element_by_tag_name("input").send_keys("2573304635@qq.com")
#邮件主题
driver.find_element_by_id("subject").send_keys("这是一封测试邮件")
#添加附件
driver.find_element_by_id("composecontainer").find_element_by_tag_name("input").send_keys("C:\\Users\\Administrator\\Desktop\\1904.01975.pdf")
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
#邮件正文
driver.find_element_by_tag_name('body').send_keys("感谢大哥，今天测试完成")
sleep(10)
driver.switch_to.parent_frame()
#发送
element=driver.find_element_by_id("toolbar")
element.find_element_by_link_text("发送").click()
# element.find_element_by_tag_name("a").click()
sleep(1000)




driver.find_element_by_id("folder_1").click()
# driver.switch_to_default_content()
# print(driver.find_element_by_tag_name("body").text)
# driver.switch_to.frame("")
driver.switch_to.frame('mainFrame')
sleep(2)
mails=driver.find_elements_by_css_selector('table.i td.l')
mail_num=len(mails)
print(mail_num)
windows=[]
for i in range(mail_num):
    print("================>",i)
    mail=driver.find_elements_by_css_selector('table.i td.l')[i]
    ActionChains(driver).context_click(mail).perform()
    driver.find_elements_by_css_selector(".menu_item")[1].click()
    # driver.switch_to.frame("mainFrame")
    sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    driver.switch_to.frame("mainFrame")
    # print(driver.find_element_by_tag_name("body").text)
    print("邮件主题=====>",driver.find_element_by_id("subject").text)
    print("发件人=======>",driver.find_element_by_xpath("//*[@id=\"mainmail\"]/div[2]/table[2]/tbody/tr/td[1]/span[2]").text)
    print("邮件时间=====>",driver.find_element_by_xpath("//*[@id=\"mainmail\"]/div[2]/table[3]/tbody/tr[1]/td[1]/b").text)
    print("邮件内容=====>",driver.find_element_by_id("contentDiv").text)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.switch_to.frame('mainFrame')
    sleep(2)

    # mail.click()
    # driver.back()


mails=driver.find_elements_by_class_name("toarea")
# try:
num=len(mails)
print(num)
for i in range(num):
    # driver.switch_to.frame("mainFrame")
    # mails = driver.find_elements_by_class_name("toarea")
    print(mails)
    mail_para=mails[i].find_elements_by_tag_name("tbody")
    for j in range(len(mail_para)):
        # mail_para[j].find_element_by_class_name("i").click()
        mail_para[j].click()
        sleep(1)
        driver.back()
        sleep(1)
        driver.switch_to.frame("mainFrame")
        mails = driver.find_elements_by_class_name("toarea")
        mail_para = mails[i].find_elements_by_tag_name("tbody")
# except NoSuchElementException :
#     print('没有这样的元素')
#     driver.close()
# except Exception as err:
#     print(err)
    #    print(type(err))
    #    print(err.args)
    # print('error')
    # driver.close()
sleep(3)
#########写信
#单击写信按钮
# driver.find_element_by_link_text("写信").click()
#
#
# print(driver.find_element_by_tag_name("html").text)
# mails=driver.find_element_by_class_name("toarea")


#
# # driver.switch_to_default_content()
# # print(driver.find_element_by_tag_name("body").text)
# driver.switch_to.frame("")
# for i in range(len(mails)):
#     mail=mails.find_element_by_tag_name("tbody")
#     mail.find_element_by_class_name("1").click()
#     sleep(100)
# for handle in driver.window_handles:
#     print(handle)
#     driver.switch_to_window(handle)
# driver.switch_to_window("mainFrame")
# print(driver.find_element_by_tag_name("body").text)
# driver.find_element_by_id("folder_1").click()
# driver.switch_to_frame('actionFrame')
# mails=driver.find_element_by_class_name("toarea")
# driver.switch_to.frame("")
# for i in range(len(mails)):
#     mail=mails.find_element_by_tag_name("tbody")
#     mail.find_element_by_class_name("1").click()
#     sleep(100)
#


sleep(10)