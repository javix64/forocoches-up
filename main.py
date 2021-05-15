import time, sys
from selenium import webdriver
post = sys.argv[1]
carpetaFirefox = '/home/x535/.mozilla/firefox/23nz704b.default-release/'
profile = webdriver.FirefoxProfile(carpetaFirefox)
driver = webdriver.Firefox(firefox_profile=profile)
driver.get(post)
for i in range(2,200):
    textarea = driver.find_element_by_id('vB_Editor_QR_iframe')
    textarea.send_keys('+',i)
    buttonRespond = driver.find_element_by_id('qr_submit')
    buttonRespond.click()
    time.sleep(60)