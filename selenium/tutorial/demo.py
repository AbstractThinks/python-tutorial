# -*- coding: utf-8 -*-
from selenium import webdriver


profile = webdriver.FirefoxProfile()

profile.set_preference('general.useragent.override','Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko)\
 Version/9.0 Mobile/13B143 Safari/601.1Name')

browser = webdriver.Firefox(profile)
# 浏览器最大化
# browser.maximize_window()

# 设置浏览器宽/高
browser.set_window_size(480, 800)

# 浏览器后退
# browser.back()

# 浏览器前进
# browser.forward()

#通过id方式定位
# browser.find_element_by_id("kw").send_keys("selenium")

#通过name方式定位
# browser.find_element_by_name("wd").send_keys("selenium")

#通过tag name方式定位
# browser.find_element_by_tag_name("input").send_keys("selenium")

#通过class name 方式定位
# browser.find_element_by_class_name("s_ipt").send_keys("selenium")

#通过CSS方式定位
# browser.find_element_by_css_selector("#kw").send_keys("selenium")

#通过xphan方式定位
# browser.find_element_by_xpath("//input[@id='kw']").send_keys("selenium")

#send_keys("XX") 用于在输入框输入内容
#click() 用于点击一个按钮
#clear() 用于清除输入框的内容

# text  获取该元素的文本
# submit  提交表单
# get_attribute  获得属性值

# 页面内嵌 iframe window等标签
# switch_to_frame()
# switch_to_window()
# implicitly_wait()

# execute_script 执行js代码


browser.get("http://www.baidu.com")
# browser.find_element_by_id("kw").send_keys("selenium")
# browser.find_element_by_id("su").click()

browser.implicitly_wait(30)


# 浏览器退出
# browser.quit()