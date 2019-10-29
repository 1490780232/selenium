from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(r'D:\software\chrome_driver\chromedriver.exe')
driver.get(r'https://www.baidu.com/')
# print(driver.find_element_by_tag_name("body"))
element=driver.find_element_by_link_text( "设置")
# hidden_submenu = driver.find_element_by_css_selector(".nav #submenu1")
actions = ActionChains(driver)
actions.move_to_element(element)
actions.perform()
sleep(1)
element=driver.find_element_by_link_text("高级搜索")
element.click()
sleep(2)
element=driver.find_element_by_id("adv_keyword")

element.send_keys("selenium")

# element = driver.find_elements_by_class_name("gpc")
# all_options = element.find_elements_by_tag_name("option")
# element.find_elements_by_class_name()寻找子元素

select = Select(driver.find_element_by_name('gpc'))
select.select_by_index(1)
sleep(2)
select.select_by_visible_text("最近一年")
select.select_by_value("stf")
# for option in all_options:
#     print("Value is: %s") % option.get_attribute("value")
#     option.click()

driver.find_element_by_class_name("advanced-search-btn").click()


print(element)

sleep(10)
class testBaidu():
    def __init__(self):
        self.driver=webdriver.chrome(r'D:\software\chrome_driver\chromedriver.exe')
    def test_baidu(self):
        driver.get(r'https://www.baidu.com/')
        # 浏览器窗口大小
        driver.set_window_size(800, 600)
        #method = getattr()
