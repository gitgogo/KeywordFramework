#coding=utf-8
from selenium import webdriver
import time
from Util.ObjectMap import *
from ProjectVar.Var import *
import traceback
from Util.Log import *

driver=None

def open_browser(browserName,*args):
	global driver
	try:
		if browserName.lower()=='ie':
			driver=webdriver.Ie(executable_path=ieDriverFilePath)
		elif browserName.lower()=='chrome':
			driver=webdriver.Chrome(executable_path=chromeDriverFilePath)
		elif browserName.lower()=='firefox':
			driver=webdriver.Firefox(executable_path=firefoxDriverFilePath)
	except Exception,e:
		info(traceback.format_exc())

def visit_url(url,*args):
	global driver
	try:
		driver.get(url)
	except Exception,e:
		info(traceback.format_exc())

def pause(seconds):
	time.sleep(float(seconds))

def close_browser():
	global driver
	driver.quit()

def enter_frame(locatorMethod,locatorExpression):
	global driver
	driver.switch_to.frame(getElement(driver,locatorMethod,locatorExpression))

def input_string(locatorMethod,locatorExpression,content):
	global driver
	getElement(driver,locatorMethod,locatorExpression).send_keys(content)

def click(locatorMethod,locatorExpression):
	global driver
	getElement(driver,locatorMethod,locatorExpression).click()

def screen_shot(path):
	driver.get_screenshot_as_file(path)

def assert_true(expect_word):
	global driver
	try:
		assert expect_word in driver.page_source
		info('assert success!')
		return True
	except AssertionError,e:
		info(e.message)
	except Exception,e:
		info(traceback.format_exc())

def login(username,passwd):
	open_browser('chrome')
	# open_browser('firefox')
	visit_url('http://mail.126.com')
	pause(3)
	enter_frame('id', 'x-URS-iframe')
	input_string('xpath', "//input[@name='email']", username)
	input_string('xpath', "//input[@name='password']", passwd)
	click('id', 'dologin')
	pause(3)
	screen_shot(screenshot_path)
	if assert_true(u'退出'):
		info('login success!')

def add_contact(name,email,phone,comment):
	login('liudongjie2015', 'liudongjie126')
	click('xpath', "//div[text()='通讯录']")
	click('xpath', "//span[text()='新建联系人']")
	info('click new contact')
	input_string('xpath', "//a[@title='编辑详细姓名']/preceding-sibling::div/input", name)
	input_string('xpath', "//*[@id='iaddress_MAIL_wrap']//input", email)
	input_string('xpath', "//*[@id='iaddress_TEL_wrap']//dd//input", phone)
	input_string('xpath', "//textarea", comment)
	click('xpath', "//span[.='确 定']")
	if assert_true(name):
		info('add new contact success!')

if __name__=='__main__':
	# open_browser('ie')
	# open_browser('chrome')
	# visit_url('http://www.baidu.com')
	# open_browser('firefox')
	# add_contact('LucyLao','test@mail.com','1898376743',u'同事')
	login('liudongjie2015', 'liudongjie126')
	close_browser()