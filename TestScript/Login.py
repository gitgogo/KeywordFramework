#coding=utf-8
from selenium import webdriver
import time
from Util.ObjectMap import *
from ProjectVar.Var import *
import traceback
from Util.Log import *
from Util.Excel import ParseExcel
from Action.Action import *

test_data_excel=ParseExcel(test_data_excel_path)
test_data_excel.set_sheet_by_index(0)

for id,row in enumerate(test_data_excel.get_all_rows()[1:],2):
	# print row[2].value,row[3].value,row[4].value
	action_name=row[action_name_col_no].value
	locator=row[locator_col_no].value
	expression=row[expression_col_no].value
	action_value=row[action_value_col_no].value
	if locator is None and expression is None and action_value is None:
		comman_line=action_name+'()'
	elif locator is None and expression is None and action_value is not None:
		comman_line=action_name+'(u"'+unicode(action_value)+'")'
	elif locator is not None and expression is not None and action_value is None:
		comman_line=action_name+'("'+locator+'","'+expression+'")'
	elif locator is not None and expression is not None and action_value is not None:
		comman_line=action_name+'("'+locator+'","'+expression+'",u"'+unicode(action_value)+'")'
	print comman_line
	try:
		global elapse_time
		time1=time.time()
		exec(comman_line)
		elapse_time="%.2f"%(time.time()-time1)
		screen_shot(screenshot_path)
		test_data_excel.write_cell_content(id,7,elapse_time)
		test_data_excel.write_cell_content(id,8,u'成功')

	except Exception,e:
		info(e.message)
		test_data_excel.write_cell_content(id, 7, elapse_time)
		test_data_excel.write_cell_content(id, 8, u'失败')
		test_data_excel.write_cell_content(id, 9, e.message)