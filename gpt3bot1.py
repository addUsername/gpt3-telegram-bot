# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 23:05:43 2020
@author: SERGI
"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

class Controller:

    def __init__(self):
            self.token = ""
            self.my_list = ["","","","","","","","","",""]
            self.text = ""
            self.run()
    
        
    def updateList(self, update, context):
        params = [update.message.text]
        params.append(update.message.from_user.first_name)
        self.my_list.pop(0)
        self.my_list.append(str(params[1])+": "+str(params[0]))
        
    def hibot(self, update, context):

        self.text = ""
        for line in self.my_list:
            if (line != ""):
                self.text += line+"\n"
        self.text += "Bot: "
        
        update.message.reply_text(self.gpt3())
        
    def gpt3(self):

        driver = webdriver.Firefox(executable_path='geckodriver.exe')
        time.sleep(4)
        URL = "https://aidungeon.io/"
        
        driver.get(URL)
        time.sleep(2)

        actions = ActionChains(driver)
        actions = actions.send_keys(Keys.TAB)
        actions = actions.send_keys(Keys.TAB)
        actions = actions.send_keys(Keys.ENTER)
        actions.perform()

        time.sleep(2)
        actions = ActionChains(driver)
        actions = actions.send_keys(Keys.TAB)
        actions = actions.send_keys(Keys.ENTER)
        actions.perform()

        time.sleep(2)
        actions = ActionChains(driver)
        actions = actions.send_keys(Keys.NUMPAD6)
        actions = actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(2)

        time.sleep(2)
        actions = ActionChains(driver)
        actions = actions.send_keys(self.text)
        actions = actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(6)

        ids = driver.find_elements_by_xpath('//*[@id]')
        for ii in ids:
                if( ii.get_attribute('id') == "root"):
                        a = ii.text.split("Bot:",1)
                        b = a[1].split("\uf54c")
                        return(b[0])
        
        
    def run(self):
        
        updater = Updater(self.token, use_context=True)
        dp = updater.dispatcher
        
        dp.add_handler(CommandHandler("hibot", self.hibot))
        dp.add_handler(MessageHandler(Filters.text, self.updateList))              
        
        updater.start_polling()
        updater.idle()
 
Controller()
