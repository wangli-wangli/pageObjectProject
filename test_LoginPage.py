# -*- coding: utf-8 -*-
# coding=utf-8
'''
Project:页面基本操作方法：如open，input_username，input_password，click_submit
'''
from selenium.webdriver.common.by import By
from test_BasePage import BasePage
from time import sleep

#继承BasePage类
class LoginPage(BasePage):
    #定位器，通过元素属性定位元素对象
    serverSelector_loc =(By.XPATH,"//span[contains(.,\'请选择服务器地址\')]")#测试服务器选择框
    serverButton_loc =(By.CSS_SELECTOR,'".anticon-setting > svg"')  # 配置服务器的图标
    server_loc =(By.XPATH, "//div[4]/div")#测试服务器
    mobileLogin_loc =(By.XPATH, " // *[ @ id = 'rc-tabs-0-tab-mobile']")#手机号登录
    phoneNumber_loc =(By.XPATH, '//*[@id="data0"]')#手机号输入框
    verificationCode_loc =(By.XPATH, '//*[@id="data0"]')#验证码输入框
    loginButton_loc=(By.XPATH, '//*[@id="root"]/div/div[1]/div/div[2]/div/div[2]/div/form/div[2]/div/div/div/button')#登录按钮
    
    
    #操作
    #通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    #打开网页
    def open(self):
    #调用page中的_open打开连接
        self._open(self.base_url, self.pagetitle)
    
    #输入用户名：调用send_keys对象，输入用户名
    def select_server(self):
        self.find_element(self.serverButton_loc).click()
        self.find_element(self.serverSelector_loc).click()
        self.find_element(self.server_loc).click()
        sleep(5)
    
    #选择手机号登录
    def select_mobileLogin(self):
        self.find_element(self.mobileLogin_loc).click()
        
    #输入手机号
    def input_phoneNumber(self,phoneNumber):
        self.find_element(self.phoneNumber_loc)[0].send_keys(self.phoneNumber)
    
    #输入验证码
    def input_verificationCode(self,verificationCode):
        self.find_element(self.verificationCode_loc)[1].send_keys(self.verificationCode)
    
    #点击登录按钮
    def click_login(self):
        self.find_element(self.loginButton_loc).click()
    
   