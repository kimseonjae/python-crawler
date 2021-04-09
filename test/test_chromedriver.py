import time

from selenium import webdriver

wd = webdriver.Chrome('C:\\Users\\rlatj\\Desktop\\AI 융복합\\chromedriver_win32\\chromedriver.exe')
wd.get('https://www.google.com')

time.sleep(3)
html = wd.page_source
print(html)

wd.close()