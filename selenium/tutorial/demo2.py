#coding:utf-8
from selenium import webdriver
from time import sleep,time,ctime
import unittest
import threading
import HTMLTestRunner

class DemoPage(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('http://www.baidu.com')

    # def testTitle(self,value='testData'):
    #     self.assertTrue(self.driver.title in self.getXmlData(value) )

    def testUrl(self):
        # dir(tutorial.HTMLTestRunner)
        print(self.driver.current_url)

        # # HTMLTestRunner.main()
        # suite = unittest.makeSuite(DemoPage)
        # # 定义自动化报告目录
        #
        # filename = '/Users/Jesse/Desktop/python-tutorial/selenium/tutorial/report.html'
        # fp = file(filename, 'wb')
        # runner = HTMLTestRunner.HTMLTestRunner(
        #     stream=fp,
        #     title=u'自动化测试报告',
        #     description=u'自动化测试报告'
        # )
        # runner.run(suite)
        # fp.close()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__=='__main__':
    # HTMLTestRunner.main()
    suite=unittest.makeSuite(DemoPage)
    #定义自动化报告目录

    filename='/Users/Jesse/Desktop/python-tutorial/selenium/tutorial/report.html'
    fp=file(filename,'wb')

    runner=HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'自动化测试报告',
        description=u'自动化测试报告'
    )
    runner.run(suite)
    fp.close()
