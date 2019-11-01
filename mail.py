from selenium import webdriver
from time import sleep

driver=webdriver.Chrome(r'D:\software\chrome_driver\chromedriver.exe')
driver.get("https://mail.qq.com")
sleep(1)
print("=========>")
driver.switch_to.frame('login_frame')
sleep(3)
# switch=driver.find_element_by_class_name("switch_btn")
# if(switch!=None):
#     switch.click()
driver.find_element_by_id("u").send_keys("1490780232")
sleep(1)
driver.find_element_by_id("p").send_keys("Lla34038885051202")


element=driver.find_element_by_id("login_button")
print(element)
element.click()
print(driver.current_url)
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("body").text)
driver.find_element_by_id("pp").send_keys("a34038885051202")

driver.find_element_by_id("folder_1").click()


driver.find_element_by_link_text("写信").click()

print(driver.find_element_by_tag_name("html").text)
mails=driver.find_element_by_class_name("toarea")


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
