def main():
  from selenium import webdriver
from seleniumwire.webdriver import ChromeOptions
import time
import random
from selenium.webdriver.common.by import By
opts = ChromeOptions()
opts.add_experimental_option("excludeSwitches", ['enable-automation'])
opts.add_argument('--no-sandbox')
opts.add_argument('--disable-dev-shm-usage')
age = random.randint(24,28)
month_b = random.randint(1,10)
day_b = random.randint(1,20)
options = {
    'proxy':
    {
        'http': 'https://lum-customer-hl_116798e2-zone-admin-route_err-pass_dyn-country-us:admin@zproxy.lum-superproxy.io:22225',
        'https': 'https://lum-customer-hl_116798e2-zone-admin-route_err-pass_dyn-country-us:admin@zproxy.lum-superproxy.io:22225'
    },
}

#with open('useragent','r') as read_user_agent:
    #useragent = read_user_agent.readlines()
#opts.add_argument('user-agent='+random.choice(useragent))
with open('username','r') as read:
    firsandlastname = read.readlines()
driver = webdriver.Chrome(options=opts)
driver.get("https://m.facebook.com")
driver.implicitly_wait(10)
crea_account_bt = driver.find_element(By.ID,'signup-button')
crea_account_bt.click()
time.sleep(3)
firstname = driver.find_element(By.ID,"firstname_input")
for fname in firsandlastname[random.randint(0,len(firsandlastname))].split(' ')[0]:
  firstname.send_keys(fname)
  time.sleep(0.5)
time.sleep(3)
lastname = driver.find_element(By.ID,'lastname_input')
for lname in firsandlastname[random.randint(0,len(firsandlastname))].split(' ')[1]:
  lastname.send_keys(lname)
  time.sleep(0.5)
time.sleep(1)
next1 = driver.find_element(By.CSS_SELECTOR,'#mobile-reg-form > div._3367._1zq9 > div:nth-child(2) > button:nth-child(1)')
next1.click()
time.sleep(1)
month = driver.find_element(By.CSS_SELECTOR,f'#month > option:nth-child({month_b})')
month.click()
time.sleep(3)
day = driver.find_element(By.CSS_SELECTOR,f'#day > option:nth-child({day_b})')
day.click()
time.sleep(3)
year = driver.find_element(By.CSS_SELECTOR,f'#year > option:nth-child({age})')
year.click()
time.sleep(3)
next2 = driver.find_element(By.CSS_SELECTOR,'#mobile-reg-form > div._3367._1zq9 > div:nth-child(2) > button:nth-child(1)')
next2.click()
time.sleep(1)
sign_email = driver.find_element(By.LINK_TEXT,'Sign Up With Email')
sign_email.click()
time.sleep(1)
insert_email = driver.find_element(By.ID,'contactpoint_step_input')
for email in firsandlastname[random.randint(0,len(firsandlastname))].replace(" ", ""):
  insert_email.send_keys(email+'chitthi.in')
  time.sleep(0.5)
time.sleep(1)
next3 = driver.find_element(By.CSS_SELECTOR,'#mobile-reg-form > div._3367._1zq9 > div:nth-child(2) > button:nth-child(1)')
next3.click()
time.sleep(1)
sex = driver.find_element(By.CSS_SELECTOR,f'#sex > div > div:nth-child(3) > div > label:nth-child({random.randint(1,2)}) > div > div > div._4g34._15d9 > span')
sex.click()
time.sleep(1)
next4 = driver.find_element(By.CSS_SELECTOR,'#mobile-reg-form > div._3367._1zq9 > div:nth-child(2) > button:nth-child(1)')
next4.click()
time.sleep(3)
random_pass = random.randint(0,9999999999999)
password = driver.find_element(By.ID,'password_step_input')
for random_password in random_pass:
  password.send_keys(random_password)
  time.sleep(0.5)
with open('SAVE_PASSWORD.txt','a') as save_password:
  save_password.write(random_password+'\n')
  save_password.close()
time.sleep(3)
sign_up = driver.find_element(By.CSS_SELECTOR,'#mobile-reg-form > div._3367._1zq9 > div:nth-child(2) > button:nth-child(4)')
sign_up.click()
time.sleep(1000)


if __name__ == '__main__':
  try:
    main()

  except:
    main()