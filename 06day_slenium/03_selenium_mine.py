# coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import  os



chrome_options = Options()
chrome_options.add_argument("--headless")
abspath = os.path.abspath(r"D:\PycharmProjects\ReptileCommonModule\06day_slenium\chromedriver_win32_chrome80.0.3987.16\chromedriver.exe")
# driver = webdriver.Chrome(executable_path=abspath)
driver = webdriver.Chrome(executable_path=abspath,chrome_options=chrome_options,)

# driver.get("http://neihanshequ.com/")
driver.get("https://www.baidu.com/")
driver.save_screenshot("./static/baidu.png")



# driver.quit()