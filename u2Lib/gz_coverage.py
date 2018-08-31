#coding:utf-8
import uiautomator2 as u2
import uiautomator2.ext.htmlreport as htmlreport
import unittest
import time

class Testgz(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.u = u2.connect('160.6.90.84:7912')
        cls.u.healthcheck()     #检查并维持守护程序的运行
        # hrp = htmlreport.HTMLReport(cls.u,'screenreport')
        # hrp.patch_click()   #每次点击前截图
        cls.u.make_toast('老哥，测试机还给徐勇。谢谢',3)
        # cls.u.show.toast('测试开始',3)

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.u.app_start('com.lphtsccft') #session restart app
        time.sleep(3)

    def testEnterGz(self):
        self.u(text='行情').click()
        self.u(text='更多').click()
        self.u(text='股转').click()

if __name__ == '__main__':
    unittest.main()

