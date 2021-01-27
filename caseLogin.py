# -*- coding: utf-8 -*-


import unittest 
from test_LoginPage import LoginPage
from selenium import webdriver

class Caselogin126mail(unittest.TestCase):
    """
          选择测试服务器，并且登录
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.url ="http://testadmin.huxin315.com/user/login"
        self.phoneNumber ="15176128570"
        self.verificationCode ="000000"
    
    #用例执行体
    def test_login_mobile(self):
        #声明LoginPage类对象
        login_page = LoginPage(self.driver, self.url, u"互训预付平台")
        #调用打开页面组件
        login_page.open()
        #选择服务器
        login_page.select_server()
        #选择手机号登录
        login_page.select_mobileLogin()
        #输入手机号
        login_page.input_phoneNumber(self.phoneNumber)
        #输入验证码
        login_page.input_verificationCode(self.verificationCode)  
        #点击登录
        login_page.click_login()    

    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()