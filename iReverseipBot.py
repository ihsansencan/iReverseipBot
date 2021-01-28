#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\033[32m'+"""
****************************************
* #iReverseipBot                       *
* @IhsanSencan                         *
* github.com/ihsansencan/iReverseipBot *
****************************************
"""+'\x1b[0m')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

siteList = input("Site List : ")
dosyam = open(siteList, "r")
listem = dosyam.read()
dosyam.close()
dom = listem.split("\n")

class iReverseipBot:
    def __init__(self):
        self.browser = webdriver.Firefox()

    def revVer(self):
        self.browser.get("https://viewdns.info/reverseip/")
        time.sleep(5)
        for i in dom:

            domainInput = self.browser.find_element_by_xpath("/html/body/font/table[2]/tbody/tr[2]/td/form/input[1]")
            domainInput.send_keys(str(i).lstrip('/:htp'))

            btnSubmit = self.browser.find_element_by_xpath("/html/body/font/table[2]/tbody/tr[2]/td/form/input[3]")
            btnSubmit.click()

            results = []
            list = self.browser.find_elements_by_xpath("/html/body/font/table[2]/tbody/tr[3]/td/font/table/tbody")

            for i in list:
                results.append(i.text)

            for item in results:
                sonucver = open("revIps_Results.txt", "a")
                sonucver.write('\n***Results start.***\n'+item+'\n***Results finish.***\n')                
                sonucver.close()
                time.sleep(5)
reverseip = iReverseipBot()
reverseip.revVer()
