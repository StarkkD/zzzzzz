import threading
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
import time
import random

options = [{
    'proxy':{
        'http': 'http://Duongvip:Duongvip1@hndc32.proxyno1.com:59954',
        'https': 'https://Duongvip:Duongvip1@hndc32.proxyno1.com:59954',
        'no_proxy' : 'localhost,127.0.0.1'
    }
},
    {
    'proxy':{
        'http': 'http://Duongvip:Duongvip1@hndc7.proxyno1.com:55305',
        'https': 'https://Duongvip:Duongvip1@hndc7.proxyno1.com:55305',
        'no_proxy' : 'localhost,127.0.0.1'
    }
},
    {
    'proxy':{
        'http': 'http://Duongvip:Duongvip1@vpdc1.proxyno1.com:15461',
        'https': 'https://Duongvip:Duongvip1@vpdc1.proxyno1.com:15461',
        'no_proxy' : 'localhost,127.0.0.1'
    }
}]

def runtest(l):
    driver = webdriver.Chrome(seleniumwire_options=options[l])

    x = l*400
    y = 10
    driver.set_window_rect(x, y, 300, 500)

    driver.get('https://vesovn.net/#/register')
    sdt = random.randint(100000000,999999999)
    passwd = 'Duongvip1'
    invite_code = '68778234430'

    time.sleep(20)


    driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div/div/div[1]/div[2]/input').send_keys(sdt)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div/div/div[3]/div[2]/input').send_keys(passwd)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div/div/div[5]/div[2]/input').send_keys(passwd)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div/div/div[7]/div[2]/input').send_keys(invite_code)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div/div/div[8]/div/div').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div/div/div[9]/button[1]').click()
    
    time.sleep(7)

#toi
    driver.get('https://vesovn.net/#/main')

    time.sleep(15)
    aid = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[2]/span[3]').text

    #ruttien
    driver.get('https://vesovn.net/#/wallet/Withdraw/AddBankCard?fromV=Withdraw-BankCard')
    time.sleep(15)
 
    driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div[2]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/div[2]/div/div[2]').click()
    time.sleep(3)

    a = open("test.txt", "r")
    in4 = a.readline()
    lines = a.readlines()
    in5 = in4.split(",")
    a.close()


    stk = in5[0]
    ten = in5[1]

    del lines[0]
    new = open("test.txt", "w+")

    for line in lines:
        new.write(line)

    new.close()

    driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[3]/input').send_keys(ten)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[4]/input').send_keys(stk)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[5]/input').send_keys(sdt)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[6]/textarea').send_keys("Ha Noi")
    driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[7]/button').click()

    with open('tk.txt', 'a') as f:
        f.write(str(sdt) + ' ' + aid + '\n')
    time.sleep(5)


    driver.quit()


soluong = 3
threads = []
for l in range(soluong):
    threads += [threading.Thread(target=runtest,args={l},)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print('ket thuc so luong')