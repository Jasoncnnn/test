'''
auth:hu anqing
date:2020.3.31
description:实现了自动从VPN登入到东南大学图书馆并进入研讨室预约系统自动登录
            初步构建了交互菜单
'''
import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait

def ChromeDriver(url):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(2)
    driver.get(url)
    #time.sleep(2)
    return driver

class login(object):

    def __init__(self,user,STU_num,code):
        self.user=user        #一卡通
        self.STU_num=STU_num  #学号
        self.code=code        #信息门户密码

    #从VPN转入到预约界面
    def VPN_login(self): 
        driver=ChromeDriver('https://vpn.seu.edu.cn')
        input_list=driver.find_elements_by_class_name('input-txt')
        input_tick=driver.find_element_by_class_name('checkbox__mark.checkbox--small')
        input_user=input_list[0]
        input_code=input_list[1]
        input_user.send_keys(self.user)
        input_code.send_keys(self.code)
        if(not input_tick.is_selected()):
            input_tick.click()
        input_code.send_keys(Keys.ENTER)
        time.sleep(1)
        wait=WebDriverWait(driver,10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'a[title="webvpn图书馆"]')))
        input_lib=driver.find_element_by_css_selector('a[title="webvpn图书馆"]')
        input_lib.click()
        #time.sleep(3)
        driver.switch_to_window(driver.window_handles[1])
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'a[class="icon-group-item"]')))
        opt_list=driver.find_elements_by_css_selector('a[class="icon-group-item"]')
        input_subscribe=opt_list[2]
        input_subscribe.click()
        time.sleep(1)
        driver.switch_to_window(driver.window_handles[2])
        return driver
    
    #登录预约界面
    def Subscribe_login(self,driver):
        wait=WebDriverWait(driver,10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'li[class="login lg_act login_hide"]')))
        click_login=driver.find_element_by_css_selector('li[class="login lg_act login_hide"]')
        click_login.click()
        time.sleep(1)
        input_id=driver.find_element_by_xpath('//div[@class="ui-dialog ui-widget ui-widget-content ui-corner-all ui-front"]/div[@id="dlg_login"]//table//input[@type="text" and @name="id"]')
        input_pwd=driver.find_element_by_xpath('//div[@class="ui-dialog ui-widget ui-widget-content ui-corner-all ui-front"]/div[@id="dlg_login"]//table//input[@type="password" and @name="pwd"]')
        #input_id.clear()
        input_id.send_keys(self.user)
        #input_pwd.clear()
        input_pwd.send_keys(self.code)
        input_pwd.send_keys(Keys.ENTER) 
        time.sleep(5)
        return driver
    
    #交互菜单
    def Interactive_Menu(self,driver):
        wait=WebDriverWait(driver,10)   
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'li[class="it"]')))
        room_list=driver.find_elements_by_css_selector('li[class="it"]')
        room1=room_list[0]
        room2=room_list[3]
        flag=1
        a=0
        while(flag):
            while(flag):
                a=input('请选择你要预定的自修室：1、单人研读室 2、彩色研讨大间\n')
                if(a=='1'):
                    room1.click()
                    flag=0
                elif(a=='2'):
                    room2.click()
                    flag=0
                else:
                    print('越界！请重新选择')
            flag=1
            while(flag):
                b=input('确认请按1，返回请按2：\n')
                if(b=='2'):
                    print('返回成功！')
                    break
                elif(b=='1'):
                    print('确认成功！\n请选择想要预定的时间（格式：8：00-11：30）:')
                    flag=0
                else:
                    print('越界！请重新选择')
                    if(a=='1'):
                        print('您已选择单人研读间')
                    elif(a=='2'):
                        print('您已选择彩色研讨大间')
    

    #守株待兔
    def SeatKiller(self,driver):
        wait=WebDriverWait(driver,10)
        

  
 


if __name__=='__main__':   
    LibSeatKiller=login('213170812','16017522','haq1999101!!!')
    driver=LibSeatKiller.VPN_login()
    driver=LibSeatKiller.Subscribe_login(driver)
    LibSeatKiller.Interactive_Menu(driver)
    while(True):
        continue
    