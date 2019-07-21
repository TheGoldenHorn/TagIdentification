######################
#SCRIPT TO LOAD LINKS#
#  By Ayush          # 
######################           
import os, json, time, socket, random, sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import TimeoutException
browser=webdriver.Firefox()
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
           
           
    return i + 1

'''def wait_for_tag():
   browser.wait = WebDriverWait(browser, 10)
   wait_tag_name= browser.wait.until(find_element_by_tag_name("body"))''' 

filename = raw_input('Enter the filename.txt containing links: ')
#filename="urls.txt"
max_count=file_len(filename)
file=open(filename,"r")
print "total links are" 
print max_count
num=max_count
for i in range (0, max_count) :
	try:
		link=file.readline()
		print("Please wait, loading...")
		print num
		print link
		num-=1

		print("\n Do not press ENTER before 'LOADED' ")

		browser.get(link)
		#time.sleep(10)
		#wait_for_tag()
		print("LOADED \n")

		
		print("Press ENTER for the next link")
		pause=raw_input(" ")
		
		
	except Exception as e:
		print e
		print("raised")
		pass

file.close()