import time, sys
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
post = sys.argv[1]
carpetaFirefox = '/home/x535/.mozilla/firefox/23nz704b.default-release/'
profile = webdriver.FirefoxProfile(carpetaFirefox)
options = Options()
options.headless = True
driver = webdriver.Firefox(firefox_profile=profile, options=options)
driver.get(post)
for i in range(2,200):
    textarea = driver.find_element_by_id('vB_Editor_QR_iframe')
    textarea.send_keys('+',i)
    buttonRespond = driver.find_element_by_id('qr_submit')
    buttonRespond.click()
    time.sleep(60)