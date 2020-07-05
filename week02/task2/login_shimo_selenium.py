from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get('https://shimo.im/welcome')
    time.sleep(3)
    
    btm = browser.find_element_by_xpath('//*[@id="homepage-header"]/nav/div[3]/a[2]/button')
    btm.click()

    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys('zhuwanjun2008@hotmail.com')
    time.sleep(3)

    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys('1qaz@WSX')
    time.sleep(3)
    
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()
   
    # 获取cookies
    cookies = browser.get_cookies()  
    print(cookies)
    time.sleep(5)

except Exception as e:
    print(e)
finally:    
    browser.close()