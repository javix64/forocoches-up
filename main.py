import time, sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
username = sys.argv[1]
password = sys.argv[2]
post = sys.argv[3]

driver = webdriver.Firefox()
driver.get("https://www.forocoches.com/foro/misc.php?do=page&template=ident")
driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div/div/div/div/div[2]/div[1]/button[1]').click()
time.sleep(2)
driver.find_element_by_name('vb_login_username').send_keys(username)
driver.find_element_by_name('vb_login_password').send_keys(password)
time.sleep(1)
driver.find_element_by_name('logb2').click()
document.find_element_by_id('checkbox').click()