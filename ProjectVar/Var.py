#encoding=utf-8
import os
from Util.FormatTime import times

#获取工程所在的目录的绝对路径
project_path=os.path.dirname(os.path.dirname(__file__))

#获取页面对象库文件的绝对路径
#page_object_path=project_path.decode("utf-8")+u"/Conf/PageObjectRepository.ini"

#测试数据excel文件的绝对路径
test_data_excel_path=project_path.decode("utf-8")+u"/TestData/126邮箱的测试用例.xlsx"


action_name_col_no=2
locator_col_no=3
expression_col_no=4
action_value_col_no=5

#截图路径
screenshot_path=os.path.join(project_path,'ScreenPictures','CapturePicture',times()+'.jpg')

#日志配置文件路径
log_config_path=os.path.join(project_path,'Conf','Logger.conf')

#浏览器驱动文件路径
ieDriverFilePath=r'D:\software\webdriver\IEDriverServer.exe'
chromeDriverFilePath=r'D:\software\webdriver\chromedriver.exe'
firefoxDriverFilePath=r'D:\software\webdriver\geckodriver.exe'

if __name__=='__main__':
    print __file__
    #print page_object_repository_path
    print test_data_excel_path
    #print os.path.exists(page_object_repository_path)
    print screenshot_path
    print log_config_path
