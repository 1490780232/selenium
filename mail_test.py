import selenium.webdriver
from time import sleep
from selenium.webdriver import ActionChains
def get_mail(driver):
    driver.find_element_by_id("folder_1").click()
    # driver.switch_to_default_content()
    # print(driver.find_element_by_tag_name("body").text)
    # driver.switch_to.frame("")
    driver.switch_to.frame('mainFrame')
    sleep(2)
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
        print("邮件主题=====>", driver.find_element_by_id("subject").text)
        print("发件人=======>",
              driver.find_element_by_xpath("//*[@id=\"mainmail\"]/div[2]/table[2]/tbody/tr/td[1]/span[2]").text)
        print("邮件时间=====>",
              driver.find_element_by_xpath("//*[@id=\"mainmail\"]/div[2]/table[3]/tbody/tr[1]/td[1]/b").text)
        print("邮件内容=====>", driver.find_element_by_id("contentDiv").text)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        driver.switch_to.frame('mainFrame')
        sleep(2)